import requests


id = None
access_token = None


try:
    with open('access_token.pickle', 'r') as f:
        access_token = f.readline()
        print("Access token was loaded")
except IOError:
        print("Access token wasn't found")
        access_token = input('Enter access token...\n\r')
        with open('access_token.pickle', 'w') as f:
            f.write(access_token)
            print("Access token was saved")


while not id:
    id = input('Enter user id...\n\r')
    try:
        int(id)
    except ValueError:
        id = None
        print('This is not id')


version_api = '5.103'
fields = 'domain,online'
name_case = 'nom'
headers = {"Accept-Language": "ru-RU, ru;q=0.9, en-US;q=0.8"}

reply = requests.get(f'https://api.vk.com/method/friends.get?user_id={id}&fields={fields}&name_case={name_case}&access_token={access_token}&v={version_api}', headers=headers)
json = reply.json()

if 'error' in json:
    print('Error. {}'.format(json['error']['error_msg']))
else:
    for item in json['response']['items']:
        print('https://vk.com/id{} {} {} {}'.format(item['id'], item['first_name'], item['last_name'], '●' if item['online'] else ''))