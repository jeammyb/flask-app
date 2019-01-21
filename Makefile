default: build

IMAGE_FULL_NAME = flask-app:latest

build:
	docker build -t ${IMAGE_FULL_NAME} .

run:
	docker container run -d -p 5000:5000 --name flask ${IMAGE_FULL_NAME} 

clean:
	docker stop flask || true
	docker rm flask || true
	docker rmi flask-app:latest