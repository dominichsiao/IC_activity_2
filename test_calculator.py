import calculator


class TestCalculatorApp:

    def test_add(self):
        assert 5 == calculator.add(1, 4)

    def test_subtract(self):
        assert 2 == calculator.subtract(5, 3)

    def test_muiltiply(self):
        assert 20 == calculator.multiply(2, 10)
