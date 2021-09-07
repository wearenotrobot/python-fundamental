users = {
    'id': 1,
    'name': 'Leanne Graham',
    'username': 'Bret',
    'email': 'sincere@april.biz',
    'address': dict(street='Kulas Light',
                    suite='Apt. 556',
                    city='Gwenborough',
                    zipcode='92998-3874',
                    geo={
                        "lat": "-37.4342",
                        "lng": "81.2423",
                    }
                )
}

print(users)
print(users['id'])
print(users['name'])
print(users['username'])
print(users['email'])
print(users['address'])
print(users['address']['geo'])
print(users['address']['geo']['lat'])
print(users['address']['geo']['lng'])
print(users)
print(type(users))

print('\n# mengubah dict menjadi json')
# mengubah python dict menjadi json, maka perlu perintah:
import json
result = json.dumps(users)
print(result)
print(type(result))

# Menulis hasilnya ke file, pakai:
with open('result.json', 'w') as file:
    json.dump(users, file)