# What is in Here

This example implements a movie search application with Atlas Search and deploys it using Opta. It is based on the [this blog post](https://www.mongodb.com/developer/how-to/build-movie-search-application/); but with some notable differences:
  1. Opta handles the creation of the Atlas database, passing its credentials into the application code
  2. Instead of Atlas Realm, this example uses a simple Flask API backend and deploys it on to a Kubernetes cluster; don't worry - you won;'t have to spin up the Kubernetes cluster yourself, Opta will do it for you in the cloud of your choice or even your local machine!
   

Lets get started!



