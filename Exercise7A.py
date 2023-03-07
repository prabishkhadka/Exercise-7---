# Import arcpy module
import arcpy

# Set workspace to the "Washington.gdb"
arcpy.env.workspace = r"C:\Geospatial Programming\week8\Exercise7\Exercise7\Exercise7_A\Washington.gdb"

# List the feature classes stored in the workspace
fcList = arcpy.ListFeatureClasses()

# Store the feature classes to citBndty and park variables
citBndry = fcList[0]
park = fcList[1]

#Create new feature layer from park feature class, allows manipulation saving the original feature class.
arcpy.MakeFeatureLayer_management(park, "park_2")

# Open UpdateCursor to interate through the features in citBndry feature class. SHAPE@- to get the boundry of each feature. and "HASParkAndRide" to update.
#initialize variable
total1 = 0
try:
    with arcpy.da.UpdateCursor(citBndry, ["SHAPE@", "HasParkAndRide"]) as cursor:
        for row in cursor:
            #Extract geometry of current feature[SHAPE@] and assign to "boundry variable"
            boundry = row[0]
            #Select the feature in park_2 that are within the extracted geometry.
            arcpy.SelectLayerByLocation_management("park_2", "WITHIN", boundry)
            #Count the number of selected features
            count = int(arcpy.management.GetCount("park_2").getOutput(0))
            #Update True to the field "HasParkAndRide" = True if geometry has park feature.
            if count > 0:
                #Get the number of cities with atleast one park
                total1 += 1
                row[1] = "True"
                cursor.updateRow(row)
    #Clean up cursor and the temporary feature class
    del cursor
    arcpy.management.Delete("park_2")
    #Get total number of cities in the give city boundary file
    total = int(arcpy.GetCount_management(fcList[0]).getOutput(0))
    #Calculate percentage of cities with atleast one park facilities
    percentage = (total1/total)*100
    print(f"The percentage of cities with atleast one park and ride facilities is : {percentage}")


except:
    print(arcpy.GetMessage())
























