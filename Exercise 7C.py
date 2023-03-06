#----------Exercise7C------------

# Import the ArcPy module
import arcpy

# Allow overwrite the existing output files
arcpy.env.overwriteOutput = True

# Set the workspace to the geodatabase containing the feature classes
arcpy.env.workspace = r"C:\Geospatial Programming\week8\Exercise7\Exercise7_C\Washington.gdb"

# Get a list of all feature classes in the workspace and print their names
fcList = arcpy.ListFeatureClasses()
for fc in fcList:
    print(fc)

    # Get a list of all fields in the feature class and print their names
    fldList = arcpy.ListFields(fc)
    for fld in fldList:
        print(fld.name)

# Create a feature layer from the first feature class in the list
arcpy.MakeFeatureLayer_management(fcList[0], "ParkAndRide500")

# Select all features with a capacity of more than 500 parking spaces
arcpy.SelectLayerByAttribute_management("ParkAndRide500", "NEW_SELECTION", "Approx_Par > 500")

# Copy the selected features to a new feature class
arcpy.CopyFeatures_management("ParkAndRide500", "ParkAndRide500plus")

# Delete the feature layer to clean up the workspace
arcpy.Delete_management("ParkAndRide500")

# Check the new feature class in the workspace and Print the name. 
if arcpy.Exists("ParkAndRide500Plus"):
    print("The new feature class only with parks more than 500 is ParkAndRide500plus")
    
