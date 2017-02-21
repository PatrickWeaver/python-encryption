def keyEncode(myString, myPassword):
  newString = ""
  for c in myPassword:
    if ord(c) > 126:
      return "Error"
  count = 0
  passwordLength = len(myPassword)
  for c in myString:
    intC = ord(c)
    if intC > 126:
      return "Error"
    if intC < 32:
      return "Error"
    offset = ord(myPassword[count])
    newIntC = intC + offset
    if newIntC > 126:
      newIntC = newIntC - 95
      if newIntC > 126:
        newIntC = newIntC - 95
    newChar = chr(newIntC)
    newString += newChar
    
    count += 1
    if count == passwordLength:
      count = 0
  return newString
  
def keyUnencode(myEncodedString, myPassword):
  newString = ""
  for c in myPassword:
    if ord(c) > 126:
      return "Error"
  count = 0
  passwordLength = len(myPassword)
  for c in myEncodedString:
    intC = ord(c)
    if intC > 126:
      return "Error"
    if intC < 32:
      return "Error"
    offset = ord(myPassword[count])
    newIntC = intC - offset
    if newIntC < 32:
      newIntC = newIntC + 95
      if newIntC < 32:
        newIntC = newIntC + 95
    newChar = chr(newIntC)
    newString += newChar
    
    count += 1
    if count == passwordLength:
      count = 0
  return newString
  
  
print("Do you want to encrypt or decrypt?")
print("1. Encrypt")
print("2. Decrypt")
choice = input()

if choice.upper() == ("1" or "ENCRYPT"):
  string = input("What is your message?\n")
  password = input("Give me a secret password:\n")
  newMessage = keyEncode(string, password)
  print("Encoded Message with offset" + str(password) + " inside ':")
  print("'" + newMessage + "'")
  print("")
  print("Unencoding to confirm . . .")
  print("")
  originalMessage = keyUnencode(newMessage, password)
  print("Unencoded Message:")
  print(originalMessage)
elif choice.upper() == ("2" or "DECRYPT"):
  string = input("What is your encrypted message?\n")
  password = input("What is your secret password?\n")
  print("")
  print("Unencoding . . .")
  print("")
  originalMessage = keyUnencode(string, password)
  print("Unencoded Message inside ':")
  print("'" + originalMessage + "'")
else:
  print("Please choose either 1 or 2.")