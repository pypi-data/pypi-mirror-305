from setuptools import setup, find_packages

setup(
    name="optima-cli",
    version="1.0.0",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    include_package_data=True,
    package_data={
        'optima': ['unimelb-mf-clients-0.7.8/**/*'],
    },
    install_requires=[
        "click>=8.1.0",
        "python-dotenv>=0.19.0",
        "requests>=2.32.0",
        "setuptools>=74.1.0",
    ],
    entry_points={
        "console_scripts": [
            "op=optima.cli:cli",
        ],
    },
    author="Ashley Wang",
    author_email="xiaohuyaw@gmail.com",
    description="OPTIMA CLI",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Environment :: Console", 
    ],
    python_requires=">=3.11",
)