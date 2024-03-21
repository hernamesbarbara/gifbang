#!/usr/bin/env python3
import cv2
import numpy as np
import os


def calculate_motion_percentage(frame1, frame2, threshold=30):
    diff = cv2.absdiff(frame1, frame2)
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, threshold, 255, cv2.THRESH_BINARY)
    change_percent = 100.0 * \
        np.count_nonzero(thresh) / (thresh.shape[0] * thresh.shape[1])
    return change_percent


def find_high_motion_segments(change_percentages, percentile=95):
    # Calculate the threshold based on a percentile
    threshold = np.percentile(change_percentages, percentile)
    print(f"Calculated Motion Intensity Threshold: {threshold}%")

    # Identify segments above the threshold
    high_motion_segments = [i for i, percentage in enumerate(
        change_percentages) if percentage > threshold]

    return high_motion_segments, threshold


frames_dir = './frames'
frames = sorted([os.path.join(frames_dir, f)
                for f in os.listdir(frames_dir) if f.endswith('.png')])

change_percentages = []
for i in range(len(frames)-1):
    frame1 = cv2.imread(frames[i])
    frame2 = cv2.imread(frames[i+1])
    change_percentage = calculate_motion_percentage(frame1, frame2)
    change_percentages.append(change_percentage)

# Find high-motion segments based on the top n% of motion intensities
top_percentile = 5.0
high_motion_segments, threshold = find_high_motion_segments(
    change_percentages, 100.0-top_percentile)

high_motion_segments_str = " ".join(map(str, high_motion_segments))

print(
    f"High-motion segments (based on top {top_percentile}%): {high_motion_segments_str}")
