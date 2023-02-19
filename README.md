# audio-book
This Python code converts a PDF file into an MP3 audio file. It uses the PyPDF2 library to extract text from each page of the PDF file and the Google Text-to-Speech (gTTS) library to convert the extracted text into an audio file.

The code opens the PDF file, reads the number of pages in the file, and then extracts the text from each page of the file. It combines the extracted text into a single string and sets the language to English. Then, it uses the gTTS library to create an audio file from the text and saves it as an MP3 file. Finally, it prints a success message indicating the number of pages in the PDF file and the name of the output audio file.
