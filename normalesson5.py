#Голубева Лидия Ильинична

# Задача-1:
import sys
import os
from easy import make_dir, remove_dir, files_in_dir, copy_file

def main():
    while True:
        print('''1 for change directory
2 for explore current directory
3 for remove directory
4 for create directory
q for quit''')
        task = input()

        if task == 'q':
            print('goodbye')
            break

        elif task == '1':
            dirname = input('enter name of the directory: ')
            file_list = files_in_dir()
            if dirname in file_list:
                os.chdir(dirname)
                print('Moved to {} successfully'.format(dirname), os.getcwd())
            else:
                print('No such directory!')

        elif task == '2':
            print(os.getcwd(), files_in_dir(dirname))

        elif task == '3':
            dirname = input('enter name of the directory: ')
            if remove_dir(dirname):
                print('{} removed successfully'.format(dirname))

        elif task == '4':
            dirname = input('enter name of the directory: ')
            if make_dir(dirname):
                print('{} created successfully'.format(dirname))


main()