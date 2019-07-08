import unittest

import crypto_proj


class TestCryptoProject(unittest.TestCase):

    def setUp(self):
        self.proj = crypto_proj.CryptoProject()

    def test_task_1(self):
        m = self.proj.task_1()
        self.assertEqual(m, '0xed9dab5d5a43e28574bdfdae5fb9a641')

    def test_task_2(self):
        password, salt = self.proj.task_2()
        self.assertEqual(password, 'martha')
        self.assertEqual(salt, 'sweetpea')

    def test_task_3(self):
        d = self.proj.task_3()
        self.assertEqual(d, '0xa537451e4840a71')

    def test_task_4(self):
        d, waldo = self.proj.task_4()
        self.assertEqual(d, '0x5caaf5fb3b66a88f27df0a822df170ecbb5251b2684fbce89e8cb32308d20134655f7512c46a17accae48916c3a595037802d055a51d1d27986f8e6ba099754d1f865d6b306f78f9f93e679dd4a64106f47b747d63121ae7b7f754a0ea5e35f2b83db446d25dd26e1d043a69d5532c68700c435567a0727a6b76ef46a40a15a9')
        self.assertEqual(waldo, 'cb52adc501dce50602b3676b58245eb0365a1d63cb27ae666807280a')

    def test_task_5(self):
        msg = self.proj.task_5()
        self.assertEqual(msg, 'bdornier3, how are you? Him? He might be okay... Well, no, probably not now.')


if __name__ == '__main__':
    unittest.main()
