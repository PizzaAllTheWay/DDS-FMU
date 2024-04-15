#!/bin/bash

# Compile
cd src
./resources/tools/linux64/repacker create -v -o dds-fmu.fmu .

# Move .fmu file to correct place
mv -f dds-fmu.fmu ..

echo ""
echo "#==================================================#"
echo "Finished compiling to 'dds-fmu.fmu' :)"
echo "#==================================================#"
echo ""



# Try format datastructure to pythons liking
echo "Fomating DDS-FMU datat structure to fit with python datastructures..."
cd resources/config/idl/
idlc -l py dds-fmu.idl
echo "Finished formating"

# Moving python data structure to correct folder
echo "Moving python DDS data structures to dds-fmu-interface"
rm -rf ../../../../dds-fmu-interface/idl
mv idl ../../../../dds-fmu-interface

# Fixing issues that are buggy
echo "Fixing issues that could cause bugs in data structure file for python"

MY_IDL_DATA_STRUCTURE_FILE="DDSFMUDataStructures.py"
cd ../../../../dds-fmu-interface/idl/
mv _dds-fmu.py $MY_IDL_DATA_STRUCTURE_FILE

sed -i '/^# root module import for resolving types$/d' "$MY_IDL_DATA_STRUCTURE_FILE"
sed -i '/^import idl$/d' "$MY_IDL_DATA_STRUCTURE_FILE"

rm .idlpy_manifest
rm __init__.py
touch __init__.py

echo ""
echo "#==================================================#"
echo "Finished python data structure setup. You can now run dds-fmu-interface code freely :)"
echo "#==================================================#"
echo ""