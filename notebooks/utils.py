import geopandas as gpd
import pandas as pd
from dateutil.relativedelta import relativedelta
import datetime
import time
import os
import geopandas as gpd
import pandas as pd
from dateutil.relativedelta import relativedelta
import datetime
import time
import os


def _assign_district(
    data: pd.DataFrame,
    districts: gpd.GeoDataFrame,
    lon_col: str,
    lat_col: str,
    prefix: str
) -> gpd.GeoDataFrame:
    """Assign district to each person in the data based on their location."""
    df = data.copy()
    if "geometry" in df.columns:
        df = df.drop(columns=["geometry"])
    gdf = gpd.GeoDataFrame(
        df, geometry=gpd.points_from_xy(df[lon_col], df[lat_col])
    )
    gdf.crs = "EPSG:4326"
    gdf = gdf.to_crs("EPSG:28992")
    result = gpd.sjoin(
        gdf,
        districts[["WK_CODE", "WK_NAAM", "geometry"]],
        how="left",
        predicate="within",
    )
    result.drop(columns=["index_right"], inplace=True)
    result.rename(
        columns={
            "WK_CODE": f"{prefix}_district_code",
            "WK_NAAM": f"{prefix}_district_name",
        },
        inplace=True,
    )
    return result


def assign_residence_district(
    data: pd.DataFrame, districts: gpd.GeoDataFrame
) -> gpd.GeoDataFrame:
    """Assign residence district to each infected person in the data based on their home location."""
    return _assign_district(data, districts, "homeLon", "homeLat", "residence")


def assign_infection_district(
    data: pd.DataFrame, districts: gpd.GeoDataFrame
) -> gpd.GeoDataFrame:
    """Assign infection district to each infected person in the data based on their infection location."""
    return _assign_district(data, districts, "infectLocationLon", "infectLocationLat", "infection")


def find_files(root_dir, filename):
    """Find all files in the root directory with the given filename."""
    matching_files = []

    for dirpath, dirnames, filenames in os.walk(root_dir):
        if filename in filenames:
            matching_files.append(os.path.join(dirpath, filename))

    return matching_files
