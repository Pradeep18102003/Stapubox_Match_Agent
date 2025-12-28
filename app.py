import streamlit as st
from src.engine import find_match

# 1. Page Configuration
st.set_page_config(page_title="StapuBox AI Matchmaker", page_icon="🏸")

# Custom Branding
st.title("🏸 StapuBox AI Matchmaker")
st.markdown("*Connecting you to the nearest players in seconds.*")

# 2. Sidebar for User Settings
with st.sidebar:
    st.header("Your Profile")
    user_pincode = st.text_input("Enter your Pincode (e.g., 201309)", value="201309")
    st.info("We use your pincode to find players within 10km.")
    
    if st.button("Clear Chat History"):
        st.session_state.messages = []
        st.rerun()

# 3. Initialize Chat History
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hi! I'm your StapuBox coach. Tell me what sport you want to play today!"}
    ]

# 4. Display Chat History
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 5. Chat Input Logic
if prompt := st.chat_input("I'm looking for a Badminton partner..."):
    # Display user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate AI response
    with st.chat_message("assistant"):
        with st.spinner("Searching for nearby players..."):
            try:
                # Call the Gemini Engine from src/engine.py
                response = find_match(prompt, user_pincode)
                st.markdown(response)
                st.session_state.messages.append({"role": "assistant", "content": response})
            except Exception as e:
                st.error(f"Error: {e}")
                st.info("Make sure your GOOGLE_API_KEY is set in .streamlit/secrets.toml")