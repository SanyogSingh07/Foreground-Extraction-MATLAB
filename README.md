# 🖼️ Foreground Extraction & Mask-Based Blending

![MATLAB](https://img.shields.io/badge/MATLAB-Simulation-orange.svg)
![Python](https://img.shields.io/badge/Python-OpenCV-blue.svg)
![Status](https://img.shields.io/badge/Status-Complete-success.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

## 📌 Project Overview
This project demonstrates the fundamentals of **Digital Image Processing (23DSDE12)** through mask-based foreground extraction and image compositing. Using a transparent image of a character (Tom/Jerry), the script dynamically generates a binary mask and blends the foreground onto a new cartoon background scene. 

The repository provides **two parallel implementations**:
1. **MATLAB (`experiment1.m`)**: The primary academic implementation.
2. **Python/OpenCV (`experiment1.py`)**: A production-grade implementation mirroring the exact MATLAB logic.

## 🚀 Features
- **Automatic Mask Generation**: Automatically detects and extracts the alpha channel of transparent images (`.png`) to create flawless binary masks without manual thresholding.
- **Robust Path Resolution**: Compatible with both local VS Code execution and MATLAB Online's virtual file system.
- **Cross-Language Validation**: Verifies results by implementing the exact mathematical operations in both MATLAB and Python.
- **Automated Directory Management**: Automatically generates the `output/` directory and saves processed step-by-step images.

## 📂 Directory Structure
```text
📦 Foreground-Extraction
 ┣ 📂 input
 ┃ ┣ 📜 tom.png            # Foreground object (with alpha channel)
 ┃ ┣ 📜 jerry.png          # Alternate foreground object
 ┃ ┗ 📜 background.jpg     # Background scene
 ┣ 📂 output
 ┃ ┣ 📜 composite.png      # Final blended image
 ┃ ┣ 📜 mask.png           # Extracted binary mask
 ┃ ┣ 📜 extracted_fg.png   # Foreground cut-out
 ┃ ┣ 📜 masked_bg.png      # Background with hole punched
 ┃ ┗ 📜 Experiment1_Results.png # 2x3 Subplot showing all steps
 ┣ 📜 experiment1.m        # MATLAB implementation
 ┣ 📜 experiment1.py       # Python/OpenCV implementation
 ┗ 📜 README.md
```

## 🛠️ Usage

### MATLAB Installation
1. Open MATLAB Desktop or [MATLAB Online](https://matlab.mathworks.com/).
2. Navigate to this repository's directory.
3. Open `experiment1.m` and click **Run**.
4. The output subplot will render, and files will be saved in `output/`.

### Python Installation
```bash
# Install dependencies
pip install opencv-python numpy matplotlib

# Run the pipeline
python experiment1.py
```

## 🧠 Methodology
1. **Read & Preprocess**: Loads images and extracts the alpha transparency channel to use as a master mask.
2. **Resize**: Rescales the background matrix and the mask matrix to perfectly match the foreground object dimensions using bicubic interpolation.
3. **Binarization & Precision**: Normalizes all image matrices to double-precision `[0, 1]` to ensure pixel-perfect array multiplication.
4. **Compositing**:
   - `Extracted Foreground = fg .* mask`
   - `Masked Background = bg .* (1 - mask)`
   - `Final Output = Extracted Foreground + Masked Background`

## 👤 Author
**Sanyog Kumar Singh**  
**USN**: 23BTRDC034  
**Subject**: Digital Image Processing (23DSDE12)
