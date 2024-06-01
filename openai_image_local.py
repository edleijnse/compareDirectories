import base64
import requests

# OpenAI API Key
with open(r"C:\\xampp\\htdocs\\api_key", "r") as file:
    api_key = file.read().strip()

# Function to encode the image
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')



def prepare_image(image_path):
  global headers, payload
  # Path to your image
  # Getting the base64 string
  base64_image = encode_image(image_path)
  headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
  }
  payload = {
    "model": "gpt-4o",
    "messages": [
      {
        "role": "user",
        "content": [
          {
            "type": "text",
            "text": "What’s in this image?"
          },
          {
            "type": "image_url",
            "image_url": {
              "url": f"data:image/jpeg;base64,{base64_image}"
            }
          }
        ]
      }
    ],
    "max_tokens": 300
  }


def get_image_content(filename):
  prepare_image(filename)
  response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
  response_data = response.json()
  first_choice = response_data["choices"][0]["message"]["content"]
  return first_choice

filename = "D:\\BilderExport\\Cows\\20231110-IMG_4248.jpg"
myImageContent = get_image_content(filename)
print(myImageContent)

