import streamlit as st
from deep_translator import GoogleTranslator
from textblob import TextBlob

def translate_text(text, dest_lang):
    translator = GoogleTranslator(source='auto', target=dest_lang)
    return translator.translate(text)

def main():
    st.title("Translator and Sentiment Analysis App")
    st.write("Built with Python")

    activities = ["Translator", "Sentiment Analysis"]
    choice = st.sidebar.selectbox("Select Operation:", activities)

    # Sidebar dropdown for Indian language codes
    indian_languages = {
        "Assamese": "as", "Bengali": "bn", "Gujarati": "gu", "Hindi": "hi",
        "Kannada": "kn", "Konkani": "gom", "Maithili": "mai", "Malayalam": "ml",
        "Manipuri (Meitei)": "mni", "Marathi": "mr", "Nepali": "ne", "Odia": "or",
        "Punjabi": "pa", "Sanskrit": "sa", "Sindhi": "sd", "Tamil": "ta",
        "Telugu": "te", "Urdu": "ur",
    }

    if choice == "Translator":
        st.write("### Translator")
        from_text = st.text_input("Enter a sentence to translate")
        to_lang = st.selectbox("Select target language", list(indian_languages.keys()))

        if from_text and to_lang:
            try:
                translated_text = translate_text(from_text, indian_languages[to_lang])
                st.success(f"Translated Text: {translated_text}")
            except Exception as e:
                st.error(f"Translation failed: {e}")

    elif choice == "Sentiment Analysis":
        st.write("### Sentiment Analysis")
        user_text = st.text_area("Enter text for sentiment analysis")

        if user_text:
            blob = TextBlob(user_text)
            sentiment = blob.sentiment.polarity
            if sentiment > 0:
                st.success("Positive Sentiment 😊")
            elif sentiment < 0:
                st.warning("Negative Sentiment 😞")
            else:
                st.info("Neutral Sentiment 😐")

if __name__ == "__main__":
    main()
