import pytest

from main import NPC


def test_name():
    mam = NPC("Mam")
    assert mam.name == "Mam"


def test_name_negative():
    with pytest.raises(TypeError) as name_empty:
        mam = NPC("")
    assert 'Укажите имя!' == str(name_empty.value)


def test_name_negative_format():
    with pytest.raises(TypeError) as name_int:
        mam1 = NPC(1)
    with pytest.raises(TypeError) as name_float:
        mam2 = NPC(1.1)
    assert 'Имя должно быть строкой!' == str(name_float.value)
    assert 'Имя должно быть строкой!' == str(name_int.value)

