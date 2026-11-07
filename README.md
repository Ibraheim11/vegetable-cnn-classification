# Vegetable Image Classification Using CNN

Phase 1 establishes a reproducible project and explores the class distribution of the [Vegetable Image Dataset on Kaggle](https://www.kaggle.com/datasets/misrakahmed/vegetable-image-dataset). Augmentation, model construction, training, and evaluation are outside this phase.

## Files

- `notebooks/vegetable_cnn_classification.ipynb`: explained, numbered setup and EDA workflow.
- `tests/test_counting.py`: lightweight synthetic tests of the notebook's actual counting function.
- `requirements.txt`: notebook dependencies.
- `AGENTS.md`: project conventions and scope.

## Run on Kaggle

1. Create a Kaggle notebook and import `notebooks/vegetable_cnn_classification.ipynb`.
2. Use **Add Input** to attach the dataset linked above.
3. Check that the attached dataset contains `train`, `test`, and `validation` folders. The notebook detects their common parent automatically under `/kaggle/input`, even if Kaggle mounts an extra nesting level. If no unique match exists, inspect the Input browser and correct the selected dataset.

4. Run all cells in order. A GPU is unnecessary. Kaggle normally provides the required libraries; install `requirements.txt` only if dependencies are missing.
5. Review split totals, detected classes, the merged count table, the grouped chart, and the balance report generated from observed counts.

The repository notebook intentionally contains no stored outputs. Counts are computed at runtime; no dataset statistics or model metrics are claimed here. The counter counts supported image filenames directly inside each class directory, without decoding images or recursively traversing subdirectories. It reports file counts, not verified usable images. Empty classes are retained, and classes missing from a split appear with zero counts in the merged table and a warning.

## Local setup and checks

Python 3.10 or later is recommended.

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m unittest discover -s tests -v
jupyter notebook notebooks/vegetable_cnn_classification.ipynb
```

The tests use temporary synthetic filenames and require only the Python standard library. They check notebook structure and code syntax as well as counting behavior. Running the dataset cells locally without Kaggle input intentionally raises a descriptive error. Do not download the image dataset into this repository.

## Next phase

After running Phase 1 on Kaggle, review the observed distribution and class consistency. Agree on a separate preprocessing and model-training plan before extending the project.
