from setuptools import setup, find_packages

setup(
    name="feroxbuster-scan",
    version="0.1.0",
    author="Your Name",
    description="A tool to download, run, and generate reports for Feroxbuster scans",
    packages=find_packages(),
    install_requires=[
        "requests",
    ],
    entry_points={
        "console_scripts": [
            "feroxbuster-scan = feroxbuster_scan.feroxbuster_scan:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
