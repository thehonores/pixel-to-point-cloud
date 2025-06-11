from pathlib import Path

from setuptools import find_packages, setup


def _parse_requirements() -> list[str]:
    path = Path(__file__).parent / "third_party/python/requirements.txt"
    with open(path, "r", encoding="utf-8") as f:
        return f.read().splitlines()


setup(
    name="oaf-vision-3d",
    version="0.1.0",
    description="Python package for OAF Vision 3D.",
    packages=find_packages(where="src/python"),
    install_requires=_parse_requirements(),
)
