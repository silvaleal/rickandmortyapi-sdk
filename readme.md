# Rick And Morty SDK - Unofficial

[![PyPI version](https://img.shields.io/pypi/v/UORickandmortyapi-sdk.svg)](https://pypi.org/project/UORickandmortyapi-sdk/)

Unofficial SDK library for interacting with the API [Rick and Morty API](https://rickandmortyapi.com/api?utm_source=chatgpt.com).


## Install

```bash
pip install UORickandmortyapi-sdk
```

## Basic Usage

```python
from uorickandmortysdk import UORickAndMortySDK

mySDK = UORickAndMortySDK().setPrefix('character')

print(mySDK.get(1))       # Get a specific character.
print(mySDK.get())        # Get multiple characters.
print(mySDK.get(page=2))  # Get characters from a specific page.
```

## Basic Example

```python
from uorickandmortysdk import UORickAndMortySDK

mySDK = UORickAndMortySDK().setPrefix('character')

rick = mySDK.get(1)

print(rick['result']['name'])
print(rick['result']['status'])
print(rick['result']['species'])
print(rick['result']['type'])
print(rick['result']['gender'])
print(rick['result']['origin']['name'])
print(rick['result']['origin']['url'])

# ------- OUTPUT --------------#
# Rick Sanchez
# Alive
# Human
#
# Male
# Earth (C-137)
# https://rickandmortyapi.com/api/location/1
```
