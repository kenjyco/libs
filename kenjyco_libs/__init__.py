import os.path
import bg_helper as bh
import fs_helper as fh
import settings_helper as sh


SETTINGS = sh.get_all_settings(__name__).get(sh.APP_ENV, {})

package_repos_base_path = SETTINGS.get('package_repos_base_path')
kenjyco_libs_repo_names = SETTINGS.get('kenjyco_libs_repo_names')
if not package_repos_base_path or not kenjyco_libs_repo_names:
    # Sync settings.ini with vimdiff
    sh.sync_settings_file(__name__)
    SETTINGS = sh.get_all_settings(__name__).get(sh.APP_ENV, {})
    package_repos_base_path = SETTINGS.get('package_repos_base_path')
    kenjyco_libs_repo_names = SETTINGS.get('kenjyco_libs_repo_names')

assert package_repos_base_path and kenjyco_libs_repo_names, 'PACKAGE_REPOS_BASE_PATH and KENJYCO_LIBS_REPO_NAMES are not set'

package_repos_base_path = fh.abspath(package_repos_base_path)
local_repos_paths_dict = {}
not_cloned = {}
for repo in kenjyco_libs_repo_names:
    repo_path = os.path.join(package_repos_base_path, repo)
    if os.path.isdir(repo_path):
        local_repos_paths_dict[repo] = repo_path
    else:
        not_cloned[repo] = repo_path
