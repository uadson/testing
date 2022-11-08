# testing
My tests repository studies

[![Build](https://github.com/uadson/testing/actions/workflows/build.yml/badge.svg?branch=main)](https://github.com/uadson/testing/actions/workflows/build.yml)
[![Tests](https://github.com/uadson/testing/actions/workflows/tests.yml/badge.svg?branch=main)](https://github.com/uadson/testing/actions/workflows/tests.yml)
[![codecov](https://codecov.io/gh/uadson/testing/branch/main/graph/badge.svg?token=FKKTAZMMBP)](https://codecov.io/gh/uadson/testing)



<a href="https://codecov.io/gh/uadson/testing" > 
 <img src="https://codecov.io/gh/uadson/testing/branch/main/graphs/sunburst.svg?token=${{ secrets.GRAPH }}"/> 
</a>

##### running tests - overview

commands:

	- command main
		pytest 

	- specific
		pytest <path>

	- with previews of test files
		pytest -v
	
	- identifying test files without running them
		pytest --collect-only (without running test)

	- viewing test coverage

		pytest --cov=<path> or pytest --cov= .
