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
  for x in range(len(arr)):
    dif = arr[-1][1] - arr[-x-1][1]
    print("*" * arr[-x-1][1] + (" " * int(dif)) + arr[-x-1][0])

dictionary = worder(file_string)
graphWords(dictionary)
