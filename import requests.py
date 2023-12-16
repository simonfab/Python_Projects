import requests
from bs4 import BeautifulSoup

# Make a request to the webpage
url = 'https://www.google.com/maps/search/business+near+me/@50.9116308,-1.2886536,13z/data=!3m1!4b1?entry=ttu'
response = requests.get(url)

print(url, response)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    print(soup)

    # Find the name and address using CSS selectors
    name_element = soup.select_one('.name')
    address_element = soup.select_one('.address')

    # Check if the elements were found before accessing their text
    if name_element:
        name = name_element.text.strip()
    else:
        name = "Name not found"

    if address_element:
        address = address_element.text.strip()
    else:
        address = "Address not found"

    # Print the results
    print(f"Name: {name}\nAddress: {address}")
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")

import requests
from bs4 import BeautifulSoup

url = 'https://www.google.com/maps/search/business+near+me/@50.9116308,-1.2886536,13z/data=!3m1!4b1?entry=ttu'
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')

    name_element = soup.find('h1')  # Find the <h1> tag for the name
    address_element = soup.find('p')  # Find the <p> tag for the address

    if name_element:
        name = name_element.text.strip()
    else:
        name = "Name not found"

    if address_element:
        address = address_element.text.strip()
    else:
        address = "Address not found"

    print(f"Name: {name}\nAddress: {address}")
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")

import requests
from bs4 import BeautifulSoup

url = 'https://www.google.com/maps/search/business+near+me/@50.9116308,-1.2886536,13z/data=!3m1!4b1?entry=ttu'
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')

    name_element = soup.find(attrs={'data-name': True})  # Find element with data-name attribute
    address_element = soup.find(attrs={'data-address': True})  # Find element with data-address attribute

    if name_element:
        name = name_element.get('data-name').strip()
    else:
        name = "Name not found"

    if address_element:
        address = address_element.get('data-address').strip()
    else:
        address = "Address not found"

    print(f"Name: {name}\nAddress: {address}")
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")

