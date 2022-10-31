from json import loads

def load_canditates(json_file):
    '''загружает список кандидатов из указанного файла'''
    with open(json_file, 'r', encoding='utf8') as data:
        employee_data = loads(data.read())
        return employee_data

def get_all(list):
    '''выводит список кандидатов на экран'''
    for canditate in list:
        print(canditate)

def get_by_pk(pk):
    '''выводит на экрана данные о кандидате по порядковому номеру'''
    candidates = load_canditates('candidates.json')
    user = candidates[pk - 1]
    return user

def get_by_skill(skill_name):
    '''ищет все вхождения указанного навыка и выводит кандитатов,
    обладающих данным навыком'''
    candidates = load_canditates('candidates.json')
    i = 0
    while i < len(candidates):
        if skill_name in str(candidates[i]['skills']).lower():
            print(candidates[i])
        i += 1



