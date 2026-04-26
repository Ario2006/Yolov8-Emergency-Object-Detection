import gdown
import os
import sys

def download_assets():
    # IDs from the links provided
    assets = {
        "train data": "1VNjXGC7w-eI-OuKDiRhTpOOETXxMNaRi",
        "test data": "1iAkA5FQ_lzZ25x-08nkpgdFMEsq1OBjY",
        "backend/models/best.pt": "1oKyaA48Pk_IZ_1ZmKy68px3kELwyfiwF"
    }

    print("🚀 Starting download of project assets from Google Drive...")

    for path, gdrive_id in assets.items():
        print(f"\n📂 Processing: {path}")
        
        # Ensure parent directories exist
        parent_dir = os.path.dirname(path)
        if parent_dir and not os.path.exists(parent_dir):
            os.makedirs(parent_dir)

        # Use gdown to download
        # If it's a folder link, gdown handles it with --folder
        is_folder = "data" in path
        
        try:
            if is_folder:
                gdown.download_folder(id=gdrive_id, output=path, quiet=False, use_cookies=False)
            else:
                gdown.download(id=gdrive_id, output=path, quiet=False, fuzzy=True)
        except Exception as e:
            print(f"❌ Error downloading {path}: {e}")
            print("Note: Make sure the Google Drive links are set to 'Anyone with the link can view'.")

    print("\n✅ All downloads complete!")

if __name__ == "__main__":
    download_assets()
