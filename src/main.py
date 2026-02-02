from pathlib import Path
import argparse

def searchFiles(directory, extension):

    path = Path(directory)
    black_dir = {'.git', '__pycache__', '.venv'}
    black_ext = {'.png', '.jpg'}

    files = []

    if not path.exists() or not path.is_dir():
        print(f"The directory {directory} does not exist or is not a directory.")
        return
    
    for file in path.rglob(f'*{extension}'):
        if any(part in black_dir for part in file.parts):
            continue
        if file.suffix in black_ext :
            continue
        files.append(file)
    
    return files

def readFiles(fileList):
    for file in fileList:
        try:
            with open(file, "r") as f:
                for num_linea, linea in enumerate(f, start=1):
                    if "API_KEY" in linea:
                        print(f"Encontrado en línea {num_linea}: {linea.strip()}")
            
        except Exception as e:
            print(f"Could not read file {file} due to error: {e}")
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Search for files with a specific extension in a directory.")

    parser.add_argument("-d", "--dir" , help="Directory to search files in", default="./src")
    parser.add_argument("-f", "--file", help="file extension to search for", default="*")
    
    args = parser.parse_args()
    
    found_files = searchFiles(args.dir, args.file)
    text = readFiles(found_files)
    print(f"Analyzing... {found_files}")
    print(text)