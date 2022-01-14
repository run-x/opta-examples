# What is this?

This is an example [opta](https://github.com/run-x/opta) configuration file to deploy [Retool](https://retool.com/) on AWS.

You can also use this button to fill in the variable fields in the config.

[![Deploy to AWS](https://raw.githubusercontent.com/run-x/opta/main/assets/deploy-to-aws-button.svg)](https://app.runx.dev/deploy-with-aws?url=https%3A%2F%2Fgithub.com%2Frun-x%2Fopta-examples%2Fblob%2Fmain%2Fretool%2Fretool-aws.yaml&name=Retool)


# What does this do?
It deploys a single container version of retool on EKS in AWS. It uses AWS managed RDS instances and elasticcache. It also sets up various other resources like VPCs, subnets, load balancers etc.

# Steps to deploy
* Fill in the required variables in the config file
* Run `opta apply -c retool-aws.yaml` on the config file

That's it. Retool is deployed on AWS. You can find the AWS load balancer URL to access the deployment by running `opta output`

To get DNS to work follow the next section

# Getting DNS to work
* Run `opta output -c retool-aws.yaml` to get the nameservers. You will see a section like this:
```yaml
name_servers = tolist([
  “ns-1384.awsdns-45.org”,
  “ns-2001.awsdns-58.co.uk”,
  “ns-579.awsdns-08.net”,
  “ns-83.awsdns-10.com”,
])
```
* Go to your domain registrar (link namecheap, godaddy, etc.) to point the domain to these nameservers.
* Update `delegated` field to `true` in the `retool-aws.yaml` file
* Run `opta apply -c retool-aws.yaml` again to generate the TLS certificate

Your domain should now be pointing to the retool deployment with secure TLS

# Can I use the cluster for other Opta services?
Yup! Opta was initially designed to split between one "environment" manifest holding all the networking & cluster setup
and many different "services" built on top of the environment. However, it is possible to have an environment and
service in a single yaml, and to keep things simple that's what is being done here. You can still create services
pointing to the lone yaml here as the "environment" (even though it deploys what can be considered a service as well),
but we'd still advise you to break the current yaml to an environment and service manifest when you feel ready just
to keep things clean.