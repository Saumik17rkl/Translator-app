import streamlit as st
from deep_translator import GoogleTranslator
from textblob import TextBlob

def translate_text(text, dest_lang):
    translator = GoogleTranslator(source='auto', target=dest_lang)
    return translator.translate(text)

def main():
    st.title("Chatbot Translator & Sentiment Analysis")
    
    indian_languages = {
        "Assamese": "as", "Bengali": "bn", "Gujarati": "gu", "Hindi": "hi",
        "Kannada": "kn", "Konkani": "gom", "Maithili": "mai", "Malayalam": "ml",
        "Manipuri (Meitei)": "mni", "Marathi": "mr", "Nepali": "ne", "Odia": "or",
        "Punjabi": "pa", "Sanskrit": "sa", "Sindhi": "sd", "Tamil": "ta",
        "Telugu": "te", "Urdu": "ur",
    }

    # Chatbot conversation history
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    st.write("### Chat with the System")
    
    # Display chat history
    for msg in st.session_state.chat_history:
        st.write(msg)

    user_input = st.text_input("User: ", key="user_input")
    
    if user_input:
        st.session_state.chat_history.append(f"User: {user_input}")
        st.write(f"System: Which language do you want to convert to?")
        
        to_lang = st.selectbox("Select Language", list(indian_languages.keys()), key="lang_select")
        
        if to_lang:
            try:
                translated_text = translate_text(user_input, indian_languages[to_lang])
                response = f"System: The translated text is: {translated_text}"
                st.session_state.chat_history.append(response)
                st.write(response)
            except Exception as e:
                st.error(f"Translation failed: {e}")

if __name__ == "__main__":
    main()
