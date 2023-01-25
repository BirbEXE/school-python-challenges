def encode(string, shift):
  encodedstreeng = ""
  for char in string:
    encodedcharr = ord(char) + int(shift)
    encodedstreeng = encodedstreeng + chr(encodedcharr)

  return(encodedstreeng)

def deencode(string, shift):
  deencodedstreeng = ""
  for char in string:
    deencodedcharr = ord(char) - int(shift)
    deencodedstreeng = deencodedstreeng + chr(deencodedcharr)

print(encode(input("enter string to encode: "), input("enter character shift: ")))