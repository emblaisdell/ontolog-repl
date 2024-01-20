import requests

SPACING = 5
API_ENDPOINT = "http://ecs-modulus-cluster-11369770.us-east-1.elb.amazonaws.com:8080/runPhoenicia"

while True:
    line = input(" "*SPACING)
    if line=="exit":
        break
    elif line=="in":
        SPACING+=1
    elif line=="out":
        SPACING-=1
    else:
        print(" "*SPACING+line)
        #out = requests.post(API_ENDPOINT,line)
        #print(" "*SPACING+str(out.content))
