import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

# the below install_requires is for python>=3.9
install_requires = [
    "setuptools >= 70.0.0",
    "zipp >= 3.19.1",  # vulnerability in verion version 3.15.0 and introduced with sqlalchemy
    "requests >= 2.32.2",  # vulnerability in version 2.26.0 and introduced with sdcensus, boto3, botocore, etc
    "pandas >= 1.2.3",
    "numpy <= 1.23.5",  # Pinned for compatability with DBR 12.2 LTS and 13.3 LTS
    "certifi >= 2023.7.22",
    "sdcensus >= 0.8.20",
    "us >= 2.0.2",
    "sqlalchemy >= 1.3.9",  # redundant for it is not used in the Databricks
    "matplotlib >= 3.8.2",
    "Pillow >= 10.0.1",
    "boto3 >= 1.17.43",
    "botocore >= 1.19.52",
    "python-Levenshtein >= 0.12.2",
    "fuzzywuzzy >= 0.18.0",
    "fonttools>=4.47.2",
    "psycopg2>=2.9.9",
    "pytest-mock>=3.12.0",
    "httpx>=0.26.0",
],

setuptools.setup(
    name="sdutilities",
    version="1.3.2",
    author="Stephen Olsen, Taylor Ward, McKenna Magoffin, Jaffar Shaik, Evan Tucker, Chintan Dalal",
    author_email="taylorward@sociallydetermined.com, \
                  mckennamagoffin@sociallydetermined.com, \
                  chintandalal@sociallydetermined.com",
    maintainer="Chintan Dalal",
    maintainer_email="chintandalal@sociallydetermined.com",
    description="This package is intended to implement uniformity across \
                 SD Data Science projects.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    Homepage="https://github.com/orgs/SociallyDetermined/",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: Other/Proprietary License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",
    install_requires=install_requires,
    package_data={
        "sdutilities": ["cfg_tables/grp_table_cfg.json", "cfg_tables/sample_table_cfg.json"]
    },
)
