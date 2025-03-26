# ==============================================================================
# ElevatorSimV2
# The purpose of this class is to simulate an elevator.
# Parameters:
#   starting floor (where the elevator begins)
#   floors to visit
#
# Notes:
#   Some input validation is included during class instantiation.
#   Nothing is returned per se, except for the getter methods
#   Again, I think this fulfills the spirit of the instructions,
#
# ==============================================================================
class ElevatorSimV2:

  def __init__(self, starting_floor: int, floor_list: list[int]):

    # validate class instantiation inputs
    if not isinstance(starting_floor, int):
      raise TypeError("starting_floor must be a positive integer value")
    if starting_floor < 1:
      raise ValueError("starting_floor must be a positive integer value")
    if not isinstance(floor_list, list):
      raise TypeError('floor_list must be a list of positive integer values')
    for item in floor_list:
      if not isinstance(item, int) or item < 1:
        raise ValueError("This isn't Hogwarts. No Platform 9 3/4 shenanigans here. floor_list must be a list of positive integer values")

    # initialize attributes
    self.TRAVEL_TIME = 10                       # single floor travel time
    self.total_travel_time = 0
    self.starting_floor = starting_floor
    self.floor_list = floor_list
    self.floor_list.insert(0, self.starting_floor)
    self.calculate_travel_time()

  # calculate the time to travel between all floors
  def calculate_travel_time(self):
    self.total_travel_time = 0
    for i in range(len(self.floor_list) - 1):
      self.total_travel_time += abs(self.floor_list[i] - self.floor_list[i+1]) * self.TRAVEL_TIME

  # get the total travel time
  def get_total_travel_time(self):
    return self.total_travel_time

  # get the list of floors to visit
  def get_floor_list(self):
    return self.floor_list




