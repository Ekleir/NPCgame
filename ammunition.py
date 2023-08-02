
class Weapon:
    __weapons_list = []

    def __init__(self, id: int, name: str, weapon_lvl: int, damage: int, cost: int):
        self.__id = id
        self.__name = name
        self.__weapon_lvl = weapon_lvl
        self.__damage = damage
        self.__cost = cost
        Weapon.__weapons_list.append(self)

    def __str__(self):
        return f'~{self.__name}~, урон - {self.__damage}'

    def __repr__(self):
        return f'\n{self.__id}) ~{self.__name}~, урон - {self.__damage}, цена - {self.__cost}'

    @staticmethod
    def get_ammunition_list():
        return Weapon.__weapons_list


kris = Weapon(1, 'Kris', weapon_lvl=1, damage=1, cost=1)
pole = Weapon(2, 'Pole', weapon_lvl=2, damage=2, cost=3)
blade = Weapon(3, 'Blade', weapon_lvl=3, damage=4, cost=7)
flamberg = Weapon(4, 'Flamberg', weapon_lvl=4, damage=8, cost=15)
devastator = Weapon(5, 'Devastator', weapon_lvl=5, damage=16, cost=31)
print(kris)
print(Weapon.get_ammunition_list())


