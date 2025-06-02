# Image to PDF maker

If you have a bunch of images (named in order) in a bunch of directories (named in order), this program converts all of them into both individual PDFs per folder and one combined PDF in the root directory.

> [IMPORTANT]
Currently, it can convert either JPG or PNG images in a particular folder (not both in the same folder).

## Requirements

- ImageMagick (version 7+)
- Python 3.8+ (for pypdf library; only if using from source)

## Usage

You can either use the binary in the Release section or build from source

### From source

1. Clone this repository using

```shell
git clone https://github.com/nathaishik/img-pdf-maker.git
```

2. Move the python file to the desired directory with the folders containing the images.

3. Create a virtual environment (venv works) in that folder
4. Install the required libraries using 

```shell
pip install -r requirements.txt
```

5. Run

```shell
python img_pdf_maker.py
```

> [NOTE]
This may consume a significant amount of memory.

### From Binary

Currently, only the binary for Windows is available. Contributors are requested to help make the binary for other platforms. `pyinstaller` module has been used to create the binary.

1. Download the appropriate binary from the Releases tab.
2. Add to PATH or move the binary to the desired location.
3. Run it.

## Output

The final PDF file will be present in the directory where the program is run from. By default it is named `combined.pdf`. You may rename it post creation.


