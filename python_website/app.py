import boto3
from flask import Flask, render_template, request

app = Flask(__name__)

# Replace with your own API Gateway details
API_GATEWAY_REGION = 'ap-south-1'  # Mumbai region
API_GATEWAY_URL = 'https://pxxzbut94j.execute-api.ap-south-1.amazonaws.com/prod/api-gpt-ml'

# Initialize the API Gateway client
client = boto3.client('apigateway', region_name=API_GATEWAY_REGION)


@app.route('/', methods=['GET', 'POST'])
def index():
    response_text = ""
    if request.method == 'POST':
        # Get the text input from the form
        text_input = request.form['text_input']

        # Prepare the API Gateway request
        api_request = {
            "method": "POST",
            "url": API_GATEWAY_URL,
            "headers": {
                "Content-Type": "application/json"
            },
            "body": {
                "input": text_input
            }
        }

        # Call the API Gateway
        response = client.test_invoke_method(restApiId='your-api-gateway-id',
                                             resourceId='your-resource-id',
                                             httpMethod='POST',
                                             body=api_request)
        if response['statusCode'] == 200:
            response_text = response['body']
        else:
            response_text = f"Error: {response['statusCode']}"

    return render_template('index.html', response_text=response_text)


if __name__ == '__main__':
    app.run(debug=True)
