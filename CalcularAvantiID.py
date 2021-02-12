import arcpy
 
# function returns list of unique values in a given field of a table
def unique_values(table , field):
	with arcpy.da.SearchCursor(table, [field]) as cursor:
		return sorted({row[0] for row in cursor})

fc = r'D:\2020\CUADRANT\GDB\Eventos_Quadrant.gdb\SpatialJoin' # path to your table or featureclass
lst = unique_values(fc, 'Field1')
with arcpy.da.UpdateCursor(fc, ['Field1', 'AvantiID']) as cursor:
	for row in cursor:
		row[1] = lst.index(row[0])
		cursor.updateRow(row)