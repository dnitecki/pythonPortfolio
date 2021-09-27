#import the Beautiful Soup module
from bs4 import BeautifulSoup

#open the local HTML file as a text file
textfile = open("UKYexample.html", encoding='utf8')

#use the findAll() function to locate all <p> tags
soup = BeautifulSoup(textfile, "html.parser")
ptags = soup.findAll("p")
#print out the class attribute value and the web address of the <a> tag for University of Kentucky Lbraries


#print out the second <p> tag
print(ptags[1])

#find the <a> tag nested in the second <p> tag
atag = ptags[1].find("a")
print(atag)

#print the web address of the hyperlink
print(atag['href'])

#print the content of the <a> tag
print(atag.text)

