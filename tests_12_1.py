import unittest


class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        run_1 = Runner('Ivan')
        for i in range(10):
            run_1.walk()
        self.assertEqual(run_1.distance, 50)

    def test_run(self):
        run_2 = Runner('Boris')
        for i in range(10):
            run_2.run()
        self.assertEqual(run_2.distance, 100)

    def test_challenge(self):
        run_1 = Runner('Иван')
        run_2 = Runner('Борис')
        for i in range(10):
            run_1.run()
            run_2.walk()
        self.assertNotEqual(run_2.distance, run_1.distance)


if __name__ == '__main__':
    unittest.main()
