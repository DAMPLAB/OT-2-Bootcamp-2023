# OT-2 Bootcamp Template for Homework Assignment

# Written by Kristen Sheldon 2023-09-22

import math
from opentrons import protocol_api
from opentrons import types

metadata = {
    "apiLevel": "2.10",
    "protocolName": "ot2_bootcamp_Kristen",
    "author": "Kristen Sheldon",
    "description": "OT-2 Bootcamp_Kristen Homework",
}

def run(protocol: protocol_api.ProtocolContext):
    # Load labware, tiprack, and pipettes
    reservoir = protocol.load_labware(
        "agilent_1_reservoir_290ml",
        location=8,
         label= 'Reagent Reservoir',
    )

    plate = protocol.load_labware(
        "usascientific_96_wellplate_2.4ml_deep",
        location=9,
         label= 'PCR Plate',
    )

    tiprack_200_1= protocol.load_labware(
        load_name="opentrons_96_filtertiprack_200ul",
        location=7,
        label="Filter Tip 200 #1",
    )

    tiprack_200_2= protocol.load_labware(
        load_name="opentrons_96_filtertiprack_200ul",
        location=4,
        label="Filter Tip 200 #2",
    )

    p300_m = protocol.load_instrument(
        instrument_name="p300_multi_gen2",
        mount="left",
        tip_racks=[tiprack_200_1, tiprack_200_2]
    )

    # Reagents in well format
    reagent = reservoir['A1']

    # Turn off robot rail lights
    protocol.set_rail_lights(True)

    # Default settings
    # Aspirate at the default flowrate of 150 ul/s
    # Dispense at the default flowrate of 300 ul/s
    # By default, the OT-2 will aspirate and dispense 1mm above the bottom of a well.

    available_deck_slots = ['1', '2', '3', '4','5', '6', '10', '11']

    #######################Start differentiation protocol with PBS Wash####################
    protocol.comment("Begin automation mwuahaha!")
    #--------------------------------Protocol Begins------------------------------
    # Using p300 multi-channel pipette to transfer 35 ul of reagent from reservior
    # into each well of 96 deep well plate.
    #------------------------ Create your automation instructions Here------------------

    p300_m.pick_up_tip()
 
    for i in range (4):
        p300_m.distribute(35, reservoir.wells("A1"), plate.columns()[i], new_tip = 'never')
 
    for i in range (4):
        p300_m.distribute(35, reservoir.wells("A1"), plate.columns()[i+4], new_tip = 'never')

    for i in range (4):
        p300_m.distribute(35, reservoir.wells("A1"), plate.columns()[i+8], new_tip = 'never')

    p300_m.drop_tip()

    # Protocol Completed!
    protocol.comment("Protocol completed YAY!")
