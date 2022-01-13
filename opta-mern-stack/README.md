## Introduction

MongoDB (Database persistence layer) + Nodejs/express (API) + React (Frontend SPA) is the popular MERN application development stack. In this post we show how you can use Opta to easily stand up this stack on a public cloud (gcp/aws) or Local development Kubernetes cluster. Follow through this post and here is what you will get:

1. An [AWS eks/Google cloud gke/Local PC Kind] Kubernetes cluster built to SOC2 security standards

2. A React single page app, containerized to run in your Kubernetes cluster

3. A Nodejs + Express app, containerized to run in your Kubernetes cluster

4. A MongoDB Atlas cluster to serve as the persistent database layer

We have adopted a fairly simple application example here to show you how to containerize your MERN stack.

And, perhaps most importantly, a couple of infrastructure-as-code Opta yaml files to do all the heavy-lifting with Opta's legendry HCL-free-Terraform magic. Lets get started!

## Pre-requisites

Opta is a new kind of Infrastructure-As-Code framework where you work with high-level constructs instead of getting lost in low level cloud configuration or having to deal with [Terraform HCL](https://blog.runx.dev/my-pet-peeves-with-terraform-f9bb37d94950). For our MERN stack example Opta will setup all the production-grade infrastucture using a couple of short yaml files!

Our MERN stack example is based on the application code created by The MongoDB Atlas team. Their [blog post](https://www.mongodb.com/languages/mern-stack-tutorial) will walk you through the Nodejs+Express backend, React frontend and MongoDB setup. You should take a moment to read the blog post, although keep in mind that most of the manual/click-on-GUI steps mentioned in the post are not applicable to this Opta Infrastructure-as-code MERN stack example.


## On your PC




Get the API end point
```
opta output -c opta-mern-server.yaml

    "load_balancer_raw_dns": "opta-atlassearchenv3-lb-d60e914f75283cca.elb.us-east-1.amazonaws.com"
}
```


# Credits
The application frontend and backend is largely derived from the [MERN
stack tutorial](https://www.mongodb.com/languages/mern-stack-tutorial) by the folks at Mongodb.com.

