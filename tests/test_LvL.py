import pytest
from lvl import LvL


def test_create_lvl():
    lvl1 = LvL()
    assert lvl1._level == 1
    assert lvl1._exp == 0
    assert lvl1._hp == 10
    assert lvl1._mp == 10
    assert lvl1._attack == 1
    assert lvl1._defense == 1


def test_create_lvl_negative():
    with pytest.raises(TypeError):
        lvl1 = LvL(1)


def test_add_exp_to_lvl():
    lvl1 = LvL()
    lvl1.add_exp_to_lvl(10)
    assert lvl1._exp == 10


def test_add_exp_to_lvl_negative():
    lvl1 = LvL()
    with pytest.raises(TypeError) as error1:
        lvl1.add_exp_to_lvl(-10)
    assert str(error1.value) == 'Полученный опыт был отрицательным! Ошибка, произошла непредвиденная деградация!'
    with pytest.raises(TypeError) as error2:
        lvl1.add_exp_to_lvl('as')
    assert str(error2.value) == 'Полученный опыт не является числом!'


