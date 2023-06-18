_var0 = 'OpenAIKey'
_var1 = "gpt-3.5-turbo-0613"
_var2 = "role"
_var3 = "system"
_var4 = "content"
_var5 = "You are a helpful assistant."
_var6 = "role"
_var7 = "user"
_var8 = "content"
_var9 = 'choices'
_var10 = 'message'
_var11 = 'content'
_var12 = "User: "
_var13 = "Assistant:"
import os                                                                       
from dotenv import load_dotenv                                                  
import openai                                                                   

                                                                                
load_dotenv()                                                                   
openai.api_key = os.getenv(_var0)                                         

def chat(prompt):
    
    response = openai.ChatCompletion.create(
        model=_var1,
        messages=[
            {_var2: _var3, _var4: _var5},
            {_var2: _var7, _var4: prompt}
        ]
    )                                                                           

    reply = response[_var9][0][_var10][_var11]                        
    return reply

                                                                                
while True:
    user_input = input(_var12)                                                
    response = chat(user_input)                                                 
    print(_var13, response)                                               
