import spacy

with open("./phrases_used_alot.txt") as f:
    # f.read reads the text, the first replace acounts for paragraphs, 
    # and the second replace turn a paragraph into a one line sentence. 
    # May not be needes for my text but it's still cool :)
    text = f.read().replace("\n\n", " ").replace("\n", " ")

nlp = spacy.load("en_core_web_sm")

doc = nlp(text)
sentences = list(doc.sents)
first_sentence = sentences[0]

# Prints each word with what is it on the side (noun, verb, aux, etc.) very cool
verbs = []
for token in sentences:
    if token.pos_ == "VERB":
        verbs.append(token)

print(verbs)


