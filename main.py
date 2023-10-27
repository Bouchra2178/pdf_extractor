import streamlit as st
from functions import create_data, get_data_from_text,get_text_from_pdf

def main():
    st.set_page_config(page_title="Biller Data Extractor")
    st.title("Bill InfoExtractor AI")
    pdfs=st.file_uploader("Upload your files in PDF format only ",type=["pdf"],
                         accept_multiple_files=True)
    button=st.button("Extract your data")
    if button:
        with st.spinner("Extracting data..."):
                df=create_data(pdfs)
                st.write(df.head())
                df["AMOUNT"]=df["AMOUNT"].astype(float)
                st.write("average bill amount:",df['AMOUNT'].mean())
                #convert to csv
                #st.write("convert into :")
                st.markdown("convert into :")
                cnvrt_csv=df.to_csv(index=False).encode("utf-8")
                st.download_button(
                    "Download to CSV",
                    cnvrt_csv,
                    "Bills.csv",
                    key="download-csv"
            
            
                )
                cnvrt_json=df.to_json(index=False).encode("utf-8")
                st.download_button(
                    "Download to JSON",
                    cnvrt_json,
                    "Bills.json",
                    key="download-json"
            
            
                )
    pass


#invoking main function
if __name__=="__main__":
  main()