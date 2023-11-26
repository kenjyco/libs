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

## Install Options

Use `pip` to install [kenjyco-libs](https://github.com/kenjyco/libs), ideally to
a [virtual environment (venv)](https://docs.python.org/3/library/venv.html). You
can choose `kenjyco-libs` (very light weight), `"kenjyco-libs[full]"`
(everything), or something in between.

- `pip install kenjyco-libs`
    - Includes: [bg-helper][], click, [fs-helper][], [input-helper][],
      [settings-helper][]
- `pip install "kenjyco-libs[bs4]"`
    - Includes: beautifulsoup4, kenjyco-libs, lxml
    - Also requires system requirements for `lxml`

    ```
    $ sudo apt-get install -y libxml2 libxslt1.1 libxml2-dev libxslt1-dev

    or

    $ brew install libxml2
    ```
- `pip install "kenjyco-libs[data]"`
    - Includes: [aws-info-helper][], [dt-helper][],
      "kenjyco-libs[nosql,sql,xmljson]", [webclient-helper][]
- `pip install "kenjyco-libs[dev]"`
    - Includes: kenjyco-libs, [readme-helper][], [testing-helper][]
- `pip install "kenjyco-libs[full]"`
    - Includes: "kenjyco-libs[bs4,data,dev,ipython]"
- `pip install "kenjyco-libs[ipython]"`
    - Includes: ipython, kenjyco-libs
- `pip install "kenjyco-libs[nosql]"`
    - Includes: [chloop][], kenjyco-libs, [mongo-helper][], [redis-helper][]
- `pip install "kenjyco-libs[sql]"`
    - Includes: [expectation-helper][], kenjyco-libs, [sql-helper][]
    - Also requires the `pg_config` executable
    - expectation-helper is only included if using Python 3.8+

    ```
    $ sudo apt-get install -y libpq-dev

    or

    $ brew install postgresql
    ```
- `pip install "kenjyco-libs[xmljson]"`
    - Includes: kenjyco-libs, xmljson

## Setup and Usage

The first time that `kenjyco_libs` is imported, the sample
[settings.ini](https://github.com/kenjyco/libs/blob/master/kenjyco_libs/settings.ini)
file will be copied to the `~/.config/kenjyco-libs` directory.

```
[default]
package_repos_base_path = ~/repos/personal/packages
kenjyco_libs_repo_names = aws-info-helper, bg-helper, chloop, dt-helper, expectation-helper, fs-helper, input-helper, libs, mongo-helper, readme-helper, redis-helper, settings-helper, sql-helper, testing-helper, webclient-helper
dependency_repos_base_path = ~/repos/some-repos

[dev]
something =

[test]
something =
```

After installing with `pip`, you will want to **run the provided
`kenjyco-dev-setup` script**. This will automatically clone kenjyco repos and
their dependencies to the paths specified in settings.ini, then reinstall the
packages in "editable mode" (i.e. the packages in the venv's site-packages
directory will be linked to the cloned kenjyco repos).

Use **kenjyco-ipython** to start ipython with all of the installed kenjyco
packages automatically imported (keeping your ipython shell history clean from
boilerplate import statements).

```
% venv/bin/kenjyco-dev-setup --help
Usage: kenjyco-dev-setup [OPTIONS]

  Clone missing repos and install more packages in editable mode

  Options:
    --help  Show this message and exit.


% venv/bin/kenjyco-ipython --help
Usage: kenjyco-ipython [OPTIONS]

  Start ipython with several things imported

Options:
  --no-vi      Do not use vi editing mode
  --no-colors  Do not use colors / syntax highlighting
  --help       Show this message and exit.
```
