#Sacramento stuff
#a) most popular zip code
#b) the average house cost
#c) BEST DEAL (largest square foot / cost ratio )


#zip code
z_dict = {} 
houses = open("./realestate-2.csv", "r")
z_count = 0
price_list = []
house_sum = 0
for line in houses:
	line = line.rstrip()
	house_parts = line.split(",")
	if house_parts[2] not in z_dict:
		z_dict[house_parts[2]] = 1
	else:
		z_dict[house_parts[2]] += 1
pop_zip = 1
pop_value = 1
for z in z_dict.keys():
	if z_dict[z] > pop_value:
		pop_value = z_dict[z]
		pop_zip = z
	else: 
		continue
print "The most popular zip code is %s with %s occurences" % (pop_zip, pop_value)

#average
z_list = []
houses = open("./realestate-2.csv", "r")
output = open("./output.txt", "wb")
z_count = 0
price_list = []
house_sum = 0
for line in houses:
	line = line.rstrip()
	house_parts = line.split(",") 
	price_list.append(house_parts[9])
	house_sum += int(house_parts[9])
average = house_sum / len(price_list)
print "The average house price is %s" % (average)


#DEAL OR NO DEAL
z_list = []
houses = open("./realestate-2.csv", "r")
z_count = 0
price_list = []
house_sum = 0
cost_list = []
sq_list = []
ratio = 100
best_deal = "a"
for line in houses:
	line = line.rstrip()
	house_parts = line.split(",")
	if float(house_parts[6]) > 0.0:
		ratio2 = float(house_parts[9]) / float(house_parts[6])
		if ratio2 < ratio:
			if ratio2 > 59.00:
				ratio = ratio2
				best_deal = house_parts[0]
print "The best deal is %s with %s dollars per square foot" % (best_deal, ratio)

# LAT AND LON 
grauer_lat = 33.0283
grauer_lon = 117.2562
houses = open("./realestate-2.csv", "r")
for line in houses: 
	line = line.rstrip()
	house_parts = line.split(",")
