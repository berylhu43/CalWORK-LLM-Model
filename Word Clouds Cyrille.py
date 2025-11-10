########################################
# CalWORKs CSA Policy Analysis Pipeline
# --------------------------------------
# Features:
# - Robust PDF extraction (pdfplumber → PyPDF2 fallback)
# - Preserves original stopwords & KEEP_TERMS
# - Defensive word statistics (no KeyError on empty input)
# - Avoids shadowing of pathlib.Path
# - Clear debug logging
# - WordCloud visualizations for TOP-20 terms
# - Sentence-level and word-level sentiment analysis
# - NEW: Computes sentence-level sentiment per Top-20 word per county
########################################

import os
import re
import zipfile
from pathlib import Path as _Path
from collections import Counter

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import nltk
from nltk.corpus import stopwords
from nltk.sentiment import SentimentIntensityAnalyzer
from wordcloud import WordCloud
import unicodedata
from nltk.stem import WordNetLemmatizer

# -------------------------------
# Quiet noisy PDF warnings (pdfminer/ghostscript style)
# -------------------------------
import logging
for noisy in (
    "pdfminer",
    "pdfminer.pdfinterp",
    "pdfminer.cmapdb",
    "pdfminer.psparser",
    "pdfminer.pdfpage"
):
    logging.getLogger(noisy).setLevel(logging.ERROR)

# -------------------------------
# Optional: DOCX readers (kept for completeness)
# -------------------------------
import docx2txt
from docx import Document

# -------------------------------
# Optional: gensim (Word2Vec) support
# -------------------------------
W2V_OK = True
try:
    from gensim.models import Word2Vec, KeyedVectors
    from gensim.downloader import load as gensim_load
except Exception:
    W2V_OK = False

# -------------------------------
# Optional: PDF readers
# -------------------------------
_PDF_BACKENDS = {}
try:
    import pdfplumber
    _PDF_BACKENDS["pdfplumber"] = True
except Exception:
    _PDF_BACKENDS["pdfplumber"] = False

try:
    import PyPDF2
    _PDF_BACKENDS["pypdf2"] = True
except Exception:
    _PDF_BACKENDS["pypdf2"] = False

# -------------------------------
# 0. Ensure NLTK resources are available
# -------------------------------
def _safe_download(resource_path: str, download_name: str):
    """
    Ensure an NLTK resource exists; download if missing.
    
    Parameters
    ----------
    resource_path : str
        Path used internally by NLTK to check for the resource.
    download_name : str
        Name of the NLTK package to download if missing.
    """
    try:
        nltk.data.find(resource_path)
    except LookupError:
        nltk.download(download_name)

# Download essential NLTK packages
_safe_download("tokenizers/punkt", "punkt")
_safe_download("tokenizers/punkt_tab", "punkt_tab")
_safe_download("corpora/stopwords", "stopwords")
_safe_download("sentiment/vader_lexicon", "vader_lexicon")

# -------------------------------
# 1. USER CONFIGURATION
# -------------------------------

# Path to ZIP file containing CalWORKs CSAs
ZIP_PATH = r'/Users/cyrillefougere/Desktop/CalWORKs data.zip'  # Edit if needed
BASE_DIR = _Path(ZIP_PATH).parent

# Folder where ZIP will be extracted
EXTRACT_DIR = BASE_DIR / "CalWORKs data_extracted"
os.makedirs(EXTRACT_DIR, exist_ok=True)

# Output folder for WordClouds and results
OUTPUT_DIR = BASE_DIR / "Word Clouds Update"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# -------------------------------
# 2. Sanity check of paths
# -------------------------------
print("=== Path Verification ===")
print("ZIP exists:", _Path(ZIP_PATH).exists())
print("Extract dir:", EXTRACT_DIR)
print("Output dir:", OUTPUT_DIR)
print("=========================")

# -------------------------------
# 3. Extract ZIP once (if not already extracted)
# -------------------------------
if (not any(EXTRACT_DIR.rglob("*"))) and _Path(ZIP_PATH).exists():
    with zipfile.ZipFile(ZIP_PATH, 'r') as zip_ref:
        zip_ref.extractall(EXTRACT_DIR)
print(f"Extracted ZIP to: {EXTRACT_DIR}")

# -------------------------------
# 4. List PDF files to analyze
# -------------------------------
pdf_files = list(EXTRACT_DIR.rglob("*.pdf"))
print("Files to analyze:")
for f in pdf_files:
    print(" -", f.relative_to(EXTRACT_DIR))

# -------------------------------
# 5. Confirm output directory exists
# -------------------------------
print(f"\nOutput folder ready: {OUTPUT_DIR}\n")