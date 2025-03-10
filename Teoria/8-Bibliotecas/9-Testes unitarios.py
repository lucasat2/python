"""

Testes Unitários

Crie uma classe Calculadora com operações básicas (soma, subtração, multiplicação, divisão) e desenvolva:

Doctests para cada método
Testes unitários usando unittest
(Pesquise !)
"""


class Calculadora:
    """
    Classe Calculadora com operações básicas.
    
    >>> calc = Calculadora()
    >>> calc.soma(2, 3)
    5
    >>> calc.subtracao(5, 2)
    3
    >>> calc.multiplicacao(3, 4)
    12
    >>> calc.divisao(10, 2)
    5.0
    >>> calc.divisao(5, 0)  # Teste de divisão por zero
    Traceback (most recent call last):
        ...
    ValueError: Divisão por zero não é permitida.
    """
    
    def soma(self, a, b):  # Método que realiza a soma de dois números
        return a + b
    
    def subtracao(self, a, b):  # Método que realiza a subtração de dois números
        return a - b
    
    def multiplicacao(self, a, b):  # Método que realiza a multiplicação de dois números
        return a * b
    
    def divisao(self, a, b):  # Método que realiza a divisão de dois números
        if b == 0:
            raise ValueError("Divisão por zero não é permitida.")  # Levanta um erro se o denominador for zero
        return a / b

if __name__ == "__main__":  # Verifica se o script está sendo executado diretamente
    import doctest  # Importa o módulo doctest para testar a documentação
    doctest.testmod()  # Executa os testes definidos nas docstrings
    
    import unittest  # Importa o módulo unittest para testes unitários

    class TestCalculadora(unittest.TestCase):  # Classe de testes unitários
        def setUp(self):  # Método que inicializa a instância da Calculadora antes de cada teste
            self.calc = Calculadora()

        def test_soma(self):  # Teste do método soma
            self.assertEqual(self.calc.soma(2, 3), 5)

        def test_subtracao(self):  # Teste do método subtração
            self.assertEqual(self.calc.subtracao(5, 2), 3)

        def test_multiplicacao(self):  # Teste do método multiplicação
            self.assertEqual(self.calc.multiplicacao(3, 4), 12)

        def test_divisao(self):  # Teste do método divisão
            self.assertEqual(self.calc.divisao(10, 2), 5.0)
            
        def test_divisao_por_zero(self):  # Teste para verificar erro na divisão por zero
            with self.assertRaises(ValueError):
                self.calc.divisao(5, 0)
    
    unittest.main()  # Executa os testes unitários
