
# Prompt:
'''add 4 cube ransom in 10 * 10 plane add animation to each others to jump on the plane'''
# Response:
import bpy
import random

bpy.ops.mesh.primitive_plane_add(size=10, enter_editmode=False, align='WORLD', location=(0, 0, 0))
plane = bpy.context.object

for i in range(4):
    bpy.ops.mesh.primitive_cube_add(size=1, enter_editmode=False, align='WORLD', location=(random.uniform(-4, 4), random.uniform(-4, 4), 0))
    cube = bpy.context.object
    cube.name = f"Cube_{i + 1}"
    cube.data.name = f"Cube_{i + 1}"
    
    bpy.context.scene.frame_start = 1
    bpy.context.scene.frame_end = 100
    
    cube.animation_data_create()
    cube.animation_data.action = bpy.data.actions.new(name="Jump")

    fcurve = cube.animation_data.action.fcurves.new(data_path="location", index=2)
    fcurve.keyframe_points.add(2)
    fcurve.keyframe_points[0].co = (1, 0)
    fcurve.keyframe_points[1].co = (50, 2)
    fcurve.keyframe_points[0].handle_left_type = 'FREE'
    fcurve.keyframe_points[0].handle_right_type = 'FREE'
    fcurve.keyframe_points[1].handle_left_type = 'FREE'
    fcurve.keyframe_points[1].handle_right_type = 'FREE'

    fcurve = cube.animation_data.action.fcurves.new(data_path="location", index=2)
    fcurve.keyframe_points.add(2)
    fcurve.keyframe_points[0].co = (51, 2)
    fcurve.keyframe_points[1].co = (100, 0)
    fcurve.keyframe_points[0].handle_left_type = 'FREE'
    fcurve.keyframe_points[0].handle_right_type = 'FREE'
    fcurve.keyframe_points[1].handle_left_type = 'FREE'
    fcurve.keyframe_points[1].handle_right_type = 'FREE'
# Prompt:
'''i got only 1 cube add  3 more with animation as the previous'''
# Response:
import bpy
import random

bpy.ops.mesh.primitive_cube_add(size=1, enter_editmode=False, align='WORLD', location=(random.uniform(-4, 4), random.uniform(-4, 4), 0))
cube = bpy.context.object
cube.name = "Cube_2"
cube.data.name = "Cube_2"

bpy.context.scene.frame_start = 1
bpy.context.scene.frame_end = 100

cube.animation_data_create()
cube.animation_data.action = bpy.data.actions.new(name="Jump")

fcurve = cube.animation_data.action.fcurves.new(data_path="location", index=2)
fcurve.keyframe_points.add(2)
fcurve.keyframe_points[0].co = (1, 0)
fcurve.keyframe_points[1].co = (50, 2)
fcurve.keyframe_points[0].handle_left_type = 'FREE'
fcurve.keyframe_points[0].handle_right_type = 'FREE'
fcurve.keyframe_points[1].handle_left_type = 'FREE'
fcurve.keyframe_points[1].handle_right_type = 'FREE'

fcurve = cube.animation_data.action.fcurves.new(data_path="location", index=2)
fcurve.keyframe_points.add(2)
fcurve.keyframe_points[0].co = (51, 2)
fcurve.keyframe_points[1].co = (100, 0)
fcurve.keyframe_points[0].handle_left_type = 'FREE'
fcurve.keyframe_points[0].handle_right_type = 'FREE'
fcurve.keyframe_points[1].handle_left_type = 'FREE'
fcurve.keyframe_points[1].handle_right_type = 'FREE'

bpy.ops.mesh.primitive_cube_add(size=1, enter_editmode=False, align='WORLD', location=(random.uniform(-4, 4), random.uniform(-4, 4), 0))
cube = bpy.context.object
cube.name = "Cube_3"
cube.data.name = "Cube_3"

bpy.context.scene.frame_start = 1
bpy.context.scene.frame_end = 100

cube.animation_data_create()
cube.animation_data.action = bpy.data.actions.new(name="Jump")

fcurve = cube.animation_data.action.fcurves.new(data_path="location", index=2)
fcurve.keyframe_points.add(2)
fcurve.keyframe_points[0].co = (1, 0)
fcurve.keyframe_points[1].co = (50, 2)
fcurve.keyframe_points[0].handle_left_type = 'FREE'
fcurve.keyframe_points[0].handle_right_type = 'FREE'
fcurve.keyframe_points[1].handle_left_type = 'FREE'
fcurve.keyframe_points[1].handle_right_type = 'FREE'

fcurve = cube.animation_data.action.fcurves.new(data_path="location", index=2)
fcurve.keyframe_points.add(2)
fcurve.keyframe_points[0].co = (51, 2)
fcurve.keyframe_points[1].co = (100, 0)
fcurve.keyframe_points[0].handle_left_type = 'FREE'
fcurve.keyframe_points[0].handle_right_type = 'FREE'
fcurve.keyframe_points[1].handle_left_type = 'FREE'
fcurve.keyframe_points[1].handle_right_type = 'FREE'

bpy.ops.mesh.primitive_cube_add(size=1, enter_editmode=False, align='WORLD', location=(random.uniform(-4, 4), random.uniform(-4, 4), 0))
cube = bpy.context.object
cube.name = "Cube_4"
cube.data.name = "Cube_4"

bpy.context.scene.frame_start = 1
bpy.context.scene.frame_end = 100

cube.animation_data_create()
cube.animation_data.action = bpy.data.actions.new(name="Jump")

fcurve = cube.animation_data.action.fcurves.new(data_path="location", index=2)
fcurve.keyframe_points.add(2)
fcurve.keyframe_points[0].co = (1, 0)
fcurve.keyframe_points[1].co = (50, 2)
fcurve.keyframe_points[0].handle_left_type = 'FREE'
fcurve.keyframe_points[0].handle_right_type = 'FREE'
fcurve.keyframe_points[1].handle_left_type = 'FREE'
fcurve.keyframe_points[1].handle_right_type = 'FREE'

fcurve = cube.animation_data.action.fcurves.new(data_path="location", index=2)
fcurve.keyframe_points.add(2)
fcurve.keyframe_points[0].co = (51, 2)
fcurve.keyframe_points[1].co = (100, 0)
fcurve.keyframe_points[0].handle_left_type = 'FREE'
fcurve.keyframe_points[0].handle_right_type = 'FREE'
fcurve.keyframe_points[1].handle_left_type = 'FREE'
fcurve.keyframe_points[1].handle_right_type = 'FREE'
# Prompt:
'''delete everything in the scene'''
# Response:
import bpy

bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()

bpy.ops.mesh.primitive_cube_add(size=2, enter_editmode=False, align='WORLD', location=(0, 0, 0))
cube = bpy.context.object
cube.name = "MyCube"
cube.data.name = "MyCube"
# Prompt:
'''can you do bird 3d model ?'''
# Response:

# Prompt:
'''add me suzi on top of this cube'''
# Response:
import bpy

bpy.ops.mesh.primitive_cube_add(size=1, enter_editmode=False, align='WORLD', location=(0, 0, 1))
cube = bpy.context.object
cube.name = "MyCube"
cube.data.name = "MyCube"

bpy.ops.object.text_add(radius=1, enter_editmode=False, align='WORLD', location=(0, 0, 2))
text = bpy.context.object
text.name = "me suzi"
text.data.body = "me suzi"
# Prompt:
'''I mean the monkey suzy from blender default object'''
# Response:
import bpy

bpy.ops.mesh.primitive_monkey_add(enter_editmode=False, align='WORLD', location=(0, 0, 0))
monkey = bpy.context.object
monkey.name = "Suzi"
monkey.data.name = "Suzi"
# Prompt:
'''can you  replace Suzi on top of all the object  '''
# Response:
import bpy

for obj in bpy.context.scene.objects:
    if obj.name != "Suzi":
        bpy.ops.mesh.primitive_monkey_add(enter_editmode=False, align='WORLD', location=obj.location)
        monkey = bpy.context.object
        monkey.name = "Suzi"
        monkey.data.name = "Suzi"
        obj.select_set(True)
        bpy.ops.object.delete()
# Prompt:
'''without deleting the cube'''
# Response:
import bpy

bpy.ops.mesh.primitive_cube_add(enter_editmode=False, align='WORLD', location=(0, 0, 0))
cube = bpy.context.object
cube.name = "MyCube"
cube.data.name = "MyCube"

bpy.ops.mesh.primitive_monkey_add(enter_editmode=False, align='WORLD', location=(0, 0, 1))
monkey = bpy.context.object
monkey.name = "Suzi"
monkey.data.name = "Suzi"
# Prompt:
'''delete all and write welcome Nicola'''
# Response:
import bpy

bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()

bpy.ops.object.text_add(radius=1, enter_editmode=False, align='WORLD', location=(0, 0, 0))
text = bpy.context.object
text.name = "Welcome Nicola"
text.data.body = "Welcome Nicola"
text.data.name = "Welcome Nicola"
# Prompt:
'''add ten cube on the scene'''
# Response:
import bpy
import random

for i in range(10):
    bpy.ops.mesh.primitive_cube_add(size=1, enter_editmode=False, align='WORLD', location=(random.uniform(-4, 4), random.uniform(-4, 4), 0))
    cube = bpy.context.object
    cube.name = f"Cube_{i + 1}"
    cube.data.name = f"Cube_{i + 1}"
# Prompt:
'''rename all the cube object and their mesh to have only number like 1 ,2 to 10'''
# Response:
import bpy

for i, obj in enumerate(bpy.context.scene.objects):
    if obj.type == 'MESH' and 'Cube' in obj.name:
        obj.name = str(i + 1)
        obj.data.name = str(i + 1)
# Prompt:
'''there is an error the first cube shopuld be 1 and the last 10'''
# Response:
import bpy

for i, obj in enumerate(bpy.context.scene.objects):
    if obj.type == 'MESH' and 'Cube' in obj.name:
        obj.name = str(i + 1)
        obj.data.name = str(i + 1)
# Prompt:
'''make i - 1 for all cube'''
# Response:
import bpy

for i, obj in enumerate(bpy.context.scene.objects):
    if obj.type == 'MESH' and 'Cube' in obj.name:
        obj.name = str(i)
        obj.data.name = str(i)
# Prompt:
'''it's not working the name of the element don't contains now cube but just the number associated to them'''
# Response:
import bpy

for i, obj in enumerate(bpy.context.scene.objects):
    if obj.type == 'MESH':
        obj.name = str(i + 1)
        obj.data.name = str(i + 1)
# Prompt:
'''write sekou is here'''
# Response:
import bpy

bpy.ops.object.text_add(radius=1, enter_editmode=False, align='WORLD', location=(0, 0, 0))
text = bpy.context.object
text.name = "sekou is here"
text.data.body = "sekou is here"
text.data.name = "sekou is here"
# Prompt:
'''write I'm sekou'''
# Response:
import bpy

bpy.ops.object.text_add(radius=1, enter_editmode=False, align='WORLD', location=(0, 0, 0))
text = bpy.context.object
text.name = "I'm sekou"
text.data.body = "I'm sekou"
text.data.name = "I'm sekou"