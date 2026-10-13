"""Download raw data into data/raw/ and record provenance in MANIFEST.csv.

Files are saved exactly as downloaded and skipped if already present.
Pass --refresh to download again (agencies revise data; a silent new
vintage makes results irreproducible).

    python src/download.py
    python src/download.py --refresh
"""
import argparse
import csv
import hashlib
import urllib.request
from datetime import date
from pathlib import Path

RAW = Path(__file__).resolve().parents[1] / "data" / "raw"
MANIFEST = RAW / "MANIFEST.csv"

# filename -> source URL
SOURCES = {
    # "cpi_u.csv": "https://fred.stlouisfed.org/graph/fredgraph.csv?id=CPIAUCSL",
}


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def fetch(filename: str, url: str, refresh: bool = False) -> Path:
    dest = RAW / filename
    if dest.exists() and not refresh:
        print(f"[skip] {filename} exists (use --refresh to re-download)")
        return dest
    print(f"[get] {url} -> {dest}")
    urllib.request.urlretrieve(url, dest)
    with MANIFEST.open("a", newline="") as f:
        csv.writer(f).writerow([filename, url, date.today().isoformat(), sha256(dest)])
    return dest


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--refresh", action="store_true", help="re-download existing files")
    args = parser.parse_args()
    RAW.mkdir(parents=True, exist_ok=True)
    for filename, url in SOURCES.items():
        fetch(filename, url, refresh=args.refresh)


if __name__ == "__main__":
    main()
