from pathlib import Path

def load_documents(folder):
   
    documents = []
    data_folder = Path(folder)

    for document in data_folder.rglob("*.txt"):
        text = document.read_text(encoding="utf-8")
        
        document = {
            "filename": document.name,
            "text": text
        }
        documents.append(document)
    return documents
