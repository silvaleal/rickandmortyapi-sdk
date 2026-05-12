from rickandmortysdk import RickAndMortySDK

mySDK = RickAndMortySDK().setPrefix('character')

# print(mySDK.get(1))       # Pegue um personagem específico.
# print(mySDK.get())        # Pegue vários personagens.
# print(mySDK.get(page=2))  # Pegue vários personagens de uma página específica.

rick = mySDK.get(1)

print(rick['result']['name'])
print(rick['result']['status'])
print(rick['result']['species'])
print(rick['result']['type'])
print(rick['result']['gender'])
print(rick['result']['origin']['name'])
print(rick['result']['origin']['url'])