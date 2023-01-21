# словарь как база данных 
def read_db(path: str) -> dict:
    db_list = []
    with open(path, 'r', encoding='UTF-8') as file:
        my_list = file.readlines()
        for line in my_list:
            id_dict = dict()
            line = line.strip()
            print(list)
    