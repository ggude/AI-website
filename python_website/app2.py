import requests
from flask import Flask, render_template, request

app = Flask(__name__)

# Replace with your own API Gateway details
API_GATEWAY_REGION = 'ap-south-1'  # Mumbai region
API_GATEWAY_URL = 'https://pxxzbut94j.execute-api.ap-south-1.amazonaws.com/prod/api-gpt-ml'

@app.route('/', methods=['GET', 'POST'])
def index():
    response_text = ""
    if request.method == 'POST':
        # Get the text input from the form
        text_input = request.form['text_input']

        # Prepare the API Gateway request
        api_request = {
            "input": text_input
        }

        # Call the API Gateway
        response = requests.post(API_GATEWAY_URL, json=api_request)
        if response.status_code == 200:
            response_text = response.text
        else:
            response_text = f"Error: {response.status_code}"

    return render_template('index.html', response_text=response_text)

if __name__ == '__main__':
    app.run(debug=True)
