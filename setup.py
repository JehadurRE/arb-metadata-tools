#!/usr/bin/env python3
"""Setup configuration for ARB Metadata Tools."""

from setuptools import setup, find_packages
from pathlib import Path

# Read the README file
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding="utf-8")

setup(
    name="arb-metadata-tools",
    version="1.1.0",
    author="Md. Jehadur Rahman Emran",
    author_email="emran.jehadur@gmail.com",
    description="Automatically manage metadata in ARB (Application Resource Bundle) localization files for Flutter, Angular, Chrome extensions, and more",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/JehadurRE/arb-metadata-tools",
    project_urls={
        "Bug Tracker": "https://github.com/JehadurRE/arb-metadata-tools/issues",
        "Documentation": "https://github.com/JehadurRE/arb-metadata-tools#readme",
        "Source Code": "https://github.com/JehadurRE/arb-metadata-tools",
        "Portfolio": "https://portfolio.jehadurre.icu",
    },
    packages=find_packages(),
    py_modules=["add_arb_metadata", "add_descriptions_intelligently"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Localization",
        "Topic :: Software Development :: Internationalization",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
        "Environment :: Console",
    ],
    keywords="arb localization i18n l10n internationalization metadata automation flutter angular chrome-extension",
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "arb-metadata=add_arb_metadata:main",
            "arb-descriptions=add_descriptions_intelligently:main",
        ],
    },
    license="MIT",
    zip_safe=False,
)
