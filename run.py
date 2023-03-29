from pathlib import Path
import argparse
from simpinkscr import simple_inkscape_scripting


def main():
    parser = argparse.ArgumentParser(description='Removes all hidden layers for each file')
    parser.add_argument('directory', help='specify directory with svg files')
    args = parser.parse_args()
    directory = Path(args.directory)
    if not directory.exists():
        print(f"Folder {directory} doesn't exist")
        return
    if not directory.is_dir():
        print(f"Path {directory} is not a dir")
        return

    for file in directory.glob("**/*.svg"):
        output_file = file.absolute().with_name(f"{file.stem}_small{file.suffix}")
        simple_inkscape_scripting.SimpleInkscapeScripting().run(
            args=[
                "--py-source",
                "remove_hidden.py",
                "--output",
                str(output_file.absolute()),
                str(file.absolute()),
            ]
        )


if __name__ == '__main__':
    main()
