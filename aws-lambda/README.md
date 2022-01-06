# What is this?

This is an example [opta](https://github.com/run-x/opta) configuration file to deploy a simple lambda function on AWS that handles API calls from the internet.

# What does this do?
It deploys a simple [python lambda function](https://github.com/awsdocs/aws-doc-sdk-examples/blob/main/python/example_code/lambda/lambda_handler_rest.py) with AWS API Gateway. It also sets up various other resources like VPCs, subnets.

# Steps to deploy
* Fill in the following required variables in the config file
  * org_name
  * account_id
* Create a zip file for your lambda.
```bash
zip my-deployment-package.zip lambda_function.py
```
Checkout [AWS docs](https://docs.aws.amazon.com/lambda/latest/dg/python-package.html) on how to package more complex lambdas
* Run `opta apply`

That's it. AWS lambda is deployed. You will see an output like this.

```
cloudwatch_log_group_name = "/aws/lambda/opta-lambdafunction-b0bf"
cloudwatch_log_group_url = "https://console.aws.amazon.com/cloudwatch/home?region=us-east-1#logsV2:log-groups/log-group/%2Faws%2Flambda%2Fopta-lambdafunction-b0bf"
function_arn = "arn:aws:lambda:us-east-1:828259620284:function:opta-lambdafunction-b0bf"
function_name = "opta-lambdafunction-b0bf"
kms_account_key_arn = "arn:aws:kms:us-east-1:828259620284:key/3a802e75-7f6f-4217-aabf-45ca0b7d9e37"
kms_account_key_id = "3a802e75-7f6f-4217-aabf-45ca0b7d9e37"
lambda_trigger_uri = "https://43neawor1c.execute-api.us-east-1.amazonaws.com/"
private_subnet_ids = [
  "subnet-0dd60ec42b37cd11b",
  "subnet-03ff99b7c866be1ff",
  "subnet-01c2d9c9c9a0f2d47",
]
```

You can visit the `lambda_trigger_uri` created above to check your microservice deployed on lambda.
