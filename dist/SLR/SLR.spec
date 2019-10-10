# -*- mode: python -*-
from kivy.deps import sdl2, glew
block_cipher = None
my_hidden_modules = [
         ( 'C:\\Users\\PROJECT 17\\Anaconda3\\Lib\\site-packages\\win32\\lib\\win32timezone.py', '.' )
         ]

a = Analysis(['main.py'],
             pathex=['C:\\Users\\PROJECT 17\\Desktop\\Sajan_Final_RealTime_prediction_using_region_of_interest\\SLRGui'],
             binaries=[],
             datas=my_hidden_modules,
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='SLR',
          debug=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,Tree('C:\\Users\\PROJECT 17\\Desktop\\Sajan_Final_RealTime_prediction_using_region_of_interest\\SLRGui'),
               a.binaries,
               a.zipfiles,
               a.datas,
               *[Tree(p) for p in (sdl2.dep_bins + glew.dep_bins)],
               strip=False,
               upx=True,
               name='SLR')
