
#Assignment Title : Name Entity Recognition in python with spacy


import spacy

# Load the English language model
nlp = spacy.load("en_core_web_sm")

def perform_ner(text):
    # Process the text using SpaCy
    doc = nlp(text)
    
    # Extract named entities and their labels
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    
    return entities

if __name__ == "__main__":
    # Example text
    text = "Apple is a popular company based in California. Tim Cook is the CEO."

    # Perform Named Entity Recognition
    named_entities = perform_ner(text)

    # Print the results
    print("Named Entities:")
    for entity, label in named_entities:
        print(f"{entity} - {label}")


'''
**************    OUTPUT

Named Entities:
Earth - LOC
third - ORDINAL
Sun - ORG

'''
