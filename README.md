# Simple AWS Lambda Docker example





## Using this project as your start
Note: The README-create.md file has the instructions on how this project was created from scratch


### Prerequisits
- Docker
- AWS Account and access setup locally
- AWS CDK - https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html



A few things to make sure yuo have in order before you begin...
- Docker is running and you are logged into your account
- Be sure you bootstrapped your CDK setup


Clone the project

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



Initialize the cloud formation scripts

```
cdk synth
```



Deploy the stack to CloudFormation

```
cdk deploy
```


The output of the deployment will include a function URL.  You can click or paste that URL into a browser and test the function.




