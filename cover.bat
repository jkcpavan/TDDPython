coverage erase
coverage run -a --source ./ unit_test.py 
coverage run -a --source ./ integration-test.py 
coverage run -a --source ./ End2End-test.py

coverage html
coverage xml
coverage report -m

start chrome .\htmlcov\index.html