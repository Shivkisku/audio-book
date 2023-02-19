# Import necessary libraries
from gtts import gTTS
import PyPDF2

# Open PDF file
with open('name.pdf', 'rb') as pdf_file:
    # Create PDF reader object
    pdf_reader = PyPDF2.PdfFileReader(pdf_file)
    num_pages = pdf_reader.numPages

    # Extract text data from each page of the PDF file
    text_list = []
    for i in range(num_pages):
        try:
            page = pdf_reader.getPage(i)
            text_list.append(page.extractText())
        except:
            # Handle exceptions gracefully
            pass

    # Combine text into a single string
    text_string = " ".join(text_list)

    # Set language to English
    language = 'en'

    # Create gTTS object and save as MP3 file
    tts = gTTS(text=text_string, lang=language, slow=False)
    audio_file = "output.mp3"
    tts.save(audio_file)

    print(f"Successfully converted {num_pages} pages to audio file: {audio_file}")
