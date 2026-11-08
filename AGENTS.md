# Project conventions

- This repository implements the **complete** CNN Vegetable Classification assignment. The notebook is the source of truth for imports, dataset EDA, preprocessing/augmentation, CNN, training, evaluation and plots.
- Keep all library imports in the first code cell and use seed 42.
- Follow the assignment exactly: ImageDataGenerator with rescaling and specified train-only augmentation; 224×224 images, batch 32, 15 classes, `subset="training"` and `subset="validation"` from the train directory.
- Do not contaminate training or internal validation with the original `validation/` or `test/` directories. The latter are external holdouts.
- The architecture must remain Sequential with three Conv2D(32,64,128) + MaxPooling blocks, Flatten, Dense(512), Dropout(0.5), and Dense(15, softmax).
- Compile Adam/categorical_crossentropy/accuracy. Train at most 20 epochs using EarlyStopping on val_loss with patience 5 and restore_best_weights True.
- Print actual evaluation metrics and draw real learning curves. Never fabricate model outputs or counts; empty execution outputs in the version-controlled notebook are intentional until a real Kaggle run.
- Use Kaggle-mounted dataset paths (support nesting), do not download image datasets into Git and do not commit large artifacts.
- Run `python -m unittest discover -s tests -v` and `nbformat.validate` when available. Static tests are **not** substitutes for a real training run on Kaggle.
