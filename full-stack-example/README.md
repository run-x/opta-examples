# What is in Here

This full stack example implements a todo list. This folder contains the following sub-folders:
* Code for an API backend written in Django Web Framework with a Postgres database 
* Code for a single-page-application that implements the todo list frontend, written in Vuejs
* Infrastructure-as-code via Opta yaml files and Dockerfiles to deploy the application into a provider
* Opta-based helm installation of the Prometheus/Grafana observability stack  

# Running the Example

You can build and run the example like so (all paths are relative to this git repository's root directory):

### Build the code docker images:

```bash
# Django API

docker build full-stack-example/api/todo-python-django/ --tag todo-api:v1

# Single page application Vuejs Frontend
docker build full-stack-example/frontend/todo-vuejs --tag todo-frontend:v1
```

## Deploy to Local Opta

Deploy the example to a Kubernetes cluster on your local machine. This will create a [Kubernetes Kind cluster](https://kind.sigs.k8s.io/docs/user/quick-start/) and deploy the example on it.  

```bash

# API
opta deploy --image todo-api:v1 --config full-stack-example/api/todo-python-django/opta/opta-api-service.yml --auto-approve --local

# Frontend
opta deploy --image todo-frontend:v1 --config full-stack-example/frontend/todo-vuejs/opta/opta-frontend-service.yml --auto-approve --local

```

Optionally, deploy the Prometheus-Grafana observability stack to monitor the infrastructure, like so

```bash
#Monitoring

#We copy the values file to /tmp because we need an absolute path for the helm chart
cp full-stack-example/monitoring/prometheus-grafana-monitoring-stack-values.yaml /tmp
opta apply --config full-stack-example/monitoring/opta-prometeus-grafana.yml --auto-approve --local

```



After the deployments are complete you can open your web-browser to see the Todo application [frontend](localhost:8080/frontend) and [API backend](http://localhost:8080/djangoapi/apis/v1/). Try adding some items to your todo list frontend and observe the data being stored in the backend API view.

You can also open the [Grafana server gui](http://localhost:8080/grafana) and login using the credentials `admin`/`prom-operator`. After you enable some Kubernetes dashboards, you may need to wait a few minutes for the data to show up.

## Deploy to AWS, GCP or Azure

Coming soon!

# Credits

This example is derived from the [Kubernetes Automation Toolkit](https://github.com/BigBitBusInc/kubernetes-automation-toolkit), an open-source learning resource by [BigBitBus Inc](https://www.bigbitbus.com/). 