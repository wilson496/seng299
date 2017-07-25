
import unittest

from mothership.base import MothershipServer


class TestMothershipBasic(unittest.TestCase):


    def test_mothership_intialization(self):
        """
        Purpose: Test regular running of mothership
        Expectation: starts instance of mothership

        :precondition: Mothership server not running
        :return:
        """
        mothership = MothershipServer()

        mothership.run()

        worker = BasicUserParseWorker("https://www.reddit.com/user/Chrikelnel")

        # Can't connect to mother, so should raise ConnectionRefusedError, but should run everything else
        self.assertRaises(ConnectionRefusedError, mothership.run)


    def test_worker_contact(arg):

        mothership = MothershipServer()

        worker = BasicUserParseWorker("https://www.reddit.com/user/Chrikelnel")

        # Can't connect to mother, so should raise ConnectionRefusedError, but should run everything else
        self.assertRaises(ConnectionRefusedError, mothership.run)

        mothership.handle_worker_contact(self, worker, "127.0.0.1")


    def fname(arg):
        pass
