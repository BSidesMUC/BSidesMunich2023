---
accepted: true
code: VDUJTX
details: true
keynote: false
layout: workshop
speakers:
- bio: Dr. Jan Van den Herrewegen has been researching (along with the inevitable
    cursing on) the security of Electronic Control Units since 2016. He defended his
    PhD thesis "Automotive Firmware Extraction and Analysis Techniques" at the University
    of Birmingham in February 2021. Since then he has stayed involved in the goings
    of the automotive world and reverse engineering through EmberCrypt, his professional
    vessel. Going from more research focused during his PhD to tackling more practical
    challenges the past years, he is eager to share what he's learned on what to do
    (and especially not do) with an unknown ECU.
  handle: false
  name: Dr. Jan Van den Herrewegen
  photo: https://pretalx.com/media/avatars/jan_vdh_NU2tu3C.jpg
timeslot:
  duration: 240
  end: 2023-10-14 13:00:00+02:00
  start: 2023-10-14 09:00:00+02:00
title: Forensic Fundamentals of Automotive Control Units
track: 2
---

# Forensic Fundamentals of Electronic Control Units


An Automotive Electronic Control Units (ECU) becomes, once installed in a vehicle, essentially a black box.
Certain aftermarket endeavours, such as retrieving crash data for insurance purposes, providing access for independent repair shops, forensic analysis of mileage correction bugs used by aftermarket tools, or reprogramming the ECU to a blank slate in order to give it a new life on the second-hand market, are impossible without authenticated access to the ECU.
In this workshop, we delve into the secret waters of ECU reverse engineering.
Firstly, we look into firmware retrieval methodology.
Therefore we introduce various frequently occuring hardware interfaces and their respective communication protocols with the ECU.
Next, we touch upon two easily accessible hardware fault-injection techniques (voltage - and electromagnetic fault injection) which can assist in accessing the ECUs internal workings.
Secondly, we apply these techniques to real-world targets in order to access their firmware.
Analysing existing diagnostic tools and MCU debuggers, we show practical ways to ease the forensic process.
We discuss which algorithms to target and how to locate them in what initially seems like a cluttered binary desert.