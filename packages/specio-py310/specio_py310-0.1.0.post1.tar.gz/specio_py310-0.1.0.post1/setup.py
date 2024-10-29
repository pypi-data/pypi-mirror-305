import os
import codecs
from setuptools import setup, find_packages

# get __version__ from _version.py
ver_file = os.path.join('specio', '_version.py')
with open(ver_file) as f:
    exec(f.read())

# get path of all data files used for testing
data_dir = [os.path.join('specio', 'core', 'tests', 'data'),
            os.path.join('specio', 'plugins', 'tests', 'data'),
            os.path.join('specio', 'tests', 'data'),
            os.path.join('specio', 'datasets', 'data')]

# recursively find the data
data_files = [(d, [os.path.join(d, f) for f in files])
              for sub_dir in data_dir
              for d, folders, files in os.walk(sub_dir)]

PACKAGES = find_packages()

CLASSIFIERS = ["Environment :: Console",
               "Intended Audience :: Science/Research",
               "License :: OSI Approved",
               "Operating System :: OS Independent",
               'Programming Language :: Python :: 2.7',
               'Programming Language :: Python :: 3.5',
               'Programming Language :: Python :: 3.6',
               'Programming Language :: Python :: 3.7',
               'Programming Language :: Python :: 3.8',
               'Programming Language :: Python :: 3.9',
               'Programming Language :: Python :: 3.10',
               'Programming Language :: Python :: 3.11',
               'Programming Language :: Python :: 3.12',
               "Topic :: Scientific/Engineering"]

description = "specio: Python input/output for spectroscopic files. A modified version of SpecIO for Python 3.10+ compatibility"
with codecs.open('README.rst', encoding='utf-8-sig') as f:
    long_description = f.read()

NAME = "specio-py310"
MAINTAINER = "Bjorn Melin"
MAINTAINER_EMAIL = "bjornmelin16@gmail.com"
DESCRIPTION = description
LONG_DESCRIPTION = long_description
LONG_DESCRIPTION_CONTENT_TYPE='text/x-rst'
URL = "https://github.com/BjornMelin/specio-py310"
DOWNLOAD_URL = "https://github.com/BjornMelin/specio-py310/archive/refs/tags/0.1.0.post1.tar.gz"
LICENSE = "BSD3"
AUTHOR = "Guillaume Lemaitre"
AUTHOR_EMAIL = "g.lemaitre58@gmail.com"
PLATFORMS = "OS Independent"
VERSION = __version__
DATA_FILES = data_files

INSTALL_REQUIRES = [
    'numpy>=1.20',  # Adjust version if needed for Python 3.10+
    'six'
]

EXTRAS_REQUIRE = {
    'tests': [
        'pytest>=6.0',  # Updated to ensure compatibility with Python 3.10+
        'pytest-cov',
        'pytest-mock'
    ],
    'docs': [
        'sphinx>=4.0',
        'sphinx-gallery',
        'sphinx_rtd_theme',
        'numpydoc',
        'matplotlib'
    ]
}

ENTRY_POINTS = {
    'console_scripts': [
        'specio=specio.cli:main'
    ]
}


opts = dict(name=NAME,
            maintainer=MAINTAINER,
            maintainer_email=MAINTAINER_EMAIL,
            description=DESCRIPTION,
            long_description=LONG_DESCRIPTION,
            long_description_content_type=LONG_DESCRIPTION_CONTENT_TYPE,
            url=URL,
            download_url=DOWNLOAD_URL,
            license=LICENSE,
            classifiers=CLASSIFIERS,
            author=AUTHOR,
            author_email=AUTHOR_EMAIL,
            platforms=PLATFORMS,
            version=VERSION,
            packages=PACKAGES,
            data_files=DATA_FILES,
            include_package_data=True,
            install_requires=INSTALL_REQUIRES,
            extras_require=EXTRAS_REQUIRE,
            entry_points=ENTRY_POINTS)


if __name__ == '__main__':
    setup(**opts)
