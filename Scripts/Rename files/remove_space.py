import glob, re, os

for filename in glob.glob("D:\\GIT\\Python\\01.Программирование_на_Pyth_для_детей\\_Pictures\\*"):
    if filename.find(' ') > 15:
        new_name = filename.replace(' ', '_')
        print(new_name)
        os.rename(filename, new_name)
    
