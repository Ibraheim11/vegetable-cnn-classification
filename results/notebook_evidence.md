# Verified Kaggle notebook execution evidence

The user uploaded an already-executed Kaggle `.ipynb` file named `notebooke3773b98ea.ipynb`. The notebook was inspected directly (all **16 code cells have execution counts and no error outputs**), and its schema was validated using `nbformat.validate`.

This is stronger evidence than the earlier screenshots: it contains the **actual embedded cell outputs and plot images** from the successful run.

## Extracted results

| Evaluation set | Accuracy | Loss |
| --- | ---: | ---: |
| Training subset — unaugmented evaluation | 0.9938 | 0.0224 |
| Internal validation | 0.9847 | 0.0572 |
| Original validation holdout | 0.9850 | 0.0581 |
| Final test holdout | 0.9840 | 0.0692 |

- Finished **20 of 20** configured epochs.
- Best monitored validation loss (full precision printed in notebook): `0.05724012851715088`.
- The Keras model summary reports **44,403,791** trainable parameters.
- Two GPUs detected; TensorFlow version `2.21.0`.
- Original dataset splits: 15,000 train / 3,000 validation / 3,000 test image files; 15 equal-size classes.
- Internal generators: 12,000 train / 3,000 validation.
- The executed notebook includes class-count and augmentation illustrations and both accuracy/loss learning curves.
- EarlyStopping had `monitor="val_loss"`, `patience=5`, and `restore_best_weights=True`, but the training ran all 20 configured epochs.

## Recovered CSV evidence (source: real notebook outputs)

- [`evaluation_metrics_recovered_from_notebook.csv`](evaluation_metrics_recovered_from_notebook.csv) — post-training `model.evaluate` outputs, transcribed from the notebook's printed evaluations. Rounded to 4 decimal places, as printed.
- [`training_history_recovered_from_notebook.csv`](training_history_recovered_from_notebook.csv) — 20 per-epoch accuracy/loss/validation values extracted from the notebook's actual Keras progress logs. Values are rounded to 4 decimal places in the logs.

**Provenance limitation:** these recovered files are **not byte-for-byte the original** `/kaggle/working/evaluation_metrics.csv` and `/kaggle/working/training_history.csv`. The downloaded `.ipynb` confirms that those files were produced, but does not embed their original file contents. Their full-precision numeric data cannot be recovered from four-decimal printed logs. Do not relabel these CSVs as the original Kaggle exports.

The executed notebook can be reviewed from the Kaggle version when it is made public: [Kaggle Notebook](https://www.kaggle.com/code/ibrahemasharf/notebook3773b98ea). Public visibility has not been independently verified.
