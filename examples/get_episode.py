from rickandmortysdk import RickAndMortySDK

mySDK = RickAndMortySDK().setPrefix('episode')

episode = mySDK.get(1)

print(episode['result']['name'])
print(episode['result']['air_date'])
print(episode['result']['episode'])
print(episode['result']['characters'])
print(episode['result']['created'])