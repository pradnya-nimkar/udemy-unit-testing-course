import unittest
from challenge import Car


class EasyTestCase(unittest.TestCase):

    def setUp(self):
        # Todo: create an object named car from the Car class
        # Todo: use the object car to start the car.
        self.car = Car() 
        #self.car._start_car = True # so car is always running at the beginnning of each test function
        
    def test_easy_input(self):
        # Todo: use the object car to add speed 4 times.
        # Todo: make sure that the current speed is 20.
        for _ in range(0,4):
            self.car.add_speed()
        self.assertEqual(self.car._speed, 20)
        self.assertEqual(self.car.current_speed(), 20)

    def test_easy_input_two(self):
        # Todo: use the object car to add speed 2 times.
        # Todo: use the object car to stop the car.
        # Todo: make sure that the current speed is 0 not -10.
        for _ in range(0,2):
            self.car.add_speed()
        self.car.stop()
        self.assertEqual(self.car._speed, 0)
        self.assertNotEqual(self.car._speed, -10)
        
        
    def tearDown(self):
        # Todo: stop the car.
        # Todo: turn off the car.
        # Todo: set the object car to None.
        self.car.stop() # stops the car
        self.car.turn_off_car() # turn off the car
        self.car = None

class MediumTestCase(unittest.TestCase):

    def setUp(self):
        # Todo: create an object named car from the Car class
        # Todo: use the object car to start the car.
        self.car = Car()
        self.car._start_car = True

    def test_medium_input(self):
        # Todo: raise an exception if the user tried to start the car while it's already on.
        # My Notes: The function should have code to raise an exception, 
        # The unit test should make sure function raises an exception when it should
        # in this case,    
        self.car._start_car = True # making sure car is on. 
        with self.assertRaises(Exception): # 
            self.car.start_car()

    def test_medium_input_two(self):
        # Todo: use the object car to remove(my question?) speed 4 times.
        # Todo: raise an exception if the user tried to turn off the car in a speed greater than 0.
        for _ in range(0,4):
            self.car.add_speed() # speed is 20
        with self.assertRaises(Exception):
            self.car.turn_off_car()
            

    def tearDown(self):
        # Todo: stop the car.
        # Todo: turn off the car.
        # Todo: set the object car to None.
        pass


class HardTestCase(unittest.TestCase):

    def setUp(self):
        # Todo: create an object named car from the Car class
        # Todo: use the object car to start the car.
        self.car = Car()
        self.car.start_car()

    def test_hard_input(self):
        # Todo: use the object car to add speed 2 times.
        # Todo: use the object car to remove speed 4 times.
        # Todo: make sure that the current speed is 0. 
        for _ in range(0,2):
            self.car.add_speed()
    
        for _ in range(0,4):
            self.car.remove_speed() # need to update the remove method:done
            
        self.assertEqual(self.car._speed, 0)
        self.assertEqual(self.car.current_speed(), 0)

    def test_hard_input_two(self):
        # Todo: use the object car to add speed 2 times.
        # Todo: stop the car.
        # Todo: stop the car.
        # Todo: stop the car.
        # Todo: make sure that the current speed is 0.
        self.car.add_speed()
        self.car.add_speed()
        self.car.stop()
        self.assertEqual(self.car.current_speed(), 0)
        

    def tearDown(self):
        # Todo: stop the car.
        # Todo: turn off the car.
        # Todo: set the object car to None.
        self.car.stop() # stops the car
        self.car.turn_off_car() # turn off the car
        self.car = None

if __name__ == '__main__':
    unittest.main()
