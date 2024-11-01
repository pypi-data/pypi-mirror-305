from CreLanguageTranslate.translateInstance import translateInstance

class LanguageTranslate():


    translateInstances = {}

    #def __init__(self):
    #  self.translateClasses.append( googleTranslate() )
    #  return None

    def getTranslatorByLanguage(self, sourceLanguage,targetLanguage):
        languagePair = sourceLanguage+' -> '+targetLanguage
        if(not languagePair in self.translateInstances):
          self.translateInstances[languagePair] = translateInstance(sourceLanguage,targetLanguage)
        return self.translateInstances[languagePair]  
               

    def translate(sourceLanguage, targetLanguage, sourceText):
        targetText = None      
        ti = self.getTranslatorByLanguage(sourceLanguage,targetLanguage)
        targetText = ti.translate(sourceText)
        return targetText


