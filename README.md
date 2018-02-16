# ops-dashboard

Operations Dashboard using Django. For now this is nothing more than a dummy django application used to figure out kubernetes deployment workflows.

Directory structure:

```
opsdash     django-created project
deploy      deployment scripts
```

## deploy

### Preparation

- Install docker
- Install google cloud SDK
- Install kubectl
- Install minikube (preferable using a virtualbox VM)
- Install helm
- Use the minikube docker daemon so that docker builds done locally can be used by minikube:
  
  `eval $(minikube docker-env)` 
  
  in fish: `eval (minikube docker-env`

### Minikube

- Set kubectl context to use minikube:

  `kubectl config use-context minikube`

- Deploy using helm chart:

  `helm install --debug ./deploy/charts/myopsdash/ --set service.type=NodePort`

- To list the helm releases:

  `helm ls`

- To open minikube dashboard in a browser

  `minikube dashboard`

- To delete a helm release:

  `helm del --purge <DEPL_NAME>` 



### gke

