# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionUtterIamabot(Action):
    def name(self) -> Text:
        return "utter_iamabot"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Hi! I am StreeSahayak, your Women's Rights Awareness Chatbot.")
        return []

class ActionDirectToLinks(Action):
    def name(self) -> Text:
        return "action_direct_to_links"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        links_response = """
         Yes. You can visit the following websites for more information:
        - [National Commission for Women (NCW)](https://ncw.nic.in/)
        - [Breakthrough India](https://www.breakthrough.tv/)
        - [Women Helpline 181](https://wcd.nic.in/whatsnew/women-helpline-181)
        - [UN Women](https://www.unwomen.org/)
        - [Global Fund for Women](https://www.globalfundforwomen.org/)
        - [Women's Aid](https://www.womensaid.org.uk/)
        - [Girls Not Brides](https://www.girlsnotbrides.org/)
        
        """
        
        dispatcher.utter_message(text=links_response)

        return []



class ActionProvideSafetyAppsForWomenIndia(Action):
    def name(self) -> Text:
        return "action_provide_safety_apps_for_women_india"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        safety_apps = [
            {
                "app_name": "Nirbhaya: Be Fearless You app",
                "link": "https://play.google.com/store/apps/details?id=com.nirbhaya"
            },
            {
                "app_name": "My Safetipin app",
                "link": "https://play.google.com/store/apps/details?id=com.safetipin.mysafetipin"
            },
            {
                "app_name": "SHe-Box (Sexual Harassment Electronic Box) app",
                "link": "https://shebox.nic.in/"
            },
            {
                "app_name": "RAHAT (Road Ahead for Humanity Action by Traffic Police) app",
                "link": "https://play.google.com/store/apps/details?id=com.delhipolice"
            },
            {
                "app_name": "Himmat Plus app (Delhi Police initiative)",
                "link": "https://play.google.com/store/apps/details?id=com.mobicop.himmatplus"
            }
        ]

        dispatcher.utter_message(text="Here are some useful apps for women's safety:")
        for app in safety_apps:
            dispatcher.utter_message(
                text=f"{app['app_name']}: {app['link']}"
            )

        return []




class ActionProvideSafetyNumbers(Action):
    def name(self) -> Text:
        return "action_provide_safety_numbers"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        safety_numbers = [
            {"name": "Women Helpline 1091", "number": "1091"},
            {"name": "Women Helpline 181", "number": "181"},
            {"name": "Child Helpline 1098", "number": "1098"},
            {"name": "Police Control Room 100", "number": "100"},
            {"name": "National Commission for Women (NCW)", "number": "+911123213204"},
            {"name": "Ministry of Women and Child Development (WCD)", "number": "+911123313789"},

        ]

        response = ""
        for safety_number in safety_numbers:
            response += f"{safety_number['name']}: {safety_number['number']}\n"

        dispatcher.utter_message(text=response)

        return []
    
class ActionProvideRightsDetails(Action):
    def name(self) -> Text:
        return "action_provide_rights_details"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        rights_details = """Here are some key rights of women in India:
        1. Right to Equality
        2. Freedom from Discrimination
        3. Protection against Violence
        4. Right to Education
        5. Political Rights
        6. Right to Inheritance
        7. Right to Work
        8. Maternity Rights
        9. Right to Health
        10. Right to Property

        
         Women in India have the right to equality, which includes equal pay for equal work and equal access to opportunities. They are protected from discrimination based on gender in various aspects of life, including employment, education, and public services. Additionally, there are laws and provisions in place to safeguard women from various forms of violence, including domestic violence, sexual harassment, and trafficking. Women also have the right to education, ensuring access to schooling and higher education. Furthermore, women have political rights, including the right to vote and stand for elections. They have the right to inherit property, allowing them to claim their rightful share of ancestral property. Women also have the right to work, with legal protections against workplace discrimination. Maternity rights ensure women's access to maternity leave and benefits during pregnancy and childbirth. Additionally, women have the right to health, including access to healthcare services and facilities. Other rights include the right to information, privacy, freedom of speech and expression, legal aid, social security, childcare, reproductive health, a safe environment, fair trials, and non-discrimination in public spaces."""
        
        dispatcher.utter_message(text=rights_details)

        return []

class ActionReportCyberstalking(Action):
    def name(self) -> Text:
        return "action_report_cyberstalking"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Provide Indian victim support information
        support_message = ("I'm sorry to hear that. Please contact one of the following helplines or visit their websites for assistance:\n"
                           "1. National Commission for Women (NCW) helpline: 1091, Website: www.ncw.nic.in\n"
                           "2. Cyber Crime Reporting Portal (Ministry of Home Affairs): Website: www.cybercrime.gov.in\n"
                           "3. Cyber Crime Cells of local police departments (e.g., Delhi, Mumbai, Bengaluru, Chennai, Kolkata): "
                           "Please check your local police department's website for contact information.")

        # Send the support message back to the user
        dispatcher.utter_message(text=support_message)
        
        return []