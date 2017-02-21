def offsetEncode(myString, myOffset):
  newString = ""
  intOffset = int(myOffset)
  for c in myString:
    intC = ord(c)
    if intC > 126:
      return "Error"
    if intC < 32:
      return "Error"
    newIntC = intC + intOffset
    if newIntC > 126:
      newIntC = newIntC - 95
    newChar = chr(newIntC)
    newString += newChar
  return newString
  
def offsetUnencode(myEncodedString, myOffset):
  newString = ""
  intOffset = int(myOffset)
  for c in myEncodedString:
    intC = ord(c)
    if intC > 126:
      return "Error"
    if intC < 32:
      return "Error"
    newIntC = intC - intOffset
    if newIntC < 32:
      newIntC = newIntC + 95
    newChar = chr(newIntC)
    newString += newChar
  return newString
  

print("Do you want to encrypt or decrypt?")
print("1. Encrypt")
print("2. Decrypt")
choice = input()

if choice.upper() == ("1" or "ENCRYPT"):
  string = input("What is your message?\n")
  offset = input("Give me a number between 1 and 93: ")
  newMessage = offsetEncode(string, offset)
  print("Encoded Message with offset" + str(offset) + "  inside ':")
  print("'" + newMessage + "'")
  print("")
  print("Unencoding to confirm . . .")
  print("")
  originalMessage = offsetUnencode(newMessage, offset)
  print("Unencoded Message:")
  print("'" + originalMessage + "'")
elif choice.upper() == ("2" or "DECRYPT"):
  string = input("What is your encrypted message?\n")
  offset = input("What is your secret offset number?\n")
  print("")
  print("Unencoding . . .")
  print("")
  originalMessage = offsetUnencode(string, offset)
  print("Unencoded Message inside ':")
  print("'" + originalMessage + "'")
else:
  print("Please choose either 1 or 2.")