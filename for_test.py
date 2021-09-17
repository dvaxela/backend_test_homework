import unittest


class Calculator:
    """Производит арифметические действия."""

    def summ(self, *args):
        """Возвращает сумму принятых аргументов."""       
        return sum(i for i in args)


class TestCalc(unittest.TestCase):
    """Тестируем Calculator."""
    
    @classmethod
    def setUpClass(cls):
        """Вызывается однажды перед запуском всех тестов класса."""
        cls.calc = Calculator()

    def test_summ(self):
        act = TestCalc.calc.summ(3, -3, 5)
        self.assertEqual(act, 5, 'summ работает неправильно')

    def test_summ_no_argument(self):
        act = TestCalc.calc.summ()
        self.assertIsNone(act, 'Функция ожидает 2 и более аргумента')
        

    def test_summ_one_argument(self):
        act = TestCalc.calc.summ(3)
        self.assertIsNone(act, 'Функция ожидает 2 и более аргумента')

if __name__ == "__main__":
    unittest.main() 