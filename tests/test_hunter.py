import unittest
from hunter import normalize, supported, evaluate

class HunterTests(unittest.TestCase):
    def test_normalize(self): self.assertEqual(normalize('Hello, WORLD!'), 'hello world')
    def test_supported(self): self.assertTrue(supported('New York', 'I visited New York.'))
    def test_unsupported(self): self.assertFalse(supported('Paris', 'I visited London.'))
    def test_empty_answer(self): self.assertFalse(supported('', 'Anything'))
    def test_evaluate(self):
        r = evaluate([{'id':'1','answer':'blue','context':'The sky is blue.'}, {'id':'2','answer':'green','context':'The sky is blue.'}])
        self.assertEqual((r['total'],r['supported'],r['unsupported'],r['support_rate']), (2,1,1,0.5))
        self.assertFalse(r['model_evaluated'])
    def test_empty(self): self.assertIsNone(evaluate([])['support_rate'])

if __name__ == '__main__': unittest.main()
