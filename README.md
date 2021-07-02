# Flask Hello example !!

This application changes the background color based on environment variable APP_COLOR, if environment variable is not present it will take random color.

And it reads the environment name from a file `/config/environment-name` if file is not present it will read from environment variable `ENVIRONMENT_NAME` and even if environment variable is not present it will take default value `default`

And you can change the background color by `http://ip-address:port-no/color/red`

And you can read the file `/config/environment-name` from UI from `http://ip-address:port-no/read-file`

### Building the application
```
docker built -t flaskapp .
```

### Running the application using newly created image
```
docker run -d -p 8081:5000 flaskapp
```

### Running the application by passing the color as environment variable
```
docker run -d -e APP_COLOR=red -p 8081:5000 flaskapp
```

### If you dont want to build docker image and you want to directly run the application
```
docker run -d -e APP_COLOR=red -p 8081:5000 vigneshsweekaran/helloworld-flask:latest
```

### Branch details
* master --> All latest changes are avialble here.
* arm64 --> This branch you can use if you want to run the docker container in `arm64` architecture servers.