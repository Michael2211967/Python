#!/usr/bin/env bash

if [ "$EUID" -ne 0 ]; then
    echo "Fehler: Root-Rechte erforderlich."
    exec sudo "$0" "$@"
fi

target_dir="/opt/farbpreis"
link_dir="/usr/local/bin"
if [ ! -d "$target_dir" ]; then
    echo "$target_dir wird erstellt ..."
    mkdir "$target_dir"
fi 

echo "die benötigten Programme werden nach $target_dir kopiert ..."
cp -u c64demo.py farbpreis.bas farbpreis.py functions.py "$target_dir"

chmod +x "$target_dir/c64demo.py"
chmod +x "$target_dir/farbpreis.py"

python3 -m compileall "$target_dir"

echo "Symlinks werden in /usr/local/bin erzeugt ..."
ln -sf "$target_dir/c64demo.py" "$link_dir/c64demo.py"
ln -sf "$target_dir/farbpreis.py" "$link_dir/farbpreis.py"

echo "Farbpreis ist erfolgreich installiert!"
