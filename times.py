import read
from dateutil import parser

df = read.load_data()

def get_hour(row):
    dt_obj = parser.parse(row)
    return dt_obj.hour

df = df["submission_time"].apply(get_hour)
print(df.value_counts())