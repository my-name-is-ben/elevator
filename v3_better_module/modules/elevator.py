# ==============================================================================
# ElevatorSimV3
# The purpose of this class is to simulate an elevator, but with a bit more
#   thought put into it to _very_ slightly approximate an actual working elevator.
#
# Notes:
#   Nothing is returned default, except through the getter methods
# ==============================================================================
class ElevatorSimV3:

  def __init__(self):

    # constants
    self.TRAVEL_TIME = 10                             # single floor travel time (seconds)
    self.WEIGHT_LIMIT = 2000                          # weight limit (pounds)
    self.SPEED_LIMIT = 5                              # upper limit for movement speed (feet/second)
    self.DEFAULT_EMERGENCY_CONTACT = 911              # default emergency contact phone number
    self.LOCAL_FIRE_DEPT_CONTACT = 0000000000         # fire / rescue phone number

    # maintenance info
    self.total_travel_time = 0                        # total travel time
    self.trip_travel_time = 0                         # travel time for a single trip (can be multiple floors)
    self.total_brake_time = 0                         # total time brakes have been applied
    self.total_travel_time = 0                        # distance elevator has traveled
    self.travel_time_since_last_cable_change = 0      # distance elevator has traveled since changing cable
    self.date_last_cable_change = None                # date of last cable change
    self.date_last_maintenance = None                 # date of last maintenance (of any sort)

    # safety info
    self.weight_limit_exceeded = False                # weight limit exceeded
    self.smoke_alarm_activated = False                # smoke alarm activated

    # floor info
    self.starting_floor = 1                           # value to default to when recovering from power loss
    self.current_floor = None                         # where elevator is current at (changes during travel)
    self.available_floors = list(range(1, 101))       # all available floors in building (1-100)
    self.inactive_floors = []                         # floors closed for maintenance, other issues
    self.floors_to_visit = []                         # floors elevator is actively moving to

    # door info
    self.door_is_open = False                         # door is open
    self.door_is_closed = False                       # door is closed
    self.door_is_opening = False                      # door is opening
    self.door_is_closing = False                      # door is closing
    self.door_obstruction_detected = False            # person / object in path of door
    self.door_error_detected = False                  # catch-all for any door sensor

    # movement info
    self.elevator_is_stopped = True
    self.elevator_is_moving = False
    self.elevator_is_moving_upward = False
    self.elevator_is_moving_downward = False
    self.elevator_movement_error_detected = False
    self.current_speed = 0
    self.current_brake_pressure = 0.0

    # entertainment
    self.music_playlist = []
    self.advertisement_playlist = []



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




