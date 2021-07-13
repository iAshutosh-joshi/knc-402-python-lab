file = open("lab4.txt","r", encoding="utf-8")
frequent_word = ""
frequency = 0
words = []
print("Lab 4 by Ashutosh Joshi")
# Traversing file line by line
for line in file:
	line_word = line.lower().replace(',','').replace('.','').split(" ");
	for w in line_word:
		words.append(w);
		
# Finding the max occured word
for i in range(0, len(words)):
	count = 1;
	for j in range(i+1, len(words)):
		if(words[i] == words[j]):
			count = count + 1;
	if(count > frequency):
		frequency = count;
		frequent_word = words[i];

print("Most repeated word: " + frequent_word)
print("Frequency: " + str(frequency))
file.close();