# Vegetable Image Classification using CNN

An academic **deep-learning computer-vision assignment** that classifies vegetable photographs into **15 classes** with a **Convolutional Neural Network built from scratch**. The entire pipeline lives in an executable, explained Kaggle notebook.

**Dataset:** [misrakahmed / Vegetable Image Dataset](https://www.kaggle.com/datasets/misrakahmed/vegetable-image-dataset)

## Assignment implementation status

| Requirement | Notebook section |
| --- | --- |
| Imports and reproducible seed | 1 |
| Kaggle dataset path auto-discovery | 2 |
| Reusable image counter for train/test/validation | 3–4 |
| Three DataFrames and merged summary | 4–5 |
| Grouped bar chart and class-balance discussion | 6–7 |
| Train augmentation and validation-only rescaling | 9 |
| `ImageDataGenerator.flow_from_directory`, 224×224, batch 32, 15 classes, seed 42 | 9–10 |
| CNN Sequential: Conv(32/64/128), pooling, Flatten, Dense(512), Dropout(0.5), Softmax(15) | 11 |
| Adam, categorical crossentropy, accuracy | 12 |
| 20 epochs max; EarlyStopping(patience=5, restore_best_weights=True) | 13 |
| Training/validation evaluation and overfitting analysis | 14 |
| Accuracy and loss curves | 15 |
| Independent original validation/test holdout evaluation (extra) | 16 |
| Real-run metrics/history CSV exports (extra) | 17 |

**Important:** the **code** for the complete pipeline is in the repo. The model has **not been trained or validated end-to-end in this GitHub commit**, and no trained accuracy, model metrics, or plots are invented. Run the notebook in Kaggle and save its actual outputs to complete the experimental evidence.

## EDA observations from the prior real Kaggle run

The previous Kaggle execution counted **21,000** image files in **15** classes:

| Split | Per class | Total |
| --- | ---: | ---: |
| train | 1,000 | 15,000 |
| validation | 200 | 3,000 |
| test | 200 | 3,000 |

The image counts were **exactly balanced within each split**. These counts come from filenames; they do not prove every image decodes successfully or that the images are duplicate-free.

## Run the complete assignment on Kaggle — no local Python or VS Code needed

1. Download the notebook from [`notebooks/vegetable_cnn_classification.ipynb`](notebooks/vegetable_cnn_classification.ipynb) using GitHub's **Download raw file** option.
2. On [Kaggle Code](https://www.kaggle.com/code), create a notebook and import the downloaded `.ipynb` (**File → Import Notebook**, or the equivalent import menu).
3. In the right-hand **Input** panel choose **Add Input** and attach the [Vegetable Image Dataset](https://www.kaggle.com/datasets/misrakahmed/vegetable-image-dataset) by **misrakahmed**.
4. Open **Settings → Accelerator** and choose an available **GPU**. A GPU is recommended for the required large Flatten → Dense(512) architecture. The notebook prints detected GPU devices.
5. Run all notebook cells **in order**. The dataset root is automatically discovered under `/kaggle/input`; it supports the actual nested mount path:
   `/kaggle/input/datasets/misrakahmed/vegetable-image-dataset/Vegetable Images`.
6. Inspect generator sizes and class maps (sections 9–10), CNN summary (section 11), completed epochs (section 13), real losses/accuracies (section 14), learning curves (section 15), and original holdout metrics (section 16).
7. Save an **executed notebook version** in Kaggle. From `/kaggle/working`, download the small `evaluation_metrics.csv` and `training_history.csv` generated after successful training. You may commit these small result files to the repo; do **not** commit the dataset or large model binaries.

Kaggle already supplies many scientific packages. If `tensorflow` is missing, use a Kaggle image/environment with TensorFlow installed. `ImageDataGenerator` is a legacy API but is used here to satisfy the explicit assignment instructions.

### What is actually evaluated?

The instructions require `validation_split=0.20` and complementary `subset` values. The **train/** directory therefore yields about **12,000** augmentation-enabled training images and **3,000** rescale-only internal-validation images. Original **validation/** and **test/** directories are kept untouched and used only after model training, as independent holdout evaluations. The training accuracy reported in section 14 is measured on the same training subset **without augmentation**, for fair comparison.

## Run local static tests (optional)

Local Python is **not needed to run the Kaggle notebook**. If Python is installed:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m unittest discover -s tests -v
```

Static tests check the notebook's JSON, syntax, dataset counter, assignment settings, and section structure. They do **not** train TensorFlow or establish real model accuracy.

## Structure

```text
notebooks/vegetable_cnn_classification.ipynb
tests/test_counting.py
tests/test_pipeline_contract.py
requirements.txt
AGENTS.md
.gitignore
README.md
```

## Reproducibility and limitations

- Random seed: `42`; image dimensions `224×224×3`; batch size `32`; 15 classes.
- The dataset is hosted by Kaggle and is not copied to this GitHub repository.
- The requested architecture is relatively large; its training time and accuracy depend on the Kaggle GPU and data.
- Train, internal validation, original validation holdout, and test are carefully separated.
- No pretrained model or test-set tuning is used. Avoid making performance claims until the actual Kaggle run is complete.
