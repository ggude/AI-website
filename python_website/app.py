import requests
import json
from flask import Flask, render_template, request

app = Flask(__name__)

# Replace with your own API Gateway details
API_GATEWAY_REGION = 'ap-south-1'  # Mumbai region
API_GATEWAY_URL = 'https://pxxzbut94j.execute-api.ap-south-1.amazonaws.com/prod/api-gpt-ml'

@app.route('/', methods=['GET', 'POST'])
def index():
    generated_text = ""
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
            response_dict = json.loads(response_text)
            if 'output' in response_dict.keys():
                output = response_dict['output']
                response_string = output.replace("'", "\"")
                response_list = json.loads(response_string)
                generated_text = response_list[0]['generated_text']
            else:
                generated_text = "Error: 'generated_text' key not found in API response"
        else:
            generated_text = f"Error: {response.status_code}"

    return render_template('index.html', generated_text=generated_text, css_file='style.css')

if __name__ == '__main__':
    app.run(debug=True)
