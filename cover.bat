coverage erase
coverage run -a --source ./ unit_test.py 
coverage run -a --source ./ integration-test.py 
coverage run -a --source ./ End2End-test.py

coverage html
coverage xml
coverage report -m --fail-under=100
pylint qrcodepkg --rcfile=.pylintrc
pylint qrrelation --rcfile=.pylintrc

start chrome .\htmlcov\index.html