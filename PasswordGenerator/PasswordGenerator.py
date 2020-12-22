#Password Generator Mini Project

from random import randint

specChars = "!@#$%^&*()_+{}:<>?"
specCharsLen = len(specChars)
nums = "1234567890"
numsLen = len(nums)
chars = "qwertyuiopasdfghjklzxcvbnm"
charsLen = len(chars)
password = ""

while len(password) < 15:
    val = randint(1,3) #randomizes whether character will be special, number, or letter
    #Randomizes which special, number, or letter is placed in password
    if val == 1: 
        ind = randint(0,specCharsLen-1)
        password = password + specChars[ind]
    elif val == 2:
        ind = randint(0,numsLen-1)
        password = password + nums[ind]
    else:
          ind = randint(0,charsLen-1)
          password = password + chars[ind]

print(password)
input()
    
