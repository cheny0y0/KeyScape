@echo off
cls
echo  KeyScape 32-bit or 64-bit Mode Setup
echo.
echo   This version requires Python 2.1 or higher.
echo   Do you wish to continue?
echo.
echo  Press any key to continue, or CTRL+C to exit the Setup.
pause>nul
if not exist %windir%\SYSTEM32\CHOICE.COM goto checkcexe
if exist %windir%\SYSTEM32\CHOICE.COM goto install32
:checkcexe
if not exist %windir%\SYSTEM32\choice.exe copy I386\CHOICE.COM %windir%\SYSTEM32
if exist %windir%\SYSTEM32\choice.exe goto install64
goto install32
:install32
md %TMP%\..\..\..\..\..\..\KEYSCAPE
copy I386\KEYSCAPE.PY %TMP%\..\..\..\..\..\..\KEYSCAPE
copy I386\KEYSCAPE.BAT %TMP%\..\..\..\..\..\..\KEYSCAPE
echo  Setup completed successfully. Files are in %TMP%\..\..\..\..\..\..\KEYSCAPE
echo.
echo  Press any key to exit the Setup...
pause>nul
goto end
:install64
echo Input the location would you like to install:
set /p tempans=
md %tempans%
copy AMD64\KEYSCAPE.PY %tempans%
copy AMD64\KEYSCAPE.BAT %tempans%
echo  Setup completed successfully.
echo.
echo  Press any key to exit the Setup...
pause>nul
goto end
:end
