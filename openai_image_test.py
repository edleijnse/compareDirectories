from openai import OpenAI

client = OpenAI()

response = client.chat.completions.create(
  model="gpt-4o",
  messages=[
    {
      "role": "user",
      "content": [
        {"type": "text", "text": "What’s in this image?, answer in German"},
        {
          "type": "image_url",
          "image_url": {
            # "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg",
            #"url": "https://paparazzi.li/wp-content/uploads/2023/06/20230613-L1008789-scaled.jpg",
            "url": "https://paparazzi.li/wp-content/uploads/2023/06/20230613-L1008865-scaled.jpg",
          },
        },
      ],
    }
  ],
  max_tokens=300,
)

print(response.choices[0])