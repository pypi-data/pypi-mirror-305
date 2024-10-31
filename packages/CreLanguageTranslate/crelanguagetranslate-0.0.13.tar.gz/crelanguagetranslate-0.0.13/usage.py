#pip3 install CreLanguageTranslate

from CreLanguageTranslate.LanguageTranslate import LanguageTranslate 

from CreLanguageTranslate.translateInstance import translateInstance

lt = LanguageTranslate()
li = lt.getTranslatorByLanguage('en','de')
tar = li.translate('tree')
print(tar)
tar2 = li.translate('house')
print(tar2)

translateInstance.getTranslatorInfo()


