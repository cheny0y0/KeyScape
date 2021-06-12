@echo off
cls
echo  KeyScape 16-bit Mode Setup
echo.
echo   This version requires Python 2.1 or higher.
echo   Do you wish to continue?
echo.
echo  Press any key to continue, or CTRL+C to exit the Setup.
pause>nul
md %TMP%\..\..\..\..\..\..\KEYSCAPE
copy N16\KEYSCAPE.PY %TMP%\..\..\..\..\..\..\KEYSCAPE
copy N16\KEYSCAPE.BAT %TMP%\..\..\..\..\..\..\KEYSCAPE
echo  Setup completed successfully. Files are in %TMP%\..\..\..\..\..\..\KEYSCAPE
echo.
echo  Press any key to exit the Setup...
pause>nul
