# AI POWERED CUSTOMER CARE CHATBOT
## Leveraging Conversational AI and NLP to Automate Customer Support for Seamless User Experience
![image](https://github.com/user-attachments/assets/d2fe72dd-0645-4b28-ae6b-1634b294ee88)

## INTRODUCTION
**VicaBot** is an AI-driven customer service chatbot built to provide fast, intelligent, and human-like responses to user inquiries. It combines a rule-based logic engine with Meta’s powerful BlenderBot NLP model to simulate real-time customer support. Designed with simplicity and scalability in mind, **VicaBot** is deployed using Streamlit and is ideal for use in e-commerce, helpdesks, and digital service platforms.

## TABLE OF CONTENT
- [Description](###Description)
- [Methodology](###Methodology)
- [Tools and Technologies](###Tools-and-technologies)
- [Deployment Scenarios](###Deployment-scenarios)
- [Project Screenshots](###Project-screenshots)
- [Video Demo](###Video-demo)

### Description 
This project demonstrates a customer care chatbot that blends AI text generation and pre-scripted decision trees to enhance digital customer service experiences. The chatbot:

- Provides instant answers to frequently asked questions like “How do I get a refund?” or “Where’s my order?”
- Uses BlenderBot, a conversational NLP model, to manage general queries and simulate real customer-agent conversations.
- Maintains context-aware conversations, storing past responses and user inputs to create a chat history.
- Built with a lightweight Streamlit interface for quick deployment and UI interaction.

### Methodology
The chatbot operates through the following workflow:

1. **User Input:** The user types a question or concern into a text input box.

2. **Rule-Based Intent Recognition:**
   - If keywords such as “refund,” “payment,” or “account” are detected, the chatbot serves a curated response.
   - If no direct match is found, it defers to BlenderBot for a general AI-generated reply.

3. **AI Response Generation:**
   - BlenderBot uses the input to predict a logical response based on pre-trained conversational data.

4. **Conversation Update:**
   - The conversation log is updated to preserve context and improve user experience.

5. **Front-End Display:**
    - The chatbot interface mimics real messaging platforms for a natural chat feel.

### Tools and Technologies
| Tool/Library        | Purpose                                 |
| ------------------- | --------------------------------------- |
| **Streamlit**       | Frontend UI for chat interaction        |
| **HuggingFace 🤗**  | Hosting and retrieving BlenderBot model |
| **BlenderBot 400M** | AI model for contextual text generation |
| **Python**          | Core logic and API integration          |
| **Warnings Module** | Suppresses model load warnings for UX   |

### Deployment Scenarios
VicBot is adaptable and can be deployed in various real-world customer-facing environments:

- **E-commerce Platforms:** Automate refund inquiries, order tracking, and account issues.

- **Customer Support Centers:** Handle tier-1 questions and escalate complex ones to human agents.

- **Healthcare Portals:** Provide administrative answers related to appointments, billing, or login access.

- **Corporate Intranets:** Assist employees with internal systems and IT-related FAQs.
