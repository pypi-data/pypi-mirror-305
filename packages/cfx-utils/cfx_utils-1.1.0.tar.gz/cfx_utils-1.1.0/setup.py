#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import (
    setup,
    find_packages,
)

extras_require = {
    'test': [
        "pytest>=8,<9",
        # "pytest-xdist",
        # "tox>=2.9.1,<3",
        "cfx-address>=1.2.0",
    ],
    'lint': [
        # "flake8==3.8.3",
        # "isort>=4.2.15,<5",
        # "mypy"  # we use pylance to check type because there is bug to use mypy Self
        # "pydocstyle>=3.0.0,<4",
    ],
    'doc': [
        # "sphinx>=4.2.0,<5",
        # "sphinx_rtd_theme>=0.1.9",
        # "towncrier>=21,<22",
    ],
    'dev': [
        "bumpversion>=0.5.3,<1",
        # "pytest-watch>=4.1.0,<5",
        "wheel",
        "twine",
        "ipython",
    ],
}

extras_require['dev'] = (
    extras_require['dev'] +  # type: ignore
    extras_require['test'] +  # noqa: W504
    extras_require['lint'] +  # noqa: W504
    extras_require['doc']
)


with open('./README.md') as readme:
    long_description = readme.read()


setup(
    name='cfx-utils',
    # *IMPORTANT*: Don't manually change the version here. Use `make bump`, as described in readme
    version='1.1.0',
    description="""cfx-utils: Common utils for conflux python packages""",
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Conflux-Dev',
    author_email='wenda.zhang@confluxnetwork.org',
    url='https://github.com/conflux-fans/cfx-utils',
    include_package_data=True,
    python_requires='>=3.7',
    install_requires=[
        # "cfx-address>=1.0.0b1",
        "typing_extensions>=4.2.0",
        "hexbytes",
        "eth-typing>=2.0.0",
        # "eth-utils>=5.0.0",
    ],
    extras_require=extras_require,
    py_modules=['cfx_utils'],
    license="MIT",
    zip_safe=False,
    keywords='conflux',
    packages=find_packages(exclude=["tests", "tests.*"]),
    package_data={'cfx_utils': ['py.typed']},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
)