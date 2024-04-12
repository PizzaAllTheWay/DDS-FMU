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
To run STC sim you simply say:

```
$ ./ospsim --api_server_url https://dnvgl-osp-api.azurewebsites.net --simulator_id "ID" --access_token "token"
```


# DDS Setup
Now that we have everything working we can start interfaceing with our DDS-FMU and by that extention other FMUs that conect and use our DDS-FMU information/data
To start you will have to use "cyclonedds-python" library, which is a good library in python to interface with DDS, this python library also provides us with tolls to analyze, send, receive and troubleshoot DDS. You can find the "cyclonedds-python" library in this github repository. Navigate to there and follow the instalation guide, to sum it upp you have to run:

```
$ pip install cyclonedds
```

Now once installed, double check that you are still runing the DDS-FMU simulation on STC. Once you are runing STC simulation you can simply check if your DDS FMU has binded with ypur custom topic, our topic for this showcase is "idl::MyCustomSignalStructure". Check if your custom topic is running by writing:

```
$ cyclonedds ls
```

Undernearh you should see a square subsection that says:

| Typename       │ "Name of your custom topic"  │

│ XTypes Type ID │ "DDS ID, for us it is unset" |

If you see something like this, that means you have done everything correctly and your DDS FMU is running well. You can continue to teh final step of interfacing

you can also run PS to see topic name specificaly, for us it is "MyCustomDDSFMUTopic"

```
$ cyclonedds ps
```

## DDS and ROS/ROS2 similarities
As you might have noticed if you read the "cyclonedds-python" library, it is very similar in nature to ROS or ROS2, and that is because ROS and ROS2 is built on top of DDS, the DDS is the foundadtion to all intersystem protocols and is the absolute standard. Next level O_O



# Interfacing DDS-FMU
Now just run the interface code like this:

```
$ cd dds-fmu-interface
$ python3 dds-fmu-interface.py
```

After that try changing in the STC interface the Inputs (These would be something that DDS-FMU would get from other FMUs and send back to DDS as its input, like some simulated data like simulated hull dynamics position or simulated IMU or GNSS data)
Also check out the STC Interface Output section (This is where our published data from DDS gets subscribed to in DDS-FMU and then send as its output to other FMUs as a control signal or something like that)


# Conclusion
With all these thing in mind. By developing custom DDS-FMU, sending it to STC for simulation, and using DDS inteface driver to bind DDS-FMU with your PC pythin code, you can escentailly have full autono0my and control of your FMUs in STC Simulator simply with a few interface scripts that can then lead to other more complexs scripts on your local PC. By mastering these concepts you have full customization and capabilities for this simulator.

