bl_info = {
    "name": "Perfect Sphere",
    "author": "sedou",
    "version": (1, 0),
    "blender": (2, 90, 3),
    "location": "View3D > Add > Mesh > New Object",
    "description": "Adds subdivided cube made out of quads with cast modifier on set to 1.0",
    "warning": "",
    "doc_url": "",
    "category": "Add Mesh",
}

import bpy
from bpy.types import Operator
from bpy.props import FloatVectorProperty
from bpy_extras.object_utils import AddObjectHelper, object_data_add
from mathutils import Vector

# Adds object with modifiers
def add_object(self, context):
    bpy.ops.mesh.primitive_cube_add(align='WORLD', location=(0, 0, 0), rotation=(0, 0, 0))
    bpy.ops.object.modifier_add(type='SUBSURF')
    bpy.context.object.modifiers["Subdivision"].levels = 3
    bpy.ops.object.modifier_add(type='CAST')
    bpy.context.object.modifiers["Cast"].factor = 1
    bpy.ops.object.modifier_apply(modifier="Subdivision")
    bpy.ops.object.modifier_apply(modifier="Cast")

class OBJECT_OT_add_object(Operator, AddObjectHelper):
    """Create a Perfect Sphere"""
    bl_idname = "mesh.add_object"
    bl_label = "Add Mesh Object"
    bl_options = {'REGISTER', 'UNDO'}

    scale: FloatVectorProperty(
        name="scale",
        default=(1.0, 1.0, 1.0),
        subtype='TRANSLATION',
        description="scaling",
    )

    def execute(self, context):

        add_object(self, context)

        return {'FINISHED'}


# Registration

def add_object_button(self, context):
    self.layout.operator(
        OBJECT_OT_add_object.bl_idname,
        text="Perfect Sphere",
        icon='SPHERE')


# This allows you to right click on a button and link to documentation
def add_object_manual_map():
    url_manual_prefix = "https://docs.blender.org/manual/en/latest/"
    url_manual_mapping = (
        ("bpy.ops.mesh.add_object", "scene_layout/object/types.html"),
    )
    return url_manual_prefix, url_manual_mapping


def register():
    bpy.utils.register_class(OBJECT_OT_add_object)
    bpy.utils.register_manual_map(add_object_manual_map)
    bpy.types.VIEW3D_MT_mesh_add.append(add_object_button)


def unregister():
    bpy.utils.unregister_class(OBJECT_OT_add_object)
    bpy.utils.unregister_manual_map(add_object_manual_map)
    bpy.types.VIEW3D_MT_mesh_add.remove(add_object_button)


if __name__ == "__main__":
    register()
