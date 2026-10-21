from language import detect_language
from loader import load_documents

print ("Multilingual Intelligence Analysis")

documents = load_documents("Data")

for document in documents:
    print(document["filename"])
    text = document["text"]
    language = detect_language(text)
    print("language:", language)
    print(text)
    print("Characters:", len(text))

