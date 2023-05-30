import pandas as pd

from typing import Any, Text, Dict, List

from rasa_sdk.events import SlotSet
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


# name remembering

class ActionReceiveName(Action):

    def name(self) -> Text:
        return "action_receive_name"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        text = tracker.latest_message['text']
        dispatcher.utter_message(text=f"I'll remember your name, {text}!")
        return [SlotSet("name", text)]


class ActionSayName(Action):

    def name(self) -> Text:
        return "action_say_name"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        name = tracker.get_slot("name")
        if not name:
            dispatcher.utter_message(text="I dont know your name, Friend.")
        else:
            dispatcher.utter_message(text=f"Your name is {name}!")
        return []


class ActionFetchAllExams(Action):
    def name(self) -> Text:
        return "action_all"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        df = pd.read_csv("Exams.csv")

        dispatcher.utter_message(text="Module - Paper - Date - Session - Category - Duration - Number of Students")

        for i, j in df.iterrows():
            dispatcher.utter_message(text=j['MODULE'] + " - " + str(j['PAPER']) + " - " + str(j['DATE']) + " - " + str(
                j['SESSION']) + " - " + str(j['CATEGORY']) + " - " + str(j['DURATION']) + " - " + str(
                j['NUMBER_OF_STUDENTS']))

        return []


class ActionFindSpecificExamModule(Action):
    def name(self) -> Text:
        return "action_fetch_module"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dframe = pd.read_csv("All_Exams.csv")
        module = tracker.latest_message['text']

        dispatcher.utter_message(text="Module - Paper - Date - Session - Category - Duration - Number of Students")

        for i, j in (dframe[dframe['MODULE'] == module]).iterrows():
            dispatcher.utter_message(text=j['MODULE'] + " - " + str(j['PAPER']) + " - " + str(j['DATE']) + " - " + str(
                j['SESSION']) + " - " + str(j['CATEGORY']) + " - " + str(j['DURATION']) + " - " + str(
                j['NUMBER_OF_STUDENTS']))

        return []


class ActionFindSpecificExamDate(Action):
    def name(self) -> Text:
        return "action_fetch_date"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dataf = pd.read_csv("All_Exams.csv")
        date = tracker.latest_message['text']

        dispatcher.utter_message(text="Module - Paper - Date - Session - Category - Duration - Number of Students")

        for i, j in (dataf[dataf['DATE'] == date]).iterrows():
            dispatcher.utter_message(text=j['MODULE'] + " - " + str(j['PAPER']) + " - " + str(j['DATE']) + " - " + str(
                j['SESSION']) + " - " + str(j['CATEGORY']) + " - " + str(j['DURATION']) + " - " + str(
                j['NUMBER_OF_STUDENTS']))

        return []


#class ActionFindAllClassTimes(Action):
#    def name(self) -> Text:
#        return "action_fetch_allClassTimes"

#    def run(self, dispatcher: CollectingDispatcher,
#            tracker: Tracker,
#            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#        df = pd.read_csv("ClassTimes.csv")

#        dispatcher.utter_message(text="Module - Class Time - Class Day")

#        for i, j in df.iterrows():
#           dispatcher.utter_message(
#                text=j['MODULE'] + " - " + str(j['CLASS TIME']) + " - " + str(j['CLASS DAY']))

 #       return []


#class ActionFindSpecificModuleTimes(Action):
#    def name(self) -> Text:
#        return "action_fetch_specModuleTimes"

#    def run(self, dispatcher: CollectingDispatcher,
#            tracker: Tracker,
#            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#        dframe = pd.read_csv("ClassTimes.csv")
#        module = tracker.latest_message['text']

#        dispatcher.utter_message(text="Module - Class Time - Class Day")

#        for i, j in (dframe[dframe['MODULE'] == module]).iterrows():
#            dispatcher.utter_message(text=j['MODULE'] + " - " + str(j['CLASS TIME']) + " - " + str(j['CLASS DAY']))

#        return []


#class ActionFindSpecificClassDay(Action):
#    def name(self) -> Text:
#        return "action_fetch_specClassDay"

#    def run(self, dispatcher: CollectingDispatcher,
#            tracker: Tracker,
#            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#        dataf = pd.read_csv("ClassTimes.csv")
#        day = tracker.latest_message['text']

#        dispatcher.utter_message(text="Module - Class Time - Class Day")

#        for i, j in (dataf[dataf['CLASS DAY'] == day]).iterrows():
#            dispatcher.utter_message(text=j['MODULE'] + " - " + str(j['CLASS TIME']) + " - " + str(j['CLASS DAY']))

#        return []

