import numpy as np
import pandas as pd

print('Hello from vim!')

f = open("4_data.txt").readlines()
data = [""]
index = 0

for row in f:
    if row == "\n":
        data.append(row)
        index += 1
    else:
        data[index] += " " + row.replace("\n", "")

for i, item in enumerate(data):
    data[i] = item.split()

for i, item in enumerate(data):
    new_item = {}
    for el in item:
        new_item |= {el[0:3]: el[4:]}
    data[i] = new_item

df = pd.DataFrame(data).drop("cid", axis=1)

for i in range(0, df.shape[0]):
    item = df.loc[
        i,
    ]
    if item.isnull().sum() == 0:
        df.loc[i, "isValid"] = "valid"
    else:
        df.loc[i, "isValid"] = "invalid"

df["isValid"].value_counts()


def validate(iyr, ecl, hgt, pid, byr, hcl, eyr):
    if np.nan in [iyr, ecl, hgt, pid, byr, hcl, eyr] or "" in [
        iyr,
        ecl,
        hgt,
        pid,
        byr,
        hcl,
        eyr,
    ]:
        return "invalid - missing values"
    elif int(byr) < 1920 or int(byr) > 2002:
        return "invalid byr"
    elif int(iyr) < 2010 or int(iyr) > 2020:
        return "invalid iyr"
    elif len(str(eyr)) != 4:
        return "invalid eyr"
    elif int(eyr) < 2020 or int(eyr) > 2030:
        return "invalid eyr"
    elif hgt[-2:] != "cm" and hgt[-2:] != "in":
        return "invalid hgt suffix"
    if hgt[-2:] == "cm":
        if int(hgt[:-2]) < 150 or int(hgt[:-2]) > 193:
            return "invalid hgt cm"
    if hgt[-2:] == "in":
        if int(hgt[:-2]) < 59 or int(hgt[:-2]) > 76:
            return "invalid hgt in"
    if hcl[0] != "#":
        return "invalid hcl"
    if hcl[0] == "#":
        if len(hcl[1:]) != 6:
            return "invalid hcl"
    if ecl not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
        return "invalid ecl"
    if len(pid) != 9:
        return "invalid pid"
    return "valid"


validate(
    hcl="#18171d",
    hgt="70in",
    byr="1926",
    iyr="2010",
    pid="18asda6cm",
    ecl="amb",
    eyr="2020",
)

df.apply(
    lambda x: validate(x.iyr, x.ecl, x.hgt, x.pid, x.byr, x.hcl, x.eyr), axis=1
).value_counts()
