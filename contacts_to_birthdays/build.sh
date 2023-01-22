python setup.py build_exe
sudo mkdir /opt/convert_birthdays
sudo cp -r ./build /opt/convert_birthdays
touch convert_birtdays
cat > convert_birtdays << EOF
#!/bin/sh
/opt/convert_birthdays/build/exe.linux-x86_64-3.10/main "\$@"
EOF

sudo mv -f convert_birtdays  /usr/bin/convert_birthdays
sudo chmod 755 /usr/bin/convert_birthdays

