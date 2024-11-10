import unittest


class Runner:
    def __init__(self, name, speed=5):

        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament(Runner):
    def __init__(self, distance, name, *participants):
        super().__init__(name)
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.run_1 = Runner and Tournament('Усэйн', 10)
        self.run_2 = Runner and Tournament('Андрей', 9)
        self.run_3 = Runner and Tournament('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for key, value in cls.all_results.items():
            print(value)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tournament_1(self):
        t1 = Tournament(90, self.run_1, self.run_3)
        t1_result = t1.start()
        TournamentTest.all_results['1'] = t1_result
        self.assertTrue(t1_result, 'Ник')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tournament_2(self):
        t2 = Tournament(90, self.run_2, self.run_3)
        t2_result = t2.start()
        TournamentTest.all_results['2'] = t2_result
        self.assertTrue(t2_result, 'Ник')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tournament_3(self):
        t3 = Tournament(90, self.run_1, self.run_2, self.run_3)
        t3_result = t3.start()
        TournamentTest.all_results['3'] = t3_result
        self.assertTrue(t3_result, 'Ник')


class RunnerTest(unittest.TestCase):
    is_frozen = False

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


if __name__ == "__main__":
    unittest.main()
