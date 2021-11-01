# What is this?

This example implements a movie search application with Atlas Search and deploys it using Opta. It is based on the [this blog post](https://www.mongodb.com/developer/how-to/build-movie-search-application/); but with some notable differences:
  1. Opta handles the creation of the Atlas database, passing its credentials into the application code
  2. Instead of Atlas Realm, this example uses a simple Flask API backend and deploys it on to a Kubernetes cluster; don't worry - you won;'t have to spin up the Kubernetes cluster yourself, Opta will do it for you in the cloud of your choice or even your local machine!
   
Atlas is currently supported in Local and AWS Opta environments. Feel free to open a Github issue if you would like to see support in GCP or Azure.

Lets get started!

## Setup

Clone this repository and use the Opta files in the `opta` sub-directory as a starting point. You will need your AWS and Atlas API credentials for spinning up a Kubernetes cluster and API keys for the [Atlas Mongo API](https://docs.atlas.mongodb.com/tutorial/manage-programmatic-access/). You do not need to configure the IP address in the API key, Opta will do that for you.

After you have downloaded these keys from the AWS console and Atlas Mongo GUIs, set them as environment variables in the terminal shell where you plan to run Opta.

```bash
# Atlas Mongo
export MONGODB_ATLAS_PUBLIC_KEY="abcdefghij"
export MONGODB_ATLAS_PRIVATE_KEY="1234015e-4503-4f95-f129-543d4e58bsdg"

# AWS 
export AWS_ACCESS_KEY_ID=AXSDFTRFFSDQAZA
export AWS_SECRET_ACCESS_KEY=ASdlksfja234sadfbjsdfgsdfg34SAD34fd
```

Next, we create the Opta environment with the AWS EKS Kubernetes cluster, as [documented here](https://docs.atlas.mongodb.com/tutorial/manage-programmatic-access/).

__Note: If you are only trying this out on your local machine, append the `--local` flag to all the opta commands so that a local Kubernetes cluster is spun up on your machine rather than the AWS EKS cluster. The Atlas Cluster will still be spun up as usual in the cloud__


Once we have the Kubernetes cluster, we can create the MongoDB application by running opta apply on the `opta/atlasmongoservice.yaml` file. Remember to set the  `mongo_atlas_project_id` in this file before running Opta.

```bash

opta apply -f atlasmongoservice.yaml

```

After a few minutes, the application will be running against the new Atlas Mongo cluster.

Before you can use the application, follow [steps 1 and 2](https://www.mongodb.com/developer/how-to/build-movie-search-application/#step-1.-spin-up-atlas-cluster-and-load-movie-data) in the original Mongodb tutorial in order to load the sample data and setup the search index in the Atlas Mongo database.

Once you are done, point your browser to the ELB load balancer (or http://localhost:8080/ in case you are using Opta Local) and search the movie database!


