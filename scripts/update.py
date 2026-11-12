#imports
from datetime import datetime, timezone
import json
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent

MODULES_DIR = ROOT_DIR / "modules"

INDEX_FILE = ROOT_DIR / "index.json"

def update():
    modules_data = {}
    for folder in sorted(MODULES_DIR.iterdir()):
        if not folder.is_dir() or folder.name.startswith(("_", ".")):
            continue

        manifest_path = folder / "manifest.json"
        if not manifest_path.exists():
            continue

        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        mod_name = manifest.get("name")

        files = [
            f.relative_to(folder).as_posix()
            for f in sorted(folder.rglob("*"))
            if f.is_file() and "__pycache__" not in f.parts
        ]

    modules_data[mod_name] = {
            "type": manifest.get("type", "unknown"),
            "name": mod_name,
            "title": manifest.get("title", mod_name),
            "description": manifest.get("description", ""),
            "version": manifest.get("version", "0.1.0"),
            "author": manifest.get("author", ""),
            "path": f"modules/{folder.name}",
            "files": files,
            "dependencies": manifest.get("dependencies", []),
        }
    
    index = {
        "repository_version": "1.0",
        "updated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "modules": modules_data,
    }

    INDEX_FILE.write_text(
        json.dumps(index, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    print(f"Modules updated: {len(modules_data)}")



if __name__ == "__main__":
    update()