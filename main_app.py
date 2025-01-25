import qrcode
from io import BytesIO
from urllib.parse import urlencode
import os
import streamlit as st
import random

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

# Function to generate and save/show a QR code
def generate_and_display_qr_code(url, filename="qr_code.png"):
    """
    Generates a QR code for the given URL, saves it as an image file,
    and displays it using the system's default image viewer.

    Args:
        url (str): The URL to encode in the QR code.
        filename (str): The name of the file where the QR code image will be saved.
    """
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill="black", back_color="white")
    img.save(filename)  # Save the QR code as an image file
    img.show()  # Open the QR code in the default image viewer

    print(f"QR Code has been saved as '{filename}'. Scan it to open the URL.")

# Main execution
if __name__ == "__main__":
    # Define the base URL for the Streamlit app
    base_url = "http://localhost:8501"  # Update this if deploying online

    # Construct the URL with a query parameter for the quote
    random_quote = generate_random_quote()
    quote_url = f"{base_url}?{urlencode({'quote': random_quote})}"

    # Generate and display the QR code
    print("Generating QR code for the webpage...")
    generate_and_display_qr_code(quote_url)

    # Instruction for running Streamlit
    print("\nTo start the Streamlit app, run the following command in a new terminal:")
    print(f"streamlit run {os.path.basename(__file__)}")

# Streamlit App
query_params = st.experimental_get_query_params()
quote_from_url = query_params.get("quote", None)

# Display the positive thought on the Streamlit app
st.title("Positive Thought")
st.write("### Here's a motivational thought to brighten your day:")
st.write(f"#### {quote_from_url[0] if quote_from_url else generate_random_quote()}")
