#Teste utilizando o retorno de uma funç~~ao chamada CalculaInss


import pytest

@pytest.mark.parametrize('salario,expected', [(3000, 330)])
def test_calcula(salario, expected):
    assert calcula_inss(salario) == expected
