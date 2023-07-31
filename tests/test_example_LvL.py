import pytest

from example import NPC


def test_name():
    mam = NPC("Mam")
    assert mam.name == "Mam"


def test_name_negative():
    with pytest.raises(TypeError) as name_empty:
        mam = NPC("")
    assert 'Укажите имя!' == str(name_empty.value)


def test_name_negative_int():
    with pytest.raises(TypeError) as name_int:
        mam = NPC(1)
    assert 'Имя должно быть строкой!' == str(name_int.value)
