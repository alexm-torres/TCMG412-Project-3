import http_access_log.txt
import requests

with open('topsites.txt') as my_file:
    array=my_file.readlines()

for i in array:
    if array[i].find("Apr") != -1 && array[i].find("1995") != -1:
        array[i].append("4")
    else if array[i].find("May") != -1 && array[i].find("1995") != -1:
        array[i].append("5")
    else if array[i].find("Jun") != -1 && array[i].find("1995") != -1:
        array[i].append("6")
    else if array[i].find("Jul") != -1 && array[i].find("1995") != -1:
        array[i].append("7")
    else if array[i].find("Aug") != -1 && array[i].find("1995") != -1:
        array[i].append("8")
    else if array[i].find("Sep") != -1 && array[i].find("1995") != -1:
        array[i].append("9")
    else if array[i].find("Oct") != -1 && array[i].find("1995") != -1:
        array[i].append("10")
    else:
        array[i] = array[i]

countsix = 0
countall = len(array)

for i in array:
    if array[i].endswith("4"):
        countsix = len(array) - countall
        break


print("Total Number of Requests in the past six months: ", countsix)
print("Total Number of Requests: ", countall)