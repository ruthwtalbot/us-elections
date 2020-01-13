import csv
import sys

year = sys.argv[1];
with open('countypres_2000-2016.csv','r') as in_file, open('usPresElections' + year + '.csv','w') as out_file:
	reader = csv.reader(in_file)
	# get the headers and write them to outfile
	h = next(reader, None) 
	writer = csv.writer(out_file)
	writer.writerow(h)

	# Iterate over counties, keep the ones from the right year.
	# Combine data with the same geoID into one row.
   	counties = dict()
   	for l in reader:
   		rowYear = l[0]
   		if not rowYear == year:
   			continue
   		fips = l[4];
   		key = rowYear +fips
   		if not key in counties:
			counties[key] = l[:5] + [l[9]];
			if len(fips) == 4:
				counties[key][4] = '0' + fips
		counties[key].append(l[8])
		
	# Write all data to outfile.
	for k in counties:
		writer.writerow(counties[k][:10])
