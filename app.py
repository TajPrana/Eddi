import streamlit as st
import openai
import os

# Page setup
st.set_page_config(page_title="Eddie the Editor – TajPrana", layout="centered")
st.title("🧘🏽‍♂️ Eddie – Your Soulful Content Editor")

# Intro
with st.expander("📖 About Eddie"):
    st.markdown("""
Eddie is your AI-powered editor for **TajPrana** content—refining everything from meditations to captions with clarity, calm, and creative flow.  
He understands instructions, adapts to tone, and returns clean, soulful drafts ready to publish.
""")

st.markdown("---")

# API key
api_key = st.text_input("🔑 import OpenAI from "openai";
const client = new OpenAI();

const response = await client.responses.create({
    model: "gpt-4.1",
    input: "Write a one-sentence bedtime story about a unicorn.",
});

console.log(response.output_text);", type="password")

# Upload or paste content
st.subheader("📄 Provide Your Content")

content_type = st.selectbox("Type of content:", [
    "Guided Meditation", "Yin Yoga Sequence", "Journal Prompt", "Social Media Caption", "Website Copy"
])

instruction = st.text_input("🧠 What kind of edit would you like?", placeholder="e.g., Soften tone and make it poetic")

uploaded_file = st.file_uploader("📤 Upload a .txt file", type=["txt"])
manual_text = st.text_area("Or paste your content here:")

# Combine content input
if uploaded_file:
    content = uploaded_file.read().decode("utf-8")
else:
    content = manual_text.strip()

# Editing function
def gpt_edit(prompt, api_key):
    try:
        openai.api_key = api_key
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are Eddie, the soulful content editor for TajPrana. You edit text in a calming, clear, poetic voice. Adjust tone based on user instruction, keep it grounded and meaningful."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        return f"⚠️ Error: {str(e)}"

# When user clicks edit
if st.button("✨ Let Eddie Edit"):

    if not api_key:
        st.warning("Please enter your OpenAI API key.")
    elif not content:
        st.warning("Please paste or upload content.")
    elif not instruction.strip():
        st.warning("Please provide editing instructions.")
    else:
        with st.spinner("Eddie is reading the vibe and rewriting your words..."):

            # Build the prompt
            final_instruction = f"""You are Eddie, a soulful and poetic editor for TajPrana. 
Your job is to edit the following content in the voice of TajPrana: clear, calm, soulful, poetic, and slightly urban. 

Content Type: {content_type}  
Editing Instructions: {instruction}  

Here is the raw content:  
\"\"\"{content}\"\"\"

Please return the fully edited version. 
If this is a Guided Meditation, end with:
'🌀 May your breath stay steady, your heart stay open, and your spirit stay light.'
"""

            edited = gpt_edit(final_instruction, api_key)

        st.subheader("🧼 Eddie’s Edited Version")
        st.text_area("Edited Content", edited, height=300)
        st.success("Done! Eddie’s got your back.")

# Footer
st.markdown("---")
st.caption("TajPrana • Speak freely, breathe deeply, heal fully.")
