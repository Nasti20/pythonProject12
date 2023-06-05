import requests
import json

status = 'available'

res = requests.get(f'https://petstore.swagger.io/v2/pet/findByStatus?status={status}', headers={'accept':'application/json'})

print(res.status_code)
print(res.text)
print(res.json())
print(type(res.json()))

# метод POST
url = 'https://petstore.swagger.io/v2/user'

headers = {
    'accept': 'application/json',
           'Content-Type': 'application/json'
}
data = {
    'id': 0,
    'username': 'Ами',
    'firstName': 'Ex',
    'lastName': 'Kuk',
    'email': 'red@mail.ru',
    'password': '123258',
    'phone': '8-911-111-11-11',
    'userStatus': 0
}

res1 = requests.post(f'https://petstore.swagger.io/v2/pet', headers=headers, json=data)

print(res1.status_code)
print(res1.json())

# метод GET

pet_id = 1
url = f'https://petstore.swagger.io/v2/pet/bbe55a42-bcc9-4d2a-b7ac-7ce6a0e84fe3'

res2 = requests.get(url)
print(res2.status_code)
print(res2.json())



# метод DELETE

pet_id = 1

url = f'https://petstore.swagger.io/v2/pet/bbe55a42-bcc9-4d2a-b7ac-7ce6a0e84fe3'

res3 = requests.delete(f'https://petstore.swagger.io/v2/pet/bbe55a42-bcc9-4d2a-b7ac-7ce6a0e84fe3')

print(res3.status_code)
print(res3.json())

# метод PUT

url = f'https://petfriends.skillfactory.ru/api/pets/9C4AEC87-37A4-4EE0-8F1B-3170C816536C'

headers = {
    'accept': 'application/json',
    'auth_key': 'ef06125f295a52c62c1c99f7cc7a697710ce1d211551bee1bee42de7',
    'Content-Type': 'application/json'
}
data = {
    'name': 'Dambo',
    'animal_type': 'rat',
    'age': '2'
}

res4 = requests.put(url, headers=headers, data=json.dumps(data))
print(res3.status_code)
print(res3.json())