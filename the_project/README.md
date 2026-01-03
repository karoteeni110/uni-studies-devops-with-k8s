# The project

## 1.6. The project, step 4: Use a NodePort Service to enable access to the project.

How to deploy with the local image:

```bash
k3d cluster delete # Clean up the clusters before
k3d cluster create --port 8765:30088@agent:0 -p 7654:80@loadbalancer --agents 2 # Create a new cluster

docker build -t todo-app:latest . # Update the image
k3d image import todo-app:latest # Update the container
kubectl apply -f manifests/deployment.yaml # Deploy the update
kubectl apply -f manifests/service.yaml # Deploy the port forwarding service
```

Output:

```
$ kubectl logs deployments/todo-app-dep 
Server started in port 8000

$ curl http://localhost:8765/
{"message":"Hello, World!"}
```
