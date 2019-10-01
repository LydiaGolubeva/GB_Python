#Голубева Лидия Ильинична

# Задача-1:
path_dir = [('dir_' + str(i + 1)) for i in range(9)]
def make_dir(paths):
    dir_path = os.path.join(os.getcwd(), paths)
    try:
        os.mkdir(dir_path)
    except:
        print(dir_path + ' Already exist')

for i in path_dir:
    make_dir(i)
# Задача-2:
def list_dir(main_path):
    for _ in os.listdir(main_path):
        print(_)
main_path = os.getcwd()
list_dir(main_path)
# Задача-3:
import shutil
def current_file_copy ():
    name_file = os.path.realpath(__file__)
    new_file = name_file +'.copy'
    if os.path.isfile(new_file) != True:
        shutil.copy(name_file, new_file)
        return new_file + ' - создан'
    else:
        return 'Файл уже скопирован'

if __name__ == '__main__':
    print(current_file_copy())