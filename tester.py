import csv
with open('sites.csv') as csvfile:
	reader = csv.reader(csvfile,delimiter=',')
	for row in reader:
		print row[1]
