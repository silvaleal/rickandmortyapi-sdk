from rickandmortysdk import RickAndMortySDK

mySDK = RickAndMortySDK().setPrefix('location')

earth = mySDK.get(1)

print(earth['result']['name'])
print(earth['result']['type'])
print(earth['result']['dimension'])
print(earth['result']['residents'])