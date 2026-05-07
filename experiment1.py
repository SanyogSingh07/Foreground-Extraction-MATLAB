import cv2
import numpy as np
import matplotlib.pyplot as plt

# STEP 1: Read Images
# Foreground image (Tom) with alpha channel
fg_rgba = cv2.imread('input/tom.png', cv2.IMREAD_UNCHANGED)
if fg_rgba is None:
    raise FileNotFoundError("input/tom.png not found")

# Extract BGR channels and Alpha channel
if fg_rgba.shape[2] == 4:
    fg = fg_rgba[:, :, :3]
    alpha = fg_rgba[:, :, 3]
else:
    fg = fg_rgba
    alpha = np.ones(fg.shape[:2], dtype=np.uint8) * 255

# Create and save the binary mask
_, mask = cv2.threshold(alpha, 128, 255, cv2.THRESH_BINARY)
cv2.imwrite('output/mask.png', mask)

# Background image
bg = cv2.imread('input/background.jpg')
if bg is None:
    raise FileNotFoundError("input/background.jpg not found")

# STEP 2: Resize Images to Match Foreground Dimensions
rows, cols = fg.shape[:2]
bg = cv2.resize(bg, (cols, rows))
mask = cv2.resize(mask, (cols, rows))

# STEP 3: Convert Mask to Binary (0 or 1 range)
mask_normalized = mask.astype(np.float64) / 255.0

# STEP 4: Convert Images to Double Precision (0 to 1 range)
fg_double = fg.astype(np.float64) / 255.0
bg_double = bg.astype(np.float64) / 255.0

# STEP 5: Create 3-Channel Mask
mask3 = np.stack([mask_normalized]*3, axis=2)

# STEP 6: Extract Foreground
extracted_fg = fg_double * mask3

# STEP 7: Remove Foreground Region from Background
extracted_bg = bg_double * (1.0 - mask3)

# STEP 8: Create Final Composite Image
final_output = extracted_fg + extracted_bg

# Save intermediate outputs
cv2.imwrite('output/extracted_fg.png', (extracted_fg * 255).astype(np.uint8))
cv2.imwrite('output/masked_bg.png', (extracted_bg * 255).astype(np.uint8))
cv2.imwrite('output/composite.png', (final_output * 255).astype(np.uint8))

# STEP 9: Display All Results (Save as matplotlib figure)
# Convert BGR to RGB for matplotlib display
fg_rgb = cv2.cvtColor(fg, cv2.COLOR_BGR2RGB)
bg_rgb = cv2.cvtColor(bg, cv2.COLOR_BGR2RGB)
extracted_fg_rgb = cv2.cvtColor((extracted_fg * 255).astype(np.uint8), cv2.COLOR_BGR2RGB)
extracted_bg_rgb = cv2.cvtColor((extracted_bg * 255).astype(np.uint8), cv2.COLOR_BGR2RGB)
final_output_rgb = cv2.cvtColor((final_output * 255).astype(np.uint8), cv2.COLOR_BGR2RGB)

plt.figure(figsize=(15, 10))
plt.suptitle('Foreground Extraction and Image Compositing', fontsize=16)

plt.subplot(2, 3, 1)
plt.imshow(fg_rgb)
plt.title('Original Foreground (Tom/Jerry)')
plt.axis('off')

plt.subplot(2, 3, 2)
plt.imshow(bg_rgb)
plt.title('Background Image')
plt.axis('off')

plt.subplot(2, 3, 3)
plt.imshow(mask, cmap='gray')
plt.title('Binary Mask')
plt.axis('off')

plt.subplot(2, 3, 4)
plt.imshow(extracted_fg_rgb)
plt.title('Extracted Foreground')
plt.axis('off')

plt.subplot(2, 3, 5)
plt.imshow(extracted_bg_rgb)
plt.title('Masked Background')
plt.axis('off')

plt.subplot(2, 3, 6)
plt.imshow(final_output_rgb)
plt.title('Final Composite Image')
plt.axis('off')

plt.tight_layout()
plt.savefig('output/Experiment1_Results.png', dpi=150)
print("Output successfully generated and saved to output/Experiment1_Results.png!")
