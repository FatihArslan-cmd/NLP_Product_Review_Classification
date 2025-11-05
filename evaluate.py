import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay, accuracy_score, precision_score, recall_score, f1_score
import joblib
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from datetime import datetime

# Kaydedilen verileri yükle
model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")
X_test, y_test, y_pred = joblib.load("eval_data.pkl")

# 🎯 Temel metrikleri hesapla
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, pos_label="Positive")
recall = recall_score(y_test, y_pred, pos_label="Positive")
f1 = f1_score(y_test, y_pred, pos_label="Positive")

print(f"\n📈 Accuracy: {accuracy:.2f}")
print(f"🎯 Precision: {precision:.2f}")
print(f"🔁 Recall: {recall:.2f}")
print(f"💡 F1-Score: {f1:.2f}")

# 📊 Confusion Matrix görseli oluştur
cm = confusion_matrix(y_test, y_pred, labels=["Positive", "Negative"])
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=["Positive", "Negative"])
disp.plot(cmap="Blues")
plt.title("Confusion Matrix")
plt.tight_layout()
plt.savefig("confusion_matrix.png", dpi=300)
plt.close()

# 📈 Metrikleri bar grafiğiyle göster
metrics = ['Accuracy', 'Precision', 'Recall', 'F1 Score']
values = [accuracy, precision, recall, f1]

plt.figure(figsize=(6, 4))
plt.bar(metrics, values, color=['skyblue', 'orange', 'limegreen', 'orchid'])
plt.ylim(0, 1)
plt.title('Model Performance Metrics')
plt.xlabel('Metrics')
plt.ylabel('Score')
for i, v in enumerate(values):
    plt.text(i, v + 0.02, f"{v:.2f}", ha='center', fontweight='bold')
plt.tight_layout()
plt.savefig("performance_metrics.png", dpi=300)
plt.close()

# 📝 PDF raporu oluştur
pdf_filename = "evaluation_report.pdf"
c = canvas.Canvas(pdf_filename, pagesize=A4)
width, height = A4

# Başlık
c.setFont("Helvetica-Bold", 20)
c.drawString(180, height - 70, "NLP Model Evaluation Report")

# Tarih
c.setFont("Helvetica", 10)
c.drawString(460, height - 90, datetime.now().strftime("%Y-%m-%d %H:%M"))

# Metrik değerlerini yaz
c.setFont("Helvetica", 12)
c.drawString(50, height - 130, f"Accuracy:  {accuracy:.4f}")
c.drawString(50, height - 150, f"Precision: {precision:.4f}")
c.drawString(50, height - 170, f"Recall:    {recall:.4f}")
c.drawString(50, height - 190, f"F1 Score:  {f1:.4f}")

# Görselleri ekle
c.drawImage("confusion_matrix.png", 50, height - 550, width=250, height=250)
c.drawImage("performance_metrics.png", 320, height - 550, width=250, height=250)

# Açıklama
c.setFont("Helvetica", 11)
text = (
    "The Confusion Matrix chart shows how the model classifies positive and negative reviews.\n"
    "The Performance Metrics chart presents a comparative view of Accuracy, Precision, Recall, and F1-Score values.\n\n"
    "These results demonstrate that the CountVectorizer (Bag-of-Words) + MultinomialNB approach\n"
    "is an effective classical NLP solution for Turkish sentiment analysis."
)

text_object = c.beginText(50, height - 600)
for line in text.split("\n"):
    text_object.textLine(line)
c.drawText(text_object)

c.showPage()
c.save()

print("\n📄 'evaluation_report.pdf' başarıyla oluşturuldu!")
print("➡️ PDF dosyasında Confusion Matrix ve metrik grafikleri yer alıyor.")
