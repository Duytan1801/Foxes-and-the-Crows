phrases = []

file = open(r"extracted_sections\section_01_Chapter_I_Elliptic_Integrals..md")

for sentence in file:
    phrases.append(sentence)


print(phrases)