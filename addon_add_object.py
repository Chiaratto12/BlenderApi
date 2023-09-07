bl_info = {
    "name": "AddObject",
    "author": "edu05",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "location": "View3D > Tool",
    "warning": "",
    "doc_url": "",
    "category": "Add Mesh",
}


import bpy

class ObjectPanel(bpy.types.Panel):
    bl_label = "Add Object"
    bl_idname = "PT_AddObject"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Object Addon'
    
    def draw(self, context):
        layout = self.layout
        
        row = layout.row()
        row.label(text = "Add a object", icon = 'CUBE')
        row = layout.row()
        row.operator("mesh.primitive_cube_add", icon = 'CUBE')
        row = layout.row()
        row.operator("mesh.primitive_uv_sphere_add", icon = 'SPHERE')

class ScalePanel(bpy.types.Panel):
    bl_label = "Change scale"
    bl_idname = "PT_ScalePanel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Object Addon'
    bl_parent_id = 'PT_AddObject'
    bl_options = {'DEFAULT_CLOSED'}
    
    def draw(self, context):
        layout = self.layout
        obj = context.object
        row = layout.row()
        layout.scale_y = 1.4
        row.operator("transform.resize")
        col = layout.column()
        col.prop(obj, "scale")


def register():
    bpy.utils.register_class(ObjectPanel)
    bpy.utils.register_class(ScalePanel)


def unregister():
    bpy.utils.unregister_class(ObjectPanel)
    bpy.utils.unregister_class(ScalePanel)


if __name__ == "__main__":
    register()
