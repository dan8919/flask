import requests
BASE="http://127.0.0.1:5000/"

data = [{"likes":10,"name":"Tim","views":100000},
        {"likes":4,"name":"kay","views":2000},
        {"likes":17,"name":"lon","views":500000},
        {"likes":12,"name":"key","views":890000}]


for i in range(len(data)):
    response = requests.put(BASE + "video/" + str(i), data[i])
    print(response.json())

input()
response = requests.delete(BASE + "video/0")
print(response)


input()
response = requests.get(BASE+"video/2")
print(response.json())