import pandas as pd

def find_similar_companies(seed_domain):

    df = pd.read_csv(
        "data/companies.csv"
    )

    return df["domain"].tolist()