import requests
import os
from pprint import pprint
import json

# Set the base URL for the Polyhaven API
POLYHAVEN_API_URL = "https://api.polyhaven.com"

def get_asset_categories(asset_type="textures"):
    """Fetch the list of available categories for a specific asset type."""
    try:
        response = requests.get(f"{POLYHAVEN_API_URL}/categories/{asset_type}")
        response.raise_for_status()
        categories = response.json()
        return categories
    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch categories: {str(e)}")
        return {}

def get_materials_list(asset_type="textures", category=None):
    """Fetch the list of available materials, optionally filtered by category."""
    try:
        url = f"{POLYHAVEN_API_URL}/assets?type={asset_type}"
        if category:
            url += f"&categories={category}"
        response = requests.get(url)
        response.raise_for_status()
        materials = response.json()
        return materials
    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch materials list: {str(e)}")
        return {}

def get_material_files(material_id):
    """Fetch the available files for a specific material."""
    try:
        response = requests.get(f"{POLYHAVEN_API_URL}/files/{material_id}")
        response.raise_for_status()
        files = response.json()
        # print("material",files)
        return files
    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch material files: {str(e)}")
        return {}

# def getMaps(material_files, map_name, resolution):
#     maps = material_files[map_name]
#     if maps[resolution]:
#         pngInfo = maps[resolution]['png']
#         pngUrl = pngInfo['url']
#         print(f'url_{map_name}', pngUrl)

# def download_material(material_name, save_dir='materials'):
#     """Download a specific material by name and print PNG URLs for Diffuse maps."""
#     # Get the list of materials
#     materials = get_materials_list()

#     # Find the material by name
#     material_info = materials.get(material_name)
#     map_list = ['Diffuse','Rough','Displacement','AO']    
#     # Fetch the files for the material using its ID
#     material_id = material_name
#     material_files = get_material_files(material_id)
    
#     for map in map_list:
#     # pprint(material_files)
#         getMaps(material_files, map,'2k')

def get_maps(material_files, map_name, resolution):
    """Extract the PNG URL for a specific map and resolution."""
    maps = material_files.get(map_name)
    if maps and resolution in maps:
        png_info = maps[resolution].get('png')
        if png_info:
            return png_info['url']
    return None

def download_material(material_name, save_dir='materials'):
    """Download the PNG files for the specified maps in their dedicated directories with the material name."""
    # Get the list of materials
    materials = get_materials_list()

    # Find the material by name
    material_info = materials.get(material_name)
    
    # Fetch the files for the material using its ID
    material_id = material_name
    material_files = get_material_files(material_id)
    
    map_list = ['Diffuse', 'Rough', 'Displacement', 'AO']    
    
    for map_name in map_list:
        # Get the PNG URL for each map
        png_url = get_maps(material_files, map_name, '2k')
        
        if png_url:
            # Create the directory to save the material if it doesn't exist
            material_dir = os.path.join(save_dir, material_name)
            if not os.path.exists(material_dir):
                os.makedirs(material_dir)
            
            # Define the full path for the downloaded material
            file_name = os.path.basename(png_url)
            save_file_path = os.path.join(material_dir, file_name)
            
            try:
                # Download the material file
                response = requests.get(png_url, stream=True)
                response.raise_for_status()
                
                # Write the content to the file
                with open(save_file_path, 'wb') as file:
                    for chunk in response.iter_content(chunk_size=8192):
                        file.write(chunk)
                
                print(f"Downloaded {map_name} for '{material_name}' and saved to '{save_file_path}'")
            except requests.exceptions.RequestException as e:
                print(f"Failed to download {map_name} for '{material_name}': {str(e)}")
        else:
            print(f"No PNG file found for {map_name} at resolution '2k'.")
            
# def fetch_filtered_materials():
#     url = f"{POLYHAVEN_API_URL}/assets?type=textures"
#     try:
#         response = requests.get(url)
#         response.raise_for_status()
#         materials = response.json()
        
#         mat_unique_ids = list(materials.keys())

#         # Save the unique IDs to a JSON file
#         with open('mat_unique_ids.json', 'w') as json_file:
#             json.dump(mat_unique_ids, json_file, indent=4)

#         print("Unique IDs file created successfully.")

#         filtered_materials = {}
#         for material_id, material_data in materials.items():
#             filtered_materials[material_id] = {
#                 "categories": material_data.get("categories", []),
#                 "tags": material_data.get("tags", [])
#             }

#         with open('filtered_materials_catalog.json', 'w') as json_file:
#             json.dump(filtered_materials, json_file, indent=4)
#         print("Filtered materials catalog created successfully.")
#     except requests.exceptions.RequestException as e:
#         print(f"Failed to fetch materials: {str(e)}")

# def download_material_from_catalog(material_name, save_dir='materials'):
#     """Download the PNG files for the specified maps using the catalog metadata."""
#     # Load the catalog JSON file
#     with open('materials_catalog.json', 'r') as file:
#         materials_catalog = json.load(file)
    
#     # Find the material metadata by name
#     material_metadata = materials_catalog.get(material_name)
#     if not material_metadata:
#         print(f"Material '{material_name}' not found in catalog.")
#         return

#     # Fetch the material files using its ID
#     material_files = get_material_files(material_name)  # Assuming material_id is same as material_name
    
#     # Define the maps you want to download
#     map_list = ['Diffuse', 'Rough', 'Displacement', 'AO']
    
#     for map_name in map_list:
#         # Get the PNG URL for each map
#         png_url = get_maps(material_files, map_name, '2k')
        
#         if png_url:
#             # Create the directory to save the material if it doesn't exist
#             material_dir = os.path.join(save_dir, material_name)
#             if not os.path.exists(material_dir):
#                 os.makedirs(material_dir)
            
#             # Define the full path for the downloaded material
#             file_name = os.path.basename(png_url)
#             save_file_path = os.path.join(material_dir, file_name)
            
#             try:
#                 # Download the material file
#                 response = requests.get(png_url, stream=True)
#                 response.raise_for_status()
                
#                 # Write the content to the file
#                 with open(save_file_path, 'wb') as file:
#                     for chunk in response.iter_content(chunk_size=8192):
#                         file.write(chunk)
                
#                 print(f"Downloaded {map_name} for '{material_name}' and saved to '{save_file_path}'")
#             except requests.exceptions.RequestException as e:
#                 print(f"Failed to download {map_name} for '{material_name}': {str(e)}")
#         else:
#             print(f"No PNG file found for {map_name} at resolution '2k'.")


if __name__ == "__main__":
    # fetch_filtered_materials()
    # download_material_from_catalog("food")
    # # Step 1: Get and display categories
    # print("Fetching available categories...")
    categories = get_asset_categories("textures")
    
    if (categories):
        category_list = list(categories.keys())
        print("Available categories:")
        for i, category in enumerate(category_list):
            print(f"{i + 1}. {category}")
        
        # Step 2: Ask the user to select a category
        category_index = int(input("Enter the number of the category you want to use: ")) - 1
        
        if 0 <= category_index < len(category_list):
            selected_category = category_list[category_index]
            print(f"Selected category: {selected_category}")
            
            # Step 3: Fetch materials in the selected category
            materials = get_materials_list("textures", selected_category)
            if materials:
                print(f"Available materials in '{selected_category}' category:")
                for material_name in materials.keys():
                    print(material_name)
                
                # Step 4: Ask the user to select a material
                material_name = input("Enter the name of the material you want to download: ")
                
                # Step 5: Download the selected material
                download_material(material_name)
            else:
                print(f"No materials found in category '{selected_category}'.")
        else:
            print("Invalid category selected.")
    else:
        print("No categories available.")
