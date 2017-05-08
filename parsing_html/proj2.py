import urllib.parse, urllib.request, urllib.error
from bs4 import BeautifulSoup
import ssl
#### Problem 1 ####
print('\n*********** PROBLEM 1 ***********')
print('New York Times -- First 10 Story Headings\n')
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
url='http://www.nytimes.com'
html=urllib.request.urlopen(url, context=ctx).read().decode()
soup = BeautifulSoup(html, 'html.parser')
counter=0
for h in soup.find_all(class_="story-heading"):
    if h.a:
        print(h.a.text.replace("\n"," ").strip())
        counter+=1
    else:
        print(h.text.replace("\n"," ").strip())
        counter+=1
    if counter>9:
        break
#### Problem 2 ####
print('\n*********** PROBLEM 2 ***********')
print('Michigan Daily -- MOST READ\n')
url="https://www.michigandaily.com"
html=urllib.request.urlopen(url, context=ctx).read().decode()
soup = BeautifulSoup(html, 'html.parser')
for ol in soup.find_all("ol"):
    for li in ol.find_all("li"):
        print(li.text.replace("\n"," ").strip())

#### Problem 3 ####
print('\n*********** PROBLEM 3 ***********')
print("Mark's page -- Alt tags\n")
url="http://newmantaylor.com/gallery.html"
html=urllib.request.urlopen(url).read().decode()
soup = BeautifulSoup(html, 'html.parser')
for img in soup.find_all("img"):
    txt=img.get("alt",0)
    if txt!=0:
        print(txt)
    else:
        print("No alternative text provided!")

#### Problem 4 ####
print('\n*********** PROBLEM 4 ***********')
print("UMSI faculty directory emails\n")
counter=0
root="https://www.si.umich.edu"
def mail_fetcher(url,count):
    url_req = urllib.request.Request(url, None, {'User-Agent': 'SI_CLASS'})
    html = urllib.request.urlopen(url_req,context=ctx).read().decode()
    soup = BeautifulSoup(html, 'html.parser')
    for aa in soup.find_all("a"):
        if aa.text=="Contact Details":
            ref=root+aa["href"]
        else:
            continue
        ref_req = urllib.request.Request(ref, None, {'User-Agent': 'SI_CLASS'})
        html_child=urllib.request.urlopen(ref_req,context=ctx).read().decode()
        soup_child=BeautifulSoup(html_child, 'html.parser')
        for div in soup_child.find_all("div",class_="field-item even"):
            if div.a and "@umich" in div.a.text:
                count+=1
                print(count,div.a.text)
    next = soup.find_all("a", title="Go to next page")
    global counter
    counter=count
    if len(next)>0:
        return root + next[0]["href"]
    else:
        return -1
url="https://www.si.umich.edu/directory?field_person_firstname_value=&field_person_lastname_value=&rid=4"
while url!=-1:
    url=mail_fetcher(url,counter)

