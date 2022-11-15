import requests

AGIFY_API = 'https://api.agify.io?name='
GENDERIZE_API = 'https://api.genderize.io?name='


def api_call(nombre):
    result_dic = []
    response = requests.get(AGIFY_API+nombre)
    agify_data = response.json()
    edad = agify_data['age']
    result_dic.append(edad)
    response2 = requests.get(GENDERIZE_API+nombre)
    genderize_data = response2.json()
    result_dic.append(genderize_data['gender'])
    return result_dic


