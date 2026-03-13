import config as cg

def load():
    try:
        with open(cg.PATH, 'r', encoding='utf-8') as file:
            i_list = file.readlines()
            return i_list
    except FileNotFoundError:
        with open(cg.PATH, 'w', encoding='utf-8') as file:
            pass

def save(i_list):
    with open(cg.PATH, 'w', encoding='utf-8') as file:
        file.writelines(i_list)


if __name__ == '__main__':
    load()