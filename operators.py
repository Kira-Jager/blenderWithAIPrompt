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

def send_prompt_to_gemini(prompt):
    # Construct a more detailed prompt for generating Blender Python scripts
    context_prompt = (
        "Generate a Blender Python script to achieve the following task: "
        f"{prompt}. The script should create a 3D object in Blender and adapt the code according to the specific task described. "
        "For text objects, the script should use 'bpy.ops.object.text_add()' to add the text and directly modify the 'body' attribute of the created object. "
        "Ensure that the script is executable in Blender's scripting environment and contains only code with no comments or explanations. "
        "Avoid creating separate 'Text' data blocks unless explicitly required by the task."
    )
    
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key={GEMINI_API_KEY}"
    data = {
        "contents": [{"parts": [{"text": context_prompt}]}]
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
        self.report({'INFO'}, f"Prompt submitted: {prompt}")

        # Send the prompt to the Gemini API
        response = send_prompt_to_gemini(prompt)
        print(response)

        # Log the full response for debugging
        # print("Full response:", response)
        
        try:
            if isinstance(response, dict):
                with open('outputAi.json', 'w') as file:
                    json.dump(response, file, indent=4)
            else:
                with open('outputAi.json', 'w') as file:
                    file.write(response)
            self.report({'INFO'}, "Response written to outputAi.json")
        except IOError as e:
            self.report({'ERROR'}, f"IOError: {str(e)}")


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

# Register the operator in Blender
def register():
    bpy.utils.register_class(AI_OT_SubmitPrompt)

def unregister():
    bpy.utils.unregister_class(AI_OT_SubmitPrompt)
    
    
    
def print_json_pretty(json_data):
    print(json.dumps(json_data, indent=4))


if __name__ == "__main__":
    register()
