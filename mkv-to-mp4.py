#!/usr/bin/env python3

import os
import argparse
import ffmpeg

def convert_to_mp4(mkv_file):
    name, ext = os.path.splitext(mkv_file)
    out_name = name + ".mp4"
    ffmpeg.input(mkv_file).output(out_name).run()
    print("Finished converting {}".format(mkv_file))

def main():
    parser = argparse.ArgumentParser(description="Convert MKV files to MP4")
    parser.add_argument("directory", type=str, help="Directory to scan for MKV files")
    
    args = parser.parse_args()
    start_dir = args.directory
    
    if not os.path.isdir(start_dir):
        print(f"Error: {start_dir} is not a valid directory")
        return

    for path, folders, files in os.walk(start_dir):
        for file in files:
            if file.endswith('.mkv'):
                print("Found file: %s" % file)
                convert_to_mp4(os.path.join(path, file))
    
    print("Finished converting all MKV files")

if __name__ == "__main__":
    main()
