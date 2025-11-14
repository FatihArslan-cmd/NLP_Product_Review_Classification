<div align="center">
  <h1>Turkish Product Review Sentiment Analysis</h1>
  <p>
    <a href="https://github.com/FatihArslan-cmd/NLP_Product_Review_Classification"><strong>🌟 Explore the docs »</strong></a>
    <br/>
    <a href="https://github.com/FatihArslan-cmd/NLP_Product_Review_Classification/issues">🐛 Report Bug</a>
    .
    <a href="https://github.com/FatihArslan-cmd/NLP_Product_Review_Classification/issues">✨ Request Feature</a>
  </p>
</div>

<hr/>

<h2>📖 Table of Contents</h2>
<ol>
  <li><a href="#about-the-project">📘 About The Project</a></li>
  <li><a href="#getting-started">🚀 Getting Started</a></li>
  <ul>
    <li><a href="#prerequisites">📋 Prerequisites</a></li>
    <li><a href="#installation">⚙️ Installation</a></li>
    <li><a href="#usage">🛠️ Usage</a></li>
  </ul>
  <li><a href="#screenshots">📷 Screenshots</a></li>
  <li><a href="#dependencies">📦 Dependencies</a></li>
  <li><a href="#contributing">🤝 Contributing</a></li>
  <li><a href="#contact">📞 Contact</a></li>
  <li><a href="#important-versions">📌 Important Versions</a></li>
</ol>

<hr/>

<h2 id="about-the-project">📘 About The Project</h2>
<p>
This project is a <strong>Turkish Product Review Sentiment Analysis</strong> tool. 
It classifies reviews as <strong>Positive</strong> or <strong>Negative</strong> using classical NLP techniques.
</p>
<p><strong>Key Features:</strong></p>
<ul>
  <li>Text preprocessing: cleaning, normalization, tokenization, stemming, lemmatization</li>
  <li>Bag-of-Words vectorization (<code>CountVectorizer</code>)</li>
  <li>Binary classification (<code>Multinomial Naive Bayes</code>)</li>
  <li>Class balancing using <code>RandomOverSampler</code></li>
  <li>Real-time user input classification</li>
  <li>Graphical evaluation with <strong>Confusion Matrix</strong> and <strong>Performance Metrics</strong></li>
  <li>PDF report generation</li>
</ul>

<hr/>

<h2 id="screenshots">📷 Screenshots</h2>
<p align="center">
  <img src="https://github.com/user-attachments/assets/confusion_matrix.png" width="300" alt="Confusion Matrix"/>
  <img src="https://github.com/user-attachments/assets/performance_metrics.png" width="300" alt="Performance Metrics"/>
  <img src="https://github.com/user-attachments/assets/evaluation_report.png" width="300" alt="PDF Report"/>
</p>

<hr/>

<h2 id="prerequisites">📋 Prerequisites</h2>
<ul>
  <li>Python 3.10+</li>
  <li>pip (latest version)</li>
  <li>Optional: virtual environment recommended</li>
</ul>

<hr/>

<h2 id="getting-started">🚀 Getting Started</h2>

<h3 id="installation">⚙️ Installation</h3>

<pre><code class="bash">
git clone https://github.com/FatihArslan-cmd/NLP_Product_Review_Classification.git
cd NLP_Product_Review_Classification
pip install -r requirements.txt
</code></pre>

<h3 id="usage">🛠️ Usage</h3>

<p><strong>Run the main program:</strong></p>
<pre><code class="bash">
python main.py
</code></pre>

<p><strong>Example console output:</strong></p>
<pre><code class="text">
Toplam yorum: 240866
İşlenecek yorum sayısı: 60216
Yorumlar temizleniyor, lütfen bekleyin...
Temizleme işlemi tamamlandı.

Sınıflandırma Sonuçları (Binary + Dengelemeli):
precision recall f1-score support
Negative 0.82 0.83 0.82 10596
Positive 0.83 0.82 0.82 10733
accuracy 0.82 21329

Örnek Tahminler:
'ürün berbat hiç beğenmedim' → Negative
'kırık geldi, hiç memnun değilim' → Negative
'mükemmel kalite çok memnun kaldım' → Positive
'parasını hak ediyor gerçekten güzel' → Positive

Başladı (çıkmak için 'q' veya 'exit' yazın)
</code></pre>

<p><strong>Test user input:</strong></p>
<pre><code class="text">
Yorum girin: berbat
'berbat' → Tahmin: Negative

Yorum girin: mükemmel
'mükemmel' → Tahmin: Positive
</code></pre>

<p><strong>Evaluate model and generate PDF report:</strong></p>
<pre><code class="bash">
python evaluate.py
</code></pre>

<p>This creates:</p>
<ul>
  <li>confusion_matrix.png</li>
  <li>performance_metrics.png</li>
  <li>evaluation_report.pdf</li>
</ul>

<hr/>

<h2 id="dependencies">📦 Dependencies</h2>
<pre><code class="text">
pandas, scikit-learn, nltk, imbalanced-learn, snowballstemmer, trnlp, matplotlib, joblib, reportlab
</code></pre>

<hr/>

<h2 id="contributing">🤝 Contributing</h2>
<p>Contributions are welcome!</p>
<ol>
  <li>Fork the project</li>
  <li>Create your feature branch (<code>git checkout -b feature/AmazingFeature</code>)</li>
  <li>Commit your changes (<code>git commit -m 'Add some AmazingFeature'</code>)</li>
  <li>Push to the branch (<code>git push origin feature/AmazingFeature</code>)</li>
  <li>Open a Pull Request</li>
</ol>

<hr/>

<h2 id="important-versions">📌 Important Versions</h2>
<ul>
  <li>Python: 3.10+</li>
  <li>scikit-learn: 1.3.0+</li>
  <li>nltk: 3.8+</li>
  <li>reportlab: 4.0+</li>
</ul>

<hr/>

<h2 id="contact">📞 Contact</h2>
<p>
<strong>Fatih Arslan</strong> – <em>Software Engineering Student</em> – <a href="https://github.com/FatihArslan-cmd">GitHub</a>
</p>
