def rotate(inputString,rotateValue):
    #lowercase lower = 97
    #lowercase upper = 122
    
    #uppercase lower = 65
    #uppercase upper = 90
    rotateValue = rotateValue % 26
    if rotateValue == 0:
            return inputString
    outputString = ''
    for charLocation in range(len(inputString)):
        charValue = ord(inputString[charLocation])
        if (charValue >= 97 and charValue <=122):
            if charValue+rotateValue > 122:
                outputString += chr(charValue + rotateValue - 26)
            else:
                outputString += chr(charValue + rotateValue)
        elif (charValue >= 65 and charValue <=90):
            if charValue + rotateValue > 90:
                outputString += chr(charValue + rotateValue - 26)
            else:
                outputString += chr(charValue + rotateValue)
        else:
            outputString += inputString[charLocation]
    return outputString