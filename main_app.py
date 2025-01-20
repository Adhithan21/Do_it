import streamlit as st
import random
import qrcode
from io import BytesIO
from urllib.parse import urlencode

# List of motivational and positive quotes
quotes = [
    "The best way to predict the future is to create it. – Peter Drucker",
    "Success is not final; failure is not fatal: It is the courage to continue that counts. – Winston Churchill",
    "The way to get started is to quit talking and begin doing. – Walt Disney",
    "Opportunities don't happen, you create them. – Chris Grosser",
    "Believe in yourself and all that you are. – Christian D. Larson",
]

# Function to generate a random quote
def generate_random_quote():
    return random.choice(quotes)

# Function to generate a QR code for a URL
def generate_qr_code(url, box_size=5):  
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=box_size,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill="black", back_color="white")
    buffer = BytesIO()
    img.save(buffer, format="PNG")
    buffer.seek(0)
    return buffer

# Check for query parameters
query_params = st.query_params  # Use Streamlit's new query params API
quote_from_url = query_params.get("quote", None)

if quote_from_url and quote_from_url[0]:  # Ensure a valid quote is passed
    st.title("Positive Thought")
    st.write(f"### {quote_from_url[0]}")  # Display the quote passed via URL
else:
    # Main page logic
    if "quote" not in st.session_state:
        st.session_state.quote = generate_random_quote()

    # Construct the URL with the quote as a query parameter
    base_url = "https://mppsn93w3hvjxkjjlfthyt.streamlit.app/"  # Replace with your deployed URL
    quote_url = f"{base_url}?{urlencode({'quote': st.session_state.quote})}"

    # Generate the QR code for this URL
    qr_code_image = generate_qr_code(quote_url, box_size=5)

    st.title("Spread Positivity with a QR Code")
    st.image(qr_code_image, caption="Scan me for a positive thought!", width=500)

    # Display the random quote on the main page
    st.write(f"### Your Quote: {st.session_state.quote}")
    st.write("### Scan the QR code to share this positivity!")
