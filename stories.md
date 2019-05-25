    ##story 001
*greet
    -utter_greet
*inform    
    -utter_greet     
    -utter_ask_location
*goodbye
      -utter_goodbye
      -export
      
    ##story 002
* greet
    - utter_greet
* inform
    - utter_ask_location
* inform{"location": "italy"}
    - slot{"location": "italy"}
    - action_weather
    - slot{"location": "italy"}
* goodbye
    - utter_goodbye
    - export
    
## Generated Story 6624087084583363871
* greet
    - utter_greet
* inform{"location": "vilnius"}
    - slot{"location": "vilnius"}
    - action_weather
    - action_weather
* greet
    - action_weather
    - action_weather

## Generated Story 7169869215662962142
* greet
    - utter_greet
* inform{"location": "berlin"}
    - slot{"location": "berlin"}
    - action_weather
    - action_weather
* goodbye

## Generated Story 2052863387068730358
* greet
    - utter_greet
* inform{"location": "berlin"}
    - slot{"location": "berlin"}
    - action_weather

## Generated Story 6319427162263353284
* greet
    - utter_greet
* inform{"location": "berlin"}
    - slot{"location": "berlin"}
    - action_weather

## Generated Story -1816710832190316474
* greet
    - utter_greet
* inform{"location": "berlin"}
    - slot{"location": "berlin"}
    - action_weather

## Generated Story 8515468202884486429
* greet
    - utter_greet
* inform{"location": "berlin"}
    - slot{"location": "berlin"}
    - action_weather

## Generated Story -4094484689580551205
* greet
    - utter_greet
* inform{"location": "berlin"}
    - slot{"location": "berlin"}
    - action_weather

## Generated Story 2929921937131707037
* greet
    - utter_greet
* inform{"location": "berlin"}
    - slot{"location": "berlin"}
    - action_weather

## Generated Story -8929643466214360405
* greet
    - utter_greet
* inform{"location": "berlin"}
    - slot{"location": "berlin"}
    - action_weather

## Generated Story 4349158683368216476
* greet
    - utter_greet
* inform{"location": "berlin"}
    - slot{"location": "berlin"}
    - action_weather
    - slot{"location": "berlin"}
* goodbye
    - action_default_fallback
    - rewind
* goodbye

## Generated Story -3130953073766382490
* greet
    - utter_greet
* inform{"location": "berlin"}
    - slot{"location": "berlin"}
    - action_weather

## Generated Story 7466092478939647714
* greet
    - utter_greet
* inform{"location": "berlin"}
    - slot{"location": "berlin"}
    - action_weather

## Generated Story 920826521964721257
* greet
    - utter_greet
* inform{"location": "berlin"}
    - slot{"location": "berlin"}
    - action_weather
    - slot{"location": "berlin"}
* goodbye
    - action_default_fallback
    - rewind
* goodbye
    - action_default_fallback
    - rewind
* inform{"location": "chennai"}
    - slot{"location": "chennai"}
    - action_weather
    - slot{"location": "chennai"}
* greet
    - action_default_fallback
    - rewind

