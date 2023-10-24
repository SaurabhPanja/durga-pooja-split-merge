from moviepy.editor import VideoFileClip, concatenate_videoclips

def merge_videos(video_paths, output_path):
    """
    Merge multiple videos into a single video.

    :param video_paths: List of paths to the video files to be merged.
    :param output_path: Path to save the merged video.
    """
    
    # Load all video clips
    clips = [VideoFileClip(vid_path) for vid_path in video_paths]

    # Concatenate video clips
    merged_video = concatenate_videoclips(clips)

    # Write the result to a file
    merged_video.write_videofile(output_path, codec='libx264')

    print(f"Videos merged and saved to {output_path}")

# Example usage:
video_paths = [
    "a.mp4",
    "b.mp4",
    "d.mp4",
    "e.mp4",
    "f.mp4"
    ]
video_paths_with_full_adv = []
for path in video_paths:
    video_paths_with_full_adv.append(path)
    # video_paths_with_full_adv.append("Fullscreen-adv-merge.mp4")
output_path = "output_merged.mp4"
merge_videos(video_paths_with_full_adv, output_path)
