[bg-helper]: https://github.com/kenjyco/bg-helper/blob/master/README.md
[aws-info-helper]: https://github.com/kenjyco/aws-info-helper/blob/master/README.md
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

### pip install kenjyco-libs

Includes: [bg-helper][], [fs-helper][], [input-helper][], and
[settings-helper][]

### pip install "kenjyco-libs[bs4]"

Includes: beautifulsoup4, kenjyco-libs, and lxml

Also requires system requirements for `lxml`

```
$ sudo apt-get install -y libxml2 libxslt1.1 libxml2-dev libxslt1-dev

or

% brew install libxml2
```

### pip install "kenjyco-libs[data]"

Includes: [aws-info-helper][], [dt-helper][], "kenjyco-libs[nosql,sql]", and
[webclient-helper][]

### pip install "kenjyco-libs[dev]"

Includes: kenjyco-libs, [readme-helper][], [testing-helper][]

### pip install "kenjyco-libs[full]"

Includes: [chloop][], and "kenjyco-libs[bs4,data,dev]"

### pip install "kenjyco-libs[nosql]"

Includes: kenjyco-libs, [mongo-helper][], [redis-helper][]

### pip install "kenjyco-libs[sql]"

Includes: [expectation-helper][], kenjyco-libs, and [sql-helper][]

Also requires the `pg_config` executable

```
$ sudo apt-get install -y libpq-dev

or

$ brew install postgresql
```
