# Compile
cd src
./resources/tools/linux64/repacker create -v -o dds-fmu.fmu .

# Move .fmu file to correct place
mv -f dds-fmu.fmu ..

echo ""
echo "Finished compiling to 'dds-fmu.fmu' :)"