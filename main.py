from lvl import LvL


class NPC:
    """
    Класс с характеристиками NPC
    """
    __slots__ = ('_name', '_level')

    def __init__(self, name: str):
        self._name = name
        self._level = LvL()
        # self._gold = 0

    def __str__(self):
        return f'Герой {self._name}\n{self._level}'

    @property
    def name(self):
        return self._name

    def __setattr__(self, key, value):
        if key == '_name' and not value:
            raise TypeError('Укажите имя!')
        if key == '_name' and not isinstance(value, str):
            raise TypeError('Имя должно быть строкой!')
        super().__setattr__(key, value)

    def get_exp(self, enemy_exp):
        return self._level.add_exp_to_lvl(enemy_exp)


if __name__ == '__main__':
    bob = NPC('Egor')
    print(bob)
    bob.get_exp(111)
    print(bob)



