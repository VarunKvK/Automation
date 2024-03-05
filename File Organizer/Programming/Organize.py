import os
import shutil

file_categories={
    'Programming':['.html', '.js', '.css','.py'],
    'Images':['.jpg','.jpeg','.png','.gif'],
    'Documents':['.doc','.pdf','.docx','.txt','.xls','.csv'],
    'Videos':['.mp4','.avi','.mov','.mkv'],
    'Apllications': ['.exe'],
    'ZipFiles':['.zip']
}

#------------------------------------------------------
#Funtion to organize
#------------------------------------------------------

def organize_files(directory):
    # This function looks into the files in the directory
    for filename in os.listdir(directory):
        src_path=os.path.join(directory,filename)
        # print(f"The src_path {src_path} & {filename}")
        #This checks wether the file exists
        if os.path.isfile(src_path):
            #If the file exists check if there is ny space in any file 
            if ' ' in filename:
                filename=filename.replace(' ', '')
            #The '_' character means that the file name and the extension of the fileis seperated and the filename is ignored 
            _, ext=os.path.splitext(filename)
            # print(f"The ext {ext}")
            ext=ext.lower()
            category=None
            # The file_category contains all the extensions and categories which is given above
            for cat, extension in file_categories.items():
                # If the extension exists then the category will be added in the variable category=None
                if ext in extension:
                    category=cat
                    break
            # when the category exists then the category will be added to the main directory
            if category:
                dest_folder=os.path.join(directory,category)
                # print(dest_folder)
                # if the category soent exist in the path then it will be created
                if not os.path.exists(dest_folder):
                    os.makedirs(dest_folder)
                # Now the folder exists and the filenme are added to the specific folder
                des_path=os.path.join(dest_folder,filename)
                # print(f"SrcPath:{src_path}, DesPath:{des_path}, Cat:{category}")
                #This moves the destination folder that is create to the src path.
                shutil.move(src_path,des_path)
                print(f"Folder Moving Complete")    
            
            
            
#------------------------------------------------------
# Replace '\' with '/''
#------------------------------------------------------

# directory_path=r"I:\WorkByVarun\Varun\Development\IntermediateDevelopment\PythonDevelopment\Automation\FileOrganizer"
directory_path=r"C:\Users\Admin\Downloads"
file_path=directory_path.replace("\\","/")
# print(file_path)


        
organize_files(file_path)