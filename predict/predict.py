import joblib

model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

print("Tahmin sistemi hazır. Çıkmak için 'q' yaz.")

while True:
    text = input("Yorum: ")
    if text.lower() == "q":
        break
    
    vec = vectorizer.transform([text])
    pred = model.predict(vec)[0]
    print(f"Tahmin: {pred}")
