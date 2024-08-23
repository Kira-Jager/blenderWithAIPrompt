
# Prompt:
'''write "sekou" with an animation on each letter upside down in a box'''
# Response:
import bpy
import math

bpy.ops.object.text_add()
text_obj = bpy.context.object
text_obj.data.body = "sekou"

text_obj.data.extrude = 0.1
text_obj.data.bevel_depth = 0.05
text_obj.data.bevel_resolution = 3

text_obj.rotation_euler = (math.pi, 0, 0)

bpy.ops.mesh.primitive_cube_add()
box_obj = bpy.context.object
box_obj.scale = (2, 2, 2)
box_obj.location = (0, 0, 0)

for i in range(len(text_obj.data.body)):
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.select_all(action='SELECT')
    bpy.ops.mesh.separate(type='LOOSE')
    bpy.ops.object.mode_set(mode='OBJECT')
    letter_obj = bpy.context.selected_objects[0]
    letter_obj.name = "Letter_" + str(i)
    letter_obj.location = (i * 1.5, 0, 0)

for i in range(len(text_obj.data.body)):
    letter_obj = bpy.data.objects["Letter_" + str(i)]
    letter_obj.animation_data_create()
    letter_obj.animation_data.action = bpy.data.actions.new(name="Letter_Animation_" + str(i))
    fcurve = letter_obj.animation_data.action.fcurves.new(data_path="location", index=2)
    fcurve.keyframe_points.add(2)
    fcurve.keyframe_points[0].co = (0, 0)
    fcurve.keyframe_points[1].co = (24, 2)
    fcurve.keyframe_points[0].interpolation = 'LINEAR'
    fcurve.keyframe_points[1].interpolation = 'LINEAR'

box_obj.name = "Box_sekou"

bpy.context.scene.frame_end = 24
# Prompt:
'''add 4 cube ransom in 100 * 100 plane add animation to each others to jump on the plane'''
# Response:
import bpy
import random

bpy.context.scene.frame_end = 100
plane_size = 100

bpy.ops.mesh.primitive_plane_add(size=plane_size, enter_editmode=False, location=(0, 0, 0))
plane = bpy.context.active_object

for i in range(4):
    bpy.ops.mesh.primitive_cube_add(size=2, location=(random.uniform(-plane_size/2, plane_size/2), random.uniform(-plane_size/2, plane_size/2), 2))
    cube = bpy.context.active_object
    cube.name = f"Cube_{i+1}"
    cube.data.name = f"Cube_{i+1}"

    cube.location[2] = 0
    cube.keyframe_insert(data_path="location", frame=0)
    cube.location[2] = 4
    cube.keyframe_insert(data_path="location", frame=25)
    cube.location[2] = 0
    cube.keyframe_insert(data_path="location", frame=50)
    cube.location[2] = 4
    cube.keyframe_insert(data_path="location", frame=75)