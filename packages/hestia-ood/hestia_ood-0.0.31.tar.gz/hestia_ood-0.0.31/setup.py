#!/usr/bin/env python

"""The setup script."""
from setuptools import setup, find_packages
from pathlib import Path


this_directory = Path(__file__).parent
readme = (this_directory / "README.md").read_text()

requirements = [
    'networkx',
    'scipy',
    'scikit-learn',
    'pandas',
    'numpy',
    'tqdm'
]

test_requirements = requirements

setup(
    author="Raul Fernandez-Diaz",
    author_email='raul.fernandezdiaz@ucdconnect.ie',
    python_requires='>=3.9',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
    description="Suite of tools for analysing the independence between training and evaluation biosequence datasets and to generate new generalisation-evaluating hold-out partitions",
    entry_points={
    },
    install_requires=requirements,
    license="MIT",
    long_description=readme + '\n\n',
    include_package_data=True,
    keywords='hestia',
    data_files=[('hestia/utils/mmseqs_fake_prefilter.sh')],
    name='hestia-ood',
    packages=find_packages(),
    long_description_content_type="text/markdown",
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/IBM/Hestia-OOD',
    version='0.0.31',
    zip_safe=False,
)
