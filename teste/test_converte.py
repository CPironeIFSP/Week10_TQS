import unittest
from numeroromano import converte

class TestConverte(unittest.TestCase):
    def test_numeros_simples(self):
        self.assertEqual(converte("I"), 1)
        self.assertEqual(converte("V"), 5)
        self.assertEqual(converte("X"), 10)
        self.assertEqual(converte("L"), 50)

    def test_numeros_combinados(self):
        self.assertEqual(converte("II"), 2)
        self.assertEqual(converte("XXII"), 22)
        self.assertEqual(converte("IX"), 9)
        self.assertEqual(converte("XXIV"), 24)

    def test_caracteres_invalidos(self):
        with self.assertRaises(ValueError):
            converte("A")

    def test_sequencia_invalida(self):
        with self.assertRaises(ValueError):
            converte("IIII")  # Adicional: Sequência inválida não suportada

    def test_entrada_vazia(self):
        with self.assertRaises(ValueError):
            converte("")  # Testa entrada vazia


if __name__ == "__main__":
    unittest.main()
