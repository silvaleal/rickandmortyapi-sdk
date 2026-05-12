from rickandmortysdk import RickAndMortySDK

mySDK = RickAndMortySDK().setPrefix('episode')

earth = mySDK.get(1)

print(earth['result']['name'])
print(earth['result']['air_date'])
print(earth['result']['episode'])
print(earth['result']['characters'])
print(earth['result']['created'])