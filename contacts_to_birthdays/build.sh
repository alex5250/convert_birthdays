# Build the executable using the setup script
python setup.py build_exe

# Create a directory to store the build files
sudo mkdir /opt/convert_birthdays

# Copy the build files to the directory
sudo cp -r ./build /opt/convert_birthdays

# Create the convert_birthdays file
touch convert_birtdays

# Write the contents to the file
cat > convert_birtdays << EOF
#!/bin/sh
/opt/convert_birthdays/build/exe.linux-x86_64-3.10/main "\$@"
EOF

# Move the file to /usr/bin
sudo mv -f convert_birtdays  /usr/bin/convert_birthdays

# Change the permissions on the file
sudo chmod 755 /usr/bin/convert_birthdays
