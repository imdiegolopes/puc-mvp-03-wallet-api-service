# Define variables
DOCKER_IMAGE_NAME = wallet_api_service_image 
DOCKER_CONTAINER_NAME = wallet_api_service_container 

export FLASK_APP=src/app/app.py
export FLASK_ENV=development
export FLASK_DEBUG=1
export FLASK_PORT=5000
export PYTHONPATH=$(shell pwd)

start:
	flask run --port=$(FLASK_PORT) --host=0.0.0.0

clean:
	rm -rf __pycache__/

# Build the Docker image
build:
		docker build -t $(DOCKER_IMAGE_NAME) .

# Run the Docker container
run:
	docker run -d -p $(FLASK_PORT):$(FLASK_PORT) --name $(DOCKER_CONTAINER_NAME) $(DOCKER_IMAGE_NAME)

# Stop and remove the Docker container
stop:
		docker stop $(DOCKER_CONTAINER_NAME)
		docker rm $(DOCKER_CONTAINER_NAME)

