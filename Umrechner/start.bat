@echo off
pip install -r requirements.txt

chcp 65001 >nul
color 0b
:AUSWAHL
cls
echo.
echo Auswahl-Menü
echo.
echo [e] Euroumrechner
echo [p] Leistungsumrechner
echo [z] Längenumrechner
echo [x] Beenden
echo.

set /p AUSWAHL=Deine Auswahl?
if /i "%AUSWAHL%" == "e" (goto EURO)
if /i "%AUSWAHL%" == "p" (goto LEISTUNG)
if /i "%AUSWAHL%" == "z" (goto LAENGEN)
if /i "%AUSWAHL%" == "x" (goto ENDE)
goto AUSWAHL

:EURO
python euro.pyw
set AUSWAHL=0
goto AUSWAHL

:LEISTUNG
python power.pyw
set AUSWAHL=0
goto AUSWAHL

:LAENGEN
python length.pyw
set AUSWAHL=0
GOTO AUSWAHL

:ENDE
echo Auf Wiedersehen %USERNAME%
pause
