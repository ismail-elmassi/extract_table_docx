import os
import pytest
from src.extract_questions_from_word import do_table_extraction

def test_extract_table_questions():
	extracted_questions= do_table_extraction(os.path.join("resources", "test_file.docx"))
	assert extracted_questions==["hello","hi"]


