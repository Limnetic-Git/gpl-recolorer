# Sprite Recolorer

A utility for batch recoloring of sprites (PNG) according to a specified GIMP palette (.gpl). It finds the nearest color using Manhattan distance and replaces every opaque pixel of the image.

## Features

- 🖼️ Supports any PNG images with alpha channel
- 🎯 Batch processing — recursively traverses all nested folders
- 📊 Nearest color search algorithm using the sum of absolute channel differences (Manhattan distance)
- 🔄 Preserves the original folder structure in the result directory
- 🧩 Supports GIMP palette format .gpl

## Requirements

- Python 3.6+
- Pillow (PIL)

## Installation

```bash
git clone https://github.com/your-username/sprite-recolorer.git
cd sprite-recolorer
pip install pillow
```
- Run script:
```bash
python recolorer.py
```
- Select the folder containing sprites to recolor
- Select a `.gpl` palette file
- Wait for completion — the result will appear in the `result/` folder

**MIT License - free to use, do what u want :)**

⭐ Star the project if you found it useful!

