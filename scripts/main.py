# main.py

from functions.readme_generator import readme_generator
import os

def main():
    directory_path = './lib'
        
    for i in range(6, 17):
        file_path = directory_path+"/0"+str(i)+"_rounds"
        
        if not os.path.exists(file_path):
            os.makedirs(file_path)
            print(f"Created directory at {file_path}")
            
        destination = os.path.join(file_path, 'README.md')
        
        readme_generator(i, destination)
        
    print(f"Script completed successfully! Author - therinMody")
    
    
main()
