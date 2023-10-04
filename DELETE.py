# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# DELETE.py
# Created on: 2016-04-06 19:32:27.00000
#   (generated by ArcGIS/ModelBuilder)
# Description: 
# ---------------------------------------------------------------------------

# Import arcpy module
import arcpy


# Local variables:
INT_FIRE_TAP20KM_shp = "X:\\02_EWS_GIS\\INTERSECT_HGU_ILOK_BUFFER\\INT_FIRE_TAP20KM.shp"
MODIS_C6_SouthEast_Asia_24h_shp = "X:\\02_EWS_GIS\\MODIS_C6_SouthEast_Asia_24h.shp"
DATA_HOTSPOT_TAP_csv = "U:\\DATA HOTSPOT TAP.csv"
VNP14IMGT_NRT_SouthEast_Asia_24h_shp = "X:\\02_EWS_GIS\\VNP14IMGT_NRT_SouthEast_Asia_24h.shp"
DATA_HOTSPOT_TAP_kmz = "S:\\DATA_HOTSPOT_TAP.kmz"
DATA_HOTSPOT_TAP_xml = "U:\\DATA HOTSPOT TAP.xml"

# Process: Delete
arcpy.Delete_management(INT_FIRE_TAP20KM_shp, "ShapeFile")

# Process: Delete (2)
arcpy.Delete_management(DATA_HOTSPOT_TAP_csv, "TextFile")

# Process: Delete (3)
arcpy.Delete_management(DATA_HOTSPOT_TAP_kmz, "File")

# Process: Delete (4)
arcpy.Delete_management(MODIS_C6_SouthEast_Asia_24h_shp, "ShapeFile")

# Process: Delete (7)
arcpy.Delete_management(VNP14IMGT_NRT_SouthEast_Asia_24h_shp, "ShapeFile")

# Process: Delete (5)
arcpy.Delete_management(DATA_HOTSPOT_TAP_xml, "File")

