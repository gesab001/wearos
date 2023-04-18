import json
import os
import zipfile
import six
from google.cloud import translate_v2 as translate
import subprocess


service_account = r"C:\Users\giova\Documents\galaxywatchbible-2b4c6501ef47_service_account.json"
#print("set GOOGLE_APPLICATION_CREDENTIALS=C:\Users\giova\Documents\galaxywatchbible-2b4c6501ef47_service_account.json")
#subprocess.call("set GOOGLE_APPLICATION_CREDENTIALS="+service_account, shell=True)
#confirmProceed = input("proceed?")
translate_client = translate.Client().from_service_account_json(service_account)


def translate_text(target, text):
    """Translates text into the target language.

    Target must be an ISO 639-1 language code.
    See https://g.co/cloud/translate/v2/translate-reference#supported_languages
    """


    if isinstance(text, six.binary_type):
        text = text.decode("utf-8")

    # Text can also be a sequence of strings, in which case this method
    # will return a sequence of results for each text.
    result = translate_client.translate(text, target_language=target)

    print(u"Text: {}".format(result["input"]))
    print(u"Translation: {}".format(result["translatedText"].encode("utf-8")))
    print(u"Detected source language: {}".format(result["detectedSourceLanguage"]))
    return  result["translatedText"]

f = open("languagesCodes.json", "r")
jsondata = json.loads(f.read())

pathtokjv = os.path.join(r"C:\Users\giova\Desktop\bible_study_galaxy_watch", "kjv.json")
fopen = open(pathtokjv,"r", encoding="utf8")
bible = json.loads(fopen.read())
fopen.close()
version = bible["version"]
bookList = {}
for number in version:
    bookName = version[number]["book_name"]
    #print (bookName + ": " + number)
    bookList[bookName.replace(" ", "-")] = number

 
path = os.path.join(r"C:/Users/giova/Desktop/workspaces_updater", "booksOfTheBibleInDifferentLanguages.json") 

f = open(path, "r", encoding="utf-8")
booksOfTheBibleInDifferentLanguages = json.loads(f.read())
f.close()

def translateTitle(languageCode):
    #source_dir  = os.path.join(appFolder, "language.js")
    #destination_dir = os.path.join(appFolder, "locales", languageCode, "language.js" )
    pathToLanguageJson = os.path.join(languageCode, "bible.json" )

    languagejsJson = getOriginalBibleVerses(pathToLanguageJson)   

    translatedTitle = translate_text(languageCode, languagejsJson["title"]);
    languagejsJson["title"] = translatedTitle.title()

    with open(pathToLanguageJson, "w", encoding="utf8") as outfile:
      json.dump(languagejsJson, outfile, ensure_ascii=False, indent=4)
      

labelsopen = open("translation.json", "r",  encoding='utf-8')
labelsjsondata = json.loads(labelsopen.read())
print(labelsjsondata)
labelsopen.close()

languagecode = input("languageCode: ")
appTitles = labelsjsondata["appTitles"]
appTitleList = []
for key in appTitles:
  #print(key)
  appTitleList.append(key)

for x in range(0, len(appTitleList)):
  appTitle = appTitleList[x]
  print(str(x) + "." + appTitle)  

appTitleInput = int(input("select apptitle: "))
appTitleKey = appTitleList[appTitleInput]
appTitleInput = input("enter app title translation: ")
labelsjsondata["appTitles"][appTitleKey][languagecode] = appTitleInput  
with open("translation.json", "w", encoding="utf-8") as outfile:
  json.dump(labelsjsondata, outfile, ensure_ascii=False, indent=4, sort_keys=True)     
