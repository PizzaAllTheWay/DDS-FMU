You can start work on the dds-fmu in the src/ folder
You mainly want to eddit these files:
    src/resources/idl/dds-fmu.idl
    src/resources/dds/dds_profile.xml
    src/resources/dds/ddsfmu_mapping.xml
Read up on the src/documentation/ folder to get a better grasp of how to use and manipulate the code



Once you are done and satisfied with the result, compile the whole src into a .fmu file using this shel scrips:
./compile_fmu.sh

Now you should see that all the changes that you have made in the code reflect in the "dds-fmu.fmu" file
