#Title:"Text Pre-Processing using NLP operations:perform Tokenization
# Stop word removal,Lemmatization ,Part-of-Speech Tagging use any sample text"

#import libraries
import spacy

# Load the language model
nlp = spacy.load("en_core_web_sm")

# Define the input text with spaces between sentences
input_text = (
   "Python is a popular programming language. "
   "It is widely used in data science."
)

# 1. Tokenization:
doc_tokens = nlp(input_text)
print("1. Tokenization:")
for token in doc_tokens:
    print(token, token.idx)

# 2. Stop Words Removal:
print("\n2. Stop Words Removal:")
filtered_tokens = [token for token in doc_tokens if not token.is_stop]
print(filtered_tokens)

# 3. Lemmatization:
print("\n3. Lemmatization:")
for token in doc_tokens:
    if str(token) != str(token.lemma_):
        print(f"{str(token):>20} : {str(token.lemma_)}")

# 4. Part of Speech Tagging:
print("\n4. Part of Speech Tagging:")
for token in doc_tokens:
    print(
        f"""
TOKEN: {str(token)}
=====
TAG: {str(token.tag_):10} POS: {token.pos_}
EXPLANATION: {spacy.explain(token.tag_)}"""
    )


#----------output-------#
"""India 0
is 6
my 9
country 12
. 18
Maharashtra 20
is 32
my 35
state 38
. 43
[India, country, ., Maharashtra, state, .]
is : be
is : be
TOKEN: India
=====
TAG: NNP        POS: PROPN
EXPLANATION: noun, proper singular

TOKEN: is
=====
TAG: VBZ        POS: AUX
EXPLANATION: verb, 3rd person singular present

TOKEN: my
=====
TAG: PRP$       POS: DET
EXPLANATION: pronoun, possessive

TOKEN: country
=====
TAG: NN         POS: NOUN
EXPLANATION: noun, singular or mass

TOKEN: .
=====
TAG: .          POS: PUNCT
EXPLANATION: punctuation mark, sentence closer

TOKEN: Maharashtra
=====
TAG: NNP        POS: PROPN
EXPLANATION: noun, proper singular

TOKEN: is
=====
TAG: VBZ        POS: AUX
EXPLANATION: verb, 3rd person singular present

TOKEN: my
=====
TAG: PRP$       POS: DET
EXPLANATION: pronoun, possessive

TOKEN: state
=====
TAG: NN         POS: NOUN
EXPLANATION: noun, singular or mass

TOKEN: .
=====
TAG: .          POS: PUNCT
EXPLANATION: punctuation mark, sentence closer"""