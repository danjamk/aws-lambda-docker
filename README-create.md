# Creating this CDK projct from scratch
These are the steps I used to create the framework for this project.  I will also mention the files I modified to complete the work.

NOTE: You need to satisfy the prerequisites mentioned in the [README.md](README.md) file


1. Create a project in GitHub (this is optional) - the project should be completely empty (not README.md file or .gitignore or license)
2. Clone the repo to the location you want to work on the project
3. cd into the directory (in this case aws-lambda-docker)
4. Run the CDK init command 

```
cdk init sample-app --language python
```

This command will create a full sample CDK project structure and sample files, including
- virutal environment
- [README.md](README.md) file (which includes details much like these)
- .gitignore
- requirements.txt file for CDK
- sample stack creation program

5. Activate the virtual environment

```
source .venv/bin/activate
```

6. Install the python requirements

```
pip install -r requirements.txt
```

7. Modify the sample code to be yours
The README.md shows what modifications I made to
- Create a directory for the docker image
- Creating the main.py program that will be the API endpoint
- Dockerfile creation
- requirements.txt file for the API
- Modifications to the stack creation code to deploy the docker image as a Lambda function