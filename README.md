# Flask/Python Service Template

This is a template for building modular web services with a
best-practice organization of files, build environment, static
analysis etc. The template can be used as a starting point for
creating your own services.

## Visual Studio Code extensions
   * Docker: ms-azuretools.vscode-docker
   * Swagger Viewer: arjun.swagger-viewer
   * OpenAPI Preview: zoellner.openapi-preview
   * Remote - Containers:  ms-vscode-remote.remote-containers
   * Python - ms-python.python
   
Recommended:
   * Live Share: ms-vsliveshare.vsliveshare
   * YAML: redhat.vscode-yaml


## Run in local environment

	$ python3 -m venv env
	$ source env/bin/activate
	$ pip install -r requirements.txt
	$ pip install -r requirements-test.txt
	
	$ export FLASK_APP=wsgi.py
	$ export FLASK_ENV=development
	$ flask run


## Run in docker

Build the development target, either from the command line or by the
Docker plugin in Visual Studio Code (from VSC Right Click on the
Dockerfile and select "Build Image..."

	docker build --rm -q -f Dockerfile \
		--label "sintef.testservice-target=development" \
		--target development \
		-t "sintef/testservice-development:latest" .


### Run from the VSC envionment

From VSC reopen the folder in Container ('F1' | Remote-Containers: Open
Folder in Container)


### Run from command line

	docker run -it --rm -d -p 5000:5000 sintef/testservice-development:latest

