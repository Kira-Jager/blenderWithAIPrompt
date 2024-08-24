import requests
import os
from pprint import pprint
import json
from dotenv import load_dotenv


# Set the base URL for the Polyhaven API
load_dotenv()
POLYHAVEN_API_URL = os.getenv('POLYHAVEN_API_URL')
GEMINI_API_KEY = os.getenv('GEMINI_TEXT_EMBEDDING_004_API_KEY')


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

    map_list = ['Diffuse', 'Rough', 'AO']

    # Dictionary to store the paths of downloaded files
    material_paths = {}

    for map_name in map_list:
        # Get the PNG URL for each map
        png_url = get_maps(material_files, map_name, '1k')

        if png_url:
            # Create the directory to save the material if it doesn't exist
            material_dir = os.path.abspath(os.path.join(save_dir, material_name))
            if not os.path.exists(material_dir):
                os.makedirs(material_dir)

            # Define the full path for the downloaded material
            file_name = os.path.basename(png_url)
            save_file_path = os.path.abspath(os.path.join(material_dir, file_name))

            try:
                # Download the material file
                response = requests.get(png_url, stream=True)
                response.raise_for_status()

                # Write the content to the file
                with open(save_file_path, 'wb') as file:
                    for chunk in response.iter_content(chunk_size=8192):
                        file.write(chunk)

                print(f"Downloaded {map_name} for '{material_name}' and saved to '{save_file_path}'")

                # Store the path in the dictionary
                material_paths[map_name.lower()] = save_file_path
            
            except requests.exceptions.RequestException as e:
                print(f"Failed to download {map_name} for '{material_name}': {str(e)}")
        else:
            print(f"No PNG file found for {map_name} at resolution '1k'.")

    # Return the dictionary containing the absolute paths of the downloaded files
    return material_paths


# Function to save both prompt and response to a JSON file
def save_prompt_to_json(prompt, response, file_name="previous_prompts.json"):
    # try:
    #     with open(file_name, "r") as file:
    #         prompts = json.load(file)
    # except FileNotFoundError:
    #     prompts = []

    # prompts.append({"prompt": prompt, "response": response})

    with open(file_name, "w") as file:
        json.dump({"prompt": prompt, "response": response}, file, indent=4)

# Function to read previous prompts and responses from the JSON file


def load_previous_prompts(file_name="previous_prompts.json"):
    try:
        with open(file_name, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def prompt_for_materials_to_gemini(prompt):
    # Construct a more detailed prompt for generating Blender Python scripts
    print("Prompt:", prompt)
    categories = get_asset_categories("textures")
    category_list = list(categories.keys())

    previous_prompts = load_previous_prompts()
    print("previous_prompts",previous_prompts)
    # previous_categories = [entry['response'] for entry in previous_prompts]

    # Include previous categories in the prompt
    prompt_part = f'''Here is the list of categories of available materials from Polyhaven:
                    {category_list}.
                    please select the most appropriate category index for the user's request: {prompt}.
                    Return only the numeric index .
                    '''

    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key={GEMINI_API_KEY}"
    data = {
        "contents": [{"parts": [{"text": prompt_part}]}]
    }
    response = requests.post(url, json=data)
    response_data = response.json()

    # Extract the category index from the response
    category_index_text = response_data.get('candidates', [{}])[0].get(
        'content', {}).get('parts', [{}])[0].get('text', '')
    # Extracts the number
    print("category_index_text", category_index_text)
    try:
        category_index = int(category_index_text)
    except ValueError:
        print("Error: The response did not contain a valid integer index.")
        return
    print("category_index", category_index)

    # Save the prompt and response to JSON for future reference
    save_prompt_to_json(prompt, category_index)

    # Proceed if the index is valid
    if 0 <= category_index < len(category_list):
        selected_category = category_list[category_index]
        print(f"Selected category: {category_index}, {selected_category}")

        # Fetch materials in the selected category
        materials = get_materials_list("textures", selected_category)
        if materials:
            material_names = list(materials.keys())
            material_prompt = f'''Here are the previous prompts I made to ask you to choose the materials categories: {previous_prompts}. 
            Choose only one material from this list: {material_names}. The material should reflect the same idea from the previous prompt.
            Return the selection in an object format with no comment nor explanation with key index = "result".'''

            # Reprompt Gemini to choose a material
            data = {
                "contents": [{"parts": [{"text": material_prompt}]}]
            }
            material_response = requests.post(url, json=data)
            material_response_data = material_response.json()
            material_name = material_response_data.get('candidates', [{}])[0].get('content', {}).get('parts', [{}])[0].get('text', '')

            # Strip out backticks and any surrounding whitespace
            # pprint(material_response_data)
            clean_material_name = material_name.replace("```json", "").replace("```", "").strip()
            print("material_name:", clean_material_name)

            try:
                # Load the cleaned response as JSON
                material_dict = json.loads(clean_material_name)
                selected = material_dict.get('result')
                
                if selected:
                    print("selected:", selected)
                    # Download the selected material
                    material_paths = download_material(selected)
                    print(material_paths)
                    return material_paths  # Return the paths to the downloaded material assets
                    
                else:
                    print("Error: 'result' key not found in the response.")
            except json.JSONDecodeError as e:
                print(f"Error: Failed to decode the material selection response. Details: {str(e)}")
                print()
    return None  # Return None if something fails


if __name__ == "__main__":
    prompt = "add a plane size 5 with an outdor material on it  "
    prompt_for_materials_to_gemini(prompt)

# if __name__ == "__main__":
#     # fetch_filtered_materials()
#     # download_material_from_catalog("food")
#     # # Step 1: Get and display categories
#     # print("Fetching available categories...")
#     categories = get_asset_categories("textures")

#     if (categories):
#         category_list = list(categories.keys())
#         print("Available categories:")
#         for i, category in enumerate(category_list):
#             print(f"{i + 1}. {category}")

#         # Step 2: Ask the user to select a category
#         category_index = int(input("Enter the number of the category you want to use: ")) - 1

#         if 0 <= category_index < len(category_list):
#             selected_category = category_list[category_index]
#             print(f"Selected category: {selected_category}")

#             # Step 3: Fetch materials in the selected category
#             materials = get_materials_list("textures", selected_category)
#             if materials:
#                 print(f"Available materials in '{selected_category}' category:")
#                 for material_name in materials.keys():
#                     print(material_name)

#                 # Step 4: Ask the user to select a material
#                 material_name = input("Enter the name of the material you want to download: ")

#                 # Step 5: Download the selected material
#                 download_material(material_name)
#             else:
#                 print(f"No materials found in category '{selected_category}'.")
#         else:
#             print("Invalid category selected.")
#     else:
#         print("No categories available.")
