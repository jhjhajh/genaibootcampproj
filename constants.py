class SystemConstants:
    SYSTEM_MESSAGE = '''
    You are a virtual assistant for Central Provident Fund Board employees and will answer questions asked directly. When relevant, at the end of your response, on a separate paragraph, include the full name of pdf or docx document in quotations and 
section where information is retrieved to back up your response. List the citations in the following format, from most relevant to least relevant:

<content of response>

Citations:


<name of document>: from <most in-depth sub-section of document where is referenced as in-depth as possible> 

'''

class UIConstants:
    PAGE_TITLE = "Chatbot"
    CHATBOT_WELCOME_MESSAGE = "Hello! I am Jenny, your friendly chatbot. How can I help you?"
    USER_INPUT_PLACEHOLDER = "Type your query here :D"
    LAYOUT = "centered"
    CONTACT_INFO = "If you encounter any issues or have any feedback, feel free to contact Jia Hui at ang_jia_hui@cpf.gov.sg via Skype, MSTeams or email."
    WARNING = "Our AI chatbot strives to offer valuable assistance, yet it acknowledges the possibility of occasional inaccuracies. Should you encounter any inconsistencies or uncertainties, we kindly suggest seeking further clarification or information. If the response provided is not satisfactory, we suggest trying to rephrase or be more specific in with your query. Your constructive feedback plays a vital role in enhancing our service. We appreciate your understanding and support."
    CHATBOT_CONTEXT = "This chatbot will help to answer queries about the schemes with documents that have been loaded. Simply select a scheme and ask away! \n\nNo refresh required even if you switch schemes."
    SUGGESTIONS = "Suggestions on how to improve your experience with the Chatbot 😄 \n1. Try to provide context to each of your query, even if it is a follow-up question. \n2. If the response provided is not satisfactory, try to rephrase or be more specific with your queries.\n3. Should you encounter any errors, try to clear cache and refresh your browser.  \n\nHope this helps to improve your experience 😄"
    
class ErrorConstants:
    GENERAL_ERROR = "An error occurred. Please refresh your browser and try again later. If the problem persists, contact Jia Hui"
    
