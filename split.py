import os
from moviepy.editor import VideoFileClip

def split_video(video_path, output_folder, duration=300):
    """
    Split video into segments of a specified duration (in seconds).

    :param video_path: Path to the video file.
    :param output_folder: Folder where the split videos will be saved.
    :param duration: Duration of each segment in seconds (default 300s or 5 minutes).
    """

    # Ensure output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Load video
    video = VideoFileClip(video_path)

    total_duration = int(video.duration)

    for i in range(0, total_duration, duration):
        # Calculate start and end times for each segment
        start_time = i
        end_time = min(i + duration, total_duration)

        # Slice video segment
        segment = video.subclip(start_time, end_time)

        # Save video segment
        segment_filename = f"{output_folder}/segment_{i//duration + 1}.mp4"
        segment.write_videofile(segment_filename, codec="libx264")

    print("Video splitting complete!")

# Example usage:
video_path = "durga-pooja-collage.mp4"
output_folder = "output"
split_video(video_path, output_folder)
