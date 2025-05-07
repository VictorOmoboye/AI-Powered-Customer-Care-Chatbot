import streamlit as st
from transformers import BlenderbotTokenizer, BlenderbotForConditionalGeneration
import warnings #off warning messages
warnings.filterwarnings("ignore", category=UserWarning, module = 'transformers')


#page configuration
st.set_page_config(
    page_title= "Vic's Chatbot",
    page_icon= "🤖",
    layout= "wide"
)

#Initiate chatbot model and tokenizer

@st.cache_resource
def load_model():
    model_name = "facebook/blenderbot-400m-distill"
    tokenizer = BlenderbotTokenizer.from_pretrained(model_name)
    model = BlenderbotForConditionalGeneration.from_pretrained(model_name)
    return tokenizer, model

tokenizer, model = load_model()


def get_customer_care_response(user_input):
    user_input_lower = user_input.lower()

# refund 

    if any(word in user_input_lower for word in ["refund", "return", "money back"]):
        if "how long" in user_input_lower:
            return "Return typically process within 3-5 business days after we recieve your returned item."
        elif "status" in user_input_lower:
           return "you can check your refund status in your account, under 'order status'."
        else:
           return "To initiate a refund, Go to setting and click refund on item or contact support at support@vicbot.com."
    
# order

    elif any(word in user_input_lower for word in ["order status", "track order", "where is my order", "order"]):
        if "delayed" in user_input_lower:
            return "Please provide order number to check for order delay."
        else:
            return "You can track your order using the tracker information sent to yout email."
        
    # Payment

    elif any(word in user_input_lower for word in ["payment", "charge", "billing"]):
        if "failed" in user_input_lower:
            return "Please verify your payment method. If problem presists, please contact an agent to rapidly help you at payment@vicbot.com."
        elif "double" in user_input_lower:
            return "If you are debited twice or got double debit, please contact support at doubledebit@vicbot.com."
        else:
            return "For payment assistance, please contact billing@vicbot.com."
        

    # Account issue
    elif any (word in user_input_lower for word in ["account issues", "account", "account issue", "login issue","login issue", "password"]):
        if "locked" in user_input_lower:
            return "Account locks are intiatied when you try multiple wrong password, kindly wait 30mins and reset your password."
        elif "reset password" in user_input_lower:
            return "Click on the reset password button and follow the instruction sent to your email."
        else:
            return "Please contact support for account issues."
        

    # Contact person
    elif any (word in user_input_lower for word in ["contact person", "contact", "assistance", "customer care"]):
        if any(word in user_input_lower for word in ["urgent", "immediately", "as soon as possible", "asap"]):
            return "we understand the urgency. Please call our emergency support line at +44773388 for immediate assistance, or email urgent@vicabot.com."
        elif any(word in user_input_lower for word in ["help", "speak", "connect"]):
            return "sure!, you can reach our customer care team 24/7 via chat or call. Visit the 'Contact Us' page on our website or call +44773388 for immediate assitance."
        else: "Our support team is here to assist you. Please let us know what you need help with or visit the 'Contact Us' section on our website for more options." 


    # shipping
    elif any (word in user_input_lower for word in ["shipping", "shipping date", "shipping details", "when shipping", "delivery", "delivery time"]):
        if any(word in user_input_lower for word in ["deleyed", "late", "not arrive", "still waiting"]):
            return "we're sorry for the deley. Please provide your order number so we can check the shipping status and give you update."
        elif any(word in user_input_lower for word in ["cost", "fee", "price"]):
            return "shipping fee vary depending on your location and shipping method. You can view the exact cost during checkout or on your order summary."
        elif any(word in user_input_lower for word in ["when", "date", "arrive", "expected"]):
            return "Shipping usually take 3-7 business days depending on your location. You can check your estimated delivery date in your order confirmation email."
        else:
            return "For shipping details, please check your email for the shipping confirmation or visit your order history for tracking information."
 
    # more




    return None


# Logic to generate chatbot response

def chatbot_response(user_input, conversation_history):
    care_response = get_customer_care_response(user_input) # First check for cc specific responses 
    if care_response:
        bot_reply = care_response
    else:
        #general response from blenderbot(pretrained model)
        inputs = tokenizer([user_input], return_tensors = "pt")
        reply_ids = model.generate(inputs['input_ids'], max_length=100, pad_token_id=tokenizer.eos_token_id)
        bot_reply = tokenizer.decode(reply_ids[0], skip_special_tokens = True)
    bot_reply = f"VicaBot: {bot_reply}" #the name the bot responds as

    # updating conversation history
    conversation_history.append(f"You: {user_input}")
    conversation_history.append(bot_reply)

    return bot_reply, conversation_history



# Streamlit UI
# for the welcome interface/message
def main():
    st.title("Vic Enterprise Customer Care Chatbot")
    st.markdown("""
    Welcome to Vic Enterprise Customer Care Chatbot, i am here to help with:
    - Order status and tracking
    - Returns and Refunds
    - Account issues
    - and many more
    """)

    # Display Conversation History
    if 'conversation' not in st.session_state:
        st.session_state.conversation = []

    # display conversation
    with st.container(height=400, border=True):
        for message in st.session_state.conversation:
            if message.startswith("VicaBot:"):
                st.markdown(f"<div style= 'text-align: left; color: blue;'>{message}</div", unsafe_allow_html= True) #Html coloring and placement
            else:
                st.markdown(f"<div style= 'text-align: right; color: green;'>{message}</div", unsafe_allow_html= True)
    user_input = st.chat_input("Type your message here.....")
# Get bot response
    if user_input:
        bot_reply,updated_conversation = chatbot_response(user_input, st.session_state.conversation)
        st.session_state.conversation = updated_conversation
        st.rerun() #rerun to update the display
    
    

if __name__=="__main__":
    main()