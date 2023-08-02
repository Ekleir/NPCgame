
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
        if not isinstance(enemy_exp, int):
            raise TypeError('Полученный опыт не является числом!')
        if enemy_exp >= 0:
            self._exp += enemy_exp
        else:
            raise TypeError('Полученный опыт был отрицательным! Ошибка, произошла непредвиденная деградация!')
        if self._exp >= 100: # выполняется ли условие повышения уровня
            lvl_up = self._exp // 100 #на случай, если опыта будет больше чем на 1 уровень
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
    lv = LvL()
    print(lv)
    lv.add_exp_to_lvl(-111)
    print(lv)
