import requests


res = requests.delete("http://localhost:3000/posts/1")
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