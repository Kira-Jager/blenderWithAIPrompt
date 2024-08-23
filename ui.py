import bpy

class AI_PT_Panel(bpy.types.Panel):
    bl_label = "AI Prompt"
    bl_idname = "AI_PT_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'AI'

    def draw(self, context):
        layout = self.layout
        layout.label(text="Enter your prompt:")
        
        
        # Text box for user input
        layout.prop(context.scene, "ai_prompt", text="Prompt", slider=True)
        
        # Button to submit the prompt
        layout.operator("ai.submit_prompt", text="Send")
