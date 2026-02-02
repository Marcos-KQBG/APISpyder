from pathlib import Path

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
            contenido = file.read_text(encoding='utf-8')
            print(f"Contents of {file}:\n{contenido}\n")
        except Exception as e:
            print(f"Could not read file {file} due to error: {e}")
    

if __name__ == "__main__":
    directory = input("Where to search for files? Press Enter to use default './src' directory.")
    file = input("Enter the file extension to search for (e.g., .py) Press enter to use default '*': ")
    if not directory:
        directory = './src'
    if not file:
        file = '*'
    
    found_files = searchFiles(directory, file)
    text = readFiles(found_files)
    print(f"Analyzing... {found_files}")
    print(text)