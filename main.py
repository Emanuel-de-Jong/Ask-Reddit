import reddit as rd
import tts as tts
# import video as vid

if __name__ == '__main__':
    rd.init()
    comment_list = rd.get_top_level_comments()
    print(comment_list[0])

    # tts.init(comment_list)