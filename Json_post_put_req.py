
import requests

body = {
    "id": 1,
    "title": "veeresh",
    "author": "typicode"
}

res = requests.put("http://localhost:3000/posts/1", data=body)
print(res)
print(dir(res))

print(res.text)
print(
    "********************************************************************************************************************")

print(res.encoding)
print(
    "********************************************************************************************************************")

print(res.url)
print(
    "********************************************************************************************************************")

print(res.cookies)
print(
    "********************************************************************************************************************")

print(res.elapsed)
print(
    "********************************************************************************************************************")

print(res.headers)
print(
    "********************************************************************************************************************")

print(res.history)
print(
    "********************************************************************************************************************")

print(res.links)
print(
    "********************************************************************************************************************")

print(res.json())
print(
    "********************************************************************************************************************")

print(res.status_code)
print(
    "********************************************************************************************************************")