# The project

## 1.5 Step 3: Port forwarding

How to deploy with the local image:

```
docker build -t todo-app:latest . # Update the image
k3d image import todo-app:latest # Update the container
kubectl apply -f manifest/deployment.yaml # Deploy the update
```

Output:

```
$ kubectl port-forward todo-app-dep-689b56b9b9-7xx4h 8000:8000
Forwarding from 127.0.0.1:8000 -> 8000
Forwarding from [::1]:8000 -> 8000
Handling connection for 8000

$ curl http://localhost:8000/ # Use another terminal
{"message":"Hello, World!"}
```
