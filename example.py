

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


class LvL:
    """
    Класс с характеристиками LvL
    """
    __slots__ = ('_level', '_exp', '_hp', '_mp', '_attack', '_defense')

    def __init__(self):
        self._level = 1
        self._exp = 0
        self._hp = 10
        self._mp = 10
        self._attack = 1
        self._defense = 1

    def __str__(self):
        return f'уровень {self._level},' \
               f' exp - {self._exp}\n' \
               f'HP:{self._hp} ' \
               f'MP:{self._mp}\n' \
               f'ATK:{self._attack} ' \
               f'DEF:{self._defense}\n'


    def add_exp_to_lvl(self, enemy_exp: int) -> None:
        """
        Добавляет опыт к прогресс-бару LvL или повышает LvL
        """
        self._exp += enemy_exp
        if self._exp >= 100:
            lvl_up = self._exp // 100
            self._level += lvl_up
            self._exp -= lvl_up * 100
            self.lvl_up_stats(lvl_up)

    def lvl_up_stats(self, lvl_up: int) -> None:
        """
        Увеличивает характеристики при повышении уровня
        """
        self._hp += lvl_up * 10
        self._mp += lvl_up * 10
        self._attack += lvl_up
        self._defense += lvl_up


if __name__ == '__main__':
    bob = NPC(1)
    print(bob)
    # bob.get_exp(111)
    # print(bob)
    # mam = NPC('1')
    # print(type(mam.name))


