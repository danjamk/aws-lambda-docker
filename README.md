# Simple AWS Lambda Docker example
On the surface this is a very simple Hello World project that shows you how to use AWS Cloud Development Kit (CDK) to 
deploy a lambda function in a docker container.  It is indeed simple.  I created it mostly as a simple jumpstart template for new projects
I create.  I like it better than others I have found because it is super simple and stands alone.  Hopefully you will appreciate it.

This approach to Lambda is valuable when your Lambda function exceeds the upload size quota of 250MB (50MB zipped).  
By using a docker image to deploy it you can create image sizes up to 10GB!  This is great when you are loading up your function with lots of
dependencies for things like AI and machine learning.  

Other features in this sample project:
- Cloud Deployent Kit - CDK allows you to create AWS infrastructure as code (similar to CloudFormation, Terrafor, Serveless, etc.) - 
except it allows you to express your infrastructure in a programming language (python in this case)
- FastAPI - The Lambda function endpoint is using FastAPI - a nice framework for creating and testing API's


## Using this project as your start
Note: The [README-create.md](README-create.md) file has the instructions on how this project was created from scratch prior to the following steps
- The Dockerfile and requirements.txt are located in the `image` directory and can be customized to your needs
- The code for the actual API is located in: `image/src/main.py`


### Prerequisites
- Docker
- AWS Account and access setup locally
- AWS CDK - [Getting started with the AWS CDK](https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html) is a great resource for setting this up.


A few things to make sure you have in order before you begin...
- Docker is running and you are logged into your account
- Be sure you bootstrapped your CDK setup - `cdk bootstrap aws://123456789012/us-east-1` (use your own account number and region)

Note: These commands were based on a Linux docker image, but also work quite well on a Mac.  They will vary slightly for a Windows machine.

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



Install the python dependencies for CDK

```
pip install -r requirements.txt
```

Install the python dependencies for local development, which in this case is testing the endpoint

```
pip install -r requirements-dev.txt
```


You may need to bootstrap the CDK environment (use your own account number and region)

```
cdk bootstrap aws://123456789012/us-east-1
```


Initialize the cloud formation scripts (not really needed, but good practice)

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



