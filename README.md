# Simple AWS Lambda Docker example

Prerequisits
AWS CDK - https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html
Docker
AWS Account and access setup locally

Be sure docker is running and you are logged in

## Using this project as your start
Note: The README-create.md file has the instructions on how this project was created from scratch

A few things to make sure yuo have in order before you begin...
- Docker is running and you are logged into your account
- Be sure you bootstrapped your CDK setup

Clone the project
`git clone https://github.com/danjamk/aws-lambda-docker.git`

Create and enable the python virtual environment
`cd aws-lambda-docker`

`python -m venv .venv`

`source .venv/bin/activate`

Install the python dependencies
`pip install -r requirements.txt`


Initialize the cloud formation scripts
`cdk synth`

Deploy the stack to CloudFormation
`cdk deploy`






Bootstrap the environment (once for your computer)
Initialize project (once for the project - but not needed if you cloned this repo)

create virtual env
source venv
install requirements


docker build -t dlambda:latest .





TODO:
- Test


