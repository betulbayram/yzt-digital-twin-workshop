import streamlit as st
from openai import OpenAI
from pypdf import PdfReader
import docx
import os

# ==========================================
# 🎓 WORKSHOP BÖLÜM 1: SAYFA AYARLARI
# ==========================================
# Burası uygulamanın tarayıcıdaki sekme adını ve ikonunu belirlediğimiz yer.
st.set_page_config(
    page_title="Dijital İkizim", 
    page_icon="👤", 
    layout="centered"
)

# ==========================================
# 🎓 WORKSHOP BÖLÜM 2: VERİ KAYNAĞINI OKUMA
# ==========================================
# Bu fonksiyon, projenin bulunduğu klasördeki sabit CV dosyasını arar.
# RAG (Retrieval Augmented Generation) mantığının ilk adımı: Veriyi metne çevirmek.
def load_cv_text():
    text = ""
    try:
        # Öncelik PDF dosyasında
        if os.path.exists("Resume.pdf"):
            reader = PdfReader("Resume.pdf")
            for page in reader.pages:
                text += page.extract_text() or ""
        
        # PDF yoksa Word dosyasına bak
        elif os.path.exists("Resume.docx"):
            doc = docx.Document("Resume.docx")
            for para in doc.paragraphs:
                text += para.text + "\n"
        
        else:
            st.error("HATA: Klasöre 'Resume.pdf' dosyasını eklemeyi unuttunuz!")
            return None
            
        return text
    except Exception as e:
        st.error(f"Dosya okunurken hata oluştu: {e}")
        return None

# ==========================================
# 🎓 WORKSHOP BÖLÜM 3: YAPAY ZEKA BAĞLANTISI
# ==========================================
api_key = st.secrets["GROQ_API_KEY"]


# Groq istemcisini başlatıyoruz (OpenAI kütüphanesi ile uyumlu çalışır)
client = OpenAI(
    api_key=api_key,
    base_url="https://api.groq.com/openai/v1"
)

# ==========================================
# 🎓 WORKSHOP BÖLÜM 4: ARAYÜZ (UI) TASARIMI
# ==========================================
# İşverenin göreceği karşılama ekranı
st.title("Merhaba, Ben [Adınız] 🙋‍♂️")
st.subheader("Dijital İkizime Hoş Geldiniz")

st.markdown("""
Burada benimle (daha doğrusu yapay zeka temsilcimle) sohbet edebilirsiniz.
CV'mi incelemek yerine, bana doğrudan soru sormayı deneyin:
- *"Hangi teknolojilerde tecrübelisin?"*
- *"En son hangi projeyi geliştirdin?"*
- *"İngilizce seviyen nedir?"*
""")

st.divider() # Görsel ayraç

# CV metnini yükle
cv_text = load_cv_text()
if not cv_text:
    st.stop() # CV yoksa uygulama çalışmasın

# ==========================================
# 🎓 WORKSHOP BÖLÜM 5: HAFIZA (SESSION STATE)
# ==========================================
# Streamlit her tıklamada kodu baştan çalıştırır. 
# Sohbet geçmişini kaybetmemek için 'session_state' kullanıyoruz.
if "messages" not in st.session_state:
    st.session_state.messages = []

# ==========================================
# 🎓 WORKSHOP BÖLÜM 6: YAPAY ZEKA KİMLİĞİ (SYSTEM PROMPT)
# ==========================================
# Bot'a nasıl davranması gerektiğini söylediğimiz en kritik kısım.
system_prompt = f"""
Sen benim dijital ikizimsin. Benim adıma, bir iş arayan adayı temsil ediyorsun.
Aşağıdaki metin benim özgeçmişimdir (CV).

KURALLAR:
1. İş verenler seninle konuştuğunda, sanki BENMİŞİM gibi "Ben dili" kullan (Örn: "Yaptım", "Gittim").
2. Samimi, profesyonel ve hevesli bir ton kullan.
3. Sadece aşağıdaki CV verisine dayanarak cevap ver. 
4. CV'de olmayan bir detay sorulursa: "Bu konuda şu an tecrübem yok ama öğrenmeye her zaman açığım" de. Asla yalan söyleme.

ÖZGEÇMİŞİM:
{cv_text}
"""

# ==========================================
# 🎓 WORKSHOP BÖLÜM 7: SOHBET DÖNGÜSÜ
# ==========================================

# 1. Eski mesajları ekrana yazdır (History)
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 2. Yeni kullanıcı girdisi bekle
if prompt := st.chat_input("Sorunuzu buraya yazın..."):
    
    # Kullanıcı mesajını ekrana bas ve hafızaya ekle
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Sistem mesajını en başa, sohbet geçmişini arkasına ekleyerek API'ye gönder
    api_messages = [{"role": "system", "content": system_prompt}] + st.session_state.messages

    try:
        # LLM'den cevap iste (Stream=True ile daktilo efekti veriyoruz)
        stream = client.chat.completions.create(
            model="openai/gpt-oss-120b", # Groq üzerindeki hızlı ve güçlü model
            messages=api_messages,
            stream=True
        )

        with st.chat_message("assistant"):
            response = st.write_stream(stream)
        
        # Bot cevabını da hafızaya ekle
        st.session_state.messages.append({"role": "assistant", "content": response})

    except Exception as e:
        st.error(f"Bağlantı hatası: {e}")