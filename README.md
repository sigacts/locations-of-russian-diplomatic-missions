# Locations of Russian Diplomatic Missions
This project captures the latitude and longitude of worldwide Russian Diplomatic outposts.

##Workflow
* Grab XML file
```
wget http://www.kdmid.ru/js/coors2.xml
```
* Parse file (update with your own Google translate API key)
```
python parseXML.py
```
* Create a CSV and then use ogr2ogr to create a GeoJSON file (I altered the filenames a bit)
```
ogr2ogr -f GeoJSON Locations-Of-Russian-Diplomatic-Missions-20150526.geojson Locations-Of-Russian-Diplomatic-Missions-20150526.vrt
```

##parseXML
* Runs each country and city name through Google Translate
* Creates an output file called `russianOutposts.csv`

##To Do
* Add in address and contact info for each mission
* Link each mission to its website
