import os.path
import bg_helper as bh
import fs_helper as fh
import settings_helper as sh


SETTINGS = sh.get_all_settings(__name__).get(sh.APP_ENV, {})

_package_repos_base_path = SETTINGS.get('package_repos_base_path')
_kenjyco_libs_repo_names = SETTINGS.get('kenjyco_libs_repo_names')
_dependency_repos_base_path = SETTINGS.get('dependency_repos_base_path')
if not _package_repos_base_path or not _kenjyco_libs_repo_names or not _dependency_repos_base_path:
    # Sync settings.ini with vimdiff
    sh.sync_settings_file(__name__)
    SETTINGS = sh.get_all_settings(__name__).get(sh.APP_ENV, {})
    _package_repos_base_path = SETTINGS.get('package_repos_base_path')
    _kenjyco_libs_repo_names = SETTINGS.get('kenjyco_libs_repo_names')
    _dependency_repos_base_path = SETTINGS.get('dependency_repos_base_path')

assert _package_repos_base_path and _kenjyco_libs_repo_names and _dependency_repos_base_path, (
    'PACKAGE_REPOS_BASE_PATH, KENJYCO_LIBS_REPO_NAMES, and DEPENDENCY_REPOS_BASE_PATH are not set'
)

_package_repos_base_path = fh.abspath(_package_repos_base_path)
_dependency_repos_base_path = fh.abspath(_dependency_repos_base_path)


def _get_clone_status_for_packages():
    cloned = {}
    uncloned = {}
    for repo in _kenjyco_libs_repo_names:
        repo_path = os.path.join(_package_repos_base_path, repo)
        if os.path.isdir(repo_path):
            cloned[repo] = repo_path
        else:
            uncloned[repo] = repo_path

    return {
        'cloned': cloned,
        'uncloned': uncloned
    }
