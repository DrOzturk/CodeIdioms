# Docker Tutorial
We are following this tutorial: https://docs.docker.com/get-started/part2/#build-the-app

## Build Image
Build this docker image with the app, running this:
```bash
docker build -t friendlyhello .
```
See result:
```bash
docker image ls
```
## Run container with the image
Run the app, mapping your machine’s port 4000 to the container’s published port 80 using -p:
```bash
docker run -p 4000:80 friendlyhello 
```

Visit page:
```bash
curl http://localhost:4000
```

Running the app in the background, in detached mode:
```bash
docker run -d -p 4000:80 friendlyhello
```
## Manage Containers 
List the running containers:
```bash
docker container ls
```

End the process, using the CONTAINER ID from above ls, like so:
```bash
docker container stop <CONTAINER ID>
```
