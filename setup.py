from setuptools import setup, find_packages


with open('README.rst', 'r') as fp:
    long_description = fp.read()

with open('requirements.txt', 'r') as fp:
    requirements = fp.read().splitlines()

with open('requirements-bs4.txt', 'r') as fp:
    requirements_bs4 = fp.read().splitlines()

with open('requirements-dev.txt', 'r') as fp:
    requirements_dev = fp.read().splitlines()

with open('requirements-ipython.txt', 'r') as fp:
    requirements_ipython = fp.read().splitlines()

with open('requirements-nosql.txt', 'r') as fp:
    requirements_nosql = fp.read().splitlines()

with open('requirements-sql.txt', 'r') as fp:
    requirements_sql = fp.read().splitlines()

with open('requirements-xmljson.txt', 'r') as fp:
    requirements_xmljson = fp.read().splitlines()

requirements_data = ['aws-info-helper', 'dt-helper', 'webclient-helper'] + requirements_sql + requirements_nosql + requirements_xmljson

setup(
    name='kenjyco-libs',
    version='0.0.7',
    description='Easily install kenjyco libs',
    long_description=long_description,
    author='Ken',
    author_email='kenjyco@gmail.com',
    license='MIT',
    url='https://github.com/kenjyco/kenjyco-libs',
    download_url='https://github.com/kenjyco/kenjyco-libs/tarball/v0.0.7',
    packages=find_packages(),
    extras_require={
        'bs4': requirements_bs4,
        'data': requirements_data,
        'dev': requirements_dev,
        'ipython': requirements_ipython,
        'full': requirements_bs4 + requirements_data + requirements_dev + requirements_ipython,
        'nosql': requirements_nosql,
        'sql': requirements_sql,
        'xmljson': requirements_xmljson,
    },
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    install_requires=requirements,
    include_package_data=True,
    package_dir={'': '.'},
    package_data={
        '': ['*.ini'],
    },
    entry_points={
        'console_scripts': [
            'kenjyco-dev-setup=kenjyco_libs.scripts.dev_setup:main',
            'kenjyco-ipython=kenjyco_libs.scripts.shell:main',
        ],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries',
        'Topic :: Utilities',
    ],
    keywords=['api', 'data', 'libs', 'cli', 'command-line', 'helper', 'kenjyco']
)
