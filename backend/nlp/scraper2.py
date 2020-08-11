from twitter_scraper import get_tweets
import csv
from tqdm import tqdm
import multiprocessing


def getUserTweets(user):
    print(user)
    tweets = []
    for tweet in get_tweets(user):
        stripped = "".join([c for c in tweet["text"] if c not in "\n"])
        tweets.append(stripped)
    return (user, tweets)


def usersTweetsToCSV(capUsers, noCapUsers, fname):
    with open(fname, "w") as f:
        writer = csv.writer(f, delimiter=",")
        with multiprocessing.Pool(len(capUsers + noCapUsers)) as p:
            results = p.map(getUserTweets, capUsers + noCapUsers)

        for user, tweets in results:
            label = "cap" if user in capUsers else "nocap"
            for tweet in tweets:
                writer.writerow([label, user, tweet])


capUsers = [
    "realDonaldTrump",
    "seanhannity",
    "UCLA",
    "UNC",
    "peta",
    "amazon",
    "microsoft",
    "flatearthorg",
    "RealCapnCrunch",
    "lancearmstrong",
    "TheOnion",
]
noCapUsers = [
    "neiltyson",
    "CDCgov",
    "wendys",
    "chilis",
    "ibm",
    "IBMWatson",
    "dannydevito",
]
if __name__ == "__main__":
    usersTweetsToCSV(capUsers, noCapUsers, "data.csv")

    # with open("data.csv", "r") as f:
    #     reader = csv.reader(f, delimiter=",")

    #     for row in reader:
    #         assert len(row) == 3
