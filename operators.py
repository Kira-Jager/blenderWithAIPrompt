import bpy
import requests
from dotenv import load_dotenv
from pprint import pprint
import os
import json
import ast

# Load the API key from the .env file
load_dotenv()
GEMINI_API_KEY = os.getenv('GEMINI_TEXT_EMBEDDING_004_API_KEY')

def gather_scene_context():
    # Gather information about the current scene
    scene_context = {
        "scene_name": bpy.context.scene.name,
        "objects": []
    }
    
    # Loop through all objects in the scene
    for obj in bpy.context.scene.objects:
        obj_info = {
            "name": obj.name,
            "type": obj.type,
            "location": tuple(obj.location),
            "rotation": tuple(obj.rotation_euler),
            "scale": tuple(obj.scale)
        }
        scene_context["objects"].append(obj_info)
    
    return scene_context

def load_previous_prompts_responses(json_file_path='outputAi.json', limit=5):
    try:
        with open(json_file_path, 'r') as file:
            previous_data = json.load(file)
            if isinstance(previous_data, list):
                # Return the last 'limit' entries from the list
                return previous_data[-limit:]
            else:
                return []
    except (IOError, json.JSONDecodeError):
        return []


def prepare_gemini_prompt(prompt, scene_context, previous_prompts_responses):
    # Construct the detailed prompt with scene context and previous prompts/responses
    context_prompt = (
        f"Current scene context: {json.dumps(scene_context)}.\n\n"
        f"Previous prompts and responses: {json.dumps(previous_prompts_responses)}.\n\n"
        f"Now, generate a Blender Python script to achieve the following task: {prompt}. "
        "The script should create a 3D object in Blender and adapt the code according to the specific task described. "
        "For text objects, the script should use 'bpy.ops.object.text_add()' to add the text and directly modify the 'body' attribute of the created object. "
        "Ensure that the script is executable in Blender's scripting environment and contains only code with no comments or explanations. "
        "Avoid creating separate 'Text' data blocks unless explicitly required by the task."
        "Rename eventually the name of created object inside the outliner and the mesh"
    )
    
    return context_prompt

def send_prompt_to_gemini(prompt):
    # Construct a more detailed prompt for generating Blender Python scripts
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key={GEMINI_API_KEY}"
    data = {
        "contents": [{"parts": [{"text": prompt}]}]
    }
    
    response = requests.post(url, json=data)
    response_data = response.json()
    
    # Extract the script from the response
    script = response_data.get('candidates', [{}])[0].get('content', {}).get('parts', [{}])[0].get('text', '')
    
    # Clean up the script
    script = clean_script(script)
    
    # Verify the script
    if not verify_script(script):
        # If script is invalid, send back to Gemini for refinement
        refined_script = request_script_refinement(script, prompt)
        return refined_script
    
    return script


def clean_script(script):
    # Remove Markdown code block delimiters and unwanted comments
    cleaned_script = script.replace('```python\n', '').replace('\n```', '').strip()
    cleaned_script = '\n'.join(
        line for line in cleaned_script.splitlines() if not line.strip().startswith('#')
    ).strip()
    return cleaned_script

def verify_script(script):
    try:
        # Check if the script is valid Python code
        ast.parse(script)
        return True
    except SyntaxError:
        return False

def request_script_refinement(script, prompt):
    # Re-request a refined script from Gemini
    context_prompt = (
        "The following script does not perform the correct operation. Refine it to create a 3D object in Blender, ensuring it is executable Python code without comments or explanations:\n"
        f"{script}\n\nTask: {prompt}"
    )
    
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key={GEMINI_API_KEY}"
    data = {
        "contents": [{"parts": [{"text": context_prompt}]}]
    }
    
    response = requests.post(url, json=data)
    response_data = response.json()
    
    # Extract the refined script from the response
    refined_script = response_data.get('candidates', [{}])[0].get('content', {}).get('parts', [{}])[0].get('text', '')
    
    return clean_script(refined_script)
    # Re-request a refined script from Gemini
    

class AI_OT_SubmitPrompt(bpy.types.Operator):
    bl_idname = "ai.submit_prompt"
    bl_label = "Submit Prompt"
    bl_description = "Submit the prompt to the AI system"

    def execute(self, context):
        prompt = context.scene.ai_prompt
        
        # Gather scene context
        scene_context = gather_scene_context()
        
        # Load previous prompts and responses
        previous_prompts_responses = load_previous_prompts_responses()
        
        # Prepare the detailed prompt
        detailed_prompt = prepare_gemini_prompt(prompt, scene_context, previous_prompts_responses)
        
        self.report({'INFO'}, f"Prompt submitted: {detailed_prompt}")
        # Send the prompt to the Gemini API
        response = send_prompt_to_gemini(detailed_prompt)
        print(response)

        append_to_json_file(prompt, response)
        append_to_python_file(prompt, response)


        # Extract and execute the script if available
        # Retrieve the script from the API response
        try:
            if isinstance(response, dict):
                # Extract the script from the correct location
                script = response.get('candidates', [{}])[0].get('content', {}).get('parts', [{}])[0].get('text', '')
            else:
                # Assume response is the script itself
                script = response

            self.report({'INFO'}, "Script received from AI.")
            print(script)

            # Execute the script in Blender
            exec(script)
            self.report({'INFO'}, "Script executed successfully.")
        except KeyError as e:
            self.report({'ERROR'}, f"KeyError: {str(e)}")
        except Exception as e:
            self.report({'ERROR'}, f"Exception: {str(e)}")

        
        return {'FINISHED'}


def append_to_json_file(prompt, response):
    try:
        entry = {"prompt": prompt, "response": response}
        
        # Open the file in read mode first to load existing data
        try:
            with open('outputAi.json', 'r') as file:
                data = json.load(file)
                if not isinstance(data, list):
                    data = []
        except (IOError, json.JSONDecodeError):  # Handle file not existing or empty/invalid JSON
            data = []

        # Append the new entry to the list
        data.append(entry)
        
        # Write the updated list back to the file
        with open('outputAi.json', 'w') as file:
            json.dump(data, file, indent=4)
        
        print("Response appended to outputAi.json")
    except IOError as e:
        print(f"IOError: {str(e)}")


# Appending prompt and response to the Python file
# Appending prompt and response to the Python file
def append_to_python_file(prompt, response):
    try:
        with open('outputAi.py', 'a') as file:  # Open in append mode
            file.write('''\n# Prompt:\n''')
            file.write(f"'''{prompt}'''\n")
            file.write("# Response:\n")
            file.write(response)  # Directly write the script as Python code
        print("Response appended to outputAi.py")
    except IOError as e:
        print(f"IOError: {str(e)}")


# Register the operator in Blender
def register():
    bpy.utils.register_class(AI_OT_SubmitPrompt)

def unregister():
    bpy.utils.unregister_class(AI_OT_SubmitPrompt)
    
    
    
def print_json_pretty(json_data):
    print(json.dumps(json_data, indent=4))


if __name__ == "__main__":
    register()
