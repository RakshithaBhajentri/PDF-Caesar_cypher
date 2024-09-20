import string
import PyPDF2
from fpdf import FPDF

# Caesar Cipher Encryption
def caesar_encrypt(message, key):
    shift = key % 26
    cipher = str.maketrans(string.ascii_lowercase, string.ascii_lowercase[shift:] + string.ascii_lowercase[:shift])
    encrypted_message = message.lower().translate(cipher)
    return encrypted_message

# Caesar Cipher Decryption
def caesar_decrypt(encrypted_message, key):
    shift = 26 - (key % 26)
    cipher = str.maketrans(string.ascii_lowercase, string.ascii_lowercase[shift:] + string.ascii_lowercase[:shift])
    message = encrypted_message.translate(cipher)
    return message

# Read text from PDF
def read_pdf(file_path):
    pdf_reader = PyPDF2.PdfReader(file_path)
    text = ""
    for page_num in range(len(pdf_reader.pages)):
        text += pdf_reader.pages[page_num].extract_text()
    return text

# Save text into PDF
def save_to_pdf(text, file_path):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, text)
    pdf.output(file_path)

# Main encryption and decryption process
def encrypt_pdf(input_pdf, key, encrypted_pdf):
    message = read_pdf(input_pdf)
    encrypted_message = caesar_encrypt(message, key)
    save_to_pdf(encrypted_message, encrypted_pdf)
    print(f'Encrypted message saved in {encrypted_pdf}')

def decrypt_pdf(encrypted_pdf, key, decrypted_pdf):
    encrypted_message = read_pdf(encrypted_pdf)
    decrypted_message = caesar_decrypt(encrypted_message, key)
    save_to_pdf(decrypted_message, decrypted_pdf)
    print(f'Decrypted message saved in {decrypted_pdf}')

# Example Usage
input_pdf = "D:/Current Data/Desktop/Month plan - Google Docs.pdf"  
encrypted_pdf = "encrypted_output.pdf"
decrypted_pdf = "decrypted_output.pdf"
key = int(input("Enter the encryption key (an integer): "))

encrypt_pdf(input_pdf, key, encrypted_pdf)
decrypt_pdf(encrypted_pdf, key, decrypted_pdf)
