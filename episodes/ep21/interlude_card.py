"""Builds card_interlude.mov: Jackson's interlude.m4a under a TIMETRAVEL card, used as an insert block before the bathroom intermission."""
import subprocess
from PIL import Image, ImageDraw, ImageFont

W, H = 1280, 720
ACC, WHITE = (255, 210, 74, 255), (255, 255, 255, 255)
bg = Image.open('bg_title.png').convert('RGBA').resize((W, H))
d = ImageDraw.Draw(bg)


def center(y, text, f, fill):
    bb = d.textbbox((0, 0), text, font=f)
    d.text(((W - bb[2] + bb[0]) / 2, y), text, font=f, fill=fill)


center(228, "UNDERPOD", ImageFont.truetype('arialbold.ttf', 30), (235, 235, 235, 255))
center(272, "TIMETRAVEL", ImageFont.truetype('arialblack.ttf', 112), ACC)
center(418, "a break from the madness", ImageFont.truetype('arialbold.ttf', 34), WHITE)
bg.save('png_interlude.png')
subprocess.run(["ffmpeg", "-v", "error", "-y", "-loop", "1", "-framerate", "30", "-i", "png_interlude.png",
                "-i", "../interlude.m4a", "-t", "3.0933",
                "-vf", "format=yuv420p,fade=t=in:st=0:d=0.2,fade=t=out:st=2.75:d=0.34",
                "-af", "loudnorm=I=-18:TP=-2:LRA=7,aresample=48000",
                "-c:v", "h264_videotoolbox", "-b:v", "10M", "-c:a", "pcm_s16le", "-ar", "48000", "-ac", "1",
                "-shortest", "card_interlude.mov"], check=True)
