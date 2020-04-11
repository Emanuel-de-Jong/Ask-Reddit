import reddit as rd
import tts as tts
import video as vid

if __name__ == '__main__':
    # rd.init()
    # comment_list = rd.get_top_level_comments()

    comment_list = [
        {
            'author': 'brokentelescope',
            'created_utc': 1586408909.0,
            'is_submitter': False,
            'score': 17723,
            'body': [
                'He was hitting his head on walls or windows when frustrated. ',
                'He just wanted *someone* there to support him.'
            ]
        },
        {
            'author': 'Luvmabubbles',
            'created_utc': 1586406830.0,
            'is_submitter': False,
            'score': 9466,
            'body': [
                'My first year teaching was like everyone says the worst year. ',
                'From there things got progressively worse. ',
                'He was hearing voices and always threatening to hurt other staff or students. ',
            ]
        }
    ]

    # tts.init()
    # tts.convert_comments_to_audio(comment_list)

    # vid.create_video(comment_list, rd.post.title)
    vid.create_video(comment_list, "What is this title?")
