import PyPDF2
import pytesseract
from PIL import Image
from pdf2image import convert_from_path

document = input("select the file you would like to be read: ")

#pdf file object.
pdfFileObject = open(document,'rb')

#converting pdf to image 
pages = convert_from_path(pdfFileObject, 500)
page = pages[0]
page.save('out.png')

img = Image.open('out.png').convert('L')

imageText = pytesseract.image_to_string(img)

print(imageText)

pdfFileObject.close()
