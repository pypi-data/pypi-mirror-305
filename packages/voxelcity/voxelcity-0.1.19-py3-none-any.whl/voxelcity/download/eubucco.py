import requests
import zipfile
import os
import geopandas as gpd
from io import BytesIO

from ..geo.utils import get_country_name
from ..file.geojson import filter_and_convert_gdf_to_geojson

country_links = {
        "Austria": "https://api.eubucco.com/v0.1/files/5e63fc15-b602-474b-a618-43080fa49db4/download",
        "Belgium": "https://api.eubucco.com/v0.1/files/08b81844-f46d-403b-bbd0-871fc5017b62/download",
        "Bulgaria": "https://api.eubucco.com/v0.1/files/4d0c2559-a3ec-4aea-bd56-e87d0261f5e5/download",
        "Croatia": "https://api.eubucco.com/v0.1/files/3638edd8-85af-4244-8208-128eedc85dcf/download",
        "Cyprus": "https://api.eubucco.com/v0.1/files/bee810d8-d4eb-4ddc-abf9-86d5247e05cf/download",
        "Czechia": "https://api.eubucco.com/v0.1/files/a130fd04-5d8c-4ea5-8383-62019cbec87f/download",
        "Czechia Other-license": "https://api.eubucco.com/v0.1/files/d044e347-7106-4516-811e-b340deac2041/download",
        "Denmark": "https://api.eubucco.com/v0.1/files/dc11a549-15db-4855-876d-ff3dfc401f76/download",
        "Estonia": "https://api.eubucco.com/v0.1/files/021d17ba-49a1-42e6-ae0b-fe73e8f02efb/download",
        "Finland": "https://api.eubucco.com/v0.1/files/c3131458-d835-4a22-8203-7d6367ae6f8f/download",
        "France": "https://api.eubucco.com/v0.1/files/0602abfe-d522-4683-a792-4dc4143a23fa/download",
        "Germany": "https://api.eubucco.com/v0.1/files/90148cbc-5bb1-4d1c-9935-8572a2a8c609/download",
        "Greece": "https://api.eubucco.com/v0.1/files/8d43e4c4-9e03-4ef1-b8c3-7bbb2ac23f4a/download",
        "Hungary": "https://api.eubucco.com/v0.1/files/bc0f8941-1b68-4c1c-9219-424c0d56d55a/download",
        "Ireland": "https://api.eubucco.com/v0.1/files/f580d806-9b32-4d1c-93ef-a4ff49889d56/download",
        "Italy": "https://api.eubucco.com/v0.1/files/e987077e-5c72-4903-a0d8-20ef8b9016de/download",
        "Italy Other-license": "https://api.eubucco.com/v0.1/files/d5a8e03f-0397-4f89-bcdd-a4bc61352ef6/download",
        "Latvia": "https://api.eubucco.com/v0.1/files/b7b3efdc-c9e1-4b70-bc81-2c4291cbdf8e/download",
        "Lithuania": "https://api.eubucco.com/v0.1/files/28862c49-25fe-4019-8c6b-cbad18d1c090/download",
        "Luxembourg": "https://api.eubucco.com/v0.1/files/0045dd6d-a2e0-4439-91c4-722856682cd6/download",
        "Malta": "https://api.eubucco.com/v0.1/files/2b4ecf81-365e-4a9b-91f6-70838c52487d/download",
        "Netherlands": "https://api.eubucco.com/v0.1/files/9f95ccbc-a095-4495-916c-6ea932f3ae10/download",
        "Poland": "https://api.eubucco.com/v0.1/files/6e8ea7fc-afcb-42b9-adbe-e12fa24048a7/download",
        "Portugal": "https://api.eubucco.com/v0.1/files/5d079772-5dd5-4dfc-95d2-393ca8edaa68/download",
        "Romania": "https://api.eubucco.com/v0.1/files/41cb29ed-e778-4b5b-807e-917ac93d48ca/download",
        "Slovakia": "https://api.eubucco.com/v0.1/files/17f71454-e4c4-41e8-b3ee-20b957abf546/download",
        "Slovenia": "https://api.eubucco.com/v0.1/files/e120065e-d6c2-42c6-b136-588072954e51/download",
        "Spain": "https://api.eubucco.com/v0.1/files/34dd019b-871f-443e-9b5d-61c29f8cb92c/download",
        "Sweden": "https://api.eubucco.com/v0.1/files/46fb09cc-38a9-46c0-bce2-d159e4b62963/download",
        "Switzerland": "https://api.eubucco.com/v0.1/files/1f4b7797-6e1e-44ab-a281-95d575360c9a/download",
}

def download_extract_open_gpkg(url):
    # Download the file
    print("Downloading file...")
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Failed to download file. Status code: {response.status_code}")

    # Extract the ZIP file
    print("Extracting ZIP file...")
    with zipfile.ZipFile(BytesIO(response.content)) as zip_ref:
        zip_ref.extractall("extracted_files")

    # Find the GPKG file
    gpkg_file = None
    for root, dirs, files in os.walk("extracted_files"):
        for file in files:
            if file.endswith(".gpkg"):
                gpkg_file = os.path.join(root, file)
                break
        if gpkg_file:
            break

    if not gpkg_file:
        raise Exception("No GPKG file found in the extracted files.")

    # Open and read the GPKG file
    print(f"Opening GPKG file: {gpkg_file}")
    gdf = gpd.read_file(gpkg_file)

    # Display basic information
    print("\nDataFrame Info:")
    print(gdf.info())

    print("\nFirst few rows:")
    print(gdf.head())

    return gdf

def load_geojson_from_eubucco(rectangle_vertices):
    country_name = get_country_name(rectangle_vertices[0][0], rectangle_vertices[0][1])
    if country_name in country_links:
        url = country_links[country_name]
    else:
        print("Your target area does not have data in EUBUCCO.")
        return None
    gdf = download_extract_open_gpkg(url)
    geojson = filter_and_convert_gdf_to_geojson(gdf, rectangle_vertices)
    return geojson