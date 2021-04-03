# extract_table_docx

You can use this API to extract questions from a survey in docx file.

The objective is to demonstrate that we can extract data from table in docx file.

The libraires used in this code are:

Python-docx: To extract table from docx file

Flask: To send the docx file via web service with POST method. The results of this method is a list of questions.

To run the code use this command:

docker-compose up --build

To call the web service you can use following url :

http://127.0.0.1:5006/extract_questions?path=/app/tests/resources/test_file.docx
