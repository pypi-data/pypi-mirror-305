# sdutilities

This package is intended to implement uniformity across SD Data Science projects.

Functions and Classes that are included in this package are those frequently used across a variety of projects.  We aim to make our code simplified and uniform by continuously updating both this package and the projects where the functions are applicable.

## Note: The latest version of this package can be used only in Databricks and directly from Github.  To use this package in Databricks, follow the instructions below:
1. Use the option of installing a wheel from S3
2. Use the following uri: `s3://sdac-s3-use1-data-ocean/silver/internal/users/data_science/interim/tests/sdutilities-<version>-py3-none-any.whl` OR
3. Always install on notebook scope as shown below, and if there any pip conflicts, please use the `--force-reinstall --no-deps` option:
```
# A full install
!pip install "/dbfs/internal/users/data_science/dist/sdutilities-1.2.8.tar.gz"
 
# To install only the log module
!pip install "/dbfs/internal/users/data_science/dist/sdutilities_log-1.0.0.tar.gz"

# if there are any conflicts, use the following option
!pip install "/dbfs/internal/users/data_science/dist/sdutilities-1.2.8.tar.gz" --force-reinstall --no-deps
```