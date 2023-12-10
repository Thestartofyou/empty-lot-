import geopandas as gpd
from shapely.geometry import Point, Polygon
import matplotlib.pyplot as plt

def find_empty_lots(gis_file_path):
    """
    Find and return empty lots from the GIS data.

    Parameters:
    - gis_file_path (str): File path to the GIS data in GeoJSON or Shapefile format.

    Returns:
    - GeoDataFrame: GeoDataFrame containing the empty lots.
    """
    try:
        # Load GIS data
        gis_data = gpd.read_file(gis_file_path)

        # Check if 'geometry' and 'status' columns exist
        if 'geometry' not in gis_data.columns or 'status' not in gis_data.columns:
            raise ValueError("The GIS data should have 'geometry' and 'status' columns.")

        # Assuming your GIS data has a 'geometry' column representing the shape of each lot
        # If it's a point layer, you can use 'Point' instead of 'Polygon' in the next line
        gis_data['geometry'] = gis_data['geometry'].apply(lambda geom: Polygon(geom) if geom else None)

        # Assuming there's a column 'status' that indicates whether a lot is empty
        empty_lots = gis_data[gis_data['status'] == 'empty']

        return empty_lots

    except Exception as e:
        print(f"Error: {e}")
        return None

def visualize_gis_data(gis_data, title="GIS Data"):
    """
    Visualize GIS data.

    Parameters:
    - gis_data (GeoDataFrame): GIS data to visualize.
    - title (str): Title for the plot.
    """
    try:
        fig, ax = plt.subplots(figsize=(10, 10))
        gis_data.plot(ax=ax, color='lightgrey', edgecolor='black')
        ax.set_title(title, fontsize=16)
        plt.show()

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Replace 'path/to/your/gis_data.geojson' with the actual path to your GIS data file
    gis_file_path = 'path/to/your/gis_data.geojson'

    empty_lots = find_empty_lots(gis_file_path)

    if empty_lots is not None:
        # Display or further process the empty lots
        print("Empty Lots:")
        print(empty_lots)

        # Visualize the GIS data with empty lots
        visualize_gis_data(empty_lots, title="Empty Lots")
