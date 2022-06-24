import requests
from requests.exceptions import HTTPError

response = requests.get('https://api.github.com')

print(response.status_code)

# If you use a Response instance in a conditional expression, 
# it will evaluate to True if the status code was between 200 and 400, and False otherwise.
if response:
    print('Great it works')
else:
    print("mmm there´s a problem")


for url in ['https://api.github.com', 'https://api.github.com/invalid']:
    try:
        response = requests.get(url)

        #if requests was successful, no Exception will be raised
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error ocurred: {http_err}')
    except Exception as err:
        print(f'HTTP error ocurred: {err}')
    else:
        print('Success!')

# To see the response's content in bytes, you use .content
print()
print('Response content using .content')
print(response.content)

# To see the response's content in text, you use .text
print()
print('Response content using .text')
response.encoding = 'utf-8' # Optional: requests infers this internally
print(response.text)

# deserialize it using .json
print()
print('Response content using .content')
print(response.json())



