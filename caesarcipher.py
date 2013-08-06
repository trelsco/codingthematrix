import string

### A crisp Caeser Cipher in Python using comprehensions and dictionary types
### originally created while taking edX 6.00x from MIT; cleaned up after learning more on comprehensions

def caesarCipher(shift):
  L = string.ascii_lowercase
  U = string.ascii_uppercase
  cipher = {U[i]:(U[shift:]+U[:shift])[i] for i in range(26)}
  cipher.update({L[i]:(L[shift:]+L[:shift])[i] for i in range(26)})
  return cipher
  
def putCoder(text,coder):
  L = string.ascii_lowercase
  U = string.ascii_uppercase
  res = ''
  for i in text:
    if i not in U and i not in L: res += i
    else: res += coder[i]
  return res
  
def applyShift(text,shift):
  return putCoder(text,caesarCipher(shift))
  
