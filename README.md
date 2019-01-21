# flask-app
Flask application sample and its docker image definition.

# Run application locally
Go to the main folder and execute the following command:
```
python app.py
```

# Run application inside a Docker container
## Build Docker image

`make build`


## Run container

`make run`


## URL Examples

`http://localhost:5000`

Or

Format: `http://localhost:5000/hello/{name}`

`http://localhost:5000/hello/jeammy`
