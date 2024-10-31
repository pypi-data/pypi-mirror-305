import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

# Import necessary modules for testing
import capote_ai.viva_questions as viva_questions
import capote_ai.pdf_to_text as pdf_to_text
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# File for question generation:
FILE_PATH = 'Sample_PDF/comp3010.pdf'

# Initialize the OpenAI client
viva_questions.init_openai(
    openai_api_key=os.getenv("OPENAI_API_KEY"),
    openai_org_key=os.getenv("OPENAI_ORG_KEY"),
    openai_proj_key=os.getenv("OPENAI_PROJ_KEY")
)

# Open the PDF file in binary mode for content extraction
with open(FILE_PATH, 'rb') as file_obj:
    assignment_content = pdf_to_text.extract_text_and_tables_from_pdf(file_obj)

# Input data for testing edge cases
empty_input_data = {
    'assignment_title': "",
    'unit_name': "",
    'assignment_content': "",
    'no_of_questions_factual_recall': 1,  # Request at least one question
    'no_of_questions_analysis_evaluation': 1,
    'no_of_questions_open_ended': 1,
    'no_of_questions_application_problem_solving': 1,
    'question_reason': "",
    'question_challenging_level': "Medium",  # Fixed: Use a valid value
    'student_year_level': ""
}

invalid_file_format_input = {
    'assignment_title': "Invalid Format Test",
    'unit_name': "N/A",
    'assignment_content': "This is not a valid PDF content.",
    'no_of_questions_factual_recall': 1,
    'no_of_questions_analysis_evaluation': 1,
    'no_of_questions_open_ended': 1,
    'no_of_questions_application_problem_solving': 1,
    'question_reason': "Test invalid file format",
    'question_challenging_level': "Medium",  # Fixed: Use a valid value
    'student_year_level': "Second Year"
}

long_essay_input_data = {
    'assignment_title': "Very Long Essay Test",
    'unit_name': "Software Engineering",
    'assignment_content': "A" * 1000000,  # Simulating a long essay with repeated 'A'
    'no_of_questions_factual_recall': 1,
    'no_of_questions_analysis_evaluation': 1,
    'no_of_questions_open_ended': 1,
    'no_of_questions_application_problem_solving': 1,
    'question_reason': "Test long essay",
    'question_challenging_level': "Hard",  # Fixed: Use a valid value
    'student_year_level': "Third Year"
}

gibberish_input_data = {
    'assignment_title': "Gibberish Test",
    'unit_name': "N/A",
    'assignment_content': "sjdhsjd shdjshdj",
    'no_of_questions_factual_recall': 1,
    'no_of_questions_analysis_evaluation': 1,
    'no_of_questions_open_ended': 1,
    'no_of_questions_application_problem_solving': 1,
    'question_reason': "Test gibberish content",
    'question_challenging_level': "Easy",  # Fixed: Use a valid value
    'student_year_level': "First Year"
}

duplicate_submission_input_data = {
    'assignment_title': "Duplicate Test",
    'unit_name': "Software Engineering",
    'assignment_content': assignment_content,
    'no_of_questions_factual_recall': 1,
    'no_of_questions_analysis_evaluation': 1,
    'no_of_questions_open_ended': 1,
    'no_of_questions_application_problem_solving': 1,
    'question_reason': "Test duplicate submission",
    'question_challenging_level': "Medium",  # Fixed: Use a valid value
    'student_year_level': "Third Year"
}

# Functional tests for question generation edge cases

# Test 1: Empty input
print(viva_questions.generate_viva_questions(empty_input_data))

# Test 2: Invalid file format
print(viva_questions.generate_viva_questions(invalid_file_format_input))

# Test 3: Excessive length essay
print(viva_questions.generate_viva_questions(long_essay_input_data))

# Test 4: Gibberish content
print(viva_questions.generate_viva_questions(gibberish_input_data))

# Test 5: Duplicate submission
print(viva_questions.generate_viva_questions(duplicate_submission_input_data))