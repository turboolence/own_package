import builtins


def test_make_video_command(add_package_path, monkeypatch):
    add_package_path("plot")
    import video as vid

    commands = []
    monkeypatch.setattr(vid.os, "system", lambda cmd: commands.append(cmd))

    vid.make_video("frame/out", "movie/result", framerate=10, zfill_n=3, theme="dark")

    expected = "ffmpeg -framerate 10 -i frame/out_%03d.png -c copy movie/result.mp4"
    assert commands and commands[0] == expected
