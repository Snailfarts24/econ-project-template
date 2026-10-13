# Project title

One or two sentences: the research question and why it matters.

## Status

Work in progress.

## Data

Raw data is **not** committed. Run `src/download.py` to fetch it. `data/raw/MANIFEST.csv` records each file's source URL, access date and SHA-256 hash.

| Source | Description | Access | License / terms |
|---|---|---|---|
| | | Public / registration / restricted | |

Data that requires registration or a data use agreement must be obtained directly from the provider. Do not commit it here.

## Layout

```
data/raw/        raw files exactly as downloaded (gitignored, except MANIFEST.csv)
data/derived/    cleaned intermediate files, parquet (gitignored)
src/             pipeline and analysis code; audit.py has merge/shape checks
tests/           pytest checks on the pipeline
output/tables/   regression tables
output/figures/  figures
paper/           draft
```

## Reproducing

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env        # add API keys if needed
python src/download.py
pytest
```

---

*Created from [econ-project-template](https://github.com/Snailfarts24/econ-project-template).*
