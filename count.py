import read
from collections import Counter

df = read.load_data()
long_string = ""
for row in df["headline"]:
    long_string += str(row).lower()
    
string_list = long_string.split(" ")
cnt = Counter()
for word in string_list:
    cnt[word] += 1

print(cnt.most_common(100))
