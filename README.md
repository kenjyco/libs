[aws-info-helper]: https://github.com/kenjyco/aws-info-helper/blob/master/README.md
[bg-helper]: https://github.com/kenjyco/bg-helper/blob/master/README.md
[chloop]: https://github.com/kenjyco/chloop/blob/master/README.md
[dt-helper]: https://github.com/kenjyco/dt-helper/blob/master/README.md
[expectation-helper]: https://github.com/kenjyco/expectation-helper/blob/master/README.md
[fs-helper]: https://github.com/kenjyco/fs-helper/blob/master/README.md
[input-helper]: https://github.com/kenjyco/input-helper/blob/master/README.md
[mongo-helper]: https://github.com/kenjyco/mongo-helper/blob/master/README.md
[readme-helper]: https://github.com/kenjyco/readme-helper/blob/master/README.md
[redis-helper]: https://github.com/kenjyco/redis-helper/blob/master/README.md
[settings-helper]: https://github.com/kenjyco/settings-helper/blob/master/README.md
[sql-helper]: https://github.com/kenjyco/sql-helper/blob/master/README.md
[testing-helper]: https://github.com/kenjyco/testing-helper/blob/master/README.md
[webclient-helper]: https://github.com/kenjyco/webclient-helper/blob/master/README.md

A meta-package that orchestrates development workflows across the kenjyco helper library ecosystem. This library provides sophisticated ecosystem coordination by grouping related extra dependency sets, managing editable installations, and cloning repositories without typical setup friciton.

Every operation interrogates actual system state rather than making optimistic assumptions, and missing components never break core functionality. It's particularly valuable as an example for developers working with complex package ecosystems who need reliable, transparent, and composable development workflows.

## Install

Use `pip` to install [kenjyco-libs](https://github.com/kenjyco/libs), ideally to a [virtual environment (venv)](https://docs.python.org/3/library/venv.html). You can choose `kenjyco-libs` (very light weight), `"kenjyco-libs[full]"` (everything), or something in between.

- `pip install kenjyco-libs`
    - Includes: [bg-helper][], click, [fs-helper][], [input-helper][], [settings-helper][]
- `pip install "kenjyco-libs[ipython]"`
    - Includes: ipython, kenjyco-libs
- `pip install "kenjyco-libs[xmljson]"`
    - Includes: kenjyco-libs, xmljson
- `pip install "kenjyco-libs[bs4]"`
    - Includes: beautifulsoup4, kenjyco-libs, lxml
    - Also requires system requirements for `lxml`

    ```
    sudo apt-get install -y libxml2 libxslt1.1 libxml2-dev libxslt1-dev
    ```

    or

    ```
    brew install libxml2
    ```
- `pip install "kenjyco-libs[nosql]"`
    - Includes: [chloop][], kenjyco-libs, [mongo-helper][], [redis-helper][]
- `pip install "kenjyco-libs[sql]"`
    - Includes: [expectation-helper][], kenjyco-libs, [sql-helper][]
    - Also requires the `pg_config` executable
    - expectation-helper is only included if using Python 3.8+

    ```
    sudo apt-get install -y libpq-dev
    ```

    or

    ```
    brew install postgresql
    ```
- `pip install "kenjyco-libs[data]"`
    - Includes: [aws-info-helper][], [dt-helper][],
      "kenjyco-libs[nosql,sql,xmljson]", [webclient-helper][]
- `pip install "kenjyco-libs[dev]"`
    - Includes: kenjyco-libs, [readme-helper][], [testing-helper][]
- `pip install "kenjyco-libs[full]"`
    - Includes: "kenjyco-libs[bs4,data,dev,ipython]"

## Default settings.ini

```ini
[default]
package_repos_base_path = ~/repos/personal/packages
kenjyco_libs_repo_names = aws-info-helper, bg-helper, chloop, dt-helper, expectation-helper, fs-helper, input-helper, libs, mongo-helper, readme-helper, redis-helper, settings-helper, sql-helper, testing-helper, webclient-helper
dependency_repos_base_path = ~/repos/some-repos

[dev]
something =

[test]
something =
```

The first time that `kenjyco_libs` is imported, the sample [settings.ini](https://github.com/kenjyco/libs/blob/master/kenjyco_libs/settings.ini) file will be copied to the `~/.config/kenjyco-libs` directory.

## QuickStart

The most powerful workflow is the **complete development environment setup** for whichever combination of "extras" that were installed via pip.

Run the provided **`kenjyco-dev-setup`** script to clone kenjyco repos and their dependencies to the paths specified in settings.ini. The packages will be reinstalled in "editable mode" (i.e. the packages in the venv's site-packages directory will be linked to the cloned kenjyco repos).

```
kenjyco-dev-setup
```

Use **`kenjyco-ipython`** to start ipython with all of the installed kenjyco packages automatically imported as their preferred 2-character aliases, keeping your ipython shell history clean from boilerplate import statements.

```
kenjyco-ipython
```

> Optionallly pass `--no-vi` to disable vi editing mode or `--no-colors` to not use colors and syntax highlighting.

## API Overview

### High-Level Workflow Functions

- **`dev_setup(py_versions='', show=True)`** - Complete ecosystem setup workflow
  - `py_versions`: String containing Python versions to make venvs for (separated by `,`, `;`, or `|`)
  - `show`: If True, show the `git`/`pip` commands before executing
  - Internal calls: `clone_all_missing()`, `install_packages_in_editable_mode()`

- **`clone_all_missing(show=True)`** - Clone package and dependency repositories locally
  - `show`: If True, show the `git` command before executing
  - Internal calls: `_clone_packages()`, `_clone_dependencies()`

- **`install_packages_in_editable_mode(show=True)`** - Install cloned packages in editable mode
  - `show`: If True, show the `pip` command before executing
  - Return: Result of pip install editable operations
  - Internal calls: `bh.tools.pip_install_editable()`

### Environment State Interrogation Functions

- **`_get_clone_status_for_packages()`** - Discover which ecosystem packages are cloned locally
  - Return: Dictionary with keys `cloned` (name to path mapping) and `uncloned` (name to expected_path mapping)
  - Internal calls: None

- **`_get_clone_status_for_dependencies()`** - Discover which dependency packages are cloned locally
  - Return: Dictionary with keys `cloned` (name→path mapping) and `uncloned` (name→expected_path mapping)
  - Internal calls: None

- **`_get_kenjyco_pkgs_in_venv()`** - Identify which ecosystem packages are installed
  - Return: Set intersection of installed packages and ecosystem package names
  - Internal calls: `bh.tools.installed_packages()`

- **`_get_dependencies_in_venv()`** - Identify which dependency packages are installed
  - Return: Set intersection of installed packages and known dependency names (lowercased)
  - Internal calls: `bh.tools.installed_packages()`

### Repository Cloning Functions

- **`_clone_packages(show=True)`** - Clone ecosystem package repositories locally
  - `show`: If True, show the `git` command before executing
  - Internal calls: `_get_clone_status_for_packages()`, `_get_kenjyco_pkgs_in_venv()`, `bh.tools.git_clone()`

- **`_clone_dependencies(show=True)`** - Clone external dependency repositories locally
  - `show`: If True, show the `git` command before executing
  - Internal calls: `_get_clone_status_for_dependencies()`, `_get_dependencies_in_venv()`, `bh.tools.git_clone()`
