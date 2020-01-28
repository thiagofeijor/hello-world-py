import glob, os, shutil, datetime
from fnmatch import fnmatch

root = '/media/pi/BERLIM'
pattern = "*.sav"

if not os.path.exists('tmp'):
    os.makedirs('tmp')
    
for path, subdirs, files in os.walk(root):
    for name in files:
        if fnmatch(name, pattern):
            print('Save localizado:', os.path.join(path, name))
            data = datetime.datetime.now().isoformat()
            novo_nome = path.replace(root, "").replace("/", "") + name + data
            shutil.copy(os.path.join(path, name), os.path.join('tmp', novo_nome))

