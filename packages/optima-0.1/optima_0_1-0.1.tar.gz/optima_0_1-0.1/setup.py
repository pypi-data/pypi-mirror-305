from setuptools import setup, find_packages

setup(
    name="optima-0.1",
    version="0.1",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    include_package_data=True,
    install_requires=[
        "click==8.1.7",
        "python-dotenv==1.0.1",
        "Requests==2.32.3",
        "setuptools==74.1.2",
    ],
    entry_points={
        "console_scripts": [
            "op=cli:cli",
        ],
    },
)