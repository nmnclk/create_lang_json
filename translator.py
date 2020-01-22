
import json
import io
import asyncio
try:
    to_unicode = unicode
except NameError:
    to_unicode = str

from googletrans import Translator
translator = Translator()

mainLanguageName = "en" #kendi oluşturduğunuz dil json dosyasının kodunu yazın. dosa adi ile aynı olmalıdır
targetLanguages = ["fr", "tr"]# çevirilmesini istediğiniz dillein kodlarını yazınız


def createNewLanguageFile(fileName):
    file = open("files/"+fileName+'.json', 'w', encoding="utf8")
    return file


def readMainLanguage(mainLanguageName):
    file = open("files/"+mainLanguageName+'.json', 'r', encoding="utf8")
    fileContent = file.read()
    return fileContent


async def tarnslatorMetot(key, mainLanguageJson, mainLanguageName, lang):
    return translator.translate(
        mainLanguageJson[key], src=mainLanguageName, dest=lang)


async def main():
    mainLanguageContent = readMainLanguage(mainLanguageName)
    mainLanguageJson = json.loads(mainLanguageContent)
    targetLanguageJson = json.loads(mainLanguageContent)

    for lang in targetLanguages:
        print("Translating for :"+lang+" ...")
        for key in mainLanguageJson.keys():
            translatedObject = await tarnslatorMetot(key, mainLanguageJson, mainLanguageName, lang)
            targetLanguageJson[key] = translatedObject.text

        print(targetLanguageJson)
        with io.open( "files/"+lang + '.json', 'w', encoding='utf8') as outfile:
            str_ = json.dumps(targetLanguageJson,
                            indent=4, sort_keys=True,
                            separators=(',', ': '), ensure_ascii=False)
            outfile.write(to_unicode(str_))

asyncio.run(main())
