# Write a shell script that creates a sample directory with files, sets initial permissions, 
# and demonstrates changing file permissions using 'chmod'.

#!/bin/bash

# Create a sample directory and navigate into it
mkdir sample_directory
cd sample_directory

# Create a sample file
touch sample_file.txt

# Set initial permissions to read and write for the owner only
chmod 600 sample_file.txt
echo 'Initial permissions:'
ls -l sample_file.txt

# Change permissions to allow the group to read the file
chmod 640 sample_file.txt
echo 'Updated permissions (group can read):'
ls -l sample_file.txt


# Explanation
# This script demonstrates basic file permission management by creating a directory and a file, setting their permissions using 'chmod', and displaying the permission states with 'ls -l'

# Initially, only the owner has read and write access

# Permissions are then modified to allow the group read access.
