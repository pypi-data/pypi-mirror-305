import os

fileName = "RevSS-Save.RevSS"

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

def findVariableLine(name):
    with open(fileName, "r") as file:
        for line_num, data in enumerate(file):

            data2 = processList(list(data))
            if data2[0] == name:
                return line_num

    raise ValueError(f"The variable '{name}' was not found in the file.")

def listVariables():
    with open(fileName, "r") as file:

        variableNames = []

        for data in file.readlines():
            data = processList(list(data))
            variableNames.append(data[0])

        print(variableNames)
        return variableNames

def save(name,data):

    if type(name) != str:
        raise TypeError

    if not os.path.isfile(fileName):
        file = open(fileName, "x")

    try:
        findVariableLine(name) ## check if variable already exists
        remove(name)
        save(name,data)
    except ValueError:
        with open(fileName, "a") as file:
            dataType = str(type(data)).removeprefix("<class '").removesuffix("'>")
            file.write(name + "|" + dataType + "|" + str(data) + "\n")

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
