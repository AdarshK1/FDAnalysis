
#Todo functions
def cleantext(txt):     #get rid of html markup and punctuation
    arr = []
    temp = ""
    for word in txt:
        for char in word:
            if (char not in punctuation):
                temp = temp + char
        temp = temp.rstrip()
        temp = temp.lower()
        arr . append (temp)
        temp = ""
    return arr



def tallyWord(txt):         #create a frequency table
    print("asdf")


punctuation = ",./?'|}{[]=+-_;:<>!@#$%^&*()`~"
fd = open("FDText.txt")
hf = open("huckfinn.txt")

fdText=fd.read()
hfText=hf.read()

fdArray = fdText.split()
hfArray = hfText.split()

fdArray2 = cleantext(fdArray)
hfArray2 = cleantext(hfArray)

fd.close()
hf.close()

print(hfArray2)



