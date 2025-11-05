To run:

pip install -r requirements.txt

python .\main.py

Output:

Toplam yorum: 240866
İşlenecek yorum sayısı: 60216
 Yorumlar temizleniyor, lütfen bekleyin...
 Temizleme işlemi tamamlandı.


 Sınıflandırma Sonuçları (Binary + Dengelemeli):
              precision    recall  f1-score   support

    Negative       0.82      0.83      0.82     10596
    Positive       0.83      0.82      0.82     10733

    accuracy                           0.82     21329
   macro avg       0.82      0.82      0.82     21329
weighted avg       0.82      0.82      0.82     21329


 Model, vectorizer ve test verisi kaydedildi.
 'evaluate.py' dosyasını çalıştırarak grafiklerle değerlendirme yapabilirsin.

 Örnek Tahminler:
 'ürün berbat hiç beğenmedim' → Negative
 'kırık geldi, hiç memnun değilim' → Negative
 'mükemmel kalite çok memnun kaldım' → Positive
 'parasını hak ediyor gerçekten güzel' → Positive

 Başladı (çıkmak için 'q' veya 'exit' yazın)

Yorum girin: berbat
 'berbat' → Tahmin: Negative

Yorum girin: mukemmel
 'mukemmel' → Tahmin: Negative

Yorum girin: Güzel ürün
 'Güzel ürün' → Tahmin: Positive

Yorum girin:


python .\evaluate.py

To get pdf of graphical results
