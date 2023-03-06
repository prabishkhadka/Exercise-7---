# Import the ArcPy module
import arcpy

# Allow overwriting the existing output files
arcpy.env.overwriteOutput = True

# Set the workspace to the geodatabase containing the feature classes
arcpy.env.workspace = r"C:\Geospatial Programming\week8\Exercise7\Exercise7\Exercise7_D\Washington.gdb"

# Get a list of all feature classes in the workspace and print their names
fcList = arcpy.ListFeatureClasses()
for fc in fcList:
    print("Feature Class : ",fc)
    print("Field Names : ")

    # Get a list of all fields in the feature class and print their names
    fldList = arcpy.ListFields(fc)
    for fld in fldList:
        print(fld.name)

# Create a feature layer from the point shapefile
arcpy.MakeFeatureLayer_management(fcList[0], "park_2")

#Initialize the variable count to count the number of features in the cityBoundary
count = 0

# Loop through the polygon shapefile
with arcpy.da.SearchCursor(fcList[1], ["SHAPE@", "NAME"]) as cursor:
    for row in cursor:
        count += 1
        boundary = row[0]
        
        # Select all points within the current polygon
        arcpy.SelectLayerByLocation_management("park_2", "WITHIN", boundary)

        # Create a new feature class with the selected points
        featureName = row[1].replace(" ", "_") + "_RideAndPark"
        arcpy.CopyFeatures_management("park_2", featureName)

# Delete the temporary feature layer
arcpy.management.Delete("park_2")

# Check the 'Federal Way' is created or not
if arcpy.Exists("Federal_Way_RideAndPark"):
    print("Desired feature layer for the city Federal Way is created")
print("The number of features created: ",count)
