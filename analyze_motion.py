#!/usr/bin/env python3
import cv2
import numpy as np
import os


def calculate_motion_intensity(frame1, frame2):
    # Calculate the absolute difference between two frames
    diff = cv2.absdiff(frame1, frame2)
    # Convert the difference to grayscale
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    # Sum up the intensity of the differences
    motion_intensity = np.sum(gray)
    return motion_intensity


def calculate_motion_percentage(frame1, frame2, threshold=30):
    # Calculate the absolute difference between two frames
    diff = cv2.absdiff(frame1, frame2)
    # Convert the difference to grayscale
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    # Apply a binary threshold
    _, thresh = cv2.threshold(gray, threshold, 255, cv2.THRESH_BINARY)
    # Calculate the percentage of pixels that have changed significantly
    change_percent = 100.0 * \
        np.count_nonzero(thresh) / (thresh.shape[0] * thresh.shape[1])
    return change_percent


frames_dir = './frames'
frames = sorted([os.path.join(frames_dir, f)
                for f in os.listdir(frames_dir) if f.endswith('.png')])

intensities = []
for i in range(len(frames)-1):
    frame1 = cv2.imread(frames[i])
    frame2 = cv2.imread(frames[i+1])
    intensity = calculate_motion_intensity(frame1, frame2)
    intensities.append(intensity)

# Threshold for high motion - adjust based on your video
thresh_intensity = 1000000  # Example threshold, adjust as needed

# Identify high-motion frames
intensity_high_motion_frames = [i for i, intensity in enumerate(
    intensities) if intensity > thresh_intensity]

print("High-motion frames (intensity):", intensity_high_motion_frames)
print("*"*80)
print()

# Use a list to store the percentage of change for each pair of frames
change_percentages = []
for i in range(len(frames)-1):
    frame1 = cv2.imread(frames[i])
    frame2 = cv2.imread(frames[i+1])
    change_percentage = calculate_motion_percentage(frame1, frame2)
    change_percentages.append(change_percentage)

# Define a new threshold for change percentage, e.g., 5% of the frame has changed
thresh_change_percent = 5  # This threshold is arbitrary; adjust as needed

# Identify high-motion frames based on the percentage of change
change_percent_high_motion_frames = [
    i for i, percentage in enumerate(change_percentages) if percentage > thresh_change_percent
]

print("High-motion frames (change percentage):",
      change_percent_high_motion_frames)
