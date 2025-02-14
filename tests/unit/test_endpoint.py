import unittest
# from tests.stack_output import function_name
import requests
import boto3


def get_stack_output(stack_name, output_key):
    client = boto3.client('cloudformation', region_name='us-east-2')  # You need to change to your region if testing
    response = client.describe_stacks(StackName=stack_name)
    for stack in response['Stacks']:
        for output in stack['Outputs']:
            if output['OutputKey'] == output_key:
                return output['OutputValue']
    return None

class EndpointTests(unittest.TestCase):
    def test_endpoint(self):
        stack_name = "AwsLambdaDockerStack"
        output_key = "FunctionUrlValue"
        function_url = get_stack_output(stack_name, output_key)

        response = requests.get(function_url)
        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        self.assertEqual(response_data, {"message": "Hello World"})


if __name__ == '__main__':
    unittest.main()
