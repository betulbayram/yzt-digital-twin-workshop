# 👤 CV 2.0: Digital Twin

Bu proje, **Streamlit** ve **Groq (gpt-oss)** kullanarak oluşturulmuş kişisel bir yapay zeka asistanıdır. Yüklenen CV'yi okur ve işverenler veya ziyaretçiler için bir "Dijital İkiz" gibi davranarak soruları yanıtlar.

RAG (Retrieval-Augmented Generation) mimarisinin temellerini öğrenmek için tasarlanmıştır.

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white) ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) ![Groq](https://img.shields.io/badge/Groq-AI-orange?style=for-the-badge)

## 📂 Proje İçeriği

* **`app.py`**: Uygulamanın ana Python kodu.
* **`requirements.txt`**: Gerekli kütüphanelerin listesi.
* **`Resume.pdf` / `Resume.docx`**: Dijital ikizin verisi (Sizin CV'niz).

---

## 🚀 1. Kurulum (Local Bilgisayar)

Projeyi kendi bilgisayarınızda çalıştırmak için aşağıdaki adımları izleyin.

### 1.1. Dosyaları Hazırlayın
Projeyi indirin veya `git clone` ile çekin. Klasörün içine **mutlaka** kendi CV'nizi (`Resume.pdf` veya `Resume.docx` ismiyle) ekleyin.

### 1.2. Sanal Ortam Oluşturun (Opsiyonel ama Önerilir)
Terminal veya komut satırını açın:

```bash
# Windows için
python -m venv venv
venv\Scripts\\activate.bat

# Mac/Linux için
python3 -m venv venv
source venv/bin/activate
```

### 1.3. Kütüphaneleri Yükleyin
```bash
pip install -r requirements.txt
```

### 1.4. API Anahtarını Ayarlayın
Projenin çalışması için **Groq API Key** gereklidir.
1. Proje klasöründe `.streamlit` adında yeni bir klasör oluşturun.
2. Bu klasörün içine `secrets.toml` adında bir dosya oluşturun.
3. İçine şu satırı yapıştırın (Kendi anahtarınızı yazın):

```toml
GROQ_API_KEY = "gsk_SeninUzunApiKeyinBurayaGelecek"
```
*(Not: Eğer bu adımı yapamazsanız, uygulama açıldığında API key'i arayüzden de girebilirsiniz.)*

### 1.5. Uygulamayı Başlatın
```bash
streamlit run app.py
```
Tarayıcınız otomatik olarak açılacak ve Dijital İkiziniz hazır! 🎉

---

## ☁️ 2. Deployment (Streamlit Cloud)

Projeyi internette yayınlamak ve linki CV'nize eklemek için:

1. **GitHub'a Yükleyin:** Proje dosyalarınızı (`app.py`, `requirements.txt`, `Resume.pdf`) GitHub hesabınızda yeni bir repository'ye yükleyin.
   * *Önemli:* `.streamlit/secrets.toml` dosyasını GitHub'a **yüklemeyin** (Güvenlik riski!).

2. **Streamlit Cloud Hesabı:** [share.streamlit.io](https://share.streamlit.io/) adresine gidin ve GitHub ile giriş yapın.

3. **Yeni Uygulama:** "New App" butonuna tıklayın ve GitHub'daki repository'nizi seçin.

4. **Secrets Ayarı (Çok Önemli):**
   * Deploy butonuna basmadan önce, aşağıda **"Advanced Settings"** butonuna tıklayın.
   * **"Secrets"** bölümüne gelin.
   * Aşağıdaki formatta API anahtarınızı yapıştırın:
   ```toml
   GROQ_API_KEY = "gsk_SeninUzunApiKeyinBurayaGelecek"
   ```
   * Save (Kaydet) diyerek çıkın.

5. **Deploy:** "Deploy!" butonuna basın. 1-2 dakika içinde siteniz canlı yayında! 🌍

---

## 🛠️ Kullanılan Teknolojiler

* **[Streamlit](https://streamlit.io/):** Web arayüzü oluşturmak için.
* **[Groq API](https://groq.com/):** İnanılmaz hızlı LLM (Llama 3) erişimi için.
* **PyPDF & Python-Docx:** Dosyaları metne çevirmek için.
* **OpenAI SDK:** Groq ile iletişim kurmak için (Groq, OpenAI uyumludur).

---

## 📝 requirements.txt Dosyası

Eğer dosya sizde yoksa, aşağıdaki içerikle `requirements.txt` oluşturabilirsiniz:

```text
streamlit
openai
pypdf
python-docx
```

---

*Bu proje Workshop kapsamında hazırlanmıştır.*
