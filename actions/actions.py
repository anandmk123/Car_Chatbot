from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet 

class ActionClearSlots(Action):
    def name(self) -> str:
        return "action_clear_slots"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain) -> list:

        # List of slots to clear
        slots_to_clear = [
            "manufacturer",
            "model",
            "kms_driven",
            "mileage",
            "fuel_type",
            "transmission_type",
            "engine",
            "max_power",
            "seats",
            "year_of_manufacture"
        ]

        # Clear the slots by setting them to None
        return [SlotSet(slot, None) for slot in slots_to_clear]
