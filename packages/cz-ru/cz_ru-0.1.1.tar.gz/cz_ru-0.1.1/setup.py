from setuptools import setup


setup(
    name="cz_ru",
    version="0.1.1",
    py_modules=["cz_ru"],
    license="MIT",
    long_description="Конфиг для Commitizen на русском языке, основанный на Conventional Commits",
    url="https://github.com/teatov/cz-ru",
    install_requires=["commitizen"],
    entry_points={
        "commitizen.plugin": [
            "cz_ru = cz_ru:CzRu"
        ]
    },
)
