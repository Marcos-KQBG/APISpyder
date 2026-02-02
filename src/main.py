from pathlib import Path
import argparse
import logging
import re
from Patterns import PATTERNS

COMPILED_PATTERNS = {
    key: re.compile(pattern) for key, pattern in PATTERNS.items()
}

def searchFiles(directory, extension):

    path = Path(directory)
    black_dir = {'.git', '__pycache__', '.venv', 'node_modules', 'dist', 'build'}
    black_ext = {'.png', '.jpg'}

    files = []

    if not path.exists() or not path.is_dir():
        logging.error(f"The directory {directory} does not exist or is not a directory.")
        return []
    
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
            if esBinario(file):
                logging.info(f"Skipping binary file: {file}")
                continue

            with open(file, "r", encoding="utf-8", errors="ignore") as f:
                for num_linea, linea in enumerate(f, start=1):
                    try:
                        for key, pattern in COMPILED_PATTERNS.items():
                            if pattern.search(linea):
                                logging.info(f"Founded {key} on line: {num_linea}: {linea.strip()} in file: {file}")
                        
                    except re.error as regex_error:
                        logging.error(f"Regex error for pattern {pattern}: {regex_error}")
 
        except Exception as e:
            logging.error(f"Could not read file {file} due to error: {e}")
    

def esBinario(filePath):
    try:
        with open(filePath, 'rb') as f:
            chunk = f.read(1024)
            if b'\x00' in chunk:
                return True
    except Exception as e:
        logging.error(f"Could not read file {filePath} due to error: {e}")
    return False

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    parser = argparse.ArgumentParser(description="Search for files with a specific extension in a directory.")

    parser.add_argument("-d", "--dir" , help="Directory to search files in", default="./src")
    parser.add_argument("-f", "--file", help="file extension to search for", default="")
    
    args = parser.parse_args()
    
    found_files = searchFiles(args.dir, args.file)

    logging.info(f"Analyzing... {found_files}")
    readFiles(found_files)
    