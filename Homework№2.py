import os

def rewriting(current, folder):
    super_hero = {}
    m = []
    for file_name in os.listdir(current):
        if file_name.endswith('.txt'):
            with open(file_name, 'rt', encoding = "utf-8") as file, open(folder, 'w', encoding = "utf-8") as P_file:
                lines = 0
                for i in file:       
                    lines += 1
                super_hero_dict = dict.fromkeys([file_name], lines)
                super_hero.update(super_hero_dict)
                sorted_tuple = sorted(super_hero.items(), key=lambda x: x[1])
                sorted_tuple = dict(sorted_tuple)
                for key,val in sorted_tuple.items():
                    P_file.write('{}\n'.format(key))
                    P_file.write('{}\n'.format(val))
                    P_file.write(file.read())
                        

current = os.getcwd()
folder = 'D:\IT\Проекты\Дом\H.txt'
rewriting(current, folder)