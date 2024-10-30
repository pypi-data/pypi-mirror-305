## Recently fixed issues
- [x] logger.py uses pyspark.dbutils which makes the package unusable outside of Databricks. Fix it, by either removing the dependency or making it optional.Fixed by adding dbutils wrapper in logger.py
- [x] All logger related functions that were added in the last commit had package issues during local testing and are now fixed, added to setup.py, and tested via test_package_compatability.py
- [x] Reintroduce the databricks-sdu packages to setup.py safely so that databricks does not cause pip install compatibility issues.
- [x] Remove hardcoded SDLogger save path in databricks and use only os environment in logger.
- [x] Add how to contribute to this repo, i.e., rules of contribution, e.g., add tests, add docstrings, etc.
- [x] Isolate the logger functions into a separate module so that they can be imported individually.

## Backlog
- [ ] Test futures.logger with the code that uses it.
- [ ] Remove build folder which is created when running `python setup.py bdist_wheel`
- [ ] Create isolated module for each function in the package so that they can be imported individually.
- [ ] Modernize build process to use toml files instead of setup.py
- [ ] Add coverage testing
- [ ] Coverage testing increase to 100%