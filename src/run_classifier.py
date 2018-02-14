
import sys, pickle
import csv_utils as utils
import pandas as pd
from keras.models import load_model
from keras.preprocessing import sequence

def main(classifier, csvfile, text_colomn):
    model = load_model(classifier)
    vocab = pickle.load(open('vocab.pkl', 'rb'))
    csv_data = pd.read_csv(csvfile)
    test_data = csv_data[text_column]
    x = utils.review_vector(command, vocab, len(vocab))
    x = sequence.pad_sequences([x], maxlen=400)
    print("Sentiment:", model.pred:qaict(x)[0][0])

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3])
