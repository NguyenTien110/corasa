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
* faq
  - respond_faq
* deny
  - utter_goodbye

## Some question from FAQ
* faq
  - respond_faq

## Ask statistic death
* ask_death
  - utter_ask_death

## Ask statistic all
* ask_all
  - utter_ask_all

## Ask statistic resolve
* ask_resolve
  - utter_ask_resolve

## Ask statistic confirm
* ask_confirm
  - utter_ask_confirm

## ask country
* ask_country
  - form_ask_covid
  - form{"name": "form_ask_covid"}   <!--Activate the form-->
  - form{"name": null}               <!--Deactivate the form-->

