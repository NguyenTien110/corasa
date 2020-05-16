#### This file contains tests to evaluate that your bot behaves as expected.
#### If you want to learn more, please see the docs: https://rasa.com/docs/rasa/user-guide/testing-your-assistant/

## happy path
* greet: xin chàooooooo
  - utter_greet
* mood_great: hoàn hảo!
  - utter_mood_great

## sad path 1
* greet: chàooo
  - utter_greet
* mood_unhappy: Tệ thật
  - utter_mood_unhappy
  - utter_ask_for_help
* affirm: Chính xác
  - utter_mood_great

## sad path 2
* greet: chào Bot
  - utter_greet
* mood_unhappy: buồn thế
  - utter_mood_unhappy
  - utter_ask_for_help
* deny: không bao giờ
  - utter_goodbye

## say goodbye
* goodbye: bye!
  - utter_goodbye

## bot challenge
* bot_challenge: Tôi đang nói chuyện với bot phải không?
  - utter_bot_challenge

## corona ask
* greet: hello
  - utter_greet
* faq: COVID-19 là gì vậy?
  - respond_faq
  - utter_ask_confirm
* deny: không bao giờ
  - utter_goodbye

## Some question from FAQ
* faq: Hình như tôi có triệu chứng của bệnh tôi phải làm gì bây giờ?
    - respond_faq
