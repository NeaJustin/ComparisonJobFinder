import PyPDF2 as pdf2
import numpy as np
import csv
import os
import json
from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup


def getContent(fp):
    line = pdf2.PdfFileReader(holder)
    content = ""
    #fixed to now read the file and go through the content of it, now will display to ensure that it is correct. 
    num_pages = pdf2.PdfFileReader(open(holder, "rb")).getNumPages()
    for i in range(0, num_pages):
        content += line.getPage(i).extractText() + "\n"
        x.write(content)
    content = " ".join(content.replace(u"\xa0", " ").strip().split())
    #content is printing out and being stored, need to have it set to be a nicer format.
    print(content)

    return content

#need to create a web scraper to get information from the listing 
def getSimpleUrl(url):
    #using a try to get the request of the url for a response, and if 
    #it responds with either HTML/XML then return the content, otherwise return none
    try:
        with closing(get(url,stream=True)) as resp:
            if is_good_response(resp):
                return resp.content
            else:
                return None
    except RequestException as e:
        log_error('error during request to {0} : {1}'.format(url, str(e)))
        return None

#if response is HTML then return true, otherwise return false
def is_good_response(resp):
    content_type = resp.headers['Content-Type'].lower()
    return(resp.status_code == 200
           and content_type is not None
           and content_type.find('html') > -1)

#using to print the error 
def log_error(e):
    print(e)

#saving the contents of the web page in a document
def getWebContent(x):
    for i, li in enumerate(html.select('li')):
        m.write(li.text)
        m.write("\n")
        print(i, li.text)

    return None

#using seperate function to write from joblistingdetails.txt
#to write to Dictionary.txt
#have it writing properly to the file, now going to see if it will
#work properly with storing in an array. 
def writeToDictionaryFile():
    jobFile = open('jobListingDetails.txt')
    dictFile = open('Dictionary.txt')

    with jobFile as h:
        with dictFile as f1:
            for line in h:
                f1.write(line)

    jobFile.close()
    dictFile.close()

    return None


#need to do the comparison now between the two files of the 
#job listing and the persons resume. 
#will be using a dictionary to look up the differences between them as
#checking which words match would help the search. 
def Matching():
    #a will be for the comparison. 
    #not sure why I have to copy over the array to a new file to be read
    #does not make sense. but will continue with it. 
    a = []
    b = []
    #no need to pass in anymore and can just open here. 
    filename = 'Dictionary.txt'
    with open(filename) as fh:
        print("made it here")
        for line in fh:   
            #appending properly for the array. 
            print("why arent you populating")
            a.append(line)
            print(a)

    return None

if __name__ == '__main__':
    holder = input("please enter the resume file\n")

    #able to read in the file, now have to parse through it. 
    if os.stat(holder).st_size == 0:
        print('File is empty')
    else:
        print('file is not empty')

    f = open(holder)
    x = open("ResumeOutputFile.txt", "w+")

    #creating the write file for the job listing details. 
    m = open("jobListingDetails.txt", "w+")
    o = open("Dictionary.txt")
    getContent(holder)
        
    #need to figure out why it is not working with input and only putting it in 
    raw_html = getSimpleUrl("https://www.indeed.com/jobs?q=software%20developer&l=Montclair%2C%20CA%2C%2091763&ts=1583876659225&rq=1&rsIdx=0&fromage=last&newcount=128&advn=523043765138470&vjk=337c8f7706e724f3")

    html = BeautifulSoup(raw_html, 'html.parser')

    getWebContent(html)

    #calling writeToDictionary to write to the text file so it can be read properly
    writeToDictionaryFile()

    #x will be the resume file, m will be the job listing
    Matching()

    m.close()
    x.close()
    o.close()
    f.close()
