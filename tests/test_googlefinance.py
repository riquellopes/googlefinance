import googlefinance
import unittest


class TestQuotes(unittest.TestCase):

    def test_one_symbol(self):
        appl = googlefinance.getQuotes('GOOG')[0]
        self.assertEqual(appl["Index"], "NASDAQ")
        self.assertEqual(appl["StockSymbol"], "GOOG")

    def test_symbols(self):
        quotes = googlefinance.getQuotes(['GOOG', 'VIE:BKS'])
        self.assertEqual(quotes[0]["Index"], "NASDAQ")
        self.assertEqual(quotes[0]["StockSymbol"], "GOOG")
        self.assertEqual(quotes[1]["Index"], "VIE")
        self.assertEqual(quotes[1]["StockSymbol"], "BKS")

    def test_empty(self):
        try:
            googlefinance.getQuotes("")
            self.assertTrue(False)
        except Exception as e:
            self.assertTrue("Can not be blank." in str(e))
