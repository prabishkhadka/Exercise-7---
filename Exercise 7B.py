#import arcpy module
import arcpy

# set workspace to the Washington.gdb
arcpy.env.workspace = r"C:\Geospatial Programming\week8\Exercise7\Exercise7\Exercise7_B\Washington.gdb"

# Store the features inside geodatabase in a list
fcList = arcpy.ListFeatureClasses()

# Loop through the list and print name of feature class and field names
for fc in fcList:
    print(fc)
    fields = arcpy.ListFields(fc)
    for flds in fields:
        print(flds.name)

# Store the features in the list to separate variable
citBoudry = fcList[0]
parkAndRide = fcList[1]

# Create new layer to store parkAndRide to keep original layer safe
arcpy.MakeFeatureLayer_management(parkAndRide, "parkAndRide_2")
#Initilaize variable
moreThanTwo = 0
# Open Update Cursor to iterate through the features in CitBoudrt fc and update the field HasTwoParkAndRides true if it has at least two parks
# SHAPE@ to extract the boundary of each feature stored in CityBoundry

try:
    with arcpy.da.UpdateCursor(citBoudry, ["SHAPE@", "HasTwoParkAndRides"]) as cursor:
        for row in cursor:
            # Store the boundary extracted in a variable
            boundry = row[0]
            
            # Select the RideandPark features inside the boundary
            arcpy.SelectLayerByLocation_management("parkAndRide_2", "WITHIN", boundry)
            
            # Get the number of features selected and store it in variable
            count = int(arcpy.management.GetCount("parkAndRide_2").getOutput(0))
            
            # Check if the count is at least 2. If yes, update the field HasParkAndRide to True and count the number of feature having at least two parks and ride
            if count >= 2:
                row[1] = "True"
                
                moreThanTwo += 1
                cursor.updateRow(row)
        del cursor
except:
    print(arcpy.GetMessage())
# Get total number of features in City Boundry 
total =int(arcpy.management.GetCount(fcList[0]).getOutput(0))
# Calculate percentage of cities that have at least two park and rides within their boundaries
percentage = (moreThanTwo / total) * 100

# Print the percentage
print("The total percentage cities that have at least two park and rides within their boundaries is : {}%".format(percentage))
