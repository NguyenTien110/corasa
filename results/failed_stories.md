## sad path 1
* greet: chàooo   <!-- predicted: inform: [chàooo](country) -->
    - slot{"country": "chàooo"}
    - utter_greet   <!-- predicted: utter_goodbye -->
* mood_unhappy: Tệ thật
    - utter_mood_unhappy
    - utter_ask_for_help
* affirm: Chính xác
    - utter_mood_great


## corona ask
* greet: hello
    - utter_greet
* faq: COVID-19 là gì vậy?
    - respond_faq
    - utter_ask_confirm   <!-- predicted: action_listen -->
    - action_listen   <!-- predicted: form_ask_covid -->
* deny: không bao giờ
    - utter_goodbye


