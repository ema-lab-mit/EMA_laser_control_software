# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['run_main.py'],
    pathex=[],
    binaries=[],
    datas=[
        (
            "C:/Users/EMA LAB laser/AppData/Local/Programs/Python/Python312/Lib/site-packages/altair/vegalite/v5/schema/vega-lite-schema.json",
            "./altair/vegalite/v5/schema/"
        ),
        (
            "C:/Users/EMA LAB laser/AppData/Local/Programs/Python/Python312/Lib/site-packages/streamlit/static",
            "./streamlit/static"
        ),
        (   
            "C:/Users/EMA LAB laser/Documents/laser_control_system/src/ui_st",
            "./ui_st"
        )
    ],
    hiddenimports=[
        "streamlit"
    ],
    hookspath=['./hooks'],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='run_main',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
