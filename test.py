import re
from moviepy.editor import *

body = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin fringilla accumsan purus. Cras nibh lorem, scelerisque at sollicitudin non, pulvinar eget lacus.\nDonec velit ex, viverra eu lacus eget, auctor facilisis neque. Cras sollicitudin consequat blandit.\nQuisque varius rutrum justo sed vulputate. Aliquam non fringilla urna,\n\nsit amet finibus erat. Nullam semper magna a suscipit pretium. Nullam dictum lorem non consequat maximus.'

# body = body.split('. ')
# temp_body = []
# sentences = []
#
# for sentence in body:
#     if '\n' in sentence:
#         sentences = sentence.split('\n')
#         sentences = [beak + (' ' * (100 - len(beak))) for beak in sentences]
#
# body[-1] = body[-1][:-2]
#
# text = 'The quick brown\nfox jumps*over the lazy dog.'
# print(re.split('; |. |\n', text))

d = '. '
body = [s + d for s in body.split(d) if s]
body[-1] = body[-1][:-2]






text = ""
sentenceclip_list = []

for sentence in body:
    text = text + sentence

    textclip = TextClip(text, fontsize=10, size=(1280, 1080), color='white', method='caption', align='West').set_duration(2)

    sentenceclip_list.append(textclip)


video = concatenate(sentenceclip_list, method="compose")

background = ImageClip('background.jpg', transparent=False)

video = CompositeVideoClip([background, video], use_bgclip=True, size=(1920, 1080))
video.write_videofile("video.mp4", fps=24)