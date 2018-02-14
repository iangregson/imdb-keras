import sys, pickle
import csv_utils as utils

from keras.models import load_model
from keras.preprocessing import sequence

def main(classifier):
    model = load_model(classifier)
    vocab = pickle.load(open('output/vocab.pkl', 'rb'))

    command = ''

    print("Enter a message and see its sentiment or type 'exit' to quit")
    while True:
        command = input()

        if command == 'exit':
            break
        else:
            x = utils.review_vector(command, vocab, len(vocab))
            x = sequence.pad_sequences([x], maxlen=400)
            print("Sentiment:", model.predict(x)[0][0])

if __name__ == "__main__":
    main(sys.argv[1])
