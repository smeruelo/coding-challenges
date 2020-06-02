import unittest

from satellite import tree_from_traversals

# Tests adapted from `problem-specifications//canonical-data.json` @ v2.0.0


class SatelliteTest(unittest.TestCase):
    def test_empty_tree(self):
        preorder = []
        inorder = []

        expected = {}
        self.assertEqual(tree_from_traversals(preorder, inorder), expected)

    def test_tree_with_one_item(self):
        preorder = ["a"]
        inorder = ["a"]

        expected = {"v": "a", "l": {}, "r": {}}
        self.assertEqual(tree_from_traversals(preorder, inorder), expected)

    def test_tree_with_many_items(self):
        preorder = ["a", "i", "x", "f", "r"]
        inorder = ["i", "a", "f", "x", "r"]

        expected = {
            "v": "a",
            "l": {"v": "i", "l": {}, "r": {}},
            "r": {
                "v": "x",
                "l": {"v": "f", "l": {}, "r": {}},
                "r": {"v": "r", "l": {}, "r": {}},
            },
        }
        self.assertEqual(tree_from_traversals(preorder, inorder), expected)

    def test_bigger_tree(self):
        preorder = ["a", "m", "n", "o", "p", "q", "x", "f", "r"]
        inorder = ["n", "m", "p", "o", "q", "a", "f", "x", "r"]

        expected = {
            "v": "a",
            "l": {
                "v": "m",
                "l": {"v": "n", "l": {}, "r": {}},
                "r": {
                    "v": "o",
                    "l": {"v": "p", "l": {}, "r": {}},
                    "r": {"v": "q", "l": {}, "r": {}},
                },
            },
            "r": {
                "v": "x",
                "l": {"v": "f", "l": {}, "r": {}},
                "r": {"v": "r", "l": {}, "r": {}},
            },
        }
        self.assertEqual(tree_from_traversals(preorder, inorder), expected)

    def test_reject_traversals_of_different_length(self):
        preorder = ["a", "b"]
        inorder = ["b", "a", "r"]

        with self.assertRaisesWithMessage(ValueError):
            tree_from_traversals(preorder, inorder)

    def test_reject_inconsistent_traversals_of_same_length(self):
        preorder = ["x", "y", "z"]
        inorder = ["a", "b", "c"]

        with self.assertRaisesWithMessage(ValueError):
            tree_from_traversals(preorder, inorder)

    def test_reject_traversals_with_repeated_items(self):
        preorder = ["a", "b", "a"]
        inorder = ["b", "a", "a"]

        with self.assertRaisesWithMessage(ValueError):
            tree_from_traversals(preorder, inorder)

    # Utility functions
    def assertRaisesWithMessage(self, exception):
        return self.assertRaisesRegex(exception, r".+")


if __name__ == "__main__":
    unittest.main()
