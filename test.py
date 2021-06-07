import calc


class TestCalculatorApp:

    def test_add(self):
        assert 5 == calc.add(1, 4)

    def test_subtract(self):
        assert 2 == calc.subtract(5, 3)

    def test_multiply(self):
        assert 10 == calc.multiply(2, 5)
