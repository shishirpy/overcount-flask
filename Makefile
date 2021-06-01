pipeline-setup-test:
	pip install -U pip
	pip install wheel
	pip install -r requirements.txt
	pytest ./ --verbose

dev-setup:
	python3 -m venv venv
	source ./venv/bin/activate
	
test:
	pytest app/

verify-style: file-style
	flake8 ./app --extend-exclude=dist,build,venv --ignore F401,E402,E501 --show-source --statistics

file-style:
	flake8 main.py config.py

verify-update: test verify-style

coverage:
	coverage run -m pytest ./app
	coverage html

run:
	python overcount.py

clean:
	rm -rf ./venv
