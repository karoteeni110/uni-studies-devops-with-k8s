# The project

## 1.4 Step 2: Create deployment.yaml for the course project

How to deploy with the local image:

```
docker build -t todo-app:latest .
kubectl get deployments todo-app-dep 
```

Output:

```
$ docker run todo-app:latest # Test the docker locally
Server started in port 8000

$ kubectl logs todo-app-dep-7b9f6464cd-nv7qh
Error from server: Get "https://172.18.0.4:10250/containerLogs/default/todo-app-dep-7b9f6464cd-nv7qh/todo-app": proxy error from 127.0.0.1:6443 while dialing 172.18.0.4:10250, code 502: 502 Bad Gateway
```
