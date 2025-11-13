#!/usr/bin/env python3
"""Setup script for UV Python Template using Copier."""

import sys
import tempfile
import shutil
from pathlib import Path

try:
    from copier import run_copy
except ImportError:
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "copier"])
    from copier import run_copy


def main():
    """Apply template using Copier."""
    print("Template setup using Copier")
    
    response = input("Continue? (y/n) [y]: ").strip()
    if response and not response.lower().startswith("y"):
        return
    
    current_dir = Path.cwd()
    
    try:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_path = Path(temp_dir)
            
            run_copy(
                src_path=str(current_dir),
                dst_path=str(temp_path / "output"),
                data={},
                unsafe=True,
                quiet=False
            )
            
            generated_path = temp_path / "output"
            
            # Remove template files
            for file_name in ["setup-template.py", "copier.yml", ".copier-answers.yml"]:
                file_path = current_dir / file_name
                if file_path.exists():
                    file_path.unlink()
            
            # Copy generated files
            for item in generated_path.iterdir():
                dest = current_dir / item.name
                if dest.exists():
                    if dest.is_dir():
                        shutil.rmtree(dest)
                    else:
                        dest.unlink()
                
                if item.is_dir():
                    shutil.copytree(item, dest)
                else:
                    shutil.copy2(item, dest)
        
        print("\nSetup complete. Next steps:")
        print("1. uv sync --group dev")
        print("2. uv run pre-commit install")
        print("3. git add . && git commit -m 'Initialize project'")
            
    except KeyboardInterrupt:
        print("Setup cancelled.")
        sys.exit(1)
    except Exception as e:
        print(f"Setup failed: {e}")
        print("Alternative: uvx copier copy . ../my-project --trust")
        sys.exit(1)


if __name__ == "__main__":
    main()