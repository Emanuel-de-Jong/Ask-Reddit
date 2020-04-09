import reddit as rd
# import tts as tts
# import video as vid

if __name__ == '__main__':
    rd.init()
    comments = rd.get_top_level_comments()
    print(rd.post.title)
    print(comments[7])
