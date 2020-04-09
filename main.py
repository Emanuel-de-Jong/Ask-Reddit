import reddit as rd
import tts as tts
# import video as vid

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
                'I had a kid who really wanted his parents to come to his graduation ceremony, but they were both sex offenders and couldn’t be on campus. ',
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
                'The first day of school I\'m getting to know the kids by asking them random questions and I ask this one boy what he wants to be when he grows up and he replies with "doesn\'t matter- I\'m going to end up in prison like my parents." Wooooah okay. ',
                'From there things got progressively worse. ',
                'He was hearing voices and always threatening to hurt other staff or students. ',
                'He was hitting his head on walls or windows when frustrated. ',
                'He came back from spring break and told me the voices told him to kill a cat he found. ',
                'By the end of the year he was sexually assaulting girls at school.'
            ]
        },
        {
            'author': 'kidswantapuppy',
            'created_utc': 1586405456.0,
            'is_submitter': False,
            'score': 15182,
            'body': [
                'I teach an algebra class and I was explaining how (in our city at least) your address tells you how far you are from the central streets like a Cartesian coordinate system. ',
                'A girl, who happens to be my daughters friend, volunteered to let me graph her address. ',
                'Three months later a boy got expelled for threatening to shoot up the school. ',
                'He had her address and written threats to kidnap her from her house. ',
                'He got the address from that class.'
            ]
        }
    ]

    tts.init()
    tts.convert_comments_to_audio(comment_list)
