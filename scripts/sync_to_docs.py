import os
import shutil
from pathlib import Path

SOURCE = "data/summaries"
TARGET = "docs/posts"

os.makedirs(TARGET, exist_ok=True)

for file in Path(SOURCE).glob("*.md"):
    target_file = Path(TARGET) / file.name
    shutil.copy(file, target_file)
    print(f"copied: {file} -> {target_file}")

print("sync done")
