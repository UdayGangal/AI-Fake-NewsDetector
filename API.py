import cohere 
COHERE_API_KEY= "1YacVfW8ggBW2aLK7nS64JLc0CUchc6Da4TW0Qy4"
co= cohere.client(COHERE_API_KEY)
examples = [
    ["NASA plans to return to the moon by 2026", "REAL"],
    ["Aliens land on Earth and take over major cities", "FAKE"],
    ["The economy grew by 3% in the last quarter", "REAL"],
    ["Elvis Presley spotted at a coffee shop in 2024", "FAKE"],
    ["Scientists discover cure for cancer in vegetables", "FAKE"],
    ["Elections to be held next month, says EC", "REAL"]
]
def classify_news(text):
  response=co.classify(inputs=[text],examples=examples)
  classification=response.classifications[0]
  return classification.prediction , classification.confidence

def genreate_real_version(fake_news_text):
  prompt=(
    f"The following news seems to be exgratted or fake:\n\n"
    f"'{fake_news_text}'\n\n"
    f"Generating a real version of this news:"
  )

response=co.generate(
  model='command-r',
  prompt=prompt,
  max_toxens=150,
  temperature=0.7
)
return response.generation[0].text.strip()