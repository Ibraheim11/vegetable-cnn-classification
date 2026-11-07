# Project conventions

- Scope is Phase 1: project setup and exploratory class-distribution analysis only. Do not add augmentation, CNNs, training, or evaluation without an explicit new request.
- Keep the notebook's numbered English explanations clear and instructional. Import all Phase 1 libraries in the first code cell and set the random seed to 42.
- Use the documented Kaggle train, test, and validation paths. Validate inputs before analysis; never download the dataset locally.
- Compute statistics from observed files only. Never fabricate counts, metrics, or saved notebook outputs.
- Keep counting deterministic, reusable, and explicit about supported extensions and nonrecursive behavior. Preserve empty classes and flag inconsistent class sets.
- Keep dependencies minimal. Test counting using temporary synthetic files, without Kaggle data. The notebook remains the source of truth for the counting function.
- Before delivery, run `python -m unittest discover -s tests -v` and validate notebook structure and code syntax. If available, also validate with `nbformat.validate`.
- Do not commit or push unless explicitly requested.
