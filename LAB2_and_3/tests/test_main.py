import unittest
import json
from main import load_data, save_output

class TestMain(unittest.TestCase):
    def test_load_data(self):
        data = load_data('input.json')
        self.assertIn('ports', data)
        self.assertIn('ships', data)
        self.assertIn('containers', data)

    def test_save_output(self):
        output = {"test": "data"}
        save_output(output, 'test_output.json')
        with open('test_output.json', 'r') as file:
            saved_data = json.load(file)
        self.assertEqual(output, saved_data)

if __name__ == '__main__':
    unittest.main()
