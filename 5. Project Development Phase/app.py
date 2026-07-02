import streamlit as st

st.set_page_config(page_title="Voice-Based Concept Understanding Analyser")

st.title("🎤 Voice-Based Concept Understanding Analyser")

st.write("Upload an audio file or enter text manually.")

uploaded_file = st.file_uploader(
    "Upload Audio",
    type=["wav", "mp3", "m4a"]
)

text = st.text_area("Or enter transcript manually")

if st.button("Analyze"):
    if uploaded_file:
        st.success("Audio uploaded successfully!")
    elif text:
        st.success("Text received successfully!")
        st.write("Transcript:")
        st.write(text)
    else:
        st.warning("Please upload an audio file or enter text.")