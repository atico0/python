# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 20:59:51 2022

@author: luisg
"""

import numpy as np

#Exercise 1 Set the random seed to 10. Then using Numpy
#create a one-dimensional array consisting
#of 30 pseudo-randomly generated values from the uniform distribution
#[0,1). Print result to the console as shown below.


?np.random.rand

#setando seed=10
np.random.seed(10)

#criando um vetor 10x4 de valores aleatórios que seguem uma
#distribuição uniforme [0, 1]
print(np.random.rand(30))


#Exercise 2 Using Numpy create a two-dimensional array with the shape
#(10, 4) pseudo-randomly generated values from the standard normal
#distribution N(0,1). Set the random seed to 20.
#Print result to the console as shown below.

?np.random.randn

#setando seed=20
np.random.seed(20)

#criando um vetor 10x4 de valores aleatórios que seguem uma
#distribuição normal padrão (N(0,1))
print(np.random.randn(10,4))


#Exercise 3 Using Numpy create a two-dimensional array with the shape
#(10, 4) pseudo-randomly generated values from the normal
#distribution N(100, 5). Set the random seed to 30.
#Print result to the console as shown below.

?np.random.normal

#minha solução:
#setando seed=30
np.random.seed(30)

#criando um vetor 10x4 de valores aleatórios que seguem uma
#distribuição N(100, 5) (minha solução)
print(np.random.normal(loc=100, scale=5, size=(10,4)))


#solução do curso
#Fazendo o mesmo acima mas nesse caso ele está criando um
#criando um vetor 10x4 de valores aleatórios que seguem uma
#distribuição normal padrão (N(0,1)) e "despadronizando" esse vetor
sigma = np.sqrt(5)
mu = 100
print(sigma * np.random.randn(10, 4) + mu)





























































































































