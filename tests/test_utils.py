import unittest

from helpers.utils import (
    remove_duplicated_space_and_line_breaks_from_cnj_input,
    remove_special_symbols_from_string,
    is_cnj_format_valid,
    remove_special_symbols_from_cnj,
    find_court_from_cnj,
)


class TestUtils(unittest.TestCase):
    def test_remove_duplicate_space_and_line_breaks_from_cnj(self):
        given = "      0710802-55." "2018.8.02.0001  "
        expected = "0710802-55.2018.8.02.0001"
        result = remove_duplicated_space_and_line_breaks_from_cnj_input(given)
        self.assertEqual(expected, result)

    def test_remove_tabulation_and_break_lines_from_cnj(self):
        given = "\n\tLorem\t\t\t\n Ipsum\t\t\t"
        expected = "Lorem Ipsum"
        result = remove_special_symbols_from_string(given)
        self.assertEqual(expected, result)

    def test_given_cnj_check_if_its_on_valid_format(self):
        result = is_cnj_format_valid("0710802-55.2018.8.02.0001")
        self.assertTrue(result)

    def test_given_cnj_check_if_its_on_invalid_format(self):
        result = is_cnj_format_valid("0710802-55.2018.8.02.00011")
        self.assertFalse(result)

    def test_given_cnj_remove_special_symbols_from_it(self):
        expected = "07108025520188020001"
        result = remove_special_symbols_from_cnj("0710802-55.2018.8.02.0001")
        self.assertEqual(expected, result)

    def test_given_cnj_return_only_court_code(self):
        # given
        cnj = "0710802-55.2018.8.02.0001"
        expected = "8.02"

        result = find_court_from_cnj(cnj)
        self.assertEqual(expected, result)


if __name__ == "__main__":
    unittest.main()
