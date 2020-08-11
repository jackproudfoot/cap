from tensorflow.keras.layers import Dense, Dropout, LSTM, Embedding, Input, GRU, Masking
from tensorflow.keras.models import Sequential, Model
from tensorflow.keras.metrics import top_k_categorical_accuracy


def make_rnn(vocab_size, embedding_size, max_len):

    input_layer = Input(shape=(None,), name="input")

    mask = Masking(mask_value=0, name="mask")(input_layer)

    # embedding
    embedding_layer = Embedding(vocab_size, embedding_size, name="embedding")(mask)

    # rnn
    rnn_fn = LSTM  # GRU/LSTM
    rnn_layers = []
    lstms = [64]
    for i, count in enumerate(lstms):
        prev = embedding_layer if i == 0 else rnn_layers[-1]
        last = i == len(lstms) - 1
        rnn_layers.append(
            rnn_fn(
                count,
                activation="relu",
                return_sequences=not last,
                name=f"recurrent{i+1}",
            )(prev)
        )

    # dense
    dense_layers = []
    denses = [(128, 0.25), (64, 0.25)]
    for i, param in enumerate(denses):
        prev = rnn_layers[-1] if i == 0 else dense_layers[-1]
        dense_layers.append(Dense(param[0], name=f"dense{i+1}")(prev))
        if param[1] > 0:
            dense_layers.append(
                Dropout(param[1], name=f"dropout{i+1}")(dense_layers[-1])
            )

    # out
    output_layer = Dense(1, activation="sigmoid", name="output")(dense_layers[-1])

    model = Model(inputs=[input_layer], outputs=[output_layer])

    model.compile(
        loss="binary_crossentropy", optimizer="nadam", metrics=["binary_accuracy"],
    )

    return model
