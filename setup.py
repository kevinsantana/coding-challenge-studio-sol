# Source: https://packaging.python.org/guides/distributing-packages-using-setuptools/

from os import path
from valid_password import __version__
from setuptools import find_packages, setup

run_requirements = [
    "alabaster==0.7.13",
    "anyio==3.6.2",
    "attrs==22.2.0",
    "Babel==2.11.0",
    "certifi==2022.12.7",
    "charset-normalizer==3.0.1",
    "click==8.1.3",
    "commonmark==0.9.1",
    "docutils==0.17.1",
    "exceptiongroup==1.1.0",
    "fastapi==0.89.1",
    "gunicorn==20.1.0",
    "h11==0.14.0",
    "idna==3.4",
    "imagesize==1.4.1",
    "iniconfig==2.0.0",
    "Jinja2==3.1.2",
    "loguru==0.6.0",
    "MarkupSafe==2.1.2",
    "packaging==23.0",
    "pluggy==1.0.0",
    "pydantic==1.10.4",
    "Pygments==2.14.0",
    "pytest==7.2.1",
    "pytz==2022.7.1",
    "recommonmark==0.7.1",
    "requests==2.28.2",
    "sniffio==1.3.0",
    "snowballstemmer==2.2.0",
    "Sphinx==5.3.0",
    "sphinx-rtd-theme==1.1.1",
    "sphinxcontrib-applehelp==1.0.4",
    "sphinxcontrib-devhelp==1.0.2",
    "sphinxcontrib-htmlhelp==2.0.1",
    "sphinxcontrib-jsmath==1.0.1",
    "sphinxcontrib-qthelp==1.0.3",
    "sphinxcontrib-serializinghtml==1.1.5",
    "starlette==0.22.0",
    "tomli==2.0.1",
    "typing_extensions==4.4.0",
    "urllib3==1.26.14",
    "uvicorn==0.20.0",
    "uvloop==0.17.0",
]

here = path.abspath(path.dirname(__file__))

with open(path.join(here, "README.md"), encoding="utf-8") as readme:
    long_description = readme.read()

setup(
    name="Valid Password Api",
    version=__version__,
    author="Kevin de Santana Araujo",
    author_email="kevin_santana.araujo@hotmail.com",
    packages=find_packages(exclude=["docs", "tests"]),
    url="https://github.com/kevinsantana/coding-challenge-studio-sol",
    description="REST Api to check valid password rules",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=run_requirements,
    python_requires=">=3.10.8",
)
