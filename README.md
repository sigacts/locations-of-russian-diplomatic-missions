# Locations of Russian Diplomatic Missions
This project captures the latitude and longitude of worldwide Russian Diplomatic outposts.

##Workflow
* Grab XML file `http://www.kdmid.ru/js/coors2.xml`
* Parse file
* Run each country and city name through Google Translate
* Create a CSV and then run through ogr2ogr to create a GeoJSON file
`ogr2ogr -f GeoJSON Locations-Of-Russian-Diplomatic-Missions-20150526.geojson Locations-Of-Russian-Diplomatic-Missions-20150526.vrt`

##To Do
* Add in address and contact info for each mission
* Link each mission to its website
