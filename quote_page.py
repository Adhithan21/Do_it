import streamlit as st

# Get the quote from the URL query parameters
quote = st.experimental_get_query_params().get("quote", ["No quote provided"])[0]

# Display headline and the quote
st.title("Positive Thought")
st.write(f"### {quote}")
