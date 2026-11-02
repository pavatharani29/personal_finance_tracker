import nltk
import string
import matplotlib.pyplot as plt

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from collections import Counter

# Download required NLTK data (run once)
nltk.download('punkt')
nltk.download('stopwords')

print("=== KEYWORD EXTRACTION USING NLP (TF-IDF BASED) ===\n")

# Input text
text = input("Enter your text paragraph:\n")

# Sentence & word tokenization
sentences = sent_tokenize(text)
words = word_tokenize(text.lower())

# Remove punctuation
words = [w for w in words if w not in string.punctuation]

# Stopword removal
stop_words = set(stopwords.words('english'))
filtered_words = [w for w in words if w not in stop_words]

# Display preprocessing info
print("\nPreprocessing text...")
print("Total Sentences :", len(sentences))
print("Total Words     :", len(words))
print("Filtered Words  :", len(filtered_words))

# -------------------------------
# Word frequency (Before TF-IDF)
# -------------------------------
freq_dist = Counter(filtered_words)
top_freq = freq_dist.most_common(10)

freq_words = [w for w, c in top_freq]
freq_values = [c / len(filtered_words) for w, c in top_freq]

# -------------------------------
# TF-IDF Calculation
# -------------------------------
vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = vectorizer.fit_transform([text])
feature_names = vectorizer.get_feature_names_out()
tfidf_scores = tfidf_matrix.toarray()[0]

tfidf_dict = dict(zip(feature_names, tfidf_scores))
sorted_tfidf = sorted(tfidf_dict.items(), key=lambda x: x[1], reverse=True)[:15]

print("\nTop Keywords and their TF-IDF Scores:\n")
print("Keyword        TF-IDF Score")
for word, score in sorted_tfidf:
    print(f"{word:<14} {score:.6f}")

# -------------------------------
# Plot 1: Top Frequent Words
# -------------------------------
plt.figure()
plt.barh(freq_words, freq_values)
plt.xlabel("Frequency")
plt.ylabel("Words")
plt.title("Top 10 Frequent Words (Before TF-IDF)")
plt.gca().invert_yaxis()
plt.show()

# -------------------------------
# Plot 2: TF-IDF Keywords
# -------------------------------
tfidf_words = [w for w, s in sorted_tfidf]
tfidf_values = [s for w, s in sorted_tfidf]

plt.figure()
plt.barh(tfidf_words, tfidf_values)
plt.xlabel("TF-IDF Score")
plt.ylabel("Keywords")
plt.title("Top Keywords by TF-IDF Score")
plt.gca().invert_yaxis()
plt.show()

print("\nKeyword Extraction using NLP completed successfully.")
