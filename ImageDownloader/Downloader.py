import requests
from Scraper import title_list
import hashlib 


def generate_hash(url):
    url_hash= hashlib.md5(url.encode()).hexdigest()
    filename= f"{url_hash}.jpg"
    return filename

def download_image(url,folder):
    try:
        #Sends an HTTP request to GET the image URL
        response = requests.get(url)
        # print(response.content)
        #Raises exception if no response from server
        response.raise_for_status()
        file=generate_hash(url)
        file_path=f"{folder}/{file}"
        print(file_path)
        with open(file_path,'wb') as f:
            f.write(response.content)
            print(f"Successfully downloaded the image at {file_path}")

        
    #If any exception is raised
    except requests.exceptions.RequestException as e:
        print("Failed to download the image")
        print(e.message)
        
    
    
    
