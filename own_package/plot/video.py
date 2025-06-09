import os
import subprocess


# Creates video using the image_path at video_path
def make_video(image_path, video_path, framerate=5, zfill_n=5, theme="bright"):
    video_cmd = [
        "ffmpeg",
        "-framerate",
        str(framerate),
        "-i",
        f"{image_path}_%0{zfill_n}d.png",
    ]

    if theme == "bright":
        video_cmd += [
            "-vf",
            "pad=ceil(iw/2)*2:ceil(ih/2)*2, fps=25, format=yuv420p",
        ]
    elif theme == "dark":
        video_cmd += ["-c", "copy"]

    video_cmd.append(f"{video_path}.mp4")

    print("Command:", " ".join(video_cmd))

    result = subprocess.run(video_cmd, capture_output=True, text=True)
    if result.returncode != 0:
        raise RuntimeError(
            f"Video creation failed with exit code {result.returncode}: {result.stderr}"
        )
