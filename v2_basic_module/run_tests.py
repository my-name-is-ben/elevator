from modules.elevator import ElevatorSimV2
import unittest


class TestElevatorModule(unittest.TestCase):

  def test_correct_inputs(self):
    sim = ElevatorSimV2(4, [1, 2, 3])
    self.assertEqual(sim.floor_list, [4, 1, 2, 3])
    self.assertEqual(sim.get_total_travel_time(), 50)

  def test_starting_floor_only_accepts_integers(self):
    with self.assertRaises(TypeError):
      sim = ElevatorSimV2('not an int', [1, 2, 3])
    with self.assertRaises(TypeError):
      sim = ElevatorSimV2(['not', 'an', 'int'], [1, 2, 3])
    with self.assertRaises(TypeError):
      sim = ElevatorSimV2([], [1, 2, 3])
    with self.assertRaises(TypeError):
      sim = ElevatorSimV2(None, [1, 2, 3])

  def test_starting_floor_only_accepts_positive_integers(self):
    with self.assertRaises(ValueError):
      sim = ElevatorSimV2(0, [1, 2, 3])
    with self.assertRaises(ValueError):
      sim = ElevatorSimV2(-1, [1, 2, 3])
    with self.assertRaises(ValueError):
      sim = ElevatorSimV2(-74674, [1, 2, 3])

  def test_floor_list_only_accepts_lists(self):
    with self.assertRaises(TypeError):
      sim = ElevatorSimV2(4, 'a')
    with self.assertRaises(TypeError):
      sim = ElevatorSimV2(4, None)
    with self.assertRaises(TypeError):
      sim = ElevatorSimV2(4, 1)
    with self.assertRaises(TypeError):
      sim = ElevatorSimV2(4, 1, 2, 3)

  def test_floor_list_only_accepts_positive_integers(self):
    with self.assertRaises(ValueError):
      sim = ElevatorSimV2(4, [0])
    with self.assertRaises(ValueError):
      sim = ElevatorSimV2(4, [1, 2, 3, -1])
    with self.assertRaises(ValueError):
      sim = ElevatorSimV2(4, [1, 2, 3, 0])
    with self.assertRaises(ValueError):
      sim = ElevatorSimV2(4, [None])
    with self.assertRaises(ValueError):
      sim = ElevatorSimV2(4, [1, 2, 3, None])
    with self.assertRaises(ValueError):
      sim = ElevatorSimV2(4, [1, 2, 3, 'test'])

  def test_travel_time_calculation_is_correct(self):
    sim1 = ElevatorSimV2(4, [])
    self.assertEqual(sim1.get_total_travel_time(), 0)
    sim2 = ElevatorSimV2(1, [2])
    self.assertEqual(sim2.get_total_travel_time(), 10)
    sim2 = ElevatorSimV2(1, [2, 3, 2])
    self.assertEqual(sim2.get_total_travel_time(), 30)
    sim2 = ElevatorSimV2(2, [2, 2, 2])
    self.assertEqual(sim2.get_total_travel_time(), 0)
    sim2 = ElevatorSimV2(1, [100])
    self.assertEqual(sim2.get_total_travel_time(), 990)


if __name__ == '__main__':
  unittest.main()





# print('elevator_sim_1')
# elevator_sim_1 = ElevatorSimV2(4, [1, 2, 3])
# print(elevator_sim_1.get_total_travel_time(), elevator_sim_1.get_floor_list())

# print('elevator_sim_2')
# elevator_sim_2 = ElevatorSimV2(4, [])
# print(elevator_sim_2.get_total_travel_time(), elevator_sim_2.get_floor_list())