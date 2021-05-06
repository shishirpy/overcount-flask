pipeline-setup-test:
	pip install -U pip
	pip install wheel
	pip install -r requirements.txt
	pytest ./ --verbose

test:
	pytest ./

verify-style: file-style
	flake8 ./app --extend-exclude=dist,build,venv --ignore F401,E402,E501 --show-source --statistics

file-style:
	flake8 main.py config.py

verify-update: test verify-style

coverage:
	coverage run -m pytest ./app
	coverage html

clean:
	rm -rf ./venv
