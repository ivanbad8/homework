import unittest
import tests_12_3

test1 = unittest.TestSuite()
test1.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))
test1.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))
runner = unittest.TextTestRunner(verbosity=2)
runner.run(test1)

