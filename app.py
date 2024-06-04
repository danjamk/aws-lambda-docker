import aws_cdk as cdk

from aws_lambda_docker.aws_lambda_docker_stack import AwsLambdaDockerStack


app = cdk.App()
AwsLambdaDockerStack(app, "AwsLambdaDockerStack")

app.synth()
