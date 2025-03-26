# ==============================================================================
# elevator.py (v1)
# The purpose of this script is to simulate an elevator.
# Inputs:
#   starting floor (where the elevator begins)
#   floors to visit
# Outputs:
#   total travel time
#   floors visited (in order)
#
# Notes:
#   No input validation outside of that provided by argparse module.
#   Output is just printed to the terminal.
#   I think this fulfills the spirit of the instructions, but it seems too easy?
# ==============================================================================

import argparse

# get the script inputs
parser = argparse.ArgumentParser(
  prog='elevator.py',
  description="""
    The purpose of this script is to simulate an elevator.
    This script requires two inputs:
      * a starting floor
      * a list of floors to visit
    This script will display two outputs:
      * total travel time
      * list of floors visited in order

    Example usage: python elevator.py -s 12 -f 32 14 7 99
  """,
  formatter_class=argparse.RawTextHelpFormatter
)

parser.add_argument(
  '-s', '--elevator_start',
  help='(required) The floor number that the elevator starts at.',
  required=True,
  type=int,
  nargs=1
)

parser.add_argument(
  '-f', '--floors',
  help='(required) The floors to visit. Example: 4 6 12 22 2',
  required=True,
  type=int,
  nargs='+'
)

args = parser.parse_args()

# variables
TRAVEL_TIME = 10                                # single floor travel time
starting_floor = args.elevator_start[0]
floor_list = args.floors
total_travel_time = 0

# add the starting floor to the floor list
floor_list.insert(0, starting_floor)

# iterate through the list to get the total_travel_time
for i in range(len(floor_list) - 1):
  total_travel_time += abs(floor_list[i] - floor_list[i+1]) * TRAVEL_TIME

# print output to terminal
print('Total travel time (seconds): ', total_travel_time)
print('Floors visited in order:     ', floor_list)

