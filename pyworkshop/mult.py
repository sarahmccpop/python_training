import unittest


def multiply(x, y):
    return x + y


# usually tests live in a test file, or module, not inline


class TestMultiply(unittest.TestCase):

    # unit test methods need to start with test_ or they won't run
    def test_multiply(self):
        test_x = 5
        test_y = 10
        self.assertEqual(multiply(test_x, test_y), 50)


# if __name__ == "__main__":
#     unittest.main()

# run this in command line  python -m unittest mult -v
