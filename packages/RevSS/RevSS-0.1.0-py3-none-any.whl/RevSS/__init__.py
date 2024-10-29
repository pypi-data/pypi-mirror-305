import os

fileName = "RevSS-Save.RevSS"

def save(adress,data):

    if type(adress) != str:
        raise TypeError

    with open(fileName, "a") as file:
        file.write(adress + "|" + str(type(data)).removeprefix("<class '").removesuffix("'>") + "|" + str(data) + "\n")

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

def load(name):

    if type(name) != str:
        raise TypeError

    with open(fileName, "r") as file:

        for data in file.readlines():
            data = processList(list(data))

            if data[0] != name:
                continue
            
            if data[1] == "int":
                return int(data[2])
            if data[1] == "bool":
                return bool(data[2])
            if data[1] == "string":
                return str(data[2])
            if data[1] == "float":
                return float(data[2])

def listVariables():
    with open(fileName, "r") as file:

        variableNames = []

        for data in file.readlines():
            data = processList(list(data))
            variableNames.append(data[0])

        print(variableNames)
        return variableNames

def findVariableLine(name):
    with open(fileName, "r") as file:
        for line_num, data in enumerate(file):

            data2 = processList(list(data))
            if data2[0] == name:
                return line_num

    raise ValueError(f"The variable '{name}' was not found in the file.")

def remove(name):

    lineToRemove = findVariableLine(name)

    with open(fileName, "r") as file:
        lines = file.readlines()
    
    if 0 <= lineToRemove < len(lines):
        del lines[lineToRemove]
    else:
        raise IndexError(f"line {lineToRemove} is out of range.")
    
    with open(fileName, "w") as file:
        file.writelines(lines)

def clearAllVariables():
    open(fileName, "w")

def removeVariableFile():
    try:
        os.remove(fileName)
    except FileNotFoundError:
        raise LookupError(f"{fileName} does not exist.")
    except PermissionError:
        raise PermissionError(f"Cannot delete {fileName}.")
