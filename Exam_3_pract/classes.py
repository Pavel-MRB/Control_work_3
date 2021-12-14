class Tomato:
    states={1:'Зелено-зрелый',2:'Бланжевый',3:'Спелый'}
    i=1

    def __init__(self,ind=2):
        self._index=ind
        self._state=self.__class__.states[1]

    def grow(self):
        Tomato.i+=1
        self._state=Tomato.states[Tomato.i]

    def is_ripe(self):
        if self._state==self.__class__.states[3]:
            print('Томат созрел')



tomat=Tomato()
print(tomat._state)
tomat.grow()
print(tomat._state)
tomat.grow()
print(tomat._state)
tomat.is_ripe()
