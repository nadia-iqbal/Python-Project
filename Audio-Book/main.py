import pyttsx3
# speaker = pyttsx3.init()
# speaker.say('hi nadia')
# speaker.runAndWait()
import PyPDF2
book = open('Microprocessor and Assembly Language-1.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages

speaker = pyttsx3.init()
for num in range(0, pages):
    page = pdfReader.getPage(0)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()
