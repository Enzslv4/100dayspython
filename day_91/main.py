import fitz
import frontend
import pyttsx3
import argparse

def extract_text_from_pdf(pdf_path):
    """Extracts text from a given PDF file."""
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text("text") + "\n"
    return text

def text_to_speech(text):
    """Converts text to speech using pyttsx3."""
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  # Adjust speed
    engine.say(text)
    engine.runAndWait()

def pdf_to_audiobook(pdf_path):
    """Extracts text from a PDF and reads it aloud."""
    text = extract_text_from_pdf(pdf_path)
    print("Extracted text:", text[:500], "...")  # Print a preview
    text_to_speech(text)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert PDF to audiobook.")
    parser.add_argument("pdf_path", help="Path to the PDF file.")
    args = parser.parse_args()
    pdf_to_audiobook(args.pdf_path)
