# Makeing an DDS-FMU
You can start work on the dds-fmu in the src/ folder
You mainly want to eddit these files:
    src/resources/idl/dds-fmu.idl
    src/resources/dds/dds_profile.xml
    src/resources/dds/ddsfmu_mapping.xml
Read up on the src/documentation/ folder to get a better grasp of how to use and manipulate the code

Once you are done and satisfied with the result, compile the whole src into a .fmu file using this shel scrips:

```
$ ./compile_fmu.sh
```

Now you should see that all the changes that you have made in the code reflect in the "dds-fmu.fmu" file



# Running DDS-FMU
You have to have a simulation platform for this part. I recomend OSP if you just beginibng. However this DDS-FMU and the interface code for teh next step is based on STC (Simulation Thrust Center) made by DNV R&D Gropup. A good interface to simulate and interface with your FMUs, simulations, dynamics, control both locally and cloud computing
Compile the FMU, upload it on the STC platform and run the simulation localy, you should now start to see that the FMU is runing and binded with DDS :)


# Interfaceing 
Now that we have everything working we can start interfaceing with our DDS-FMU and by that extention other FMUs that conect and use our DDS-FMU information/data
To start you will have to use "cyclonedds-python" library, which is a good library in python to interface with DDS, this python library also provides us with tolls to analyze, send, receive and troubleshoot DDS. You can find the "cyclonedds-python" library in this github repository. Navigate to there and follow the instalation guide, to sum it upp you have to run:

```
$ pip install cyclonedds
```



