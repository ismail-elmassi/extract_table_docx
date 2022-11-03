"""
This is  extract questions from word file
"""
import pandas as pd
from docx.api import Document

UPLOADS_FOLDER = "uploads"

def do_extraction(filename):
    """ This is  do extraction function """
    table_questions = do_table_extraction(filename)
    resp = {}
    if table_questions:
        resp['TABLE_QUESTIONS'] = table_questions
    return resp

def do_table_extraction(filename):
    """ This is  do table extraction function """
    document = Document(filename)
    output = []
    for table in document.tables:
        data = []
        keys = None
        for i, row in enumerate(table.rows):
            text = (cell.text for cell in row.cells)
            if i == 0:
                keys = tuple(text)
                continue
            row_data = dict(zip(keys, text))
            data.append(row_data)
        df_data = pd.DataFrame(data)
        output = df_data.T.reset_index().values.tolist()[0]
        output = list(filter(None, output))
        print(output)
    return output
