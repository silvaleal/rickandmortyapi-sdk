from uorickandmortysdk import UORickAndMortySDK

mySDK = UORickAndMortySDK().setPrefix('character')

earth = mySDK.get(1)

print(earth['result']['name'])
print(earth['result']['type'])
print(earth['result']['dimension'])
print(earth['result']['residents'])