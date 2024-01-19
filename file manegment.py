import os
import shutil

def organize_files(target_directory):
    for filename in os.listdir(target_directory):
        if os.path.isfile(os.path.join(target_directory, filename)):
            _, file_extension = os.path.splitext(filename)
            destination_folder = os.path.join(target_directory, file_extension[1:])
            
            if not os.path.exists(destination_folder):
                os.makedirs(destination_folder)
            
            shutil.move(os.path.join(target_directory, filename), os.path.join(destination_folder, filename))

if __name__ == "__main__":
    target_directory = input("Enter the target directory path: ")
    organize_files(target_directory)
    print("Files organized successfully.")
