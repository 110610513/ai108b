import os, re, json
import random

def readJSON(fileName = ""):
    if fileName!='':
        strList = fileName.split(".")
        if strList[len(strList)-1].lower() == "json":
            with open(fileName,mode='r', encoding="utf-8") as file:
                return json.loads(file.read())

data = readJSON("data.json")
famous = data["famous"]
before = data["before"]
after = data['after']
bosh = data['bosh']

xx = "test"

repeat = 2

def shuf(bosh):
    global repeat
    poll = list(bosh) * repeat
    while True:
        random.shuffle(poll)
        for e in poll:
            yield e

nextBosh = shuf(bosh)
nextFam = shuf(famous)

def giveSentense():
    global nextFam
    xx = next(nextFam)
    xx = xx.replace("a",random.choice(before))
    xx = xx.replace("b",random.choice(after))
    return xx

def another():
    xx = ". "
    xx += "\r\n"
    xx += "    "
    return xx

if __name__ == "__main__":
    xx = input("Title: ")
    length = input("Article length: ")
    for x in xx:
        tmp = str()
        while (len(tmp) < int(length)) :
            branch = random.randint(0,100)
            if branch < 5:
                tmp += another()
            elif branch < 20 :
                tmp += giveSentense()
            else:
                tmp += next(nextBosh)
        tmp = tmp.replace("x", xx)
        print(tmp)