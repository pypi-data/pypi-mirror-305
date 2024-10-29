# tests/test_validators.py

import unittest
from unittest.mock import patch
from path_friendly_filename_generator.validators import (
    contains_invalid_characters,
    is_too_long,
    is_reserved_name,
    is_valid_filename
)
from path_friendly_filename_generator.exceptions import PathFriendlyFilenameGeneratorError

class TestValidators(unittest.TestCase):

    @patch('path_friendly_filename_generator.validators.get_invalid_characters')
    def test_contains_invalid_characters(self, mock_invalid_chars):
        mock_invalid_chars.return_value = set('<>:"/\\|?*')
        self.assertTrue(contains_invalid_characters('file<name>.txt'))
        self.assertFalse(contains_invalid_characters('filename.txt'))
        self.assertTrue(contains_invalid_characters('invalid|name'))
        self.assertFalse(contains_invalid_characters('valid_name'))

    @patch('path_friendly_filename_generator.validators.get_max_filename_length')
    def test_is_too_long(self, mock_max_length):
        mock_max_length.return_value = 10
        self.assertTrue(is_too_long('abcdefghijk'))  # 11 chars > 10
        self.assertFalse(is_too_long('abcdef'))      # 6 chars <= 10

    @patch('path_friendly_filename_generator.validators.get_reserved_names')
    def test_is_reserved_name_windows(self, mock_reserved_names):
        mock_reserved_names.return_value = {'CON', 'PRN', 'AUX', 'NUL', 'COM1', 'LPT1'}

        self.assertTrue(is_reserved_name('CON'))
        self.assertTrue(is_reserved_name('PRN.txt'))
        self.assertTrue(is_reserved_name('COM1.doc'))
        self.assertFalse(is_reserved_name('normal.txt'))
        self.assertFalse(is_reserved_name('CON1'))

    @patch('path_friendly_filename_generator.validators.get_reserved_names')
    def test_is_reserved_name_other_os(self, mock_reserved_names):
        mock_reserved_names.return_value = {'CON', 'NUL'}

        self.assertTrue(is_reserved_name('CON'))
        self.assertTrue(is_reserved_name('nul.txt'))
        self.assertFalse(is_reserved_name('normal.txt'))
        self.assertFalse(is_reserved_name('CON1'))

    @patch('path_friendly_filename_generator.validators.is_reserved_name')
    @patch('path_friendly_filename_generator.validators.is_too_long')
    @patch('path_friendly_filename_generator.validators.contains_invalid_characters')
    def test_is_valid_filename(self, mock_contains_invalid, mock_is_too_long, mock_is_reserved):
        mock_contains_invalid.return_value = False
        mock_is_too_long.return_value = False
        mock_is_reserved.return_value = False

        self.assertTrue(is_valid_filename('valid_filename.txt'))

        mock_contains_invalid.return_value = True
        self.assertFalse(is_valid_filename('invalid|name.txt'))
        mock_contains_invalid.return_value = False

        mock_is_too_long.return_value = True
        self.assertFalse(is_valid_filename('a' * 300 + '.txt'))
        mock_is_too_long.return_value = False

        mock_is_reserved.return_value = True
        self.assertFalse(is_valid_filename('CON.txt'))
        mock_is_reserved.return_value = False

        self.assertFalse(is_valid_filename(''))
        self.assertFalse(is_valid_filename('   '))
        self.assertFalse(is_valid_filename(' . . '))

    def test_is_valid_filename_spaces_and_dots(self):
        from path_friendly_filename_generator.validators import is_valid_filename
        self.assertFalse(is_valid_filename(' . . '))
        self.assertFalse(is_valid_filename('   .   '))

    def test_is_valid_filename_unicode(self):
        from path_friendly_filename_generator.validators import is_valid_filename
        self.assertTrue(is_valid_filename('文件_名__测试_.txt'))
        self.assertFalse(is_valid_filename('文件<>名?.txt'))

    # ====================== New Test Cases ======================

    def test_is_valid_filename_unicode_only(self):
        from path_friendly_filename_generator.validators import is_valid_filename
        self.assertTrue(is_valid_filename('测试文件.txt'))
        self.assertFalse(is_valid_filename('测试<>文件?.txt'))

    def test_is_valid_filename_none_input(self):
        from path_friendly_filename_generator.validators import is_valid_filename
        self.assertFalse(is_valid_filename(None))

    def test_is_valid_filename_empty_string(self):
        from path_friendly_filename_generator.validators import is_valid_filename
        self.assertFalse(is_valid_filename(''))

    # ============================================================

if __name__ == '__main__':
    unittest.main()
