import spacy

with open("./phrases_used_alot.txt") as f:
    # f.read reads the text, the first replace acounts for paragraphs, 
    # and the second replace turn a paragraph into a one line sentence. 
    # May not be needes for my text but it's still cool :)
    text = f.read().replace("\n\n", " ").replace("\n", " ")

nlp = spacy.load("en_core_web_sm")

doc = nlp(text)

words = {'verbs':[], 'aux':[], 'adjective':[], 'pronoun':[]}
for token in doc:
    if token.pos_ == "VERB":
        words['verbs'].append(token)
    if token.pos_ == "AUX":
        words["aux"].append(token)
    if token.pos_ == "ADJ":
        words["adjective"].append(token)
    if token.pos_ == "PRON":
        words["pronoun"].append(token)


print(words)
