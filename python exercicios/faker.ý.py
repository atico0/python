# -*- coding: utf-8 -*-
"""
Created on Sun Oct  2 13:39:01 2022

@author: luisg
"""

#documentaoção
#https://faker.readthedocs.io/en/stable/

#importando
import faker

#pritando nome aleatório
print(faker.Faker().name())
fake = faker.Faker()
print(fake.name())



#adicionando dados aleatórios 
from faker.providers import internet
fake.add_provider(internet)

print(fake.ipv4_private())
print(fake.ascii_email())

#providers oficiais podem ser importados dessa forma
from faker.providers import geo
fake.add_provider(geo)

fake.latlng()


#para providers da comunidade é necessário baixar os pacotes 
conda install faker_music #não funcionou
pip install faker_music # funcionou
from faker_music import MusicProvider

fake.add_provider(MusicProvider)
print(fake.music_genre())




fake.sentence()


names = [fake.unique.first_name() for i in range(500)]
names
fake.random
fake.random.getstate()


fake1 = faker.Faker(['pt_BR', 'en_US', 'ja_JP'])
for c in range(100):
    print(fake1.name())

