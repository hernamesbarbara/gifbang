## Setup

1. Save youtube URLs in urls.txt, one URL per line (no headers)
1. Run `get_mp4s.py` to download those youtube videos and save them as mp4s
1. Next, run `res480p.sh` to reduce resolution of the input video for faster processing and smaller file size
1. Run `extract_frames.sh` to save 1 .png still for every frame in the video to "./frames/"
1. Then run `analyze_motion.py` which will look for patterns and changes between frames. for example, it will look at how different pixels are from one png still to the next.
1. TODO do something useful with the output of `analyze_motion.py`
