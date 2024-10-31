

# newsapiLanguages =  ["ar","de","en","es","fr","he","it","nl","no","pt","ru","sw","ur","zh"]
# newsapiLanguages =  ["ar","de","en","es","fr","he","it","nl","no","pt","ru","sw","zh",   "el","ja"]

## DATA_PATH = Path.cwd()

class TranslateBase:

    def __init__(self):
        ## ts = int(time.time())
        self.allLanguages = []
        return None

    def getServiceName(self):
        return 'unknown'


'''
def splitText(inText, maxLength=4000, splitBy=["\n\n","\n","."]):
    ##print([splitBy, inText])
    outText = []
    if(not isinstance(inText, list)):
      inText = [inText]
    if(len(splitBy)<1):
       return inText
    for oneText in inText:
      if(len(oneText)<maxLength):
        outText.append(oneText)
      else:  
        if(splitBy[0] in oneText): 
          nTxt = math.ceil(len(oneText)/maxLength)
          maxLen = math.floor(len(oneText)/nTxt)        
          collectedText = ""
          firstChunk = True
          ##print([splitBy[0], oneText, oneText.split(splitBy[0])])
          for singleText in oneText.split(splitBy[0]):
            if(not firstChunk):
              collectedText += splitBy[0]  
            if(len(collectedText + singleText)>maxLen):
               if(len(collectedText)>0):
                 outText.append(collectedText)
               collectedText = singleText
            else:
               collectedText += singleText
            firstChunk = False
          if(len(collectedText)>0):
            outText.append(collectedText)
        else:
          outText.append(oneText) 
    ##print(['out', outText]) 
    if(len(splitBy)>1):
      return splitText(outText, maxLength, splitBy[1:])
    return outText 
'''


'''
# small Split
def transLarge(txt):
    if(len(txt)<4000):
        return gt.translate(txt) 
    else:
        sentences = txt.split('.')  
        count = len(sentences)
        half = round(count/2)
        first = '. '.join(sentences[:half])
        second = '. '.join(sentences[half:])
        firstT = transLarge(first)
        secondT = transLarge(second)
        return firstT + " " + secondT


'''
