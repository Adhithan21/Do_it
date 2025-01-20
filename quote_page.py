import streamlit as st

# Display headline and the quote
st.title("Positive Thought")

# Display the quote on the page (this will change with each scan)
st.write(f"Quote generated: {st.session_state.quote}")
