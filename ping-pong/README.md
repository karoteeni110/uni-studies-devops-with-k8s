# Ping-pong app

## Exercise 1.9. More services

Clean up the old cluster:

```bash
k3d cluster delete
k3d cluster create --port 8082:30080@agent:0 -p 8081:80@loadbalancer --agents 2
```

How to deploy ping-pong:

```bash
docker build -t ping-pong:latest . # Use local image
k3d image import ping-pong:latest
kubectl apply -f ./manifests/deployment.yaml
kubectl apply -f ./manifests/service.yaml
kubectl apply -f ./manifests/ingress.yaml
```

Output:

```bash
$ curl localhost:8081/pingpong
"pong 1"
$
$
$ curl localhost:8081/pingpong
"pong 2"
$
$
$ curl localhost:8081/pingpong
"pong 3"
```