Install Options
---------------

``pip install kenjyco-libs``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Includes:
`bg-helper <https://github.com/kenjyco/bg-helper/blob/master/README.md>`__,
`fs-helper <https://github.com/kenjyco/fs-helper/blob/master/README.md>`__,
`input-helper <https://github.com/kenjyco/input-helper/blob/master/README.md>`__,
and
`settings-helper <https://github.com/kenjyco/settings-helper/blob/master/README.md>`__

``pip install "kenjyco-libs[bs4]"``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Includes: beautifulsoup4, kenjyco-libs, and lxml

Also requires system requirements for ``lxml``

::

   $ sudo apt-get install -y libxml2 libxslt1.1 libxml2-dev libxslt1-dev

   or

   % brew install libxml2

``pip install "kenjyco-libs[data]"``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Includes:
`aws-info-helper <https://github.com/kenjyco/aws-info-helper/blob/master/README.md>`__,
`dt-helper <https://github.com/kenjyco/dt-helper/blob/master/README.md>`__,
“kenjyco-libs[nosql,sql]”, and
`webclient-helper <https://github.com/kenjyco/webclient-helper/blob/master/README.md>`__

``pip install "kenjyco-libs[dev]"``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Includes: kenjyco-libs,
`readme-helper <https://github.com/kenjyco/readme-helper/blob/master/README.md>`__,
`testing-helper <https://github.com/kenjyco/testing-helper/blob/master/README.md>`__

``pip install "kenjyco-libs[full]"``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Includes:
`chloop <https://github.com/kenjyco/chloop/blob/master/README.md>`__,
and “kenjyco-libs[bs4,data,dev]”

``pip install "kenjyco-libs[nosql]"``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Includes: kenjyco-libs,
`mongo-helper <https://github.com/kenjyco/mongo-helper/blob/master/README.md>`__,
`redis-helper <https://github.com/kenjyco/redis-helper/blob/master/README.md>`__

``pip install "kenjyco-libs[sql]"``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Includes:
`expectation-helper <https://github.com/kenjyco/expectation-helper/blob/master/README.md>`__,
kenjyco-libs, and
`sql-helper <https://github.com/kenjyco/sql-helper/blob/master/README.md>`__

Also requires the ``pg_config`` executable

::

   $ sudo apt-get install -y libpq-dev

   or

   $ brew install postgresql
