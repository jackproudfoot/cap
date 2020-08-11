import tensorflow as tf
import csv
from tqdm import tqdm
import util
import lstm
import numpy as np
import pickle

max_seq_length = 16
vocab_size = 2048
embedding_size = 32
datafile = "data.csv"  # "data_no_rt.csv"
noRT = False


if __name__ == "__main__":
    cap_X = []
    nocap_X = []
    with open("data.csv", "r") as f:
        reader = csv.reader(f, delimiter=",")
        for row in tqdm(reader):
            if noRT and row[2] == "rt":
                continue
            if row[0] == "cap":
                cap_X.append(row[3])
            else:
                nocap_X.append(row[3])

    print(f"Initially {len(cap_X)} cap tweets and {len(nocap_X)} no-cap tweets.")

    minl = min(len(cap_X), len(nocap_X))
    np.random.shuffle(cap_X)
    np.random.shuffle(nocap_X)
    cap_X = cap_X[:minl]
    nocap_X = nocap_X[:minl]

    X = cap_X + nocap_X
    Y = [0] * len(cap_X) + [1] * len(nocap_X)
    del cap_X
    del nocap_X
    Y = np.array(Y)

    util.shuffle_in_unison(X, Y)

    tokenizer = tf.keras.preprocessing.text.Tokenizer(
        vocab_size,
        filters='!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~\t\n',
        lower=True,
        split=" ",
        char_level=False,
        oov_token="<unk>",
    )
    tokenizer.fit_on_texts(X)
    thresh, count = 10, 0
    for _, c in tokenizer.word_counts.items():
        count += 1 if c > thresh else 0
    print(f"{count} words used > {thresh} times")

    X = tokenizer.texts_to_sequences(X)
    X = tf.keras.preprocessing.sequence.pad_sequences(X, maxlen=max_seq_length)
    print(X.shape)

    ### training ###
    model = lstm.make_rnn(vocab_size, embedding_size, max_seq_length)

    stopper = tf.keras.callbacks.EarlyStopping(
        monitor="val_loss",
        min_delta=0,
        patience=3,
        verbose=1,
        mode="auto",
        restore_best_weights=True,
    )

    model.fit(
        X,
        Y,
        epochs=10,
        batch_size=32,
        validation_split=0.15,
        shuffle=True,
        verbose=1,
        callbacks=[stopper],
    )

    model.save("models/model.h5")
    with open("models/tokenizer.pickle", "wb") as f:
        pickle.dump(tokenizer, f, protocol=pickle.HIGHEST_PROTOCOL)
    with open("models/tokenizer.pickle", "rb") as f:
        tokenizer = pickle.load(f)

    print(tokenizer.texts_to_sequences(["this is a test sentence"]))
