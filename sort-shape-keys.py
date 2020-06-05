import bpy

ob = bpy.context.object
skeys = ob.data.shape_keys.key_blocks 

skey_names = sorted(skeys.keys(), key=lambda v: v.upper())

for name in skey_names:
   if name.lower() != 'basis':
      idx = skeys.keys().index(name)
      ob.active_shape_key_index = idx
      bpy.ops.object.shape_key_move(type='BOTTOM')
