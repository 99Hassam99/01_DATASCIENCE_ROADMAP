import requests

# Your Hugging Face API key
API_KEY = "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"
API_URL = "https://api-inference.huggingface.co/models/gpt2"

# The headers with your API key
headers = {"Authorization": f"Bearer {API_KEY}"}

# Function to send a prompt to the Hugging Face API
def query_huggingface_api(prompt):
    response = requests.post(API_URL, headers=headers, json={"inputs": prompt})
    return response.json()

# Test the API with a prompt
output = query_huggingface_api("What is martial arts?")
print("API Response:", output)  # Print the entire response for debugging

# Check if the output has the expected structure
if isinstance(output, list) and len(output) > 0:
    print(output[0]['generated_text'])
else:
    print("Unexpected response format or empty response.")
