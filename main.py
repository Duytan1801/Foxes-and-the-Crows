
texts = []

file = open(r'shakespeare.txt')

for line in file:
    for word in line.split():
        if word != "\n" and "\\" not in word:
            texts.append(word)

counts = {}

for text in texts:
    if text not in counts:
        counts[text] = 1
    else:
        counts[text] += 1


sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)

#print(sorted_counts)
top_10 = sorted_counts[:60]
print(top_10)
#print(texts)