from unittest.case import TestCase
from unittest.main import main
from unittest import TestCase, main
#from utils import to_str

class AssertTestCase(TestCase):
    def second_test(self):
        excepted = 12
        found = 2*5
        self.assertEqual(excepted, found)

    def first_test(self):
        expected = 12
        found = 2*5
        assert expected == found

    


if __name__ == "__main__":
    main()