import random
import struct
import wave
import soundcloud
import os, re, urllib


SONG_NAME = 'FinalTESTING'

requiredParams = {
        'sending': {
            'ID':'Application ID for Soundcloud API',
            'secret': 'Application secret for Soundcloud API',
            'username': 'Username of Soundcloud account to post data to',
            'password': 'Password of Soundcloud account to post data to'
            },
        'recieving': {
            'song_name':'Name of the sound file to be downloaded'
            }
        }

def send(data, params):
    client = soundcloud.Client(
        client_id=os.environ.get('SOUNDCLOUD_ID'),
        client_secret=os.environ.get('SOUNDCLOUD_Secret'),
        username=os.environ.get('SOUNDCLOUD_GMAIL'),
        password=os.environ.get('SOUNDCLOUD_PASS')
    )

    frames = []

    f = open('test.txt','r')
    for i in f:
        frames.append(i)

    wf = wave.open('output.wav', 'wb')
    wf.setnchannels(1)
    wf.setframerate(44100)
    wf.setsampwidth(2)
    wf.writeframes(b''.join(frames))
    wf.close()

    print "Done creating sound file"
    track = client.post('/tracks', track={
        'title': SONG_NAME,
        'sharing':'public',
        'asset_data': open('output.wav','rb'),
        'tag_list':'tag1 \"hip hop\"',
        'downloadable': 'true' })
    print "Done uploading"

    #TODO: Remove this comment
    #os.remove('output.wav')

    return

def receive(params):
    #TODO: Make this work
    urllib.urlretrieve("http://soundcloud.com/user255215947/" +SONG_NAME+ "/download", 'file.wav')
    wf = wave.open('file.wav', 'r')
    print wf.readframes(100)


    # TRYING TO OPEN IT AS A TXT FILE
    #f = open('file.wav','r')
    #for i in f.read():
    #    print struct.unpack('s', i)
    #struct.pack('c',f.read())
    
if __name__ == "__main__":
    #send(1,1)
    receive(1)
