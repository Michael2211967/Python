import os

def files(directory=os.getcwd()):
    files = []
    files.append(directory)
    listdir = os.listdir(directory)
    for file in listdir:
        files.append(file)
    return files

if __name__ == "__main__":
    files1 = files()
    print(files1)
