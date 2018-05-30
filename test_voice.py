# Import the required module for text 
# to speech conversion
from gtts import gTTS
#import vlc
 
# This module is imported so that we can 
# play the converted audio
import os
 
# The text that you want to convert to audio
mytext = 'it is hard enough for CISOs to deal with humans in their enterprises. A new report from a security vendor warns increasingly they have to deal with cobots, slang for collaborative robots that work alongside peoples in workplaces. ' 
# Language in which you want to convert
language = 'en'
 
# Passing the text and language to the engine, 
# here we have marked slow=False. Which tells 
# the module that the converted audio should 
# have a high speed
myobj = gTTS(text=mytext, lang=language, slow=False)
 
# Saving the converted audio in a mp3 file named
# welcome 
myobj.save("welcome.mp3")
 
# Playing the converted file
#p=vlc.Mediaplayer("welcome.mp3")
#p.play()
os.system("mpg321 welcome.mp3")
