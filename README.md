# Simple AWS Lambda Docker example
On the surface this is a very simple Hello World project that shows you how to use AWS Cloud Development Kit (CDK) to deploy a lambda function in a docker container.  This is valuable when your Lambda function exceeds the upload size quota of 250MB (50MB zipped).  By using a docker image to deploy it you can create image sizes up to 10GB!

Other features in this sample project:
- Cloud Deployent Kit - CDK allows you to create AWS infrastructure as code (similar to CloudFormation, Terrafor, Serveless, etc.) - except it allows you to experss your infrastructure in a programming language (python in this case)
- FastAPI - The Lambda function endpoint is using FastAPI - a nice framework for creating and testing API's



## Using this project as your start
Note: The [README-create.md](README-create.md) file has the instructions on how this project was created from scratch prior to the following steps


### Prerequisits
- Docker
- AWS Account and access setup locally
- AWS CDK - [Getting started with the AWS CDK](https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html) is a great resource for setting this up.



A few things to make sure yuo have in order before you begin...
- Docker is running and you are logged into your account
- Be sure you bootstrapped your CDK setup

Note: These commands were based on a Linux system, but also work quite well on a Mac.  They will vary slighlty for a Windows machine.

### The Steps
Clone the GitHub project

```
git clone https://github.com/danjamk/aws-lambda-docker.git
```


Create and enable the python virtual environment

```
cd aws-lambda-docker
python -m venv .venv
source .venv/bin/activate
```



Install the python dependencies

```
pip install -r requirements.txt
```

You may need to bootstrap the CDK environment (use your own account number and region)

```
cdk bootstrap aws://123456789012/us-east-1
```



Initialize the cloud formation scripts

```
cdk synth
```



Deploy the stack to CloudFormation

```
cdk deploy
```


The output of the deployment will include a function URL.  You can click or paste that URL into a browser and test the function.



You can clean up the resources by destroying the stack

```
cdk destroy
```



