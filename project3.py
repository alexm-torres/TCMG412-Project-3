import http_access_log.txt
import requests

with open("http_access_log.txt") as file_in:
    array = []
    for line in file_in:
        array.append(line)

for i in array:
    print(array)
#    if array[i].find("Apr") != -1 and array[i].find("1995") != -1:
 #       array[i].append("4")
  #  elif array[i].find("May") != -1 and array[i].find("1995") != -1:
   #     array[i].append("5")
    #elif array[i].find("Jun") != -1 and array[i].find("1995") != -1:
     #   array[i].append("6")
    #elif array[i].find("Jul") != -1 and array[i].find("1995") != -1:
     #   array[i].append("7")
    #elif array[i].find("Aug") != -1 and array[i].find("1995") != -1:
     #   array[i].append("8")
    #elif array[i].find("Sep") != -1 and array[i].find("1995") != -1:
     #   array[i].append("9")
    #elif array[i].find("Oct") != -1 and array[i].find("1995") != -1:
     #   array[i].append("10")
    #else:
     #   array[i] = array[i]

countsix = 0
countall = len(array)

for i in array:
    if array[i].endswith("4"):
        countsix = len(array) - countall
        break


print("Total Number of Requests in the past six months: ", countsix)
print("Total Number of Requests: ", countall)