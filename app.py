import streamlit as st

# Set page config
st.set_page_config(page_title="TajPrana Agent - Eddie", layout="centered")

# Title
st.title("🧘‍♂️ TajPrana Agent: Eddie")

# Description
st.markdown("""
## 👋 Meet Eddie  
Eddie is your dedicated content editing agent for **TajPrana**.

### 🌟 Role:
Eddie refines, enhances, and polishes all content created under the TajPrana brand. Whether it’s:
- Guided meditation scripts  
- Yin yoga class descriptions  
- Journal prompts  
- Digital product text  
- Website or social media copy  

Eddie ensures it reflects the calm, wisdom, and urban soul of TajPrana—always clean, clear, and aligned with the brand's voice.

---

🛠️ *Need your content edited with the Eddie touch?*  
Just upload or paste it below and let Eddie handle the rest.  
""")

# Content input area
user_input = st.text_area("📝 Paste your content here for Eddie to edit:")

# Dummy edit function (placeholder)
def eddie_edit(text):
    # Placeholder logic for now—this would be replaced with real NLP editing logic
    return text.strip().capitalize() + " ✨ [Edited by Eddie]"

# If user submits content
if st.button("✨ Let Eddie Edit"):
    if user_input:
        edited = eddie_edit(user_input)
        st.subheader("🧼 Eddie’s Edited Version")
        st.success(edited)
    else:
        st.warning("Please enter some content for Eddie to edit.")

# Footer
st.markdown("---")
st.caption("Powered by TajPrana • May your breath stay steady, your heart stay open, and your spirit stay light.")
