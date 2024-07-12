# main.py

from functions.readme_generator import readme_generator
import os

def main():
    directory_path = './lib'
        
    for i in range(6, 17):
        folder_name = f"{i:02}_rounds"
        file_path = os.path.join(directory_path, folder_name)
        
        if not os.path.exists(file_path):
            os.makedirs(file_path)
            print(f"Created directory at {file_path}")
            
        destination = os.path.join(file_path, 'README.md')
        
        readme_generator(i, destination)
        
    print(f"Script completed successfully! Author - therinMody")
    
    
main()
