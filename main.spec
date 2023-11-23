# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['main.py'],
    pathex=['C:\\Users\\zero\\PycharmProjects\\codec\\venv\\Lib\\site-packages'],
    binaries=[],
    datas=[
                 # rutas de las bibliotecas necesarias (cssbeautifier, jsbeautifier.)
                 ('C:\\Users\\zero\\PycharmProjects\\codec\\venv\\Lib\\site-packages\\cssbeautifier', 'cssbeautifier'),
                 ('C:\\Users\\zero\\PycharmProjects\\codec\\venv\\Lib\\site-packages\\jsbeautifier', 'jsbeautifier'),
             ],
    hiddenimports=['cssbeautifier', 'jsbeautifier', 'six'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='organizador-codigo',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='C:\\Users\\zero\\Documents\\codigoorganizador\\logo.ico',
)
