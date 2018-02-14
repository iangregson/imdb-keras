
import sys, pickle
import csv_utils as utils
import pandas as pd
from keras.models import load_model
from keras.preprocessing import sequence

def main(classifier, csvfile, text_colomn):
    # load up our stored modeland vocab
    model = load_model(classifier)
    vocab = pickle.load(open('vocab.pkl', 'rb'))

    # load our data that we want to run predictions on and drop any rows without data in the specified column
    csv_data = pd.read_csv(csvfile)
    csv_data = csv_data[pd.notnull(data[text_column])]

    # Get a copy of column we're making predictions on and vectorize it
    csv_data['text'] = csv_data[text_column].apply(lambda x: utils.review_vector(x, vocab, len(vocab)))

    # normalize the vectors and make our predictions
    x = sequence.pad_sequences(csv_data['text'], maxlen=400)
    csv_data['sentiment'] = model.predict(x)

    # save out our new file with just the columns we want
    columns = ['FLILEG_ID', 'CLISEN_NAME', 'SERREP_DESCRIPTION', 'sentiment']
    output = csv_data[columns]
    output.to_csv('output/predictions.csv', encoding='utf-8', index=False)

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3])
