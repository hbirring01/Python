original = input('Enter a sentence that you wanat to translate to pig latin: ').lower().strip()

words = original.split()

newWords = []

vowels = ['a', 'e', 'i', 'o', 'u']

for word in words:
    if word[0] in vowels:
        newWords.append(word + 'yay')
    else:
        vowelPosition = 0
        for letter in word:
            if letter not in vowels:
                vowelPosition += 1
            else:
                break 
        cons = word[:vowelPosition]
        rest = word[vowelPosition:]
        newword = rest + cons + 'yay'
        newWords.append(newword)

output = ' '.join(newWords)
    
print(output)
