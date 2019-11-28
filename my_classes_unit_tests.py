import unittest
from my_classes import child_class

class child_class_tests(unittest.TestCase):

    # set up method for the whole class
    def setUp(self):
        self.child_1 = child_class('wagner')

    # test constructor
    def test_local_var_1_is_set(self):
        self.assertTrue(self.child_1.local_var_1)

    # test case for method : concat_to_local_var(text)
    def test_concat_to_local_var(self):
        actual = self.child_1.concat_to_local_var(' is cool')

        expected = 'wagner is cool'

        self.assertEqual(actual, expected)

    # test case for exception
    def test_throws_exception(self):
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            self.child_1.concat_to_local_var(5)

# run test cases in main app
if __name__ == '__main__':
    unittest.main()

# run tests in a specific class
#suite = unittest.TestLoader().loadTestsFromTestCase(child_class_tests)
#unittest.TextTestRunner(verbosity=2).run(suite)