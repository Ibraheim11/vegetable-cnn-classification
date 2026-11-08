# CNN Vegetable Classification — Experimental Results

## Provenance

The figures below are **observed model outputs** from the user's completed Kaggle notebook execution, shared as screenshots after training. They are not simulated, estimated, or copied from model code. The screenshot-shared numbers are rounded to four decimal places unless otherwise noted. The original exact CSV exports are stored in the user's Kaggle session, not attached to this repository.

- Kaggle notebook: [Vegetable CNN run](https://www.kaggle.com/code/ibrahemasharf/notebook3773b98ea) (**visibility of this Kaggle version has not been independently confirmed**).
- Notebook code: [vegetable_cnn_classification.ipynb](../notebooks/vegetable_cnn_classification.ipynb)
- Kaggle runtime: TensorFlow 2.21.0; two GPU devices detected.
- Dataset: Vegetable Image Dataset by misrakahmed.
- Training duration: **20 epochs** (the maximum configured); EarlyStopping was enabled but did not halt training early.
- Best observed monitored validation loss during training: **0.05724012851715088**. With `restore_best_weights=True`, the final evaluation uses the restored best weights.

## Dataset and sampling

| Split directory | Number of images | Images per class |
| --- | ---: | ---: |
| train | 15,000 | 1,000 |
| validation | 3,000 | 200 |
| test | 3,000 | 200 |
| **Total** | **21,000** | **1,400** |

The 15 classes are balanced by image count. The specified `validation_split=0.2` applies **within the train directory**: 12,000 images for training and 3,000 for internal validation. The original `validation/` and `test/` folders remain independent holdouts, used after training.

## Final evaluations

| Evaluation set | Accuracy | Loss |
| --- | ---: | ---: |
| Training subset (rescaling only for evaluation) | **0.9938 (99.38%)** | 0.0224 |
| Internal validation subset | **0.9847 (98.47%)** | 0.0572 |
| Original validation holdout | **0.9850 (98.50%)** | 0.0581 |
| Final test holdout | **0.9840 (98.40%)** | 0.0692 |

- **Training – internal validation accuracy gap:** +0.0092 (about **0.92 percentage points**). This is a small observed gap and does not on its own suggest severe overfitting.
- Training and validation accuracy curves generally improved over 20 epochs; validation loss fluctuated, including a spike around epoch 17, before returning near its previous best.
- The best validation-loss weights were restored, and the resulting independent test accuracy was **98.40%**.

## Model and settings

- From-scratch Keras Sequential CNN with 3 convolution/max-pooling blocks: 32, 64, and 128 filters, 3×3 kernels, ReLU.
- `Flatten → Dense(512, ReLU) → Dropout(0.5) → Dense(15, Softmax)`.
- 224×224 RGB images; batch size 32; seed 42; `ImageDataGenerator` training augmentation and rescaling.
- Adam optimizer, categorical crossentropy loss, accuracy metric.
- Maximum 20 epochs; `EarlyStopping(monitor="val_loss", patience=5, restore_best_weights=True)`.
- Model summary displayed **44,403,791 trainable parameters**.

## Reproducibility and evidence status

The screenshots show the completed training history, training/internal-validation evaluation, accuracy/loss curves, independent holdout evaluation, and successful creation of `/kaggle/working/evaluation_metrics.csv` and `/kaggle/working/training_history.csv`.

This document is a **human-verified transcription of visible output**, not an automatically downloaded Kaggle artifact. The two original CSV files and an executed Kaggle notebook version should be saved and made accessible separately. The source notebook in this repository intentionally has blank output cells, so metrics are presented here with transparent provenance instead of altering its execution state.
