import os

# def main():
#     print(os.name)
#     print(os.uname().version)
#
#     print(os.getlogin())
#     print(os.environ)
#     print(os.environ.get("HOME")) #получить пути
#     print(os.getenv("HOME"))
#
# """Создание директории + переход в нее"""
#     os.mkdir("test") #создать директорию
#     os.rmdir("test") #удалить директорию
#     os.mkdir("testingpp1")
#     os.chdir("testingpp1")
#     with open("letter", "w") as let_wr:
#         let_wr.write("Привет, Стив Джобс!") #Создаем директорию,в ней папку
#
# """Вывод содержимого"""
#     print(os.listdir(".")) #что внутри директориии
#     os.chdir("../") #шаг назад
#     print(os.listdir("."))
#
# """Выдача прав"""
#     os.chmod("testingpp" , 0o777, follow_symlinks=True) #метод позволяет менять права через симлине
#     os.rename("старое название", "новое") #смена имени директории


def create_dir():
    # os.makedirs("test/inested/inested") #создание нескольких директорий
    os.removedirs("test/inested/inested") #удаление нескольких директорий
    #os.renames("старое", "новое")

def paths():
    print(os.path.exists("/zakharden")) #проверяет наличие пути
    print(os.path.isdir("main.py"))
    print(os.path.isfile("main.py"))

    files = [path for path in os.listdir() if os.path.isfile(path)]  #список файлов
    dirs = [path for path in os.listdir() if os.path.isdir(path)] #список директорий
    print(files)
    print(dirs)
    PathInMain = os.path.abspath("main.py")
    print(PathInMain) #получение абсолютного пути
    print(os.path.basename(PathInMain))  #получение имени директории из абсолютного пути
    print(os.path.getsize(PathInMain)) #получение размера файла


# main()
#create_dir()
paths()