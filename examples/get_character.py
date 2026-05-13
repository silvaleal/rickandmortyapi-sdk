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