import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import matplotlib




import operator
file = open("file.txt", "r")
file_string = str(file.read())

def worder(string):
    dc = {}
    string = string.replace(",", "") 
    string = string.replace(".", "")
    string = string.replace(";", "")
    string = string.replace('"', "")
    string = string.replace(":", "")
    string = string.replace("(", "")
    string = string.replace(")", "")
    string = string.split(" ")
    for elem in string:
        elem = str(elem).lower()
        if elem in dc:
            dc[elem] += 1
        else:
            dc[elem] = 1
    dc = sorted(dc.items(), key=lambda kv: kv[1])
    
    return (dc)
def graphWords(arr):
    words = []
    
    usage_amounts = []
    for bar in arr:
        if bar[1] == 1 or bar[1] == 2:
            pass
        else:
            words.append(bar[0])
            usage_amounts.append(bar[1])

    y_pos = np.arange(len(words))
    y_pos = [2*i for i in y_pos]
    plt.figure(figsize=(20,10))
    plt.barh(y_pos, usage_amounts, align='center', alpha=0.5)
    plt.yticks(y_pos, words)
    plt.xlabel('Usage')
    plt.title('Word usage')

    
    plt.show()
    
    

dictionary = worder(file_string)
graphWords(dictionary)

    
