## Setup

1. Save youtube URLs in urls.txt, one URL per line (no headers)
1. Run `get_mp4s.py` to download those youtube videos and save them as mp4s
1. Next, run `res480p.sh` to reduce resolution of the input video for faster processing and smaller file size
1. Run `extract_frames.sh` to save 1 .png still for every frame in the video to "./frames/"
1. Then run `analyze_motion.py` which will look for patterns and changes between frames. for example, it will look at how different pixels are from one png still to the next.
1. TODO do something useful with the output of `analyze_motion.py`

## TODOs

#### Make a pipeline that can be reused easily

1. Read URLs from a file and save mp4s in high resolution 720p or 1080p
1. Convert to 480p
1. Extract 1 frame per second of footage
1. Analyze motion and find high motion segments
1. The high motion frames represent the starting frame for the output gifs we will generate
1. Generate 10 second gifs for each high motion frame
1. Figure out a clever way to choose the "best" of the gifs that were generated

## Bonus TODOs

Instead of looking at similarity and difference of pixels frame to frame, perhaps we can use a n-frame window

for instance, if our gifs are going to be 10 seconds long and we are looking at 1 frame per second, you could create a windowed comparison

Define a window size, which specifies how many consecutive frames you want to consider together.
Slide this window frame by frame through your list of frames.

For each window, compute the motion intensity or change percentage across all frames within the window.
Use a threshold to determine if the motion intensity or change percentage within the window exceeds a certain value.

If the motion within the window is considered high, mark the frames within that window as part of a high-motion segment.
