# Locations of Russian Diplomatic Missions
This project captures the latitude and longitude of worldwide Russian Diplomatic outposts.

##Workflow
* Grab the XML file form the Consular Department of the Russian Foreign Ministry website
```
wget http://www.kdmid.ru/js/coors2.xml
```
* Parse the file (add in your Google translate API key)
```
python parseXML.py
```
* Use ogr2ogr to produce a GeoJSON file from the CSV (I altered the filenames a bit)
```
ogr2ogr -f GeoJSON Locations-Of-Russian-Diplomatic-Missions-20150526.geojson Locations-Of-Russian-Diplomatic-Missions-20150526.vrt
```

##parseXML.py Explained
* Reads in the XML file
* Runs each country and city name through Google Translate
* Creates a CSV output file called `russianOutposts.csv`

##To Do
* Add in address and contact info for each mission
* Link each mission to its public website
