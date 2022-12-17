import unittest

from task1 import *


class TestConverter(unittest.TestCase):

    def test_prepare_md_titles(self):
        data = '# title Hello world\n# description Some description'
        title, description = prepare_md_titles(data)
        self.assertEqual(title, 'Hello world')
        self.assertEqual(description, 'Some description')

    def test_prepare_md_titles_with_empty_data(self):
        data = ''
        title, description = prepare_md_titles(data)
        self.assertEqual(title, None)
        self.assertEqual(description, None)

    def test_prepare_md_titles_with_extra_data(self):
        data = '# title Hello world\n# description Some description\n# tag set, list'
        title, description = prepare_md_titles(data)
        self.assertEqual(title, 'Hello world')
        self.assertEqual(description, 'Some description')

    def test_prepare_md_link(self):
        data = "MERGE TWO LISTS"
        new_md_link = prepare_md_link(data)
        self.assertEqual(new_md_link, '+ [MERGE TWO LISTS](#merge-two-lists)')

    def test_prepare_md_format(self):
        title = "Hello World"
        description = "Print 'hello, world!'"
        source_code = "def HelloWorld():\n\tprint('hello, world!')"
        answer = prepare_md_format(title, description, source_code)
        self.assertEqual(answer, "## Hello World\n\nPrint 'hello, world!'\n\n```python\ndef HelloWorld():\n\tprint('hello, world!')\n```")

    def test_convert_data_with_empty_old_content(self):
        data = "# title Hello World\n# description Print 'hello, world!'\n# ---end----\n\ndef HelloWorld():\n\tprint('hello, world!')"
        old_md_content = ''
        answer = "+ [Hello World](#hello-world)\n--------------------------------\n\n## Hello World\n\nPrint 'hello, world!'\n\n```python\ndef HelloWorld():\n\tprint('hello, world!')\n```"
        converted = convert_data(data, old_md_content)
        self.assertEqual(converted, answer)
    def test_convert_data_with_old_content(self):
        data = "# title Print World\n# description Print 'world'\n# ---end----\n\ndef world():\n\tprint('world')"
        old_md_content = "+ [Print Hello](#print-hello)\n--------------------------------\n\n## Print Hello\n\nPrint 'hello'\n\n```python\ndef Hello():\n\tprint('hello')\n```"
        answer = "+ [Print Hello](#print-hello)\n+ [Print World](#print-world)\n--------------------------------\n\n## Print Hello\n\nPrint 'hello'\n\n```python\ndef Hello():\n\tprint('hello')\n```\n\n## Print World\n\nPrint 'world'\n\n```python\ndef world():\n\tprint('world')\n```"
        converted = convert_data(data, old_md_content)
        self.assertEqual(converted, answer)



if __name__ == "__main__":
    unittest.main()