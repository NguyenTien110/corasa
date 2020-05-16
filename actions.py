# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from crawl_data import fetching_general_data
from crawl_data.fetching_general_data import run_query
from typing import Any, Text, Dict, List, Union

import logging
logger = logging.Logger(__name__)

import json

from rasa_sdk.forms import FormAction
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import (
    SlotSet,
    UserUtteranceReverted,
    ConversationPaused,
    EventType,
    ActionExecuted,
    UserUttered,
)

class ActionGreetUser(Action):
    """bỏ qua các input không lường trước"""

    def name(self):
        return "action_greet"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_template("utter_greet", tracker)
        return [UserUtteranceReverted()]

class ActionDefaultAskAffirmation(Action):
    """đưa ra 1 vài câu hỏi thường gặp khi gặp intent không hiểu"""

    def name(self) -> Text:
        return "action_default_ask_affirmation"

    def __init__(self) -> None:
        import pandas as pd

        self.intent_mappings = pd.read_csv('./intent_mapping.csv')
        self.intent_mappings.fillna("", inplace=True)
        self.intent_mappings.entities = self.intent_mappings.entities.map(
            lambda entities: {e.strip() for e in entities.split(",")}
        )

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[EventType]:

        intent_ranking = tracker.latest_message.get("intent_ranking", [])
        print(len(intent_ranking))
        print(intent_ranking)
        if len(intent_ranking) > 1:
            diff_intent_confidence = intent_ranking[0].get("confidence") - intent_ranking[1].get("confidence")
            if diff_intent_confidence < 0.2:
                intent_ranking = intent_ranking[:2]
            else:
                intent_ranking = intent_ranking[:1]
        print(intent_ranking)
        first_intent_names = [
            intent.get("name", "").get()
            for intent in intent_ranking
            if intent.get("name", "") != "out_of_scope"
        ]

        message_title = (
            "Xin lỗi, có vẻ mình không hiểu ý của bạn lắm 🤔 Có phải bạn muốn ..."
        )

        entities = tracker.latest_message.get("entities", [])
        entities = {e["entity"]: e["value"] for e in entities}

        entities_json = json.dumps(entities)

        buttons = []
        for intent in first_intent_names:
            logger.debug(intent)
            logger.debug(entities)
            buttons.append(
                {
                    "title": self.get_button_title(intent, entities),
                    "payload": "/{}{}".format(intent, entities_json),
                }
            )

        buttons.append(
            {
                "title": "Something else",
                "payload": "Tôi hỏi câu khác :(",
            }
        )

        dispatcher.utter_message(text=message_title, buttons=buttons)

        return []

    def get_button_title(self, intent: Text, entities: Dict[Text, Text]) -> Text:
        default_utterance_query = self.intent_mappings.intent == intent
        utterance_query = (self.intent_mappings.entities == entities.keys()) & (
            default_utterance_query
        )

        utterances = self.intent_mappings[utterance_query].button.tolist()

        if len(utterances) > 0:
            button_title = utterances[0]
        else:
            utterances = self.intent_mappings[default_utterance_query].button.tolist()
            button_title = utterances[0] if len(utterances) > 0 else intent

        return button_title.format(**entities)

class ActionAskCovidInfor(FormAction):
    def name(self) -> Text:
        return "form_ask_covid"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ["country", "city"]
    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        return {
            "country": [
                self.from_entity(entity="country"),
                self.from_text(intent="inform"),
            ],
            "city": [
                self.from_entity(entity="city"),
                self.from_text(intent="inform")
            ],
        }

    def request_next_slot(self, dispatcher, tracker, domain):
        user_message = tracker.latest_message.get("text")
        logger.debug(user_message)

        for slot in self.required_slots(tracker):
            if self._should_request_slot(tracker, slot):
                logger.debug("Request next slot '%s'", slot)
                if slot == "country":
                    dispatcher.utter_message(template="utter_ask_country")
                    mess = tracker.latest_message['entities']

                    print("messes: /{}", mess, type(mess))
                    return [SlotSet('country', mess)]

                if slot == "city":
                    country = tracker.get_slot("country")
                    if(country == "Việt Nam"):
                        
                        return [SlotSet('country', None)]
                    else:
                        dispatcher.utter_message(template="utter_ask_city")
                        mess = tracker.latest_message['entities'][0].get('value')
                        print("messes: /{}", mess)
                        return [SlotSet('country', mess)]

        return None


    def submit(self, dispatcher, tracker, domain) -> List[Dict]:
        # do something here
        intent = tracker.latest_message['intent'].get('name')
        print(intent)
        # intent = intent.split('_')
        # print(intent)
        country = tracker.get_slot("country")
        city = tracker.get_slot("city")
        print(country, city[0])
        if country == "Việt Nam":
            data = run_query(fetching_general_data.vietnam_status)['totalVietNam']

            message_title = "Thông tin Việt Nam\nconfirmed: ", data['confirmed']
            dispatcher.utter_message(text=message_title)

        return []
