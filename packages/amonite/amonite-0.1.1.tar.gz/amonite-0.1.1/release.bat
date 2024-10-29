REM Create a venv if not already there.
CALL py -m venv .

REM Activate the venv.
CALL ./Scripts/activate.bat

REM Install or upgrade build.
CALL py -m pip install --upgrade build
REM Build the release.
CALL py -m build

REM Install or upgrade twine.
CALL py -m pip install --upgrade twine
REM Release to PyPi.
REM python3 -m twine upload --repository pypi dist/*
CALL py -m twine upload dist/*

REM Install the package from testPyPi.
REM python3 -m pip install --index-url https://test.pypi.org/simple/ --no-deps amonite-mathorga