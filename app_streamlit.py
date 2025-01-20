import streamlit as st

# Main Streamlit app to display the quote from URL parameters
quote = st.experimental_get_query_params().get("quote", ["No quote provided"])[0]

# Display headline and the quote
st.title("Positive Thought")
st.write(f"### {quote}")
