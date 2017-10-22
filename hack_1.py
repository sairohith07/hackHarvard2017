
# coding: utf-8

# In[139]:


from google.cloud import speech
import os


# In[142]:


os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="C:\\Users\\Tanvi Patil\\Downloads\\json_file.json"


# In[143]:


client = speech.SpeechClient()


# In[145]:


audio_init = "C:\\Users\\Tanvi Patil\\Desktop\\hack_harvard_stuff\\man1_nb.wav"
with io.open(audio_init, 'rb') as audio_file:
        content = audio_file.read()


# In[148]:


audio = types.RecognitionAudio(content=content)
config = types.RecognitionConfig(
    encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
    sample_rate_hertz=8000,
    language_code='en-US',enable_word_time_offsets=True)


# In[149]:


response = client.recognize(config, audio)


# In[150]:


for result in response.results:
        print('Transcript: {}'.format(result.alternatives[0].transcript))


# In[151]:


for wr in result.alternatives[0].words:
    print(wr)

