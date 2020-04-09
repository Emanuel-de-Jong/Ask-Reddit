import pyttsx3


engine = None


def init(voice='HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0',
         rate=150, volume=1.0):
    global engine
    engine = pyttsx3.init()

    engine.setProperty('voice', voice)
    engine.setProperty('rate', rate)
    engine.setProperty('volume', volume)

    print('tts init complete')
    return True


def convert_comments_to_audio(comment_list, extension='mp3'):
    for i in range(len(comment_list)):
        comment = comment_list[i]

        for j in range(len(comment['body'])):
            sentence = comment['body'][j]

            engine.save_to_file(sentence, 'comments\\' + str(i) + '-' + str(j) + '.' + extension)

    engine.runAndWait()

    print('tts convert_comments_to_audio complete')
    return True
