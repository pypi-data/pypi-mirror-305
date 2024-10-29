fileName = "RevSS-Save.RevSS"

def save(adress,data):

    if type(adress) != str:
        raise TypeError

    saveFile = open(fileName, "a")
    saveFile.write(adress + "|" + str(type(data)).removeprefix("<class '").removesuffix("'>") + "|" + str(data) + "\n")
    saveFile.close()

def processList(list):
    processedList = []
    data = ""
    for i in list:

        if i == "|":
            processedList.append(data)
            data = ""
            continue
        
        if i == "\n":
            processedList.append(data)
            return processedList

        if i != "|":
            data += i
            continue

def load(requestedName):

    if type(requestedName) != str:
        raise TypeError

    file = open(fileName, "r")

    for data in file.readlines():
        data = processList(list(data))

        if data[0] != requestedName:
            continue
        
        if data[1] == "int":
            return int(data[2])
        if data[1] == "bool":
            return bool(data[2])
        if data[1] == "string":
            return str(data[2])
        if data[1] == "float":
            return float(data[2])