import os
import zipfile
from .main import AddressLookup

# Paths to optional files
optional_files_dir = os.path.join(os.path.dirname(__file__), "optional_files")
model_zip_path = os.path.join(optional_files_dir, "clean_address_transformer_model.zip")
model_path = os.path.join(optional_files_dir, "clean_address_transformer_model.pth")
mappings_path = os.path.join(optional_files_dir, "mappings.json")
tokenizer_path = os.path.join(optional_files_dir, "tokenizer")

def ensure_files():
    if os.path.exists(model_zip_path):  # Only proceed if optional files are present
        if not os.path.exists(model_path):
            print("Extracting model files...")
            with zipfile.ZipFile(model_zip_path, 'r') as zip_ref:
                zip_ref.extractall(optional_files_dir)

        if not os.path.exists(mappings_path):
            raise FileNotFoundError("Required file mappings.json not found in optional_files.")

        if not os.path.exists(tokenizer_path):
            raise FileNotFoundError("Required tokenizer folder not found in optional_files.")
    else:
        print("Optional files not installed. To include them, use `pip install llama-cleanup[all]`.")

# Ensure optional files are loaded only if present
ensure_files()

# Make AddressLookup available on import
__all__ = ["AddressLookup"]

