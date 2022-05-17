import os
import shutil
main_folder = '/data/gcs/lungNENomics/work/MathianE/Carcnoid_Milione/Carcinoid_Milione'
l_files =  os.listdir(main_folder)
id = [] 
duplicated = []
for f in l_files:
    if f.find('.svs') != -1:
        id_c =  f.split('_')[0]
        if id_c not in id:
        	id.append(id_c)
        else:
        	duplicated.append(id_c)
        	print('id_c  ', id_c)
duplicated.sort()
print(duplicated)

all_id = set(id)
os_tiles = '/home/mathiane/ln_LNEN_work_mathian/Tiles_512_512_Milione'
tiles_fl = os.listdir(os_tiles)
f_tiled =  []
for f in tiles_fl:
	if f in all_id:
		f_tiled.append(f)
f_tiled = set(f_tiled)
