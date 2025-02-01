    pdf_content=input_pdf_setup(upload_file)
            response=get_Gemini_response(input_Prompt2,pdf_content,input_text)
            st.subheader("the responses is")
            st.write(response)