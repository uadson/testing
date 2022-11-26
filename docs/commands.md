pytest .
pytest <path_name>
pytest -v
pytest -x "stop on first asserterror"
pytest --pdb "debbuger"
pytest -k filter results

messages:

. -> passed
F -> fail
x -> expected fail
X -> expected fail but not fail
s -> skiped

reports:

pytest --junitxml report.xml
