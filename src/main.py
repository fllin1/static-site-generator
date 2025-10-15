import sys

from pathlib import Path
import shutil

from pull_out_big_gun import generate_pages_recursive


def source_to_destination(input_dir: str, output_dir: str):
    root_dir = Path(__file__).resolve().parents[1]
    source_dir = root_dir / input_dir
    if not source_dir.exists():
        raise FileNotFoundError(f"Source directory {source_dir} does not exist")

    destination_dir = root_dir / output_dir
    if not destination_dir.exists():
        destination_dir.mkdir(parents=True)
    else:
        shutil.rmtree(destination_dir)
        destination_dir.mkdir(parents=True)

    for file in source_dir.iterdir():
        if file.is_file():
            shutil.copy(file, destination_dir / file.name)
        elif file.is_dir():
            source_to_destination(file, destination_dir / file.name)


def main():
    basepath = sys.argv[1] if len(sys.argv) > 0 else "/"
    source_to_destination("static", "docs")
    generate_pages_recursive(basepath, "content", "template.html", "docs")


if __name__ == "__main__":
    main()
