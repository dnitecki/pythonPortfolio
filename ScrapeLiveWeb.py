#import needed modules
from bs4 import BeautifulSoup
import requests
#provide the web address of the live web
url = 'http://libraries.uky.edu'
#obtain information from the live web
page = requests.get(url)
# parse the page to obtain the parent div tag
soup = BeautifulSoup(page.text, "html.parser")
div = soup.find('div', class_="sf-middle")
#locate the three child div tags
contacts = div.find_all("div", class_="dashing-li-last")
#print out the first child div tag to examine it
print(contacts[0])
#obtain information from each child tag
for contact in contacts:
    #obtain the area name
    area = contact.find('span', class_="featured_area")
    print(area.text)
    #obtain the phone and email
    atags = contact.find_all('a', href = True)
    for atag in atags:
        print(atag.text)
