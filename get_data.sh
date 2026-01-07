#!/bin/bash

set -euo pipefail

# get_data.sh
# Downloads the three Chroma vector databases from the shared Google Drive folder
# and places them under ./embedding (project root).

EMBEDDING_DIR="embedding"
GDRIVE_FOLDER_URL="https://drive.google.com/drive/folders/1a5670fJZs36StnebNV3MKptbbmvzvmDA?usp=drive_link"

echo "Creating embedding directory..."
mkdir -p "$EMBEDDING_DIR"

# Check dependencies
if ! command -v gdown >/dev/null 2>&1; then
  echo "ERROR: gdown is not installed. Install it with: python3 -m pip install --user gdown"
  exit 1
fi

echo "Downloading vector databases from Google Drive folder..."
# This will download ALL items inside the folder into ./embedding
# (Requires a recent gdown version with --folder support.)
gdown --folder "$GDRIVE_FOLDER_URL" -O "$EMBEDDING_DIR" --quiet

echo "\nDownloaded items under: ./$EMBEDDING_DIR"

echo "\nExpected folders (examples):"
echo "  - chroma_jsonl_db[Huggingface Embedding]/"
echo "  - chroma_sip_csa_db[Huggingface Embedding]/"
echo "  - chroma_sip_csa_db[openai_embed3]/"

echo "\nDone."