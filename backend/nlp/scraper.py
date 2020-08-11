from twitter_scraper import get_tweets
import csv
from tqdm import tqdm


def usersTweetsToCSV(capUsers, noCapUsers, fname):
    with open(fname, "w") as f:
        writer = csv.writer(f, delimiter=",")
        for user in capUsers + noCapUsers:
            print(f"getting {user}'s tweets")
            label = "cap" if user in capUsers else "nocap"
            for tweet in tqdm(get_tweets(user, pages=200)):
                stripped = "".join([c for c in tweet["text"] if c not in "\n"])
                if len(stripped.split()) < 3:
                    continue
                rt = "rt" if tweet["isRetweet"] else "oc"
                writer.writerow([label, user, rt, stripped])


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
    "kanyewest",
    "BreitbartNews",
    "msrebeccablack",
    "gregory_school",
    "walmart",
    "hannanrhodes",
    "loganpaul",
    "jakepaul",
    "therealoj32",
    "realshkreli",
    "RTErdogan",
    "tiktok_us",
    "KDTrey5",
]
noCapUsers = [
    "neiltyson",
    "CDCgov",
    "wendys",
    "chilis",
    "ibm",
    "IBMWatson",
    "dannydevito",
    "barackobama",
    "jcolenc",
    "costcocanada",
    "codyko",
    "jimmytatro",
    "jacindaardern",
    "robgronkowski",
    "jimmybuffett",
    "kingjames",
    "gordonramsay",
    "ArvindKrishna",
    "mrahtelli2",
]
if __name__ == "__main__":
    usersTweetsToCSV(capUsers, noCapUsers, "data.csv")

    # with open("data.csv", "r") as f:
    #     reader = csv.reader(f, delimiter=",")

    #     for row in reader:
    #         assert len(row) == 3
