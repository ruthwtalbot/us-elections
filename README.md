# us-elections


## Data processing steps:
* Download data from https://electionlab.mit.edu/data
* Run combine.py to separate out data by year
* Run ogr2ogr command to combine csv with geo data:
	* ogr2ogr -sql "select inshape.*, <csvname>.* from inshape left join '<csvname>.csv'.<csvname> on on inshape.GEOID = <csvname>.FIPS" shape_join.shp inshape.shp
* Create geojson file from shapefile 
	* ogr2ogr   -f GeoJSON <output>.json  shape_join.shp
* Opt: create topojson file
	* topojson <input>.json  -o <output>.json  -p
