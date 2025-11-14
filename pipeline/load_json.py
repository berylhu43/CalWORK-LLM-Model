import os
import json
import re
import shutil
from langchain_core.documents import Document
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
JSONL_DIR = os.path.join(BASE_DIR, "..", "data", "jsonl")
PERSIST_DIR = os.path.join(BASE_DIR, "..", "embedding", "chroma_jsonl_db[Huggingface Embedding]")
COLLECTION = "dashboard_json"

def normalize_text(text: str) -> str:
    text = text.strip()
    text = re.sub(r"(\$?\d{1,3}(?:,\d{3})*(?:\.\d+)?%?)", lambda m: f"[NUM:{m.group(1)}]", text)
    text = re.sub(r"\s+", " ", text)
    return text

def build_jsonl_vectorstore(refresh=False):
    documents = []

    for filename in os.listdir(JSONL_DIR):
        if filename.endswith(".jsonl"):
            with open(os.path.join(JSONL_DIR, filename), "r") as f:
                for line in f:
                    json_obj = json.loads(line)
                    text = normalize_text(json_obj["text"])
                    meta = json_obj.get("metadata", {})
                    documents.append(Document(page_content=text, metadata=meta))

    embedding_func = HuggingFaceEmbeddings(
        model_name="BAAI/bge-m3",
        model_kwargs={"device": "cuda"},
        encode_kwargs={"normalize_embeddings": True}
    )

    if refresh and os.path.exists(PERSIST_DIR):
        print(f"Clearing existing Chroma directory: {PERSIST_DIR}")
        shutil.rmtree(PERSIST_DIR)

    vectorstore = Chroma(
        collection_name=COLLECTION,
        persist_directory=PERSIST_DIR,
        embedding_function=embedding_func
    )

    texts = [doc.page_content for doc in documents]
    metadatas = [doc.metadata for doc in documents]
    batch_size = 128
    for i in range(0, len(texts), batch_size):
        vectorstore.add_texts(texts[i:i+batch_size], metadatas[i:i+batch_size])
        print(f"Embedded {i + batch_size} / {len(texts)}")

    vectorstore.persist()
    print(f"✅ Chroma collection '{COLLECTION}' created.")

    return vectorstore

if __name__ == "__main__":
    vs = build_jsonl_vectorstore(refresh=True)
    results = vs.similarity_search("orientation attendance Alameda", k=2)
    for i, r in enumerate(results):
        print(f"\nResult {i+1}: {r.page_content[:300]}")
        print(f"Metadata: {r.metadata}")