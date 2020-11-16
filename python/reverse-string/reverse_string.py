def reverse(inputString):
    outputString=''
    for index in range(len(inputString)):
        outputString= outputString + inputString[-index-1]
    return outputString
    pass

