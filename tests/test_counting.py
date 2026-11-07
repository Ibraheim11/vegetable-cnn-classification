"""Validate the notebook and test its actual counter without third-party imports."""
import ast
import json
from pathlib import Path
import tempfile
import unittest


NOTEBOOK = Path(__file__).resolve().parents[1] / 'notebooks' / 'vegetable_cnn_classification.ipynb'


def load_notebook():
    return json.loads(NOTEBOOK.read_text(encoding='utf-8'))


def load_counter():
    for cell in load_notebook()['cells']:
        if cell['cell_type'] == 'code':
            tree = ast.parse(''.join(cell['source']))
            for node in tree.body:
                if isinstance(node, ast.FunctionDef) and node.name == 'count_images':
                    namespace = {'Path': Path}
                    exec(compile(ast.Module(body=[node], type_ignores=[]), str(NOTEBOOK), 'exec'), namespace)
                    return namespace['count_images']
    raise AssertionError('Notebook must define count_images')


class PhaseOneTests(unittest.TestCase):
    def test_notebook_structure_and_syntax(self):
        notebook = load_notebook()
        self.assertEqual(notebook['nbformat'], 4)
        self.assertEqual(notebook['metadata']['kernelspec']['name'], 'python3')
        codes = [c for c in notebook['cells'] if c['cell_type'] == 'code']
        self.assertTrue(codes)
        for cell in codes:
            compile(''.join(cell['source']), str(NOTEBOOK), 'exec')
            self.assertEqual(cell['outputs'], [])
            self.assertIsNone(cell['execution_count'])
        imports = ast.parse(''.join(codes[0]['source']))
        self.assertTrue(any(isinstance(n, ast.Import) for n in imports.body))

    def test_counts_extensions_empty_classes_and_nonrecursive_behavior(self):
        count_images = load_counter()
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / 'Carrot').mkdir()
            (root / 'Bean').mkdir()
            for name in ['one.jpg', 'two.PNG', 'three.JpEg', 'notes.txt']:
                (root / 'Carrot' / name).touch()
            (root / 'loose.jpg').touch()
            (root / 'Carrot' / 'nested').mkdir()
            (root / 'Carrot' / 'nested' / 'ignored.jpg').touch()
            (root / 'Carrot' / 'directory.jpg').mkdir()
            self.assertEqual(count_images(root), {'Bean': 0, 'Carrot': 3})
            self.assertEqual(list(count_images(root)), ['Bean', 'Carrot'])

    def test_missing_path_and_file_path_raise(self):
        count_images = load_counter()
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            with self.assertRaises(FileNotFoundError):
                count_images(root / 'missing')
            file = root / 'file.txt'
            file.touch()
            with self.assertRaises(NotADirectoryError):
                count_images(file)

    def test_no_class_folders_raises(self):
        with tempfile.TemporaryDirectory() as directory:
            with self.assertRaises(ValueError):
                load_counter()(Path(directory))


if __name__ == '__main__':
    unittest.main()
