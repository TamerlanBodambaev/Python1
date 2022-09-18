s = input('Enter a string')

print("The original string is : " + str(s))

letter = "е"

word_count = 0

word = 0

for i in range(len(s)):
	if s[i][1] == letter:
		word += 1
		word_count = 1
		
	elif s[i] == " ":
		
		word_count = 0
		
print("Words count :", word)

