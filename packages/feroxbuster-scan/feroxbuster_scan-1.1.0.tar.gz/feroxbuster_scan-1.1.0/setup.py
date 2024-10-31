from setuptools import setup, find_packages

setup(
    name="feroxbuster-scan",  # Package name
    version="1.1.0",  # Version number
    author="Adithya A N",  # Author name
    author_email="your_email@example.com",  # Author email (optional)
    description="A tool to download, run, and generate reports for Feroxbuster scans",  # Short description
    long_description=open('README.md').read(),  # Include README for long description
    long_description_content_type='text/markdown',  # Indicate that the long description is in Markdown format
    packages=find_packages(),  # Automatically find packages in the project
    install_requires=[  # Package dependencies
        "requests",
    ],
    entry_points={  # Entry points for command line scripts
        "console_scripts": [
            "feroxbuster-scan = feroxbuster_scan.feroxbuster_scan:main",
        ],
    },
    classifiers=[  # Classifiers for package metadata
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",  # Specify Python version requirements
)
