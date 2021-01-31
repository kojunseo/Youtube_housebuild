import pandas as pd

def save(location, cleaness, built_in):
    idx = len(pd.read_csv("database.csv"))
    new_df = pd.DataFrame({"location":location,
                           "cleaness":cleaness,
                           "built_in":built_in}, 
                         index = [idx])
    new_df.to_csv("database.csv",mode = "a", header = False)
    return None

def load_list():
    house_list = []
    df = pd.read_csv("database.csv")
    for i in range(len(df)):
        house_list.append(df.iloc[i].tolist())
    return house_list

def now_index():
    df = pd.read_csv("database.csv")
    return len(df)-1


def load_house(idx):
    df = pd.read_csv("database.csv")
    house_info = df.iloc[idx]
    return house_info


if __name__ =="__main__":
    load_list()