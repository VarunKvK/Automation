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
    title_list=[]
    images_element=soup.find_all('div',class_="MorZF")
    for image in images_element:
        image_list=image.find_all('img')
        for img in image_list:
            src=img.get('src')
            title=img.get('alt')
            if src:
                image_urls.append(src)
                title_list.append(title)
    title_list=[title for title in title_list if title is not None]

            
     