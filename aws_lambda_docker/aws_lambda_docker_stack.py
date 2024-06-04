import os
from constructs import Construct
from aws_cdk import (
    Duration,
    Stack,
    aws_iam as iam,
    aws_sqs as sqs,
    aws_sns as sns,
    aws_sns_subscriptions as subs,
    aws_lambda as _lambda,
)

import aws_cdk as cdk


class AwsLambdaDockerStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        function_name = f"AwsLambdaDockerFunction"

        # Build the docker image
        docker_function = _lambda.DockerImageFunction(self,
                                                      function_name,
                                                      code=_lambda.DockerImageCode.from_image_asset("./image"),
                                                      timeout=Duration.seconds(300),
                                                      memory_size=1024
                                                      )

        # Create the endpoint for the function
        function_url = docker_function.add_function_url(
            auth_type=_lambda.FunctionUrlAuthType.NONE,
            cors={
                "allowed_methods": [_lambda.HttpMethod.ALL],
                "allowed_headers": ["*"],
                "allowed_origins": ["*"],
            }
        )

        # Provide output to for the function
        cdk.CfnOutput(self, "FunctionUrlValue", value=function_url.url)

        #grant access to ssm for parameter store
        docker_function.add_to_role_policy(iam.PolicyStatement(
            actions=["ssm:GetParameter"],
            resources=["*"]
        ))

        print(f"Lambda Function URL: {function_url.url}")



