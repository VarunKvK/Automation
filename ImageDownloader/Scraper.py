import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    #Sends request to specific url and get the required data
    response=requests.get(url)
    
    #Parse the HTML content of the specific page
    soup=BeautifulSoup(response.text,'html.parser')
    # print(soup)
    
    #Find the image element on the website and then extract their urls
    image_urls=[]
    images_element=soup.find_all('div',class_="MorZF")
    for image in images_element:
        image_list=image.find_all('img')
        for img in image_list:
            src=img.get('src')
            if src:
                image_urls.append(src)
            
     