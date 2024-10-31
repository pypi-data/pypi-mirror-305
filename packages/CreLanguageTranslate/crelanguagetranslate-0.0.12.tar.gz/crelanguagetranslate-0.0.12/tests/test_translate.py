from unittest import TestCase

from CreLanguageTranslate.LanguageTranslate import LanguageTranslate 

class TestTranslate(TestCase):
    def test_simple_translate(self):
        lt = LanguageTranslate()
        li = lt.getTranslatorByLanguage('en','de')
        tarTree = li.translate('tree')
        self.assertEqual('Baum', tarTree)
        tarHouse = li.translate('house')
        self.assertEqual('Haus', tarHouse)

