import streamlit as st
import asyncio
from googletrans import Translator
from textblob import TextBlob
import os
# Function to handle async translation
async def translate_text(text, dest_lang):
    translator = Translator()
    translation = await translator.translate(text, dest=dest_lang)
    return translation.text

def main():
    st.title("Translator and Sentiment Analysis App")
    st.write("Built with Python")

    activities = ["Translator", "Sentiment Analysis"]
    choice = st.sidebar.selectbox("Select Operation:", activities)

    # Sidebar with Indian language codes
    st.sidebar.subheader("Indian Language Codes")
    indian_languages = {
        "Assamese": "as", "Bengali": "bn", "Gujarati": "gu", "Hindi": "hi",
        "Kannada": "kn", "Konkani": "gom", "Maithili": "mai", "Malayalam": "ml",
        "Manipuri (Meitei)": "mni", "Marathi": "mr", "Nepali": "ne", "Odia": "or",
        "Punjabi": "pa", "Sanskrit": "sa", "Sindhi": "sd", "Tamil": "ta",
        "Telugu": "te", "Urdu": "ur",
    }
    
    for lang, code in indian_languages.items():
        st.sidebar.write(f"**{lang}**: `{code}`")

    if choice == "Translator":
        st.write("### Translator")
        from_text = st.text_input("Enter a sentence to translate (Press Enter)")
        from_code = st.text_input("Enter a language code (e.g., 'hi' for Hindi, 'ta' for Tamil)")

        if from_text and from_code:  # Trigger automatically when both fields have values
            try:
                translated_text = asyncio.run(translate_text(from_text, from_code))
                st.success(f"Translated Text: {translated_text}")
            except Exception as e:
                a=os.system("ping www.google.com")
                if a==1:
                    st.write("Please Check Your internet connection")
                else:
                    st.write("Wrong Language code")
               

                st.error(f"Translation failed: {e}")

    elif choice == "Sentiment Analysis":
        st.write("Sentiment Analysis")
        user_text = st.text_area("Enter text for sentiment analysis (Press Enter)")

        if user_text:  # Trigger automatically
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
