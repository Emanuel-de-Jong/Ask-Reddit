from moviepy.editor import *


def create_video(comment_list, title, fontsize=30, text_color='white', fps=24, screen_size=(1920, 1080), bg_image='background.jpg'):
    commentclip_list = []

    for i in range(len(comment_list)):
        comment = comment_list[i]
        text = ""
        sentenceclip_list = []

        for j in range(len(comment['body'])):
            sentence = comment['body'][j]

            text = text + sentence

            audio_path = 'comments\\' + str(i) + '-' + str(j) + '.mp3'
            audioclip = AudioFileClip(audio_path)
            audioclip = CompositeAudioClip([audioclip])

            textclip = TextClip(text, fontsize=fontsize, size=(1280, 1080), color=text_color, method='caption', align='West')
            textclip = textclip.set_duration(audioclip.duration)

            sentenceclip = textclip.set_audio(audioclip)
            sentenceclip_list.append(sentenceclip)

        commentclip = concatenate(sentenceclip_list, method="compose")
        commentclip_list.append(commentclip)

    video = concatenate(commentclip_list, method="compose")

    background = ImageClip(bg_image, transparent=False)

    video = CompositeVideoClip([background, video], use_bgclip=True, size=screen_size)
    video.write_videofile("video.mp4", fps=fps)

    print('video create_video complete')
    return True






# screensize = (1920,1080)
# text = ('''MoviePy is a Python module for video editing, which can be used for basic operations (like cuts, concatenations, title insertions), video compositing (a.k.a. non-linear editing), video processing, or to create advanced effects. It can read and write the most common video formats, including GIF.''')
#
# text_list = text.split(" ")
#
#
#
# clip_list = []
# i = 0
# b = 4
# while len(text_list) + 1 > b:
#
#     text = str(" ".join(text_list[i:b]))
#     try:
#         txt_clip = TextClip(text, fontsize = 50, color = 'black',size=screensize,bg_color = 'white',method='caption',align='West').set_duration(1)
#         clip_list.append(txt_clip)
#         b += 4
#
#     except UnicodeEncodeError:
#         txt_clip = TextClip("Issue with text", fontsize = 70, color = 'white').set_duration(2)
#         clip_list.append(txt_clip)
#
# final_clip = concatenate(clip_list, method = "compose")
#
# final_clip.write_videofile("my_concatenation9.mp4", fps = 24, codec = 'mpeg4')







# import moviepy.editor as mpy
# import gizeh as gz
# from math import pi
#
#
# VIDEO_SIZE = (640, 480)
# BLUE = (59/255, 89/255, 152/255)
# GREEN = (176/255, 210/255, 63/255)
# WHITE = (255, 255, 255)
# WHITE_GIZEH = (1, 1, 1)
# SB_LOGO_PATH = './assets/StackBuildersLogo.jpg'
# DURATION = 10
#
#
# def render_text(t):
#     surface = gz.Surface(640, 60, bg_color=WHITE_GIZEH)
#     text = gz.text(
#         "Let's build together", fontfamily="Charter",
#         fontsize=30, fontweight='bold', fill=BLUE, xy=(320, 40))
#     text.draw(surface)
#     return surface.get_npimage()
#
#
# def draw_stars(t):
#     surface = gz.Surface(640, 120, bg_color=WHITE_GIZEH)
#     for i in range(5):
#         star = gz.star(
#             nbranches=5, radius=120*0.2, ratio=0.5,
#             xy=[100*(i+1), 50], fill=GREEN, angle=t * pi)
#         star.draw(surface)
#     return surface.get_npimage()
#
#
# if __name__ == '__main__':
#     sb_logo = mpy.ImageClip(SB_LOGO_PATH). \
#         set_position(('center', 0)).resize(width=200)
#     text = mpy.VideoClip(render_text, duration=DURATION)
#     stars = mpy.VideoClip(draw_stars, duration=DURATION)
#
#     video = mpy.CompositeVideoClip(
#         [
#             sb_logo,
#             text.set_position(
#                 ('center', sb_logo.size[1])),
#             stars.set_position(
#                 ('center', sb_logo.size[1] + text.size[1])
#             )
#         ],
#         size=VIDEO_SIZE).\
#         on_color(
#             color=WHITE,
#             col_opacity=1).set_duration(DURATION)
#
#     video.write_videofile('video_with_python.mp4', fps=10)
