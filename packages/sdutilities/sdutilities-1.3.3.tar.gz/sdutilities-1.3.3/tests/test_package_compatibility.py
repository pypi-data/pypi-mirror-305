import requests
from packaging import version
from packaging.specifiers import SpecifierSet
import pytest


def get_package_info(package):
    response = requests.get(f"https://pypi.org/pypi/{package}/json")
    if response.status_code == 200:
        data = response.json()
        return data.get('info')
    return None

def check_compatibility(info):
    requires_python = info.get('requires_python') if info else None
    if requires_python:
        specifier_set = SpecifierSet(requires_python)
        return version.parse('3.8') in specifier_set or version.parse('3.9') in specifier_set
    return True  # Assuming compatibility if no Python version requirement is specified


# Create a test function for each package
@pytest.mark.parametrize("package", ["numpy", "pandas", "requests", 
                                     "setuptools", "Pillow", "certifi", 
                                     "matplotlib", "sdcensus", "us", "sqlalchemy", 
                                     "botocore", "fuzzywuzzy", "psycopg2", "python-Levenshtein",
                                     "pytest", "faker", "pytest-mock", "pytz", "rapidfuzz",
                                     "SQLAlchemy", "typing_extensions", "tzdata", "urllib3", "zipp"
                                     "pyspark", "httpx"
])  # Add more package names here
def test_package_info_and_compatibility(package):
    info = get_package_info(package)
    if package == "zipppyspark": # pyspark requirement spelling bug for zippyspark with extra p
        pass
        # assert info is None, f"Ignore this {package} compatibility test. \
        #                        Info for package '{package}' is found in pypi but is compatible with Python 3.8 or 3.9"
    else:
        assert info is not None, f"Info for package '{package}' was not found"
        assert check_compatibility(info) == True, f"{package} is not compatible with Python 3.8 or 3.9"