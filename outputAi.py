
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
# Prompt:
'''add a cube size 3 and add to it an herringbone materials'''
# Response:
import bpy

bpy.ops.mesh.primitive_cube_add(size=3, enter_editmode=False, location=(0, 0, 0))
cube = bpy.context.object
cube.name = "HerringboneCube"
cube.data.name = "HerringboneCube"

material = bpy.data.materials.new(name="HerringboneMaterial")
material.use_nodes = True
material_output = material.node_tree.nodes["Material Output"]
principled_bsdf = material.node_tree.nodes["Principled BSDF"]
material.node_tree.links.new(principled_bsdf.outputs["BSDF"], material_output.inputs["Surface"])

image_texture = material.node_tree.nodes.new("ShaderNodeTexImage")
image_texture.image = bpy.data.images.load("path/to/your/herringbone.png")  # Replace with the actual path to your image

material.node_tree.links.new(image_texture.outputs["Color"], principled_bsdf.inputs["Base Color"])
# Prompt:
'''add a cube of size with an herringbone materials to it'''
# Response:
import bpy

bpy.ops.mesh.primitive_cube_add(size=3, enter_editmode=False, location=(0, 0, 0))
cube = bpy.context.object
cube.name = "HerringboneCube"
cube.data.name = "HerringboneCube"

material = bpy.data.materials.new(name="HerringboneMaterial")
material.use_nodes = True
material_output = material.node_tree.nodes["Material Output"]
principled_bsdf = material.node_tree.nodes["Principled BSDF"]
material.node_tree.links.new(principled_bsdf.outputs["BSDF"], material_output.inputs["Surface"])

image_texture = material.node_tree.nodes.new("ShaderNodeTexImage")
image_texture.image = bpy.data.images.load("materials\\grey_plaster_02\\grey_plaster_02_diff_2k.png")

material.node_tree.links.new(image_texture.outputs["Color"], principled_bsdf.inputs["Base Color"])
# Prompt:
'''add a plane with an herringbone material'''
# Response:
import bpy

bpy.ops.mesh.primitive_plane_add(size=2, enter_editmode=False, location=(0, 0, 0))
plane = bpy.context.object
plane.name = "HerringbonePlane"
plane.data.name = "HerringbonePlane"

material = bpy.data.materials.new(name="HerringboneMaterial")
material.use_nodes = True
material_output = material.node_tree.nodes["Material Output"]
principled_bsdf = material.node_tree.nodes["Principled BSDF"]
material.node_tree.links.new(principled_bsdf.outputs["BSDF"], material_output.inputs["Surface"])

image_texture = material.node_tree.nodes.new("ShaderNodeTexImage")
image_texture.image = bpy.data.images.load("D:\\Sekou\\OwnWork\\BlenderGpt\\materials\\cobblestone_floor_001\\cobblestone_floor_001_diff_2k.png")

material.node_tree.links.new(image_texture.outputs["Color"], principled_bsdf.inputs["Base Color"])
plane.data.materials.append(material)
# Prompt:
'''add a plane size 4 with a floor herringbone material '''
# Response:
import bpy

bpy.ops.mesh.primitive_plane_add(size=4, enter_editmode=False, location=(0, 0, 0))
plane = bpy.context.object
plane.name = "HerringbonePlane"
plane.data.name = "HerringbonePlane"

material = bpy.data.materials.new(name="HerringboneMaterial")
material.use_nodes = True
material_output = material.node_tree.nodes["Material Output"]
principled_bsdf = material.node_tree.nodes["Principled BSDF"]
material.node_tree.links.new(principled_bsdf.outputs["BSDF"], material_output.inputs["Surface"])

plane.data.materials.append(material)
# Prompt:
'''add a plane size 4 with a floor herringbone material '''
# Response:
import bpy

bpy.ops.mesh.primitive_plane_add(size=4, enter_editmode=False, location=(0, 0, 0))
plane = bpy.context.object
plane.name = "HerringbonePlane"
plane.data.name = "HerringbonePlane"

material = bpy.data.materials.new(name="HerringboneMaterial")
material.use_nodes = True
material_output = material.node_tree.nodes["Material Output"]
principled_bsdf = material.node_tree.nodes["Principled BSDF"]
material.node_tree.links.new(principled_bsdf.outputs["BSDF"], material_output.inputs["Surface"])

plane.data.materials.append(material)
# Prompt:
'''add a plane size 5 with an outdor material on it'''
# Response:
import bpy

bpy.ops.mesh.primitive_plane_add(size=5, enter_editmode=False, location=(0, 0, 0))
plane = bpy.context.object
plane.name = "OutdoorPlane"
plane.data.name = "OutdoorPlane"

material = bpy.data.materials.new(name="OutdoorMaterial")
material.use_nodes = True
material_output = material.node_tree.nodes["Material Output"]
principled_bsdf = material.node_tree.nodes["Principled BSDF"]
material.node_tree.links.new(principled_bsdf.outputs["BSDF"], material_output.inputs["Surface"])

plane.data.materials.append(material)
# Prompt:
'''add a plane size 5 with an outdor material on it'''
# Response:
import bpy

bpy.ops.mesh.primitive_plane_add(size=5, enter_editmode=False, location=(0, 0, 0))
plane = bpy.context.object
plane.name = "OutdoorPlane"
plane.data.name = "OutdoorPlane"

material = bpy.data.materials.new(name="OutdoorMaterial")
material.use_nodes = True
material_output = material.node_tree.nodes["Material Output"]
principled_bsdf = material.node_tree.nodes["Principled BSDF"]
material.node_tree.links.new(principled_bsdf.outputs["BSDF"], material_output.inputs["Surface"])

plane.data.materials.append(material)
# Prompt:
'''add a plane size 5 with an outdor material on it'''
# Response:
import bpy

bpy.ops.mesh.primitive_plane_add(size=5, enter_editmode=False, location=(0, 0, 0))
plane = bpy.context.object
plane.name = "OutdoorPlane"
plane.data.name = "OutdoorPlane"

material = bpy.data.materials.new(name="OutdoorMaterial")
material.use_nodes = True
material_output = material.node_tree.nodes["Material Output"]
principled_bsdf = material.node_tree.nodes["Principled BSDF"]
material.node_tree.links.new(principled_bsdf.outputs["BSDF"], material_output.inputs["Surface"])

plane.data.materials.append(material)
# Prompt:
'''add a plane size 5 with an outdor material on it'''
# Response:
import bpy

bpy.ops.mesh.primitive_plane_add(size=5, enter_editmode=False, location=(0, 0, 0))
plane = bpy.context.object
plane.name = "OutdoorPlane"
plane.data.name = "OutdoorPlane"

material = bpy.data.materials.new(name="OutdoorMaterial")
material.use_nodes = True
material_output = material.node_tree.nodes["Material Output"]
principled_bsdf = material.node_tree.nodes["Principled BSDF"]
material.node_tree.links.new(principled_bsdf.outputs["BSDF"], material_output.inputs["Surface"])

diffuse_texture = bpy.data.images.new("DiffuseTexture", 2048, 2048)
diffuse_texture.filepath = "D:\\Sekou\\OwnWork\\BlenderGpt\\materials\\aerial_grass_rock\\aerial_grass_rock_diff_2k.png"
diffuse_texture.file_format = 'PNG'
diffuse_texture.colorspace_settings.name = 'sRGB'

rough_texture = bpy.data.images.new("RoughTexture", 2048, 2048)
rough_texture.filepath = "D:\\Sekou\\OwnWork\\BlenderGpt\\materials\\aerial_grass_rock\\aerial_grass_rock_rough_2k.png"
rough_texture.file_format = 'PNG'
rough_texture.colorspace_settings.name = 'Non-Color'

displacement_texture = bpy.data.images.new("DisplacementTexture", 2048, 2048)
displacement_texture.filepath = "D:\\Sekou\\OwnWork\\BlenderGpt\\materials\\aerial_grass_rock\\aerial_grass_rock_disp_2k.png"
displacement_texture.file_format = 'PNG'
displacement_texture.colorspace_settings.name = 'Non-Color'

ao_texture = bpy.data.images.new("AOTexture", 2048, 2048)
ao_texture.filepath = "D:\\Sekou\\OwnWork\\BlenderGpt\\materials\\aerial_grass_rock\\aerial_grass_rock_ao_2k.png"
ao_texture.file_format = 'PNG'
ao_texture.colorspace_settings.name = 'Non-Color'

diffuse_node = material.node_tree.nodes.new("ShaderNodeTexImage")
diffuse_node.image = diffuse_texture

rough_node = material.node_tree.nodes.new("ShaderNodeTexImage")
rough_node.image = rough_texture

displacement_node = material.node_tree.nodes.new("ShaderNodeTexImage")
displacement_node.image = displacement_texture

ao_node = material.node_tree.nodes.new("ShaderNodeTexImage")
ao_node.image = ao_texture

material.node_tree.links.new(diffuse_node.outputs["Color"], principled_bsdf.inputs["Base Color"])
material.node_tree.links.new(rough_node.outputs["Color"], principled_bsdf.inputs["Roughness"])
material.node_tree.links.new(displacement_node.outputs["Color"], principled_bsdf.inputs["Displacement"])
material.node_tree.links.new(ao_node.outputs["Color"], principled_bsdf.inputs["Ambient Occlusion"])

plane.data.materials.append(material)
# Prompt:
'''add a plane size 5 with an outdor material on it'''
# Response:
import bpy

bpy.ops.mesh.primitive_plane_add(size=5, enter_editmode=False, location=(0, 0, 0))
plane = bpy.context.object
plane.name = "OutdoorPlane"
plane.data.name = "OutdoorPlane"

material = bpy.data.materials.new(name="OutdoorMaterial")
material.use_nodes = True
material_output = material.node_tree.nodes["Material Output"]
principled_bsdf = material.node_tree.nodes["Principled BSDF"]
material.node_tree.links.new(principled_bsdf.outputs["BSDF"], material_output.inputs["Surface"])

diffuse_texture = bpy.data.images.new("DiffuseTexture", 1024, 1024)
diffuse_texture.filepath = "D:\\Sekou\\OwnWork\\BlenderGpt\\materials\\aerial_grass_rock\\aerial_grass_rock_diff_1k.png"
diffuse_texture.file_format = 'PNG'
diffuse_texture.colorspace_settings.name = 'sRGB'

rough_texture = bpy.data.images.new("RoughTexture", 1024, 1024)
rough_texture.filepath = "D:\\Sekou\\OwnWork\\BlenderGpt\\materials\\aerial_grass_rock\\aerial_grass_rock_rough_1k.png"
rough_texture.file_format = 'PNG'
rough_texture.colorspace_settings.name = 'Non-Color'

ao_texture = bpy.data.images.new("AOTexture", 1024, 1024)
ao_texture.filepath = "D:\\Sekou\\OwnWork\\BlenderGpt\\materials\\aerial_grass_rock\\aerial_grass_rock_ao_1k.png"
ao_texture.file_format = 'PNG'
ao_texture.colorspace_settings.name = 'Non-Color'

diffuse_node = material.node_tree.nodes.new("ShaderNodeTexImage")
diffuse_node.image = diffuse_texture

rough_node = material.node_tree.nodes.new("ShaderNodeTexImage")
rough_node.image = rough_texture

ao_node = material.node_tree.nodes.new("ShaderNodeTexImage")
ao_node.image = ao_texture

material.node_tree.links.new(diffuse_node.outputs["Color"], principled_bsdf.inputs["Base Color"])
material.node_tree.links.new(rough_node.outputs["Color"], principled_bsdf.inputs["Roughness"])
material.node_tree.links.new(ao_node.outputs["Color"], principled_bsdf.inputs["Ambient Occlusion"])

plane.data.materials.append(material)
# Prompt:
'''add a plane size 5 with an outdor material on it'''
# Response:
import bpy

bpy.ops.mesh.primitive_plane_add(size=5, enter_editmode=False, location=(0, 0, 0))
plane = bpy.context.object
plane.name = "OutdoorPlane"
plane.data.name = "OutdoorPlane"

material = bpy.data.materials.new(name="OutdoorMaterial")
material.use_nodes = True
material_output = material.node_tree.nodes["Material Output"]
principled_bsdf = material.node_tree.nodes["Principled BSDF"]
material.node_tree.links.new(principled_bsdf.outputs["BSDF"], material_output.inputs["Surface"])

diffuse_texture = bpy.data.images.new("DiffuseTexture", 1024, 1024)
diffuse_texture.filepath = "D:\\Sekou\\OwnWork\\BlenderGpt\\materials\\aerial_ground_rock\\aerial_ground_rock_diff_1k.png"
diffuse_texture.file_format = 'PNG'
diffuse_texture.colorspace_settings.name = 'sRGB'

rough_texture = bpy.data.images.new("RoughTexture", 1024, 1024)
rough_texture.filepath = "D:\\Sekou\\OwnWork\\BlenderGpt\\materials\\aerial_ground_rock\\aerial_ground_rock_rough_1k.png"
rough_texture.file_format = 'PNG'
rough_texture.colorspace_settings.name = 'Non-Color'

ao_texture = bpy.data.images.new("AOTexture", 1024, 1024)
ao_texture.filepath = "D:\\Sekou\\OwnWork\\BlenderGpt\\materials\\aerial_ground_rock\\aerial_ground_rock_ao_1k.png"
ao_texture.file_format = 'PNG'
ao_texture.colorspace_settings.name = 'Non-Color'

diffuse_node = material.node_tree.nodes.new("ShaderNodeTexImage")
diffuse_node.image = diffuse_texture

rough_node = material.node_tree.nodes.new("ShaderNodeTexImage")
rough_node.image = rough_texture

ao_node = material.node_tree.nodes.new("ShaderNodeTexImage")
ao_node.image = ao_texture

mix_node = material.node_tree.nodes.new("ShaderNodeMixRGB")
mix_node.blend_type = 'MULTIPLY'

material.node_tree.links.new(diffuse_node.outputs["Color"], mix_node.inputs[1])
material.node_tree.links.new(ao_node.outputs["Color"], mix_node.inputs[2])
material.node_tree.links.new(mix_node.outputs["Color"], principled_bsdf.inputs["Base Color"])
material.node_tree.links.new(rough_node.outputs["Color"], principled_bsdf.inputs["Roughness"])

plane.data.materials.append(material)
# Prompt:
'''add a cube with herringbone materials'''
# Response:
import bpy

bpy.ops.mesh.primitive_cube_add(size=1, enter_editmode=False, location=(0, 0, 0))
cube = bpy.context.object
cube.name = "HerringboneCube"
cube.data.name = "HerringboneCube"

material = bpy.data.materials.new(name="HerringboneMaterial")
material.use_nodes = True
material_output = material.node_tree.nodes["Material Output"]
principled_bsdf = material.node_tree.nodes["Principled BSDF"]
material.node_tree.links.new(principled_bsdf.outputs["BSDF"], material_output.inputs["Surface"])

diffuse_texture = bpy.data.images.new("DiffuseTexture", 1024, 1024)
diffuse_texture.filepath = "D:\\Sekou\\OwnWork\\BlenderGpt\\materials\\cobblestone_floor_01\\cobblestone_floor_01_diff_1k.png"
diffuse_texture.file_format = 'PNG'
diffuse_texture.colorspace_settings.name = 'sRGB'

rough_texture = bpy.data.images.new("RoughTexture", 1024, 1024)
rough_texture.filepath = "D:\\Sekou\\OwnWork\\BlenderGpt\\materials\\cobblestone_floor_01\\cobblestone_floor_01_rough_1k.png"
rough_texture.file_format = 'PNG'
rough_texture.colorspace_settings.name = 'Non-Color'

ao_texture = bpy.data.images.new("AOTexture", 1024, 1024)
ao_texture.filepath = "D:\\Sekou\\OwnWork\\BlenderGpt\\materials\\cobblestone_floor_01\\cobblestone_floor_01_ao_1k.png"
ao_texture.file_format = 'PNG'
ao_texture.colorspace_settings.name = 'Non-Color'

diffuse_node = material.node_tree.nodes.new("ShaderNodeTexImage")
diffuse_node.image = diffuse_texture

rough_node = material.node_tree.nodes.new("ShaderNodeTexImage")
rough_node.image = rough_texture

ao_node = material.node_tree.nodes.new("ShaderNodeTexImage")
ao_node.image = ao_texture

mix_node = material.node_tree.nodes.new("ShaderNodeMixRGB")
mix_node.blend_type = 'MULTIPLY'

material.node_tree.links.new(diffuse_node.outputs["Color"], mix_node.inputs[1])
material.node_tree.links.new(ao_node.outputs["Color"], mix_node.inputs[2])
material.node_tree.links.new(mix_node.outputs["Color"], principled_bsdf.inputs["Base Color"])
material.node_tree.links.new(rough_node.outputs["Color"], principled_bsdf.inputs["Roughness"])

cube.data.materials.append(material)
# Prompt:
'''add a cube with a material of indoor flooring on it'''
# Response:
import bpy

bpy.ops.mesh.primitive_cube_add(size=1, enter_editmode=False, location=(0, 0, 0))
cube = bpy.context.object
cube.name = "IndoorFloorCube"
cube.data.name = "IndoorFloorCube"

material = bpy.data.materials.new(name="IndoorFloorMaterial")
material.use_nodes = True
material_output = material.node_tree.nodes["Material Output"]
principled_bsdf = material.node_tree.nodes["Principled BSDF"]
material.node_tree.links.new(principled_bsdf.outputs["BSDF"], material_output.inputs["Surface"])

diffuse_texture = bpy.data.images.new("DiffuseTexture", 1024, 1024)
diffuse_texture.filepath = "D:\\Sekou\\OwnWork\\BlenderGpt\\materials\\brown_planks_03\\brown_planks_03_diff_1k.png"
diffuse_texture.file_format = 'PNG'
diffuse_texture.colorspace_settings.name = 'sRGB'

rough_texture = bpy.data.images.new("RoughTexture", 1024, 1024)
rough_texture.filepath = "D:\\Sekou\\OwnWork\\BlenderGpt\\materials\\brown_planks_03\\brown_planks_03_rough_1k.png"
rough_texture.file_format = 'PNG'
rough_texture.colorspace_settings.name = 'Non-Color'

ao_texture = bpy.data.images.new("AOTexture", 1024, 1024)
ao_texture.filepath = "D:\\Sekou\\OwnWork\\BlenderGpt\\materials\\brown_planks_03\\brown_planks_03_ao_1k.png"
ao_texture.file_format = 'PNG'
ao_texture.colorspace_settings.name = 'Non-Color'

diffuse_node = material.node_tree.nodes.new("ShaderNodeTexImage")
diffuse_node.image = diffuse_texture

rough_node = material.node_tree.nodes.new("ShaderNodeTexImage")
rough_node.image = rough_texture

ao_node = material.node_tree.nodes.new("ShaderNodeTexImage")
ao_node.image = ao_texture

mix_node = material.node_tree.nodes.new("ShaderNodeMixRGB")
mix_node.blend_type = 'MULTIPLY'

material.node_tree.links.new(diffuse_node.outputs["Color"], mix_node.inputs[1])
material.node_tree.links.new(ao_node.outputs["Color"], mix_node.inputs[2])
material.node_tree.links.new(mix_node.outputs["Color"], principled_bsdf.inputs["Base Color"])
material.node_tree.links.new(rough_node.outputs["Color"], principled_bsdf.inputs["Roughness"])

cube.data.materials.append(material)
# Prompt:
'''add a plane size 5 with an outdor material on it'''
# Response:
import bpy

bpy.ops.mesh.primitive_plane_add(size=5, enter_editmode=False, location=(0, 0, 0))
plane = bpy.context.object
plane.name = "OutdoorPlane"
plane.data.name = "OutdoorPlane"

material = bpy.data.materials.new(name="OutdoorMaterial")
material.use_nodes = True
material_output = material.node_tree.nodes["Material Output"]
principled_bsdf = material.node_tree.nodes["Principled BSDF"]
material.node_tree.links.new(principled_bsdf.outputs["BSDF"], material_output.inputs["Surface"])

diffuse_texture = bpy.data.images.load("D:\\Sekou\\OwnWork\\BlenderGpt\\materials\\aerial_grass_rock\\aerial_grass_rock_diff_1k.png")
rough_texture = bpy.data.images.load("D:\\Sekou\\OwnWork\\BlenderGpt\\materials\\aerial_grass_rock\\aerial_grass_rock_rough_1k.png")
ao_texture = bpy.data.images.load("D:\\Sekou\\OwnWork\\BlenderGpt\\materials\\aerial_grass_rock\\aerial_grass_rock_ao_1k.png")

diffuse_node = material.node_tree.nodes.new("ShaderNodeTexImage")
diffuse_node.image = diffuse_texture

rough_node = material.node_tree.nodes.new("ShaderNodeTexImage")
rough_node.image = rough_texture

ao_node = material.node_tree.nodes.new("ShaderNodeTexImage")
ao_node.image = ao_texture

mix_node = material.node_tree.nodes.new("ShaderNodeMixRGB")
mix_node.blend_type = 'MULTIPLY'

material.node_tree.links.new(diffuse_node.outputs["Color"], mix_node.inputs[1])
material.node_tree.links.new(ao_node.outputs["Color"], mix_node.inputs[2])
material.node_tree.links.new(mix_node.outputs["Color"], principled_bsdf.inputs["Base Color"])
material.node_tree.links.new(rough_node.outputs["Color"], principled_bsdf.inputs["Roughness"])

plane.data.materials.append(material)
# Prompt:
'''write sekou on it'''
# Response:
import bpy

bpy.ops.object.text_add(enter_editmode=False, location=(0, 0, 0))
text = bpy.context.object
text.name = "sekou"
text.data.body = "sekou"

material = bpy.data.materials.new(name="sekouMaterial")
material.use_nodes = True
material_output = material.node_tree.nodes["Material Output"]
principled_bsdf = material.node_tree.nodes["Principled BSDF"]
material.node_tree.links.new(principled_bsdf.outputs["BSDF"], material_output.inputs["Surface"])

diffuse_texture = bpy.data.images.load("D:\\Sekou\\OwnWork\\BlenderGpt\\materials\\aerial_grass_rock\\aerial_grass_rock_diff_1k.png")
rough_texture = bpy.data.images.load("D:\\Sekou\\OwnWork\\BlenderGpt\\materials\\aerial_grass_rock\\aerial_grass_rock_rough_1k.png")
ao_texture = bpy.data.images.load("D:\\Sekou\\OwnWork\\BlenderGpt\\materials\\aerial_grass_rock\\aerial_grass_rock_ao_1k.png")

diffuse_node = material.node_tree.nodes.new("ShaderNodeTexImage")
diffuse_node.image = diffuse_texture

rough_node = material.node_tree.nodes.new("ShaderNodeTexImage")
rough_node.image = rough_texture

ao_node = material.node_tree.nodes.new("ShaderNodeTexImage")
ao_node.image = ao_texture

mix_node = material.node_tree.nodes.new("ShaderNodeMixRGB")
mix_node.blend_type = 'MULTIPLY'

material.node_tree.links.new(diffuse_node.outputs["Color"], mix_node.inputs[1])
material.node_tree.links.new(ao_node.outputs["Color"], mix_node.inputs[2])
material.node_tree.links.new(mix_node.outputs["Color"], principled_bsdf.inputs["Base Color"])
material.node_tree.links.new(rough_node.outputs["Color"], principled_bsdf.inputs["Roughness"])

text.data.materials.append(material)
# Prompt:
'''add me a big plane with a material of brick'''
# Response:
import bpy

bpy.ops.mesh.primitive_plane_add(size=10, enter_editmode=False, location=(0, 0, 0))
plane = bpy.context.object
plane.name = "BrickPlane"
plane.data.name = "BrickPlane"

material = bpy.data.materials.new(name="BrickMaterial")
material.use_nodes = True
material_output = material.node_tree.nodes["Material Output"]
principled_bsdf = material.node_tree.nodes["Principled BSDF"]
material.node_tree.links.new(principled_bsdf.outputs["BSDF"], material_output.inputs["Surface"])

diffuse_texture = bpy.data.images.load("D:\\Sekou\\OwnWork\\BlenderGpt\\materials\\stone_floor\\stone_floor_diff_1k.png")
rough_texture = bpy.data.images.load("D:\\Sekou\\OwnWork\\BlenderGpt\\materials\\stone_floor\\stone_floor_rough_1k.png")
ao_texture = bpy.data.images.load("D:\\Sekou\\OwnWork\\BlenderGpt\\materials\\stone_floor\\stone_floor_ao_1k.png")

diffuse_node = material.node_tree.nodes.new("ShaderNodeTexImage")
diffuse_node.image = diffuse_texture

rough_node = material.node_tree.nodes.new("ShaderNodeTexImage")
rough_node.image = rough_texture

ao_node = material.node_tree.nodes.new("ShaderNodeTexImage")
ao_node.image = ao_texture

mix_node = material.node_tree.nodes.new("ShaderNodeMixRGB")
mix_node.blend_type = 'MULTIPLY'

material.node_tree.links.new(diffuse_node.outputs["Color"], mix_node.inputs[1])
material.node_tree.links.new(ao_node.outputs["Color"], mix_node.inputs[2])
material.node_tree.links.new(mix_node.outputs["Color"], principled_bsdf.inputs["Base Color"])
material.node_tree.links.new(rough_node.outputs["Color"], principled_bsdf.inputs["Roughness"])

plane.data.materials.append(material)
# Prompt:
'''add a cube here with size .1'''
# Response:
import bpy

bpy.ops.mesh.primitive_cube_add(size=0.1, enter_editmode=False, location=(0, 0, 0))
cube = bpy.context.object
cube.name = "Cube"
cube.data.name = "Cube"

material = bpy.data.materials.new(name="CubeMaterial")
material.use_nodes = True
material_output = material.node_tree.nodes["Material Output"]
principled_bsdf = material.node_tree.nodes["Principled BSDF"]
material.node_tree.links.new(principled_bsdf.outputs["BSDF"], material_output.inputs["Surface"])

diffuse_texture = bpy.data.images.load("D:\\\\Sekou\\\\OwnWork\\\\BlenderGpt\\\\materials\\\\stone_floor\\\\stone_floor_diff_1k.png")
rough_texture = bpy.data.images.load("D:\\\\Sekou\\\\OwnWork\\\\BlenderGpt\\\\materials\\\\stone_floor\\\\stone_floor_rough_1k.png")
ao_texture = bpy.data.images.load("D:\\\\Sekou\\\\OwnWork\\\\BlenderGpt\\\\materials\\\\stone_floor\\\\stone_floor_ao_1k.png")

diffuse_node = material.node_tree.nodes.new("ShaderNodeTexImage")
diffuse_node.image = diffuse_texture

rough_node = material.node_tree.nodes.new("ShaderNodeTexImage")
rough_node.image = rough_texture

ao_node = material.node_tree.nodes.new("ShaderNodeTexImage")
ao_node.image = ao_texture

mix_node = material.node_tree.nodes.new("ShaderNodeMixRGB")
mix_node.blend_type = 'MULTIPLY'

material.node_tree.links.new(diffuse_node.outputs["Color"], mix_node.inputs[1])
material.node_tree.links.new(ao_node.outputs["Color"], mix_node.inputs[2])
material.node_tree.links.new(mix_node.outputs["Color"], principled_bsdf.inputs["Base Color"])
material.node_tree.links.new(rough_node.outputs["Color"], principled_bsdf.inputs["Roughness"])

cube.data.materials.append(material)