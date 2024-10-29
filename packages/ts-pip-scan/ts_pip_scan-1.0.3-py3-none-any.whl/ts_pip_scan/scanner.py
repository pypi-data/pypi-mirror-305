import json
import os
import re
import sys
import time
from importlib.metadata import Distribution, PackageNotFoundError, distribution, files
from pathlib import Path
from pprint import pprint
from typing import Optional
from git import Repo, InvalidGitRepositoryError
from ts_pip_scan.models import Config
from ts_pip_scan.ts_client import ApiClient

class Scanner:
    IMPORT_STATEMENTS_REGEX = re.compile(r'(?:from|import) ([\w]+)(?:.*)')
    REQUIRES_PACKAGES_REGEX = re.compile(r'([\w\-]+)(?:.*)')

    def __init__(self, path: Path, config: Config) -> None:
        self._config = config
        self._path = path
        self._processed_packages = set()
        self._client = ApiClient(self._config.base_url, self._config.apiKey)

    def _get_git_branch(self):
        try:
            repo = Repo(self._path)
            return repo.active_branch.name
        except InvalidGitRepositoryError:
            return None
        except TypeError:
            # In the pipeline git branch HEAD is detached CI_COMMIT_BRANCH contain commit branch
            return os.environ.get("CI_COMMIT_BRANCH")
        except Exception:
            print("Can not determine git branch")
            return None

    def _find_python_files(self, folder):
        """Recursively find all Python files in the given directory."""
        python_files = []
        for root, dirs, files in os.walk(folder):
            for file in files:
                if file.endswith('.py'):
                    python_files.append(os.path.join(root, file))
        return python_files

    def _extract_imports(self, file_path):
        """Extract all imported packages from a Python file."""
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        return set(self.IMPORT_STATEMENTS_REGEX.findall(content))

    def _get_package_dist(self, package)-> Optional[Distribution]:
        try:
            dist = distribution(package)
            return dist
        except PackageNotFoundError:
            return None

    def _get_package_dependencies(self, requires) -> list[str]:
        if requires:
            for require in requires:
                all_matches = self.REQUIRES_PACKAGES_REGEX.findall(require)
                for dep in all_matches:
                    yield dep


    def _create_package_dependencies(self, packages):
        installed_packages = []
        for package in packages:
            try:
                installed_packages.append(distribution(package))
            except PackageNotFoundError:
                continue

        for pkg_dist in installed_packages:
            pkg_metadata = pkg_dist.metadata
            name = pkg_metadata.get('Name', "")
            version = pkg_metadata.get('Version', [])
            if version:
                version = [version]
            pkg_dep  = {
                    "name": name,
                    "key": f"pip:{name.lower()}",
                    "versions": version
            }

            if name not in self._processed_packages:
                self._processed_packages.add(name)

                pkg_licenses = pkg_metadata.get('License', [])
                if pkg_licenses:
                    pkg_licenses = [{"name": pkg_licenses}]

                pkg_dep["private"] = False
                pkg_dep["description"] = pkg_metadata.get('Summary', "")
                pkg_dep["homepageUrl"] =  pkg_metadata.get('Home-page', "")
                pkg_dep["repoUrl"] =  pkg_metadata.get('Download-URL', "")
                pkg_dep["checksum"] =  ""
                pkg_dep["licenses"] = pkg_licenses
                deps = [dep for dep in self._get_package_dependencies(pkg_dist.requires)]
                pkg_dep["dependencies"] = [dep for dep in self._create_package_dependencies(deps)]
            yield pkg_dep

    def evaluate_scan(self,scan_id):


        counter= 0
        scan = None
        while counter <= 6:
            scan = self._client.get_scan(scan_id)
            status = scan["analysisStatus"]
            if  status == "Finished":
                break
            print(f"TS analysis not done. analysisStatus: {status} \nTrying in 10 seconds")
            counter += 1
            time.sleep(10)
        if scan is None:
            print(f"Could not fetch scan results after {counter} tries")
            sys.exit(1)

        legal_warnings: int = scan["statistics"]["legal"]["warnings"]
        legal_violations: int = scan["statistics"]["legal"]["violations"]
        vulnerability_warnings: int = scan["statistics"]["vulnerability"]["warnings"]
        vulnerability_violations: int = scan["statistics"]["vulnerability"]["violations"]

        legal_checks = {}
        vulnerability_checks = {}
        success = True

        if legal_warnings > self._config.max_legal_warnings:
            legal_checks["warnings"] = legal_warnings
            success = False
        if legal_violations > self._config.max_legal_violations:
            legal_checks["violations"] = legal_violations
            success = False
        if vulnerability_warnings > self._config.max_vulnerability_warnings:
            vulnerability_checks["warnings"] = vulnerability_warnings
            success = False
        if vulnerability_violations > self._config.max_vulnerability_violations:
            vulnerability_checks["violations"] = vulnerability_violations
            success = False

        checks = {
            "success": success,
            "legal": legal_checks,
            "vulnerability": vulnerability_checks
        }
        if checks["success"]:
            print("TS evaluation success")
        else:
            print("TS evaluation failed: ")
            pprint(checks)
            sys.exit(1)
        return scan

    def _save_output(self, data: dict, output_path):

        if output_path is None or not Path(output_path):
            output_path = Path(self._path)
        if output_path.is_dir():
            output_path = os.path.join(output_path, "ts-output.json")
        with open(output_path, "w") as fp:
            json.dump(data, fp , indent=4)

    def scan(self, evaluate=False, output=None):
        python_files = self._find_python_files(self._path)
        all_imports = set()
        for file_path in python_files:
            imports = self._extract_imports(file_path)
            all_imports.update(imports)
        module_name = self._config.module or self._path.name
        git_branch = self._get_git_branch()
        
        print("Git branch:", git_branch)
        dependencies = [dep for dep in self._create_package_dependencies(all_imports)]
        scan_info = {
            'project': self._config.project,
            'module': module_name,
            'moduleId': f"pip:{module_name}",
            "branch": git_branch,
            'dependencies': dependencies
        }
        output_data = {
            "dependencies": dependencies,
        }
        if not self._config.skip_upload:
            result = self._client.post_scan(scan_info)
            output_data["scan"] = result
            scan_id = result["scanId"]
            if evaluate:
                scan_analsis = self.evaluate_scan(scan_id)
                output_data["scan_analysis"] = scan_analsis

        self._save_output(output_data, output)
