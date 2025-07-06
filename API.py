import cohere

COHERE_API_KEY = "1YacVfW8ggBW2aLK7nS64JLc0CUchc6Da4TW0Qy4"
co = cohere.Client(COHERE_API_KEY)

examples = [
    ["NASA plans to return to the moon by 2026", "REAL"],
    ["Aliens land on Earth and take over major cities", "FAKE"],
    ["The economy grew by 3% in the last quarter", "REAL"],
    ["Elvis Presley spotted at a coffee shop in 2024", "FAKE"],
    ["Scientists discover cure for cancer in vegetables", "FAKE"],
    ["Elections to be held next month, says EC", "REAL"]
]

def classify_news(text):
    response = co.classify(
        inputs=[text],
        examples=[cohere.ClassifyExample(x[0], x[1]) for x in examples]
    )
    classification = response.classifications[0]
    return classification.prediction == "FAKE", classification.confidences[0].confidence

def generate_real_version(fake_news_text):
    prompt = (
        f"The following news seems to be exaggerated or fake:\n\n"
        f"'{fake_news_text}'\n\n"
        f"Generate a more realistic and factual version of this news:"
    )

    response = co.generate(
        model='command-r',
        prompt=prompt,
        max_tokens=150,
        temperature=0.7
    )
    return response.generations[0].text.strip()
