from CreLanguageTranslate.googleTranslate import googleTranslate
import random

class translateInstance():

    translateClasses = []
    
    def __init__(self, sourceLanguage,targetLanguage):
      self.sourceLanguage = sourceLanguage
      self.targetLanguage = targetLanguage
      if(not translateInstance.translateClasses):
          print('Init all translators once')
          translateInstance.translateClasses.append( googleTranslate() )
          # add more

      self.translateInstances = []
      for translateClass in translateInstance.translateClasses:
        if((sourceLanguage in translateClass.sourceLanguages) and (targetLanguage in translateClass.targetLanguages)): 
          self.translateInstances.append( translateClass )
      return None

    def translate(self, sourceText):
        targetText = None
        if(self.translateInstances):
          anyTranslator = random.choice(self.translateInstances)
          targetText = anyTranslator.translate(sourceText, self.sourceLanguage, self.targetLanguage)      
        return targetText

    def getTranslatorInfo():
      for translateClass in translateInstance.translateClasses:
        print(translateClass.getServiceName())
        print(['counter: ',translateClass.callCounter, 'len:',translateClass.totalTextLength])       

                
