#!/usr/bin/env python
# coding: utf-8

# In[8]:


from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet

class ActionWeather(Action):
    def name(self):
        return 'action_weather'

    def run(self, dispatcher, tracker, domain):
        from apixu.client import ApixuClient
        api_key = '2ba4cf94bbc2427791294257191205' #your apixu key
        client = ApixuClient(api_key)
        loc = tracker.get_slot('location')
        current = client.current(q=loc)
        country = current['location']['country']
        city = current['location']['name']
        condition = current['current']['condition']['text']
        temperature_c = current['current']['temp_c']
        humidity = current['current']['humidity']
        wind_mph = current['current']['wind_mph']
        response = """It is currently {} in {} at the moment. The temperature is {} degrees, the humidity is {}% and the 
                        wind speed is {} mph.""".format(condition, city, temperature_c, humidity, wind_mph)
        ##loc = tracker.get_slot('location')
        ##response = "weather is absolutely fantastic"
        dispatcher.utter_message(response)
        return [SlotSet('location',loc)]


# In[ ]:





# In[ ]:




