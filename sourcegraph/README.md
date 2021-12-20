# What is this?

This is an example [opta](https://github.com/run-x/opta) configuration file to deploy sourcegraph on AWS.

You can also use this button to fill in the variable fields in the config.

[![Deploy to AWS](https://raw.githubusercontent.com/run-x/opta/main/assets/deploy-to-aws-button.svg)](https://app.runx.dev/deploy-with-aws?url=https%3A%2F%2Fgithub.com%2Frun-x%2Fopta-examples%2Fblob%2Fmain%2Fsourcegraph%2Fsourcegraph.yaml&name=Sourcegraph)


# What does this do?
It deploys a single container version of sourcegraph on EKS in AWS. It uses AWS managed RDS instances and also sets up various other resources like VPCs, subnets, load balancers etc.

# Steps to deploy
* Fill in the required variables in the config file
* Run `opta apply -c sourcegraph.yaml` on the config file

That's it. Sourcegraph is deployed on AWS. You can find the AWS load balancer URL to access the deployment by running `opta output`

To get DNS to work follow the next section

# Getting DNS to work
* Run `opta output -c sourcegraph.yaml` to get the nameservers. You will see a section like this:
```yaml
name_servers = tolist([
  “ns-1384.awsdns-45.org”,
  “ns-2001.awsdns-58.co.uk”,
  “ns-579.awsdns-08.net”,
  “ns-83.awsdns-10.com”,
])
```
* Go to your domain registrar (link namecheap, godaddy, etc.) to point the domain to these nameservers.
* Update `delegated` field to `true` in the `sourcegraph.yaml` file
* Run `opta apply -c sourcegraph.yaml` again to generate the TLS certificate

Your domain should now be pointing to the sourcegraph deployment with secure TLS