from setuptools import find_packages, setup

setup(
    name="pyarch",
    description="PyArch desktop client",
    version="0.1-beta",
    author="Jay Godara",
    entry_points={
        "console_scripts": [
            "pyarch = pyarch:main"
        ]
    }
)
