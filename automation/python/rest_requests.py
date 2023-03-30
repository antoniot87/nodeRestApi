# Import libraries
import requests

### GET SAMPLES ###

URL = "https://jsonplaceholder.typicode.com/users"
r_get = requests.get(url=URL)
data = r_get.json()

# SAMPLE 1 : Extracting id, name and email of the first matching location
id = data[0]['id']
name = data[0]['name']
email = data[0]['email']
print("ID:%s\nName:%s\nEmail:%s \n" %(id, name, email))

# SAMPLE 2 : List all street values with for loop
for i in data:
    print(i['address']['street'])

# SAMPLE 3 :List all email values with lambda for loop
[print(x['email']) for x in data]
print('\n*********************\n')

### POST SAMPLES ###

# SAMPLE 1 : Album json variable data POST to typicode service.
URL = "https://jsonplaceholder.typicode.com/albums"
json = {
    "userId": 20,
    "id": 201,
    "title": "Hi alimesut.wordpress.com readers..."
}
r_post = requests.post(url=URL, json=json)
print(r_post.status_code)

# SAMPLE 2 : Album json file data POST to typicode service.
URL = "https://jsonplaceholder.typicode.com/albums"
files = {'file': open('selam.json', 'rb')}
r_post = requests.post(url=URL, files=files)
print(r_post.status_code)
print(r_post.content)  # To see the change

# SAMPLE 3 : Posts json variable data POST to typicode service.
URL = "https://jsonplaceholder.typicode.com/posts"
p_value = '{"userId":1,"id":101,"title":"blog diaries","body":"RIP 2nd post inserted."}'
r_post = requests.post(url=URL, data=p_value)
print(r_post.status_code)
print(r_post.content)
print('\n*********************\n')

### PATCH SAMPLES ###

# SAMPLE 1 : PATCH Best Practice
URL = "https://jsonplaceholder.typicode.com/users/2"
u_value = '{"email":"ali@mesut.com","address":{"city":"Diyarbakir"}}'
r_patch= requests.patch(url=URL, data=u_value)
print(r_patch.status_code)
print(r_patch.content)  # To see the change
print('\n*********************\n')

# SAMPLE 2 : PATCH request fantasy method :)
URL = "https://jsonplaceholder.typicode.com/users/2"
r_get = requests.get(url=URL)
data = r_get.json()

print(data['email'])
print(data['address']['city'])
data['email'] = 'ali@mesut.com'
data['address']['city'] = 'Diyarbakir'
print(data['email'])
print(data['address']['city'])

r_patch = requests.patch(url=URL, json=data)
print(r_patch.status_code)
print(r_patch.content)  # To see the change
print('\n*********************\n')

### PUT SAMPLES ###

# SAMPLE 1 : Spesific value update with PUT
URL = "https://jsonplaceholder.typicode.com/users/2"
u_value = '{"email":"ali@mesut.com","address":{"city":"Diyarbakir"}}'
r_put = requests.put(url=URL, data=u_value)
print(r_put.status_code)
print('\n*********************\n')

### DELETE SAMPLES ###

# SAMPLE 1 :
URL = "https://jsonplaceholder.typicode.com/users/1"
r_delete = requests.delete(url=URL, data={})
print(r_delete.status_code)
print(r_delete.content)  # To see the change
print('\n*********************\n')

### OPTIONS SAMPLES ###

# SAMPLE 1 :
URL = "https://jsonplaceholder.typicode.com/"
r_options = requests.options(url=URL)
print(r_options.status_code)
print(r_options.content)  # To see the change