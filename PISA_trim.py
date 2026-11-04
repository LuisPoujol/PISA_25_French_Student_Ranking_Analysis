import pandas as pd
import pyreadstat

FILE = "CY09_MS_STU_PUF.sav"

#columns I want to keep
cols = [
    "CNT", "CNTSCHID", "CNTSTUID",          # country, school id, student id
    "PV1MATH", "PV2MATH", "PV3MATH", "PV4MATH", "PV5MATH",
    "PV6MATH", "PV7MATH", "PV8MATH", "PV9MATH", "PV10MATH",   # math scores
    "ST004D01T", "ST001D01T", "GRADE", "REPEAT", "IMMIG",     # gender, grade, etc
    "ESCS", "HOMEPOS", "HISEI", "PAREDINT", "BELONG",         # background
    "W_FSTUWT",                                               # weight
]

#read only those column
df, meta = pyreadstat.read_sav(FILE, usecols=cols, apply_value_formats=False)
print("all students:", df.shape)

#France
df = df[df["CNT"] == "FRA"]
print("french students:", df.shape)
print("number of schools:", df["CNTSCHID"].nunique())

#save
df.to_csv("pisa2025_france.csv", index=False)
