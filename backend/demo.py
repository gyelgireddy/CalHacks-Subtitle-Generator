import io
import os

# Imports the Google Cloud client library
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types

# Instantiates a client
client = speech.SpeechClient()

# The name of the audio file to transcribe
file_name = os.path.join(
    os.path.dirname(__file__),
    'resources',
    '61a.wav')

# Loads the audio into memory
with io.open(file_name, 'rb') as audio_file:
    content = audio_file.read()
    audio = types.RecognitionAudio(content=content)

config = types.RecognitionConfig(
    encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
    sample_rate_hertz=44100,
    language_code='en-US',
    enable_word_time_offsets=True)

# Detects speech in the audio file
response = client.recognize(config, audio)

i = 1
words = []
bookend = {
        "start": None,
        "end": None
    }
    
for result in response.results:
    # print('Transcript: {}'.format(result.alternatives[0].transcript))
    alternative = result.alternatives[0]
    # print(u'Transcript: {}'.format(alternative.transcript))
    # print('Confidence: {}'.format(alternative.confidence))

    # Original Implementation
    # for word_info in alternative.words:
    #     word = word_info.word
    #     start_time = word_info.start_time
    #     end_time = word_info.end_time
    #     print('Word: {}, start_time: {}, end_time: {}'.format(
    #         word,
    #         start_time.seconds + start_time.nanos * 1e-9,
    #         end_time.seconds + end_time.nanos * 1e-9))
    
    


    for word_info in alternative.words:
        word = word_info.word
        start_time = word_info.start_time
        end_time = word_info.end_time
        words.append(word)
        if ((len(words) - 1) % 8) == 0:
            bookend["start"] = "00:" + "00:" + str(start_time.seconds) + "," + str(int(start_time.nanos * 1e-8)) + "00"
        elif (len(words) % 8) == 0:
            bookend["end"] = "00:" + "00:" + str(end_time.seconds) + "," + str(int(end_time.nanos * 1e-8)) + "00"
            print("\n")
            print(i)
            print(bookend["start"] + " --> " + bookend["end"])
            for item in words:
                print(item, end=' ')
                words = []
                i += 1
        


