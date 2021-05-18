hello:
	echo "Check the pipeline, the best engineer has just arrived"
install:
	pip3 install --upgrade pip &&\
		pip3 install -r requirements.txt

all: hello install