import unittest
from banco import Banco

class TesteBanco(unittest.TestCase):
    def test_adicionar_e_obter_saldo(self):
        banco = Banco()
        banco.adicionar_cliente("João", 1000)
        self.assertEqual(banco.obter_saldo("João", 1000))

if __name__ == "__main":
    unittest.main()