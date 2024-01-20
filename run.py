import requests
import os

SPACING = 1
API_ENDPOINT = "http://ecs-modulus-cluster-11369770.us-east-1.elb.amazonaws.com:8080/runPhoenicia"

os.system("clear") # clear screen

while True:
    line = input(" "*SPACING)
    if line=="exit":
        break
    elif line=="":
        continue
    elif line=="in":
        SPACING+=1
    elif line=="out":
        SPACING-=1
    else:
        print(" "*SPACING,end="")
        out = requests.post(API_ENDPOINT,line)
        print(out.content.decode("utf-8"))
