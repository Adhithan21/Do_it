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
    # Add more quotes as needed...
]

# Function to generate a random quote
def generate_random_quote():
    return random.choice(quotes)

# Function to generate a QR code for a URL
def generate_qr_code(url, box_size=5):  # Reduced box size for smaller QR codes
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=box_size,  # Control size of the QR code
        border=4,
    )
    qr.add_data(url)  # Adding the URL directly into the QR code
    qr.make(fit=True)

    img = qr.make_image(fill="black", back_color="white")
    buffer = BytesIO()
    img.save(buffer, format="PNG")
    buffer.seek(0)
    return buffer

# Main Streamlit app
if "quote" not in st.session_state:
    st.session_state.quote = generate_random_quote()

# Replace with your deployed Streamlit app URL (this must be the deployed URL)
base_url = "https://jdphi9htaatxcuurgc5rhm.streamlit.app/"  # Replace with your actual deployed URL

# Construct the URL with the quote as a query parameter
quote_url = f"{base_url}?{urlencode({'quote': st.session_state.quote})}"

# Generate the QR code for this URL
qr_code_image = generate_qr_code(quote_url, box_size=5)

# Display instructions and QR code
st.title("Spread Positivity with a QR Code")
st.write("### Scan the QR code below to reveal a positive thought!")

# Display the QR code image
st.image(qr_code_image, caption="Scan me for a positive thought!", width=500)

