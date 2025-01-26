import string
import matplotlib.pyplot as plt
from collections import Counter

stop_words = open('stop_words.txt', encoding='utf-8').read()
stop_words_cleaned = stop_words.translate(str.maketrans('', '', string.punctuation))
stop_words_tokanized = stop_words_cleaned.split()

text = open('read.txt', encoding='utf-8').read()
lower_case = text.lower()

cleaned_text = lower_case.translate(str.maketrans('', '', string.punctuation))

tokanized_words = cleaned_text.split()

final_words = []
for word in tokanized_words:
    if word not in stop_words_tokanized:
        final_words.append(word)

emotion_list = []
with open('emotions.txt', 'r') as file:
    for line in file:
        clear_line = line.replace('\n', '').replace(',', '').replace("'", '')
        word, emotion = clear_line.split(':')
        
        if word in final_words:
            emotion_list.append(emotion)


w = Counter(emotion_list)
print(w)

fig, ax1 = plt.subplots()
ax1.bar(w.keys(), w.values())
fig.autofmt_xdate()

plt.savefig('graph.png')
plt.show()