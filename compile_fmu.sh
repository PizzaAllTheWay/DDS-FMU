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

# Try to format data structure to Python's liking
echo "Formatting DDS-FMU data structure to fit with Python datastructures..."

# Check if the directory exists
if [ -d "resources/config/idl/" ]; then
    cd resources/config/idl/
    # Check if the IDL file exists
    if [ -f "dds-fmu.idl" ]; then
        idlc -l py dds-fmu.idl
        echo "Finished formatting"
    else
        echo "could not open file at location: dds-fmu.idl"
        exit 1
    fi
else
    echo "Directory resources/config/idl/ does not exist"
    exit 1
fi

# Moving Python data structure to the correct folder
echo "Moving Python DDS data structures to dds-fmu-interface"
if [ -d "../../../../dds-fmu-interface/idl" ]; then
    rm -rf ../../../../dds-fmu-interface/idl
fi
mv idl ../../../../dds-fmu-interface/

# Check if the move was successful
if [ ! -d "../../../../dds-fmu-interface/idl" ]; then
    echo "Failed to move idl directory"
    exit 1
fi

# Fixing issues that are buggy
echo "Fixing issues that could cause bugs in data structure file for Python"

MY_IDL_DATA_STRUCTURE_FILE="DDSFMUDataStructures.py"
if [ -d "../../../../dds-fmu-interface/idl/" ]; then
    cd ../../../../dds-fmu-interface/idl/
    if [ -f "_dds-fmu.py" ]; then
        mv _dds-fmu.py $MY_IDL_DATA_STRUCTURE_FILE
    else
        echo "_dds-fmu.py does not exist"
        exit 1
    fi
    if [ -f "$MY_IDL_DATA_STRUCTURE_FILE" ]; then
        sed -i '/^# root module import for resolving types$/d' "$MY_IDL_DATA_STRUCTURE_FILE"
        sed -i '/^import idl$/d' "$MY_IDL_DATA_STRUCTURE_FILE"
    else
        echo "$MY_IDL_DATA_STRUCTURE_FILE does not exist"
        exit 1
    fi
    if [ -f ".idlpy_manifest" ]; then
        rm .idlpy_manifest
    fi
    if [ -f "__init__.py" ]; then
        rm __init__.py
    fi
    touch __init__.py
else
    echo "Directory ../../../../dds-fmu-interface/idl/ does not exist"
    exit 1
fi

echo ""
echo "#==================================================#"
echo "Finished Python data structure setup. You can now run dds-fmu-interface code freely :)"
echo "#==================================================#"
echo ""
