import json
import re
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report
from imblearn.over_sampling import RandomOverSampler
import nltk
from nltk.corpus import stopwords
import snowballstemmer
from trnlp import TrnlpWord  # 
import joblib 

# Türkçe stopwords indir
nltk.download('stopwords')

# Veri yolu
data_path = "data/urunler-yorumlar.json"

# Veri yükleme
with open(data_path, 'r', encoding='utf-8-sig') as f:
    data = json.load(f)

# Her ürünün yorumlarını tek listeye dönüştür
reviews = []
for product in data:
    for r in product["reviews"]:
        reviews.append({
            "product_name": product["name"],
            "brand": product["brand"],
            "star": r["star"],
            "review": r["review"]
        })

df = pd.DataFrame(reviews)
print(f"Toplam yorum: {len(df)}")
df = df.sample(frac=0.25, random_state=42)
print(f"İşlenecek yorum sayısı: {len(df)}")

# Boş yorumları çıkar
df = df.dropna(subset=["review"])

# ⭐ Binary (2 sınıf) sentiment mapping
def map_sentiment(star):
    if star >= 4:
        return "Positive"
    else:
        return "Negative"

df["label"] = df["star"].apply(map_sentiment)

#  --- NLP ÖN İŞLEME ---
stemmer = snowballstemmer.stemmer('turkish')
lemmatizer = TrnlpWord()

def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zçğıöşü\s]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    text = ' '.join([stemmer.stemWord(w) for w in text.split()])

    lemmas = []
    for word in text.split():
        lemmatizer.setword(word)
        lemmas.append(lemmatizer.get_stem)
    text = ' '.join(lemmas)
    return text


print(" Yorumlar temizleniyor, lütfen bekleyin...")
df["review"] = df["review"].apply(preprocess_text)
print(" Temizleme işlemi tamamlandı.\n")

# Eğitim verisini hazırla
X = df["review"]
y = df["label"]

stop_words = stopwords.words("turkish")
vectorizer = CountVectorizer(stop_words=stop_words)
X_vec = vectorizer.fit_transform(X)

ros = RandomOverSampler(random_state=42)
X_resampled, y_resampled = ros.fit_resample(X_vec, y)

# Eğitim / Test bölme
X_train, X_test, y_train, y_test = train_test_split(
    X_resampled, y_resampled, test_size=0.2, random_state=42
)

# Model
model = MultinomialNB()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print("\n Sınıflandırma Sonuçları (Binary + Dengelemeli):")
print(classification_report(y_test, y_pred))

# 🔹 Model ve vectorizer kaydet
joblib.dump(model, "model.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")
joblib.dump((X_test, y_test, y_pred), "eval_data.pkl")

print("\n Model, vectorizer ve test verisi kaydedildi.")
print(" 'evaluate.py' dosyasını çalıştırarak grafiklerle değerlendirme yapabilirsin.\n")

#  Örnek tahmin
sample_texts = [
    "ürün berbat hiç beğenmedim",
    "kırık geldi, hiç memnun değilim",
    "mükemmel kalite çok memnun kaldım",
    "parasını hak ediyor gerçekten güzel"
]
sample_vec = vectorizer.transform(sample_texts)
sample_pred = model.predict(sample_vec)

print(" Örnek Tahminler:")
for txt, pred in zip(sample_texts, sample_pred):
    print(f" '{txt}' → {pred}")

print("\n Başladı (çıkmak için 'q' veya 'exit' yazın)\n")

while True:
    user_input = input("Yorum girin: ").strip()
    if user_input.lower() in ["q", "exit"]:
        print(" Program sonlandırıldı.")
        break
    if not user_input:
        print(" Boş metin girdiniz, lütfen tekrar deneyin.")
        continue
    user_vec = vectorizer.transform([user_input])
    user_pred = model.predict(user_vec)[0]
    print(f" '{user_input}' → Tahmin: {user_pred}\n")
