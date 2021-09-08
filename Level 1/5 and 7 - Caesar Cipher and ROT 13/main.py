def readString():
    encodedString = input("-> ")
    rotValue = int(input("Enter the Value of ROT or 99 for Brute Force: "))
    print()

    return encodedString, rotValue

def decodeString(encodedString, rotValue):
    decodeList = []
    for char in encodedString:
        char = ord(char) - rotValue
        char = chr(char)
        decodeList.append(char)
  
    decodedString = "".join(decodeList)

    return decodedString

def bruteForce(encodedString):
    passList = []

    for x in range(31):
        decodeString = []
        
        for char in encodedString:
            char = ord(char) - x
            char = chr(char)
            decodeString.append(char)
        
        passList.append(''.join(decodeString))

    return passList

def main():
    encodedString, rotValue = readString()

    if rotValue == 99:
        arrayResults = bruteForce(encodedString)
        for x, result in enumerate(arrayResults):
            print(f"Attempt #{x} - {result}")

    else:
        decodedString = decodeString(encodedString, rotValue)
        print(decodedString)

if __name__ == '__main__':
    main()
