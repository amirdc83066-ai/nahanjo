@echo off
chcp 65001 > nul
title Build Nahanjo EXE

echo =========================================
echo Checking PyInstaller...
echo =========================================

py -m PyInstaller --version >nul 2>&1
if errorlevel 1 (
    echo PyInstaller is not installed for this Python.
    echo Install it with:
    echo py -m pip install pyinstaller
    pause
    exit /b 1
)

echo =========================================
echo Cleaning old build files...
echo =========================================

if exist build rmdir /s /q build
if exist dist rmdir /s /q dist
if exist Nahanjo.spec del /f /q Nahanjo.spec

echo =========================================
echo Starting PyInstaller build...
echo =========================================

py -m PyInstaller ^
--clean ^
--noconfirm ^
--onefile ^
--windowed ^
--name "Nahanjo" ^
--icon "ui\logo.ico" ^
--paths "." ^
--collect-all sklearn ^
--collect-all scipy ^
--collect-all pandas ^
--collect-all numpy ^
--collect-all joblib ^
--collect-all threadpoolctl ^
--collect-submodules sklearn ^
--collect-submodules scipy ^
--collect-submodules pandas ^
--collect-submodules numpy ^
--collect-submodules matplotlib ^
--collect-submodules PyQt5 ^
--hidden-import=sklearn ^
--hidden-import=sklearn.ensemble ^
--hidden-import=sklearn.tree ^
--hidden-import=sklearn.utils ^
--hidden-import=sklearn.neighbors ^
--hidden-import=sklearn.preprocessing ^
--hidden-import=sklearn.metrics ^
--hidden-import=scipy ^
--hidden-import=scipy.sparse.csgraph ^
--hidden-import=numpy ^
--hidden-import=pandas ^
--hidden-import=joblib ^
--hidden-import=threadpoolctl ^
--hidden-import=PyQt5 ^
--hidden-import=PyQt5.QtCore ^
--hidden-import=PyQt5.QtGui ^
--hidden-import=PyQt5.QtWidgets ^
--hidden-import=PyQt5.uic ^
--add-data "ui;ui" ^
--add-data "core;core" ^
--add-data "ai_layer;ai_layer" ^
--add-data "data;data" ^
--add-data "ui\logo.ico;ui" ^
--add-data "ui\Vazir.ttf;ui" ^
--add-data "ui\ai_prompt.txt;ui" ^
main.py

echo =========================================
echo BUILD FINISHED SUCCESSFULLY
echo =========================================

echo.
echo EXE Location:
echo dist\Nahanjo.exe
echo.

pause
