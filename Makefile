hello:
	echo "Check the pipeline, the best engineer has just arrived"
install:
	pip3 install --upgrade pip &&\
		pip install requirements.txt
test:
	python3 -m pytest -vv test_udacity.py

all: hello install