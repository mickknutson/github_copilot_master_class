import unittest
from program import Program

class TestProgram(unittest.TestCase):
    def setUp(self):
        self.program = Program()

    def test_log_startup(self):
        # Test that log_startup method logs the correct message
        expected_message = "Application starting up..."
        self.program.log_startup()
        self.assertIn(expected_message, self.program.logger.get_logs())

    def test_load_json(self):
        # Test that load_json method reads the JSON file correctly
        expected_course_title = "Python Course"
        expected_num_engagements = 3

        self.program.load_json()

        # Check if the course title is correct
        self.assertEqual(expected_course_title, self.program.logger.get_logs()[-1])

        # Check if the number of engagements is correct
        self.assertIn(f"Number of engagements: {expected_num_engagements}", self.program.logger.get_logs())

    def test_load_csv(self):
        # Test that load_csv method reads the CSV file correctly
        expected_rupee_per_usd = 60

        self.program.load_csv()

        # Check if the rupee per USD value is correct
        self.assertIn(f"1 USD is worth {expected_rupee_per_usd} Rupees.", self.program.logger.get_logs())

if __name__ == '__main__':
    unittest.main()