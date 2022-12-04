import copy
import random

# Consider using the modules imported above.


class Hat:
    def __init__(self, *args, **kwargs):
        cont = []
        for k, v in kwargs.items():
            if v == 0:
                #kwargs[k] = 1
                v = 1
            for i in range(0, v):
                cont.append(k)

        self.contents = cont

    def draw(self, numero):
        retiradas = []
        if numero > len(self.contents):
            return self.contents
        for i in range(0, numero):
            i = random.choice(self.contents)
            retiradas.append(i)
            self.contents.remove(i)

        return retiradas


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    sucesso = 0
    
    for i in range(0, num_experiments):
        #l = ['azul','azul','azul','azul','vermelho','vermelho','verde','verde','verde','verde','verde','verde']
        #k = hat.contents
        k = hat.contents.copy()
        cont = 0
        d = dict()
        for i in range(0, num_balls_drawn):
            bola = random.choice(k)

            if d.get(bola):
                cont += 1
                d[bola] = cont
            else:
                d.update({bola: 1})
            k.remove(bola)

        if d == expected_balls:
            #print('Iguais')
            sucesso += 1

    return sucesso/num_experiments
    #print(num_experiments, sucesso)


h1 = Hat(azul=3, verde=3)


hat2 = Hat(blue=3,red=2,green=6)
print(experiment(hat=hat2, expected_balls={"blue":2,"green":1}, num_balls_drawn=4, num_experiments=1000))

#print(experiment(hat=h1, expected_balls={
#      'azul': 3, 'verde': 1}, num_balls_drawn=5, num_experiments=10))
