import numpy as np
import pandas as pd
import time
import pytumblr

# Retrieve Environment Variables
A = environ['A']
B = environ['B']
C = environ['C']
D = environ['D']

# Authenticate via OAuth
client = pytumblr.TumblrRestClient(A,B,C,D)

mins = 60
hours = 60*mins

# Read Tags
with open("tags.txt","r") as f:
    tag_line = f.readline()
    tags = tag_line.split(",")
#Select Tag
asum=0
while asum<100:
    n = np.random.randint(len(tags))
    a = client.tagged(tags[n])
    print(tags[n])
    print(len(a))
    try:
        for i in range(1,len(a)):
            print("liked")
            client.like(a[i]['id'],a[i]["reblog_key"])
        asum = asum + len(a)
        time.sleep(5)
        print(asum)
    except:
        print("error")
        time.sleep(10)