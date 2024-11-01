import os
from setuptools import setup

dir_path = os.path.dirname(os.path.realpath(__file__))
filepath = os.path.join(dir_path, "README.md")
with open(filepath, encoding="utf-8") as f:
    readme = f.read()

setup(
    name="cz_ru",
    version="0.1.2",
    py_modules=["cz_ru"],
    license="MIT",
    long_description=readme,
    url="https://github.com/teatov/cz-ru",
    install_requires=["commitizen"],
    entry_points={
        "commitizen.plugin": [
            "cz_ru = cz_ru:CzRu"
        ]
    },
)
