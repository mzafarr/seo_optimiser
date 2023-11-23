import ast
import json
import re
import streamlit as st
import pandas as pd
import base64  # Add import for base64
from rules import seo_rules, example_input, example_output
from openai import OpenAI

openai_api_key = st.secrets["OPENAI_API_KEY"]
client = OpenAI(api_key = openai_api_key)

st.title("AI Product Optimization")

uploaded_file = st.file_uploader(
    "Upload a spreadsheet file", type=["xlsx", "xls", "csv"])

if uploaded_file is not None:
    try:
        # Read the uploaded file into a DataFrame
        df = pd.read_excel(uploaded_file) if uploaded_file.name.endswith(
            ('.xls', '.xlsx')) else pd.read_csv(uploaded_file)

        # in all cells of the df replace all single and double quotes with a space
        df = df.replace({'\'': ' ', '\"': ' '}, regex=True)

        column_names = ['Optimized', 'optimized']
        found_column = None
        for column_name in column_names:
            if column_name in df.columns:
                found_column = column_name
                break
        if found_column is not None:
            df_filtered = df.loc[df[found_column].str.lower() != 'yes']
        else:
            print('Neither "Optimized" nor "optimized" columns exist in the DataFrame.')

        # Define the expected column names
        # expected_columns = [
        #     'Title', 'product_type', 'google_product_category', 'brand', 'description',
        #     'condition', 'gender', 'product_highlight', '[product_detail]',
        #     'is_bundle', 'Adult', 'Age group', 'Certification', 'Color', 'size_type', 'Shipping',
        #     'Condition', 'Material', '[min_handling_time]','[product_height]',
        #     '[max_handling_time]', 'Multipack', 'Pattern', 'unit_pricing_measure',
        #     '[product_length]', '[product_width]', 'Size', 'size_system',
        #     '[product_weight]', 'unit_pricing_base_measure'
        # ]
        # # Ensure all expected columns are present, or add missing columns with empty strings
        # for column in expected_columns:
        #     if column not in df.columns:
        #         df[column] = ""

        # drop rows with all null values
        df = df.dropna(how='all')
        # Convert DataFrame to a list of dictionaries
        data = df.to_dict(orient='records')

        # SEO Optimization
        st.header("SEO Optimization")
        # Iterate through each product record
        optimized_data = []  # Create an empty list to store optimized records
        with st.spinner("Optimizing product data..."):
            for record in data:
                optimized_record = {}
                # Send the record to the GPT API for optimization
                response = client.chat.completions.create(
                    model="gpt-3.5-turbo-1106",
                    # model="ft:gpt-3.5-turbo-0613:personal::8DkooenP",
                    response_format={"type": "json_object"},
                    messages=[{
                        "role": "system",
                        "content": f"You are an expert at optimizing product details for getting more clicks and having better seo on online stores. Optimize each product detail according to [SEO_RULES] given below and also a basic grammar and spell check and remove any extra spaces in it or any capital or lower case mistake. Make sure to check each product detail against the [SEO_RULES] of that particular detail, as each detail has its own rules. If a property has a value of an empty string or any kind of null value, you have to analyze all the details of this product and find a good or optimized answer for that property. Your response must be in json format. After finding the optimized answer for each property. Make sure to keep the previous values of each key if it did not require optimization.\n\n [SEO_RULES] = '''{seo_rules}'''"},
                        {
                        "role": "user",
                        "content": f"{record}"
                    }],
                )

                # Convert JSON to Python dictionary
                # python_dict = json.loads(json_string)

                # Load JSON data into a Pandas DataFrame
                # df = pd.read_json(json_data)

                # "content": f"""here are details_of_a_product='''{record}'''\n\n Optimize each product \
                # detail according to the [SEO_RULES] given below and besides optimisation also do a basic \
                # grammer and spell check \
                # and remove any extra spaces in it or any upper case or lower case mistake. Make sure to \
                # check each product detail against the SEO rules of that particular detail, as each \
                # detail has its own rules. If a property has a value of an empty string or any kind of null value, you \
                # have to analyze all the details of this product and find an answer for it and if possible \
                # think of a good or optimized answer for that property. After finding the optimized answer for \
                # each property, you have to return the product_details in the exact same format and structure \
                # as given to you. Your final answer must be in the form of a proper python dictionary and make sure to keep \
                # the previous values of each key if it did not require optimization. The format will be a python dictionary with \
                # """
                # \n\n[SEO_RULES]: '''{seo_rules}'''
                optimized_value = response.choices[0].message.content
                # valid_json = optimized_value.replace("'", "\"")
                optimized_value = optimized_value.replace('\n', ' ').strip()


                optimized_value = json.loads(optimized_value)
                print(optimized_value)
                # Append the optimized record to the list
                optimized_data.append(optimized_value)

        st.subheader("Optimized Product Records:")
        # st.write(optimized_data)

        # Convert the optimized data list to a DataFrame
        optimized_df = pd.DataFrame(optimized_data)
        # set optimized column to yes for all
        optimized_df['Optimized'] = 'yes'
        st.subheader("Download Optimized Data")
        # Save the optimized data as an Excel file
        excel_file = 'optimized_data.xlsx'
        optimized_df.to_excel(excel_file, index=False)

        st.subheader("Download Optimized Data")
        with pd.ExcelWriter(excel_file, engine='xlsxwriter') as writer:
            optimized_df.to_excel(writer, sheet_name='Sheet1', index=False)
        excel_data = open(excel_file, 'rb').read()
        b64 = base64.b64encode(excel_data).decode()
        st.markdown(
            f'<a href="data:application/octet-stream;base64,{b64}" '
            f'download="optimized_data.xlsx">Click here to download the optimized data as Excel</a>',
            unsafe_allow_html=True
        )

    except Exception as e:
        st.error(
            "Error reading the file. Please make sure it's a valid spreadsheet file.")
        st.error(str(e))
