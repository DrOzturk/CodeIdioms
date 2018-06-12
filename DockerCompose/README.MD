# Docker Compose
Based on:
https://docs.docker.com/compose/overview/
- Define and run multi-container Docker applications. 
- Use a YAML file to configure your application’s services. 

## docker-compose.yml format
More: https://docs.docker.com/compose/compose-file/

## Start all 

```bash
docker-compose up
```
See images:
```bash
docker image ls
```

See containers:
```bash
docker container ls -a
```

See processes:
```bash
docker ps
```

## Access Service
```bash
curl http://0.0.0.0:5000/
```
or Visit in your browser:
[http://localhost:5000](http://localhost:5000) or [http://0.0.0.0:5000](http://0.0.0.0:5000)

