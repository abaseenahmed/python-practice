print("_____________________________ Strings Data Types ___________________________")
string = "Hello, This is a simple string data type program in Python."
print(f'The string is: {string}')

#------------------------ Question No 1 -----------------------
str = "Madam"
if all(str[i] == str[-i -1] for i in range(len(str) // 2)):
    print(f'The string "{str}" is a palindrome.')
else:
    print(f'The string "{str}" is not a palindrome.')

#------------------------ Question No 2 -----------------------
name = input("Enter your name: ")
print(f'Hello, {name}! Welcome to the program.')

#------------------------ Question No 3 -----------------------
charStr = input("Enter a string: ")
charCount = len(charStr)
print(f'The number of characters in the string "{charStr}" is: {charCount}.')

#------------------------ Question No 4 -----------------------
titleStr = input("Enter a Title: ")
titleUpper = titleStr.upper()
titleLower = titleStr.lower()
titleCapitalize = titleStr.capitalize()
titleTitle = titleStr.title()
print(f'The original title is: {titleStr}')
print(f'The title in uppercase is: {titleUpper}')
print(f'The title in lowercase is: {titleLower}')
print(f'The title with the first letter capitalized is: {titleCapitalize}')
print(f'The title in title case is: {titleTitle}')

#------------------------ Question No 5 -----------------------
wordStr = input("Enter a word: ")
repeat = int(input("Enter the number of times to repeat the word: "))
repeatedWord = wordStr * repeat
print(f'The word "{wordStr}" repeated {repeat} times is: {repeatedWord}')

#------------------------ Question No 6 -----------------------
nameInitials = input("Enter your full name: ")
initials = ''.join([name[0].upper() for name in nameInitials.split()])
print(f'The initials of your name "{nameInitials}" are: {initials}')

#------------------------ Question No 7 -----------------------
sentenceStr = input("Enter a sentence: ")
removeSpaces = sentenceStr.replace(" ", "")
print(f'The sentence without spaces is: {removeSpaces}')


#------------------------ Question No 8 -----------------------
strSentence = input("Enter a sentence: ")
reversedSentence = strSentence[::-1]
print(f'The reversed sentence is: {reversedSentence}')
print(strSentence.center(50, '-'))
print(strSentence.count('a'))
print(strSentence.encode('utf-8'))
print(strSentence.endswith('.'))
print(strSentence.find('is'))
print(strSentence.expandtabs())
print(strSentence.format())
print(strSentence.zfill(20))