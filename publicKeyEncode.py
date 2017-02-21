from random import randint

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def coprime(a, b):
    return gcd(a, b) == 1
  
primesUnder20 = [11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

def generateKeys():
  
  print("Pick one of the following prime numbers:")
  for p in primesUnder20:
    print(p)
  print()
  prime1 = int(input())
  if prime1 not in primesUnder20:
    return ["Error", "Not a valid prime number."]
  print("-- Prime 1: " + str(prime1))
  print()
  
  print("Pick another of the following prime numbers:")
  for p in primesUnder20:
    if p != prime1:
      if p != prime1 - 1:
        if p != prime1 + 1:
          print(p)
  print()
  prime2 = int(input())
  if prime2 not in primesUnder20:
    return ["Error", "Not a valid prime number."]
  if prime2 == prime1:
    return ["Error", "Primes chosen are the same"]
  print("-- Prime 2: " + str(prime2))
  print()
  
  modulus = prime1 * prime2
  coprimesOf = (prime1 - 1) * (prime2 - 1)
  print("-- Modulus: " + str(modulus))
  
  print()
  print("Pick one of the following coprimes with " + str(coprimesOf) + " [(" + str(prime1) + " - 1) * (" + str(prime2) + " - 1)]:")
  validEEs = []
  for n in range(2, coprimesOf):
    if coprime(n, coprimesOf):
      validEEs.append(n)
      print(n)
  print()
  print("Pick one of the above coprimes with " + str(coprimesOf) + " [(" + str(prime1) + " - 1) * (" + str(prime2) + " - 1)]:")
  print()
  ee = int(input())
  if ee in validEEs:
    print("-- Encryption Exponent: " + str(ee))
    print()
    publicKeys = [ee, modulus]
  else:
    return ["Error", "Not a valid coprime."]
  
  de = 0
  for n in range(2, coprimesOf):
    if (n * ee) % coprimesOf == 1:
      de = n
      print("-- Decrypt Exponent: " + str(de))
      privateKeys = [de, modulus]
      return [publicKeys, privateKeys]
  if de == 0:
    return ["Error", "No private decrypt exponent found."]
  return["Error", "Ended without valid return"]

def charToTildeString(tildeString, nonAsciiInt):
  if nonAsciiInt > 93:
    rand = randint(0, 93)
    tildeString += chr(rand + 32)
    nonAsciiInt = nonAsciiInt - rand
    return charToTildeString(tildeString, nonAsciiInt)
  else:
    tildeString += chr(nonAsciiInt + 32)
    tildeString += "~"
    return tildeString
  

def encrypt(plainMessage, key):
  newString = ""
  count = 0
  for c in plainMessage:
    intC = ord(c) - 32
    if intC > 93:
      return "Error"
    if intC < 0:
      return "Error"
    newIntC = ((intC**key[0]) % key[1])
    if newIntC > 93:
      tildeAdd = charToTildeString("~", newIntC)
      newString += tildeAdd
    else: 
      newChar = chr(newIntC + 32)
      newString += newChar
      count += 1
      if count > 93:
        count = 0
  return newString
  
def decrypt(encMessage, key):
  newString = ""
  tildeBank = 0
  inTilde = False
  count = 0
  for c in encMessage:
    convChar = False
    if c == "~":
      if inTilde:
        intC = tildeBank
        tildeBank = 0
        inTilde = False
        convChar = True
      else:
        inTilde = True
    else:
      if inTilde:
        tildeBank += ord(c) - 32
      else:
        intC = ord(c) - 32
        if intC > 93:
          return "Error"
        if intC < 0:
          return "Error"
        convChar = True
    if convChar:
      newIntC = ((intC**key[0]) % key[1])
      newChar = chr(newIntC + 32)
      newString += newChar
      count +=1
      if count > 93:
        count = 0
  return newString

print("Do you want to encrypt or decrypt or generate keys?")
print("1. Encrypt")
print("2. Decrypt")
print("3. Generate Keys")
choice = input()

if choice.upper() == ("1" or "ENCRYPT" or "E"):
  message = input("What is your message?")
  keys = []
  keys.append(int(input("\nWhat is the first number in your recipient's public key?\n")))
  keys.append(int(input("\nWhat is the second number in your recipient's public key?\n")))
  encryptedMessage = encrypt(message, keys)
  print("\nEncrypted message inside ' ':\n'" + encryptedMessage + "'")
  
elif choice.upper() == ("2" or "DECRYPT" or "D"):
  message = input("What is your encrypted message?")
  keys = []
  keys.append(int(input("\nWhat is the first number in your private key?\n")))
  keys.append(int(input("\nWhat is the second number in your private key?\n")))
  decryptedMessage = decrypt(message, keys)
  print("\nDecrypted message inside ' ':\n'" + decryptedMessage + "'")

elif choice.upper() == ("3" or "GENERATE KEYS" or "GENERATEKEYS" or "KEYS" or "GENERATE" or "G"):
  keys = generateKeys()
  print("Your new keys are below. Keep your private key somehwere safe. Share your public key.")
  print("Public Keys: " + str(keys[0][0]) + ", " + str(keys[0][1]))
  print("Private Keys: " + str(keys[1][0]) + ", " + str(keys[1][1]))
  
else:
  print("Please choose either 1, 2, or 3.")