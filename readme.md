# Sensorix for OpenPiGlide

## Purpose
This project is currently in early stage development and is tested with groud experiments only.
Once finished this pythonic daemon will provide an alternative to the well-known OpenVario project, which relies on 
technology from 2012. In 2021 there are better sensors, embedded systems and new displays available, which allow for 
more generic solutions and greater flexibility on what technology to use.

## Setup
This project will run on any embedded platform that is supported by XCSoar, the heart of this project. As a test bench
we use the RaspberryPi with its great hardware specs. All you need to spin the system up is therefore any RaspberryPi
with a 40-GPIO-pin connector and at least 1GB of RAM. The optimal choice at the moment is the model 3B+.
Raspbian in its latest distribution is used without any further additions. Make sure to run Python 3.9 on the RPi.

Once the project is ready to be used in a glider, we will provide an installation script that will set your RPi up with
XCSoar, the sensor daemon, and everything else you will need.

The idea is to give you freedom of choice what peripherals to use without being limited to LVDS or DSI screen since 
their availability became worse over the years. The project will provide support for all OpenVario peripherals.
