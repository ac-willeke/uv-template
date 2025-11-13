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


def cleanup_template_files(current_dir):
    """Remove all template files and conditional directories."""
    removed = False
    
    # Remove .jinja files recursively
    for jinja_file in current_dir.rglob("*.jinja"):
        if jinja_file.exists():
            print(f"Removing: {jinja_file.relative_to(current_dir)}")
            jinja_file.unlink()
            removed = True
    
    # Remove conditional files and directories (those with {% if ... %} syntax)
    for item in current_dir.iterdir():
        if ("{% if" in item.name and "{% endif %}" in item.name) or item.name.startswith("{% if"):
            print(f"Removing: {item.relative_to(current_dir)}")
            if item.is_dir():
                shutil.rmtree(item)
            else:
                item.unlink()
            removed = True
    
    # Remove specific template setup files
    template_files = ["setup-template.py", "copier.yml", ".copier-answers.yml"]
    for file_name in template_files:
        file_path = current_dir / file_name
        if file_path.exists():
            print(f"Removing: {file_path.relative_to(current_dir)}")
            file_path.unlink()
            removed = True
    
    return removed


def main():
    """Apply template using Copier."""
    current_dir = Path.cwd()
    
    print("Template setup using Copier")
    print("1. Full setup (generate template and cleanup)")
    print("2. Cleanup only (remove template artifacts)")
    
    choice = input("Choose option (1/2) [1]: ").strip()
    
    if choice == "2":
        print("Running cleanup only...")
        if cleanup_template_files(current_dir):
            print("Cleanup complete!")
        else:
            print("No template files found to clean up.")
        return
    
    response = input("Continue with full setup? (y/n) [y]: ").strip()
    if response and not response.lower().startswith("y"):
        return
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
            
            # Clean up template files
            cleanup_template_files(current_dir)
            
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