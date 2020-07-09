"""
Unit Test for pretty_print_json
"""
from unittest import TestCase

from problems.string.pretty_print_json import PrettyPrintJSON


class TestPrettyPrintJSON(TestCase):
    """
    Unit test for PrettyPrintJSON
    """

    def test_solve(self):
        """Test solve

        Args:
            self: TestPrettyPrintJSON

        Returns:
            None

        Raises:
            None
        """
        # Given
        input_string = '{"id": "0001","type": "donut","name": "Cake","ppu": 0.55,"batters":{"batter":[{ "id": "1001", "type": "Regular" },{ "id": "1002", "type": "Chocolate" }]},"topping":[{ "id": "5001", "type": "None" },{ "id": "5002", "type": "Glazed" }]}'

        pretty_print_problem = PrettyPrintJSON(input_string)

        # When
        result = pretty_print_problem.solve()

        # Then
        self.assertEqual(result, '''{
 "id": "0001",
 "type": "donut",
 "name": "Cake",
 "ppu": 0.55,
 "batters":
 {
  "batter":
  [
   {
     "id": "1001",
     "type": "Regular" 
   },
   {
     "id": "1002",
     "type": "Chocolate" 
   }
  ]
 },
 "topping":
 [
  {
    "id": "5001",
    "type": "None" 
  },
  {
    "id": "5002",
    "type": "Glazed" 
  }
 ]
}
''')
