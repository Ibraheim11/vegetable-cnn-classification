"""Static checks for the complete notebook, without requiring TensorFlow or Kaggle data."""
import ast
import json
from pathlib import Path
import unittest

NOTEBOOK = Path(__file__).resolve().parents[1] / "notebooks" / "vegetable_cnn_classification.ipynb"


def read_notebook():
    return json.loads(NOTEBOOK.read_text(encoding="utf-8"))


class CNNNotebookContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.nb = read_notebook()
        cls.cells = [c for c in cls.nb["cells"] if c["cell_type"] == "code"]
        cls.source = "\n".join("".join(c["source"]) for c in cls.cells)

    def test_notebook_syntax(self):
        self.assertEqual(self.nb["nbformat"], 4)
        self.assertEqual(len({c["id"] for c in self.nb["cells"]}), len(self.nb["cells"]))
        for cell in self.cells:
            ast.parse("".join(cell["source"]))
            self.assertIsNone(cell["execution_count"])
            self.assertEqual(cell["outputs"], [])

    def test_imports_in_first_code_cell(self):
        first = "".join(self.cells[0]["source"])
        for expected in ("import tensorflow as tf", "import numpy as np", "import pandas as pd",
                         "import matplotlib.pyplot as plt", "ImageDataGenerator",
                         "Sequential", "EarlyStopping"):
            self.assertIn(expected, first)

    def test_augmentation_and_split(self):
        for expected in ("rescale=1.0 / 255.0", "rotation_range=20",
                         "width_shift_range=0.1", "height_shift_range=0.1",
                         "shear_range=0.1", "zoom_range=0.1",
                         "horizontal_flip=True", "validation_split=VALIDATION_SPLIT",
                         'subset="training"', 'subset="validation"',
                         'target_size=IMAGE_SIZE', 'batch_size=BATCH_SIZE',
                         'class_mode="categorical"', "seed=SEED"):
            self.assertIn(expected, self.source)
        self.assertIn('VALIDATION_SPLIT = 0.20', self.source)
        self.assertIn("NUM_CLASSES = 15", self.source)
        self.assertIn("IMAGE_SIZE = (224, 224)", self.source)
        self.assertIn("BATCH_SIZE = 32", self.source)

    def test_model_architecture_and_compile(self):
        for expected in ("Conv2D(32", "Conv2D(64", "Conv2D(128",
                         "MaxPooling2D", "Flatten()", "Dense(512",
                         "Dropout(0.5)", "Dense(NUM_CLASSES",
                         'activation="softmax"', "optimizer=Adam()",
                         'loss="categorical_crossentropy"',
                         'metrics=["accuracy"]'):
            self.assertIn(expected, self.source)

    def test_training_callbacks_and_evaluation(self):
        for expected in ('MAX_EPOCHS = 20', 'monitor="val_loss"',
                         'patience=5', 'restore_best_weights=True',
                         'epochs=MAX_EPOCHS', "model.fit(", "model.evaluate(",
                         'history.history["accuracy"]', 'history.history["val_accuracy"]',
                         'history.history["loss"]', 'history.history["val_loss"]'):
            self.assertIn(expected, self.source)

    def test_holdout_untouched_and_export(self):
        for expected in ("set(train_ds.filepaths).isdisjoint(set(val_ds.filepaths))",
                         'directory=str(VALIDATION_DIR)', 'directory=str(TEST_DIR)',
                         "training_history.csv", "evaluation_metrics.csv"):
            self.assertIn(expected, self.source)


if __name__ == "__main__":
    unittest.main()
