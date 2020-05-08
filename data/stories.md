## happy path
* greet
  - utter_greet
* mood_great
  - utter_mood_great

## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_mood_unhappy
  - utter_ask_for_help
* affirm
  - utter_mood_great

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_mood_unhappy
  - utter_ask_for_help
* deny
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_bot_challenge

## corona ask
* greet
  - utter_greet
* COVID_19
  - respond_faq
  - utter_ask_confirm
* deny
  - utter_goodbye

## Some question from FAQ
* faq
    - respond_faq
