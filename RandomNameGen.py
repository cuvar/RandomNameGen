import random

def pickNamePart(s):
    element = ""

    f = open(s, "r")
    l = f.readlines()
    f.close

    element = l[random.randint(0, len(l) - 1)]
    
    return element




if __name__ == "__main__":
    
    name = ""

    #choose name parts
    adj = pickNamePart("adjectives.txt")
    noun = pickNamePart("nouns.txt")
    
    #set name together
    name = "{}-{}".format(adj, noun).replace("\n", "")
    
    #output
    print("\n------- RandomNameGen.py -------")
    print("\n{}\n".format(name))

    input("Press enter to exit")