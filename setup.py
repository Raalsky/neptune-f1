from setuptools import setup

base_requirements = []

develop_requirements = [
    "pre-commit",
    "pytest",
]

setup(
    name="neptune-f1",
    version="0.1.0",
    packages=["neptune_f1"],
    url="https://github.com/Raalsky/neptune-f1",
    license="MIT",
    author="raalsky",
    author_email="raalsky@gmail.com",
    description="EA F1 2021 telemetry integration with Neptune.ai",
    install_requires=base_requirements,
    extras_require={"dev": develop_requirements},
)
