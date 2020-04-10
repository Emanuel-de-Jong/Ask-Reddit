from moviepy.editor import *
import soundfile as sf


def create_video(comment_list, fontsize=20, color='white', fps=24, codec='mpeg4'):
    clip_list = []

    for i in range(len(comment_list)):
        comment = comment_list[i]

        for j in range(len(comment['body'])):
            sentence = comment['body'][j]
            audio_path = 'comments\\' + str(i) + '-' + str(j) + '.mp3'

            file = sf.SoundFile(audio_path)
            file_length = round(len(file) / file.samplerate)

            try:
                videoclip = TextClip(sentence, fontsize=fontsize, color=color)
                videoclip = videoclip.set_duration(file_length)

                audioclip = AudioFileClip(audio_path)

                clip = videoclip.set_audio(audioclip)

                clip_list.append(clip)
            except UnicodeEncodeError:
                print('video create_video error:')
                print('UnicodeEncodeError while initializing TextClip with txt:')
                print(sentence)
                print('or AudioFileClip at:')
                print(audio_path)

    video = concatenate(clip_list, method="compose")
    video.write_videofile("video.mp4", fps=fps, codec=codec)

    print('video create_video complete')
    return True




# audio = AudioFileClip("audio.mp3")
# video1 = VideoFileClip("video1.mp4")
# video2 = VideoFileClip("video2.mp4")
# final = concatenate_videoclips([video1, video2]).set_audio(audio)
# final.write_videofile("output.mp4")







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
