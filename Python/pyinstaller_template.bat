echo "Packaging..."
rmdir /S /Q dist
rmdir /S /Q ../TOOL_NAME
pyinstaller --noconsole TOOL_NAME.py
xcopy ../dist/TOOL_NAME/* ../TOOL_NAME_RELEASE/ /s /e
echo "Done"
pause