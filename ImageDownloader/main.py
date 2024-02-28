from Scraper import scrape_website
from Downloader import download_image

def main():
    #Url You want to use
    website_url="https://unsplash.com/"
    
    #Specify the url in the function created
    scrape_website(website_url)
    download_image()
    

if __name__=="__main__":
    main()