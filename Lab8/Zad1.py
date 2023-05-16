from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import matplotlib.pyplot as plt
from collections import Counter
from wordcloud import WordCloud

import re

with open('data/article.txt', 'r') as file:
    data = file.read().replace('\n', ' ')
    words = re.sub("[^a-zA-Z ]+", "", data)
    tokens = word_tokenize(words)

# print(tokens)

stop_words = set(stopwords.words('english'))
stop_words.add('say')
stop_words.add('says')
stop_words.add('said')

filtered = [w for w in tokens if not w.lower() in stop_words]

# print(filtered)

lemmatizer = WordNetLemmatizer()

lemmatized = [lemmatizer.lemmatize(w) for w in filtered]

# print(lemmatized)

print("Word count: " + str(len(lemmatized)))

word_counts = Counter(lemmatized)

top_words = word_counts.most_common(10)

words_list = [x[0] for x in top_words]
counts_list = [x[1] for x in top_words]

plt.bar(words_list, counts_list)
plt.title('Most common words')
plt.xlabel('Word')
plt.ylabel('Count')
plt.show()

bigstring = (" ").join(lemmatized)

wordcloud = WordCloud(width = 750, height = 500).generate(bigstring)
plt.figure(figsize=(15,8))
plt.imshow(wordcloud)
plt.axis("off")
plt.savefig("your_file_name"+".png", bbox_inches='tight')
plt.show()
plt.close()