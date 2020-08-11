import tensorflow as tf
import pickle

model_name = "models/model.h5"


def determine_cap(model, tokenizer, query):
    test_seq = tokenizer.texts_to_sequences([query])
    # test_seq = tf.keras.preprocessing.sequence.pad_sequences(
    #     test_seq, maxlen=max_seq_length
    # )
    return model.predict(test_seq)[0]


if __name__ == "__main__":
    model = tf.keras.models.load_model(model_name)
    with open("models/tokenizer.pickle", "rb") as f:
        tokenizer = pickle.load(f)

    test_sentences = [
        "i love ucla",
        "i love usc",
        "i love duke",
        "i love unc",
        "this is a test sentence",
        "cnn is fake news",
        "obama is my lord and savior jesus christ",
        "mcdonalds has rats in their soup",
        "i do steroids lmao #tourdefrance",
        "this is cap",
        "this isn't cap",
        "innovation that excites",
        "alexa buy groceries",
        "lmao i just bought whole foods #nocap",
        "jesus did nothing wrong",
        "cole anthony is the goat",
        "I love riding bicycles",
        "pandemic makes people sad",
        "mmm crunchy cereral in my belly mmmm",
        "appetizers for dayz",
        "I love trojan",
        "jupiter is sexy",
        "crawdads are my favorite vegetable",
        "I have four brothers and sisters and two are born on the same day",
        "the best cereal to wake up to",
        "give your family the nutrition they deserve with crunch",
        "microsoft",
        "surface",
        "alexa play despacito",
        "north carolina",
        "students",
        "semester",
        "tuition",
        "kung flu",
        "chinese virus",
        "covid 19",
        "coronavirus",
        "i have the constitutional right not to wear a mask",
        "SAD!",
        "we should buy thatsc.app",
        "we shouldn't buy thatsc.app",
        "maple syrup is awesome",
        "costco perpetrated crimes against humanity",
        "I love hockey",
        "subscribe to my only fans account for more exclusive content uwu",
        "Im extremely sorry for my previous actions, I have grown since then",
        "go tar heels",
        "burger king makes the best fries",
    ]

    for sentence in test_sentences:
        nocapProb = determine_cap(model, tokenizer, sentence)
        label = "NOCAP" if nocapProb >= 0.5 else "CAP"
        print(f"{label} - {sentence}")
