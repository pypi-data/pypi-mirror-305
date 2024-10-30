# If issues related to python package version compatibility arise, follow the steps below to fix them:

0. To make changes next time do the following to check the package locally first:
1. Check recommendations
2. Delete all of its PR
3. Update the code associated with the vulnerabilities
4. python -m venv <path>/test_venv
5. source <path>test_venv
6. cd <path>/sdutilities_package
7. python setup.py sdist
8. pip install dist/sdutilities-1.2.<new version>.tar.gz
9. python -c "import sys;print(sys.executable); import sdutilities;"  
10. (check the packages and its version) pip freeze
11. If there is no error, than the distribution is portable!
12. Finally, as soon on creates a PR to main, the Synk test runner starts, and if it shows passed then its ready for a peer review.
