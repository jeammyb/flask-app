# flask-app
Flask application sample and its docker image definition.

[![](https://images.microbadger.com/badges/image/jeammyb/flask-app.svg)](https://microbadger.com/images/jeammyb/flask-app "Get your own image badge on microbadger.com")

## Run application locally
Go to the main folder and execute the following command:
```
python app.py
```

## Run application inside a Docker container
#### Build Docker image:

`make build`


#### Run container:

`make run`

#### To download the image and run container:
`docker container run -d -p 5000:5000 --name flask jeammyb/flask-app:latest`

## URL Examples

`http://localhost:5000`

Or

Format: `http://localhost:5000/hello/{name}`

`http://localhost:5000/hello/jeammy`
