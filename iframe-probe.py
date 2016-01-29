from __future__ import print_function
import json

# Run ffprobe with:
# ffprobe -show_frames -print_format json <infile> > output.json

frames = json.load(open("output.json"))["frames"]

gop_count = 0

for frame in frames:
    if frame["media_type"] == "video":

        if frame["pict_type"] == 'I' and gop_count > 1:
            # end of GOP
            print(" GOP={gop_count}".format(gop_count=gop_count+1))
            print(frame["pict_type"], end='')
            gop_count = 1
        else:
            print(frame["pict_type"], end='')
            gop_count += 1

print(" GOP={gop_count}".format(gop_count=gop_count+1))