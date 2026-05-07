% =========================================================
% Experiment 1: Foreground Extraction and Image Compositing
% Using Tom and Jerry Images
% Student: Sanyog Kumar Singh | USN: 23BTRDC034
% Subject: Digital Image Processing (23DSDE12)
% =========================================================

clc;
clear;
close all;

%% STEP 1: Read Images

% Foreground image (Tom or Jerry)
% Check if image is in 'input/' folder (local) or current folder (MATLAB Online)
if exist('input/tom.png', 'file')
    [fg, map, alpha] = imread('input/tom.png');
elseif exist('tom.png', 'file')
    [fg, map, alpha] = imread('tom.png');
else
    error('Unable to find tom.png. Please ensure it is uploaded to MATLAB Online.');
end

% Background image
if exist('input/background.jpg', 'file')
    bg = imread('input/background.jpg');
elseif exist('background.jpg', 'file')
    bg = imread('background.jpg');
else
    error('Unable to find background.jpg. Please ensure it is uploaded to MATLAB Online.');
end

%% STEP 2: Resize Images to Match Foreground Dimensions

[rows, cols, ~] = size(fg);

% Resize background to match foreground
bg = imresize(bg, [rows cols]);

%% STEP 3: Create Binary Mask from Alpha Channel

% If the image has a transparent background (alpha channel), use it as the mask.
if ~isempty(alpha)
    mask = alpha > 128; % Convert alpha to logical binary mask
else
    % Fallback if no transparency: generate auto-mask using intensity
    gray = rgb2gray(fg);
    mask = imbinarize(gray);
    mask = imfill(mask, 'holes');
    mask = bwareaopen(mask, 500);
end

%% STEP 4: Convert Images to Double Precision

fg   = im2double(fg);
bg   = im2double(bg);
mask = im2double(mask);

%% STEP 5: Create 3-Channel (RGB) Mask

% Replicate single-channel mask across all 3 colour channels
mask3 = cat(3, mask, mask, mask);

%% STEP 6: Extract Foreground

% Keep only the foreground object (Tom/Jerry) using the mask
extracted_fg = fg .* mask3;

%% STEP 7: Remove Foreground Region from Background

% Cut out the region where Tom/Jerry will be placed
extracted_bg = bg .* (1 - mask3);

%% STEP 8: Create Final Composite Image

% Combine extracted foreground + masked background
final_output = extracted_fg + extracted_bg;

%% STEP 9: Display All Results

figure('Name', 'Foreground Extraction and Image Compositing');

subplot(2, 3, 1);
imshow(fg);
title('Original Foreground (Tom/Jerry)');

subplot(2, 3, 2);
imshow(bg);
title('Background Image');

subplot(2, 3, 3);
imshow(mask);
title('Binary Mask');

subplot(2, 3, 4);
imshow(extracted_fg);
title('Extracted Foreground');

subplot(2, 3, 5);
imshow(extracted_bg);
title('Masked Background');

subplot(2, 3, 6);
imshow(final_output);
title('Final Composite Image');

%% STEP 10: Save Outputs to Folder

% Create 'output' directory if it doesn't exist
if ~exist('output', 'dir')
    mkdir('output');
end

% Save outputs to the 'output' directory
imwrite(mask, 'output/mask.png');
imwrite(extracted_fg, 'output/extracted_fg.png');
imwrite(extracted_bg, 'output/masked_bg.png');
imwrite(final_output, 'output/composite.png');

% Save the entire figure
set(gcf, 'PaperPositionMode', 'auto');
print('output/Experiment1_Results','-dpng','-r0');
