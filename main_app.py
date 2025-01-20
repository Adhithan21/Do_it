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

# Check for URL query parameters (when the user scans the QR code)
query_params = st.experimental_get_query_params()
quote_from_url = query_params.get("quote", None)

if quote_from_url and len(quote_from_url) > 0:
    # This is the redirect page, display the quote passed via the URL
    st.title("Positive Thought")
    st.write(f"### {quote_from_url[0]}")  # Display the quote
else:
    # Main page logic (displaying random quote and generating QR code)
    if "quote" not in st.session_state:
        st.session_state.quote = generate_random_quote()  # Generate a random quote

    # Construct the URL with the quote as a query parameter (for the redirect page)
    base_url = "https://your-deployed-url.streamlit.app/"  # Replace with your actual deployed URL
    quote_url = f"{base_url}?{urlencode({'quote': st.session_state.quote})}"

    # Generate the QR code for this URL
    qr_code_image = generate_qr_code(quote_url, box_size=5)

    # Display the QR code and random quote on the main page
    st.title("Spread Positivity with a QR Code")
    st.image(qr_code_image, caption="Scan me for a positive thought!", width=300)
    st.write(f"### Today's Positive Thought: {st.session_state.quote}")
    st.write("Scan the QR code to share positivity with others!")
