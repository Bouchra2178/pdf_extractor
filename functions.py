import os
import openai
import re
from dotenv import find_dotenv, load_dotenv
from langchain.llms import OpenAI
from langchain.document_loaders import PyPDFLoader
from langchain.chat_models import ChatOpenAI
from pypdf import PdfReader
from langchain.prompts import PromptTemplate
import pandas as pd
import regex

   #find variables env
load_dotenv(find_dotenv())
openai.api_key = os.getenv("OPENAI_API_KEY")


#open ai chat api
model = "gpt-3.5-turbo"

chat = ChatOpenAI(temperature=0.9, model=model)

def get_text_from_pdf(pdf):
    txt=''
    pdf_reader = PdfReader(pdf)
    for page in pdf_reader.pages:
        txt += page.extract_text()
    return txt

def get_data_from_text(pages_data):
    template = """Extract all the following values : Invoice ID, DESCRIPTION, Date, 
         UNIT PRICE,AMOUNT, Bill For, From and Terms from: {pages}

        Expected output: remove any dollar symbols add  curly braces {{{{'Invoice ID': '1001329','DESCRIPTION': 'phone and data bills','Date': '24/05/2019','UNIT PRICE': '500.00', 'AMOUNT': '450.00', 'Bill For': 'Rosa Zayn', 'From': 'Orbito orbit', 'Terms': 'Net 30 Days'}}}}
        """

    prompt_template = PromptTemplate(input_variables=["pages"], template=template)
    llm = OpenAI(temperature=.7)
    full_response=llm(prompt_template.format(pages=pages_data))
    
    return full_response

def create_data(all_pdfs):
    df=pd.DataFrame({
        "Invoice ID":pd.Series(dtype='int'),
        "DESCRIPTION":pd.Series(dtype="str"),
        "Date":pd.Series(dtype="str"),
        "UNIT PRICE":pd.Series(dtype="str"),
        "AMOUNT":pd.Series(dtype="int"),
        "Bill For":pd.Series(dtype="str"),
        "From":pd.Series(dtype="str"),
        "Terms":pd.Series(dtype="str") 
    })
    
    for pdf in all_pdfs:

        text=get_text_from_pdf(pdf)

        #extracted data using llm
        data=get_data_from_text(text)
        print("dataaaaaa******************")
        print(data)
                # Define the regular expression pattern
                
        pattern = r'{(.+)}'
        
        
        # Use the re.search function to find the first match
        match = re.search(pattern, data, re.DOTALL)

        # Check if a match was found
        if match:
            # Extract the text within curly braces from the match
            extracted_text = match.group(1)
            print(extracted_text)
            data_dict = eval('{' + extracted_text + '}')
            print(data_dict)
            
        else:
            print("No match found.")
        df = pd.concat([df, pd.DataFrame([data_dict])], ignore_index=True)
        print("*************") 
        print("Succesfuly done !!!")

    return df
            

    
    