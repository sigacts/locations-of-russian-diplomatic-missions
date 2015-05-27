import csv
import sys
import json
import time
import random
import requests
import HTMLParser
import unicodedata
from xml.dom.minidom import parseString


def getFile():
	fileObj = open('coors2.xml','r')
	fileContent = fileObj.read()
	fileObj.close()

	return fileContent


def runTranslate(queryText):
	requestURL = "https://www.googleapis.com/language/translate/v2?"
	queryParams = {	'key': '{{API_KEY}}',
					'source': 'ru',
					'target': 'en',
					'q': queryText}

	r = requests.get(requestURL, params = queryParams)
	if r.status_code == 200:
		queryResponse = r.text
	else:
		sys.quit()
	translatedText = jsonParse(queryResponse)

	return translatedText


def jsonParse(jsonStr):
	jsonStr = jsonStr
	jsonObj = json.loads(jsonStr)
	translatedText = jsonObj["data"]["translations"][0]["translatedText"]

	return translatedText


def parseXML(dom):
	itemList = []
	h = HTMLParser.HTMLParser()

	for i in dom.getElementsByTagName('RKZU'):
		itemLat = i.attributes["latitude"].value
		itemLng = i.attributes["longitude"].value

		itemCtry = i.attributes["country"].value
		tranCtry = runTranslate(itemCtry)
		tranCtry = unicodedata.normalize('NFKD', tranCtry)
		tranCtry = tranCtry.encode('ASCII', 'ignore')
		tranCtry = h.unescape(tranCtry)

		itemCity = i.attributes["city"].value
		tranCity = runTranslate(itemCity)

		itemType = i.attributes["type"].value
		tranType = runTranslate(itemType)

		tempList = [tranCtry, tranCity, itemLat, itemLng, tranType]
		itemList.append(tempList)

		#Avoid hitting the API too frequently
		delayOps()

	return itemList


def delayOps():
	timerCount = random.choice([1, 2, 3])
	time.sleep(timerCount)

	return timerCount


def main():
	xmlStr = getFile()
	dom = parseString(xmlStr)
	itemList = parseXML(dom)

	outFile = open("russianOutposts.csv", "wb")
	writer = csv.writer(outFile)
	for z in itemList:
		writer.writerow(z)
	outFile.close()


if __name__ == "__main__":
	main()