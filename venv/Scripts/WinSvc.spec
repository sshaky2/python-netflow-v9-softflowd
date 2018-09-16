# -*- mode: python -*-

block_cipher = None


a = Analysis(['C:\\Users\\sshakya\\Documents\\GitHub\\python-netflow-v9-softflowd\\WinSvc.py'],
             pathex=['C:\\Users\\sshakya\\Documents\\GitHub\\python-netflow-v9-softflowd\\venv\\Scripts'],
             binaries=[],
             datas=[],
             hiddenimports=['win32timezone'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='WinSvc',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True )
