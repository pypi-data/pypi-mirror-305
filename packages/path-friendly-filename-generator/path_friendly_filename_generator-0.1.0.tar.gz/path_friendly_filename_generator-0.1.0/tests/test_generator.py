import unittest
from unittest.mock import patch
from path_friendly_filename_generator.generator import make_filename_safe
from path_friendly_filename_generator.exceptions import InvalidReplacementCharacterError

class TestGenerator(unittest.TestCase):

    @patch('path_friendly_filename_generator.generator.get_reserved_names')
    @patch('path_friendly_filename_generator.generator.get_max_filename_length')
    @patch('path_friendly_filename_generator.generator.get_invalid_characters')
    def test_make_filename_safe_windows(self, mock_invalid_chars, mock_max_length, mock_reserved_names):
        mock_invalid_chars.return_value = set('<>:"/\\|?*')
        mock_max_length.return_value = 255
        mock_reserved_names.return_value = {'CON', 'PRN', 'AUX', 'NUL', 'COM1', 'LPT1'}

        original = 'example<file>:name?.txt'
        expected = 'example_file_name_.txt'
        result = make_filename_safe(original)
        self.assertEqual(result, expected)

        original_reserved = 'CON.txt'
        expected_reserved = 'CON_reserved.txt'
        result_reserved = make_filename_safe(original_reserved)
        self.assertEqual(result_reserved, expected_reserved)

        long_name = 'a' * 300 + '.txt'
        expected_trimmed = 'a' * (255 - 4) + '.txt'  # 251 'a's + '.txt'
        result_trimmed = make_filename_safe(long_name)
        self.assertEqual(len(result_trimmed), 255)
        self.assertTrue(result_trimmed.endswith('.txt'))

    @patch('path_friendly_filename_generator.generator.get_reserved_names')
    @patch('path_friendly_filename_generator.generator.get_max_filename_length')
    @patch('path_friendly_filename_generator.generator.get_invalid_characters')
    def test_make_filename_safe_linux(self, mock_invalid_chars, mock_max_length, mock_reserved_names):
        mock_invalid_chars.return_value = {'/', '\0'}
        mock_max_length.return_value = 255
        mock_reserved_names.return_value = {'CON', 'NUL'}

        original = 'example/file\0name.txt'
        expected = 'example_file_name.txt'
        result = make_filename_safe(original)
        self.assertEqual(result, expected)

        long_name = 'a' * 300 + '.txt'
        expected_trimmed = 'a' * (255 - 4) + '.txt'  # 251 'a's + '.txt'
        result_trimmed = make_filename_safe(long_name)
        self.assertEqual(len(result_trimmed), 255)
        self.assertTrue(result_trimmed.endswith('.txt'))

    @patch('path_friendly_filename_generator.generator.get_reserved_names')
    @patch('path_friendly_filename_generator.generator.get_max_filename_length')
    @patch('path_friendly_filename_generator.generator.get_invalid_characters')
    def test_make_filename_safe_freebsd(self, mock_invalid_chars, mock_max_length, mock_reserved_names):
        mock_invalid_chars.return_value = {'/', '\0'}
        mock_max_length.return_value = 255
        mock_reserved_names.return_value = {'CON', 'NUL'}

        original = 'example/file\0name.txt'
        expected = 'example_file_name.txt'
        result = make_filename_safe(original)
        self.assertEqual(result, expected)

        long_name = 'a' * 300 + '.txt'
        expected_trimmed = 'a' * (255 - 4) + '.txt'  # 251 'a's + '.txt'
        result_trimmed = make_filename_safe(long_name)
        self.assertEqual(len(result_trimmed), 255)
        self.assertTrue(result_trimmed.endswith('.txt'))

    @patch('path_friendly_filename_generator.generator.get_reserved_names')
    @patch('path_friendly_filename_generator.generator.get_max_filename_length')
    @patch('path_friendly_filename_generator.generator.get_invalid_characters')
    def test_make_filename_safe_solaris(self, mock_invalid_chars, mock_max_length, mock_reserved_names):
        mock_invalid_chars.return_value = {'/', '\0'}
        mock_max_length.return_value = 255
        mock_reserved_names.return_value = {'CON', 'NUL'}

        original = 'example/file\0name.txt'
        expected = 'example_file_name.txt'
        result = make_filename_safe(original)
        self.assertEqual(result, expected)

        long_name = 'a' * 300 + '.txt'
        expected_trimmed = 'a' * (255 - 4) + '.txt'  # 251 'a's + '.txt'
        result_trimmed = make_filename_safe(long_name)
        self.assertEqual(len(result_trimmed), 255)
        self.assertTrue(result_trimmed.endswith('.txt'))

    def test_make_filename_safe_empty_or_whitespace(self):
        from path_friendly_filename_generator.generator import make_filename_safe
        self.assertEqual(make_filename_safe(''), 'untitled')
        self.assertEqual(make_filename_safe('   '), 'untitled')
        self.assertEqual(make_filename_safe(' . . '), 'untitled')

    def test_make_filename_safe_no_extension(self):
        from path_friendly_filename_generator.generator import make_filename_safe
        original = 'example<file>name'
        expected = 'example_file_name'
        result = make_filename_safe(original)
        self.assertEqual(result, expected)

    def test_make_filename_safe_consecutive_replacements(self):
        from path_friendly_filename_generator.generator import make_filename_safe
        original = 'file***name???test'
        expected = 'file_name_test'
        result = make_filename_safe(original)
        self.assertEqual(result, expected)

    def test_make_filename_safe_only_invalid_characters(self):
        from path_friendly_filename_generator.generator import make_filename_safe
        original = '<>:"/\\|?*'
        expected = 'untitled'
        result = make_filename_safe(original)
        self.assertEqual(result, expected)

    def test_make_filename_safe_custom_replacement_char(self):
        from path_friendly_filename_generator.generator import make_filename_safe
        original = 'example<file>:name?.txt'
        expected = 'example-file-name-.txt'
        result = make_filename_safe(original, replacement_char='-')
        self.assertEqual(result, expected)

    def test_make_filename_safe_unicode_characters(self):
        from path_friendly_filename_generator.generator import make_filename_safe
        original = '文件<名>:测试?.txt'
        expected = '文件_名_测试_.txt'
        result = make_filename_safe(original)
        self.assertEqual(result, expected)

    def test_make_filename_safe_multiple_consecutive_invalid_characters(self):
        from path_friendly_filename_generator.generator import make_filename_safe
        original = 'file***name???test.txt'
        expected = 'file_name_test.txt'
        result = make_filename_safe(original)
        self.assertEqual(result, expected)

    def test_make_filename_safe_leading_trailing_invalid_characters(self):
        from path_friendly_filename_generator.generator import make_filename_safe
        original = '***file_name.txt???'
        expected = 'file_name.txt'
        result = make_filename_safe(original)
        self.assertEqual(result, expected)

    def test_make_filename_safe_reserved_names_case_insensitive(self):
        from path_friendly_filename_generator.generator import make_filename_safe
        original = 'CON.TXT'  # Use uppercase 'CON'
        expected = 'CON_reserved.TXT'
        result = make_filename_safe(original)
        self.assertEqual(result, expected)

    def test_make_filename_safe_extremely_long_filename(self):
        from path_friendly_filename_generator.generator import make_filename_safe
        original = 'a' * 300 + '.txt'
        expected = 'a' * 251 + '.txt'  # 251 'a's + '.txt'
        result = make_filename_safe(original)
        self.assertEqual(len(result), 255)
        self.assertTrue(result.endswith('.txt'))

    def test_make_filename_safe_only_replacement_characters(self):
        from path_friendly_filename_generator.generator import make_filename_safe
        original = '___'
        expected = 'untitled'
        result = make_filename_safe(original, replacement_char='_')
        self.assertEqual(result, expected)

    def test_make_filename_safe_mixed_invalid_valid_characters(self):
        from path_friendly_filename_generator.generator import make_filename_safe
        original = 'good<bad>name?.txt'
        expected = 'good_bad_name_.txt'
        result = make_filename_safe(original)
        self.assertEqual(result, expected)

    def test_make_filename_safe_multiple_extensions(self):
        from path_friendly_filename_generator.generator import make_filename_safe
        original = 'archive.tar.gz'
        expected = 'archive.tar.gz'
        result = make_filename_safe(original)
        self.assertEqual(result, expected)

    def test_make_filename_safe_reserved_names_other_os(self):
        from path_friendly_filename_generator.generator import make_filename_safe
        original = 'NUL.txt'  # Use uppercase 'NUL'
        expected = 'NUL_reserved.txt'
        result = make_filename_safe(original)
        self.assertEqual(result, expected)

    def test_make_filename_safe_reserved_names_case_other_os(self):
        from path_friendly_filename_generator.generator import make_filename_safe
        original = 'NUL.txt'
        expected = 'NUL_reserved.txt'
        result = make_filename_safe(original)
        self.assertEqual(result, expected)

    # ====================== New Test Cases ======================

    def test_make_filename_safe_unicode_with_emoji(self):
        from path_friendly_filename_generator.generator import make_filename_safe
        original = '📄file<name>.txt'
        expected = 'file_name_.txt'
        result = make_filename_safe(original)
        self.assertEqual(result, expected)

    def test_make_filename_safe_none_input(self):
        from path_friendly_filename_generator.generator import make_filename_safe
        self.assertEqual(make_filename_safe(None), 'untitled')

    def test_make_filename_safe_invalid_replacement_char(self):
        from path_friendly_filename_generator.generator import make_filename_safe
        with self.assertRaises(InvalidReplacementCharacterError) as context:
            make_filename_safe('example.txt', replacement_char='?')
        self.assertEqual(str(context.exception), "'?' is an invalid replacement character.")

    def test_make_filename_safe_invalid_replacement_char_unicode(self):
        from path_friendly_filename_generator.generator import make_filename_safe
        with self.assertRaises(InvalidReplacementCharacterError) as context:
            make_filename_safe('example.txt', replacement_char='/')
        self.assertEqual(str(context.exception), "'/' is an invalid replacement character.")

    def test_make_filename_safe_legacy_windows(self):
        from path_friendly_filename_generator.generator import make_filename_safe
        original = 'thisisaverylongfilename.txt'
        expected = 'thisisav.txt'  # 8 characters + '.txt'
        result = make_filename_safe(original, legacy_windows=True)
        self.assertEqual(result, expected)

    def test_make_filename_safe_legacy_windows_with_no_extension(self):
        from path_friendly_filename_generator.generator import make_filename_safe
        original = 'thisisaverylongfilename'
        expected = 'thisisav'  # 8 characters
        result = make_filename_safe(original, legacy_windows=True)
        self.assertEqual(result, expected)

    def test_make_filename_safe_legacy_windows_short_filename(self):
        from path_friendly_filename_generator.generator import make_filename_safe
        original = 'short.txt'
        expected = 'short.txt'  # Already compliant
        result = make_filename_safe(original, legacy_windows=True)
        self.assertEqual(result, expected)

    # ============================================================

if __name__ == '__main__':
    unittest.main()
