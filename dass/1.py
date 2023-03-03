import nltk
nltk.download('punkt') # only required the first time you run this program

text = input("Enter a text: ")

sentences = nltk.sent_tokenize(text)
for i, sentence in enumerate(sentences):
    num_previous_sentences = i
    print("Sentence", i+1, "has", num_previous_sentences, "previous sentences.")
    print(sentence)