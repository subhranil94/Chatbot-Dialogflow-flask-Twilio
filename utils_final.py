import dialogflow_v2 as dialogflow
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "euppchatbot-falvjy-b3e11662b170.json"
dialogflow_session_client = dialogflow.SessionsClient()
PROJECT_ID = "euppchatbot-falvjy"

def detect_intent_from_text(text, session_id, language_code='en'):
    session = dialogflow_session_client.session_path(PROJECT_ID, session_id)
    text_input = dialogflow.types.TextInput(text=text, language_code=language_code)
    query_input = dialogflow.types.QueryInput(text=text_input)
    response = dialogflow_session_client.detect_intent(session=session, query_input=query_input)
    return response.query_result

def fetch_reply(q,session):
    response_new = detect_intent_from_text(q,session)
    return response_new.fulfillment_text
    