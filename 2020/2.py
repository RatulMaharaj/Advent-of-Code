import pandas as pd


def check_password(pwd, ltr, min_occ, max_occ):
    count = 0
    for i in pwd:
        if i == ltr:
            count += 1

    if count >= min_occ and count <= max_occ:
        return "valid"
    else:
        return "invalid"


df = pd.read_csv("2_data.txt", names=["Data"])

df["rpt"] = df["Data"].map(lambda x: x.split()[0])
df["ltr"] = df["Data"].map(lambda x: x.split()[1][0])
df["pwd"] = df["Data"].map(lambda x: x.split()[2])
df["min_occ"] = df["rpt"].map(lambda x: int(x.split("-")[0]))
df["max_occ"] = df["rpt"].map(lambda x: int(x.split("-")[1]))
df.drop("Data", axis=1, inplace=True)
df.drop("rpt", axis=1, inplace=True)
df.head()


soln = df.apply(
    lambda x: check_password(x.pwd, x.ltr, x.min_occ, x.max_occ), axis=1
).value_counts()


def check_password2(pwd, ltr, first_pos, second_pos):

    if pwd[first_pos - 1] == ltr and pwd[second_pos - 1] != ltr:
        return "valid"
    elif pwd[first_pos - 1] != ltr and pwd[second_pos - 1] == ltr:
        return "valid"
    else:
        return "invalid"


df.apply(
    lambda x: check_password2(x.pwd, x.ltr, x.min_occ, x.max_occ), axis=1
).value_counts()
