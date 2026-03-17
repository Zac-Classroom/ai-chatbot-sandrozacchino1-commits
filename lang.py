from langchain.chat_models import init_chat_model
from dotenv import dotenv_values

userdata=dotenv_values()

print(userdata)

llm = init_chat_model(
    model=userdata["MODEL"]
    , base_url=userdata["URL"]
    , api_key=userdata["API_KEY"]
    , temperature=userdata["TEMPERATURE"]
)

risposta = llm.invoke("""
            Sei un assistente. Rispondi brevemente alla domanda 
            dell'utente se l'argomento è contenuto nel seguente contesto
            altrimento rispondi che non lo sai
                      
                      
            CONTESTO:
            prodotti disponibili
            - ASPIRAPOLVERE, PREZZO 100€
            - IPHONE PREZZO, 1500€
            - TV SAMSUNG, PREZZO 100€
           
            DOMANDA DELL'UTENTE:          
            mi piace l'iphone che mi suggerisci?
           """)

print(risposta.content)