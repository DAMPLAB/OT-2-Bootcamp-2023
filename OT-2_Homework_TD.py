#Import API

import math
from opentrons import protocol_api
from opentrons import types

metadata = {
        'apiLevel': '2.10',
        'protocolName': 'ot2_bootcamp_tadhg',
        'author': 'tadhg Daly',
        'description': 'Tadhgs OT-2 Homework',
}

def run(protocol: protocol_api.ProtocolContext) :
    # Load labware, tiprack, and pipettes
    reservoir = protocol.load_labware(
        'agilent_1_reservoir_290ml',
        location=8,
        label = 'Reagent Reservoir',
    )

    plate = protocol.load_labware(
        load_name = 'opentrons_96_wellplate_2.4ml_deep',
        location = 9,
        label = 'PCR Plate',
    )

    tiprack_200_1 = protocol.load_labware(
        load_name = 'opentrons_96_filtertiprack_200ul',
        location = 7,
        label = 'Filter Tip 200 #1',
    )

    tiprack_200_2 = protocol.load_labware(
        load_name = 'opentrons_96_filtertiprack_200ul',
        location = 4,
        label = 'Filter Tip 200 #2',
    )

    p300_m = protocol.load_instrument(
        instrument_name = 'p300_multi_gen2',
        mount = 'left'
        tip_racks = [tiprack_200_1, tiprack_200_2]
    )

    #Reagenets in well format
    reagent = reservoir ['A1']

    #Turn off robot rail lights
    protocol.set_rail_lights(True)

    #Default settings
    #Aspirtae at the default flowrate of 150 ul/s
    #Dispense at the default flowrate of 300 ul/s
    # By default, the OT-2 will aspirtae and dispense 1mm above the bottom of a well
    
    available_deck_slots = ['1' ,'2' ,'3' ,'4' ,'5' ,'6' ,'10' ,'11']

#    p300_m.pick_up_tip ()
#    p300_m.aspirate (35, plate['A1'])
#    p300_m.dispense (35, plate

    p300_m.pick_up_tip ()
    
    for i in range(12):
        p300_m.transfer(35, reservoir.wells('A1'), plate.columns()[i], new_tip = 'never')
    
    #for i in range(4):
    #    p300_m.distribute(35, reservoir.wells('A1'), plate.rows()[i+4], new_tip = 'never')

    #for i in range(4):
    #    p300_m.distribute(35, reservoir.wells('A1'), plate.rows()[i+8], new_tip = 'never')

    p300_m.drop_tip ()
