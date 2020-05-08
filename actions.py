# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"


from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import UserUtteranceReverted


class ActionGreetUser(Action):
    """Revertible mapped action for utter_greet"""

    def name(self):
        return "action_greet"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_template("utter_greet", tracker)
        return [UserUtteranceReverted()]

# class ActionDefaultAskAffirmation(Action):
#     """Asks for an affirmation of the intent if NLU threshold is not met."""
#
#     def name(self) -> Text:
#         return "action_default_ask_affirmation"
#
#     def __init__(self) -> None:
#         import pandas as pd
#
#         self.intent_mappings = pd.read_csv(INTENT_DESCRIPTION_MAPPING_PATH)
#         self.intent_mappings.fillna("", inplace=True)
#         self.intent_mappings.entities = self.intent_mappings.entities.map(
#             lambda entities: {e.strip() for e in entities.split(",")}
#         )
#
#     def run(
#         self,
#         dispatcher: CollectingDispatcher,
#         tracker: Tracker,
#         domain: Dict[Text, Any],
#     ) -> List[EventType]:
#
#         intent_ranking = tracker.latest_message.get("intent_ranking", [])
#         if len(intent_ranking) > 1:
#             diff_intent_confidence = intent_ranking[0].get(
#                 "confidence"
#             ) - intent_ranking[1].get("confidence")
#             if diff_intent_confidence < 0.2:
#                 intent_ranking = intent_ranking[:2]
#             else:
#                 intent_ranking = intent_ranking[:1]
#         first_intent_names = [
#             intent.get("name", "")
#             for intent in intent_ranking
#             if intent.get("name", "") != "out_of_scope"
#         ]
#
#         message_title = (
#             "Sorry, I'm not sure I've understood " "you correctly 🤔 Do you mean..."
#         )
#
#         entities = tracker.latest_message.get("entities", [])
#         entities = {e["entity"]: e["value"] for e in entities}
#
#         entities_json = json.dumps(entities)
#
#         buttons = []
#         for intent in first_intent_names:
#             logger.debug(intent)
#             logger.debug(entities)
#             buttons.append(
#                 {
#                     "title": self.get_button_title(intent, entities),
#                     "payload": "/{}{}".format(intent, entities_json),
#                 }
#             )
#
#         # /out_of_scope is a retrieval intent
#         # you cannot send rasa the '/out_of_scope' intent
#         # instead, you can send one of the sentences that it will map onto the response
#         buttons.append(
#             {
#                 "title": "Something else",
#                 "payload": "I am asking you an out of scope question",
#             }
#         )
#
#         dispatcher.utter_message(text=message_title, buttons=buttons)
#
#         return []
#
#     def get_button_title(self, intent: Text, entities: Dict[Text, Text]) -> Text:
#         default_utterance_query = self.intent_mappings.intent == intent
#         utterance_query = (self.intent_mappings.entities == entities.keys()) & (
#             default_utterance_query
#         )
#
#         utterances = self.intent_mappings[utterance_query].button.tolist()
#
#         if len(utterances) > 0:
#             button_title = utterances[0]
#         else:
#             utterances = self.intent_mappings[default_utterance_query].button.tolist()
#             button_title = utterances[0] if len(utterances) > 0 else intent
#
#         return button_title.format(**entities)
