from Scraper import scrape_website,image_urls
from Downloader import download_image

def main():
    #Url You want to use
    website_url="https://unsplash.com/"
    
    num_images= int(input("Number of images to download: "))
    #Specify the url in the function created
    scrape_website(website_url)
    
    folder_path=r"I:\WorkByVarun\Varun\Development\IntermediateDevelopment\PythonDevelopment\Automation\ImageDownloader\Images"
    folder_path=folder_path.replace("\\","/")
    for url in image_urls[:num_images]:
        download_image(url,folder_path)
    

if __name__=="__main__":
    main()