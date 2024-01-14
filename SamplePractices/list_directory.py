import os
def main():
    directory = ("Enter the direcrtory: ")
    list_directory(directory)

def list_directory(path='.'):
    """
        This function prints all files and directories in the given directory.
        :args path: Path to the directory, default is current directory
    """
    names = os.listdir(path)
    names.sort()
    for name in names:
        print(name, end='')
main()