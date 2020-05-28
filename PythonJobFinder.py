import PyPDF2 as pdf2
import os

def getContent(fp):
    line = pdf2.PdfFileReader(holder)
    content = ""
    #fixed to now read the file and go through the content of it, now will display to ensure that it is correct. 
    num_pages = pdf2.PdfFileReader(open(holder, "rb")).getNumPages()
    for i in range(0, num_pages):
        content += line.getPage(i).extractText() + "\n\n"
    content = " ".join(content.replace(u"\xa0", " ").strip().split())
    #content is printing out and being stored, need to have it set to be a nicer format.
    print(content)
    return content


if __name__ == '__main__':
    holder = input("please enter the resume file\n")

    #able to read in the file, now have to parse through it. 
    if os.stat(holder).st_size == 0:
        print('File is empty')
    else:
        print('file is not empty')

    f = open(holder)

    getContent(holder)
    #code goes here then close at the end
    f.close()