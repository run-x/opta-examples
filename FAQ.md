# Can I use the cluster for other Opta services?
Yup! Opta was initially designed to split between one "environment" manifest holding all the networking & cluster setup
and many different "services" built on top of the environment. However, it is possible to have an environment and
service in a single yaml, and to keep things simple that's what is being done in many places in this repo. You can still create services
pointing to the lone yaml here as the "environment" (even though it deploys what can be considered a service as well),
but we'd still advise you to break the current yaml to an environment and service manifest when you feel ready just
to keep things clean.