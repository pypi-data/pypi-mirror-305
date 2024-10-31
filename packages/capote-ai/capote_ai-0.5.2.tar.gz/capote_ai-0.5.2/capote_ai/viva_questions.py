from enum import Enum
from pydantic import BaseModel, ValidationError
from openai import OpenAI
from typing import List


class QuestionTypeEnum(str, Enum):
    factual_recall = 'factual_recall'
    open_ended = 'open_ended'
    conceptual_understanding = 'conceptual_understanding'
    analysis_and_evaluation ='analysis_and_evaluation'
    application_problem_solving = 'application_problem_solving'

class VivaQuestions(BaseModel):
    question:str
    question_type: QuestionTypeEnum
    
    class Config:
        use_enum_values = True


class Questions(BaseModel):
    questions: List[VivaQuestions]
    
    
# Initialise OpenAI client
client = None

# Method for initialising openAI client
def init_openai(openai_api_key, openai_org_key, openai_proj_key):
    """
    Initialise the OpenAI client with the provided API key, organization key, and project key.
    
    Args:
        openai_api_key (str): The API key for authenticating with OpenAI.
        openai_org_key (str): The organization key for OpenAI.
        openai_proj_key (str): The project key for OpenAI.
    """
    global client
    client = OpenAI(
        api_key=openai_api_key,
        organization=openai_org_key,
        project=openai_proj_key
    )
#
# Method for generating viva questions, expects a single dict with all req values
def generate_viva_questions(input_data):
    """
    Generate viva questions based on the provided input data.

    Args:
        input_data (dict): A dictionary containing required values:
            - assignment_title (str): Title of the assignment.
            - unit_name (str): Name of the unit.
            - no_of_questions_factual_recall (int): Number of factual recall questions.
            - no_of_questions_analysis_evaluation (int): Number of analysis and evaluation questions.
            - no_of_questions_open_ended (int): Number of open-ended questions.
            - no_of_questions_application_problem_solving (int): Number of application and problem-solving questions.
            - no_of_questions_conceptual_understanding (int): Number of conceptual understanding questions.
            - question_challenging_level (str): Level of question difficulty (e.g., Easy, Medium, Hard, Challenging).
            - student_year_level (str): Year level of the student (e.g., First Year, Second Year).
            - assignment_content (str): The content of the assignment.

    Returns:
        tuple: A tuple containing a success status (bool) and a response (str or dict).
    """
    
    # Check if OpenAI client is initialized
    if not client:
        return False, "OpenAI client not initialized, refer to README.md"
    
    # Required fields
    required_fields = [
        'assignment_title', 'unit_name', 'question_challenging_level', 'student_year_level',
        'assignment_content'
    ]

    # Check for missing required fields
    missing_fields = [field for field in required_fields if field not in input_data]
    if missing_fields:
        return False, f"Missing required fields: {', '.join(missing_fields)}"

    # Extract values from input_data
    assignment_title = input_data['assignment_title']
    unit_name = input_data['unit_name']
    question_challenging_level = input_data['question_challenging_level']
    student_year_level = input_data['student_year_level']
    assignment_content = input_data['assignment_content']

    # Optional question types
    question_types = {
        'Factual recall': 'no_of_questions_factual_recall',
        'Conceptual understanding': 'no_of_questions_conceptual_understanding',
        'Analysis and evaluation': 'no_of_questions_analysis_evaluation',
        'Application and problem-solving': 'no_of_questions_application_problem_solving',
        'Open-ended': 'no_of_questions_open_ended'
    }

   # Extract and validate question counts
    question_counts = {}
    for question_type, field_name in question_types.items():
        if field_name in input_data:
            try:
                count = int(input_data[field_name])
                if count < 0:
                    return False, f"Number of {question_type} questions must be a non-negative integer."
                if count > 0:
                    question_counts[question_type] = count
            except ValueError:
                return False, f"Number of {question_type} questions must be a valid integer."

    total_questions = sum(question_counts.values())
    
    # No questions requested for any type - returns false
    if total_questions == 0:
        return False, "At least one question must be requested."

    # Validate question challenging level
    valid_levels = ['Easy', 'Medium', 'Hard', 'Challenging']
    if question_challenging_level not in valid_levels:
        return False, f"Invalid question challenging level. Must be one of: {', '.join(valid_levels)}"

    try:
        prompt = f"""
        You are a renowned expert university professor in {unit_name} tasked with creating a comprehensive oral examination for a student's assignment. Your goal is to generate insightful questions that thoroughly assess the student's understanding, critical thinking skills, and ability to apply knowledge from their assignment

        Assignment Details:
        Title: {assignment_title}
        Unit: {unit_name}
        Student Year Level: {student_year_level}

        Your task is to create {total_questions} oral examination questions that rigorously test the student's understanding and knowledge of the subject matter. Each question should be {question_challenging_level}.
        When generating questions, focus on assessing these three key areas:

        - Familiarity: Is the student familiar with the content as written?
        - Discussion Proficiency: Can the student engage in a meaningful conversation about the concepts presented?
        - Critical Expansion: Can the student expand upon the assignment's content by exploring related ideas and concepts?
        """
            
        prompt += """
        Generate the following number of questions for each type, aligned with appropriate levels of Bloom's taxonomy:
                """
            
        for question_type, count in question_counts.items():
            prompt += f"- {question_type} questions: {count}\n"

        prompt +=f"""
        Remember to maintain your reputation for comprehensive and insightful questioning. Your questions should not only test the student's knowledge of the assignment content but also their ability to think critically about the subject and apply concepts to new situations. Pay special attention to key themes, methodologies, and arguments presented in the assignment.
        
        IMPORTANT INSTRUCTIONS:
        - You MUST strictly refer ONLY to the assignment content provided below for context regarding the assignment. 
        - The assignment details provided above are only for general context; do not rely solely on that information. 
        - The question must ONLY contain the actual question and not mention the question type.
        
        Analyze the assignment content provided at the end of this prompt thoroughly to ensure that your questions are directly relevant and appropriately challenging for a university-level oral examination.
        Assignment Content: 

        {assignment_content}
        """
        completion = client.beta.chat.completions.parse(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": prompt},
                {"role": "user", "content": f"{assignment_content}"}
            ],
            max_tokens=800,
            response_format= Questions
        )
        
        # Parse response into dictionary:
        response = completion.choices[0].message
        
        if (response.refusal):
            return False, (response.refusal)
        else:
            return True, transform_questions(response.parsed.questions)

    except Exception as e:
        return False, f"Error generating questions: {str(e)}"


def regenerate_questions(input_data):
    """
    Regenerate viva questions based on the provided input data.

    Args:
        input_data (dict): A dictionary containing required values:
            - assignment_title (str): Title of the assignment.
            - unit_name (str): Name of the unit.
            - question_reason (list): List of dictionaries containing:
                - question_n (str): The flagged question.
                - reason (str): The reason for regeneration.
                - question_type (str): The type of the question.
            - assignment_content (str): The content of the assignment.

    Returns:
        tuple: A tuple containing a success status (bool) and a response (str or dict).
    """
    
    # Check if OpenAI client is initialized
    if not client:
        return False, "OpenAI client not initialized, refer to README.md"
    
    # Required fields
    required_fields = [
        'assignment_title', 'unit_name', 'question_reason',
        'assignment_content'
        # question_type?
    ]
    #Expected AI variable naming:
    ai_qn_cat = ['analysis_and_evaluation', 'application_problem_solving', 'factual_recall', 'open_ended', 'conceptual_understanding']
    
    # Check for missing required fields
    missing_fields = [field for field in required_fields if field not in input_data]
    if missing_fields:
        return False, f"Missing required fields: {', '.join(missing_fields)}"

    # Extract values from input_data
    assignment_title = input_data['assignment_title']
    unit_name = input_data['unit_name']
    assignment_content = input_data['assignment_content']
    question_reason = input_data['question_reason']

    # ## --
    # question_reason = [
    #     {"question": "What was the primary challenge during Sprint 0?", "reason": "Too vague"},
    #     {"question": "Explain the design choices made in Sprint 1.", "reason": "Not aligned with assignment content"}
    # ]
    # ## --
    try:
        # Regeneration prompt
        regen_prompt = f"""
        As a University Professor teaching {unit_name}, a student has submitted their assignment for {assignment_title}.
        The following questions have been flagged for regeneration based on markers feedback and have an associated reason:
        """

        # Loop through questions, reasons, and question types
        for item in question_reason:
            # Find the key that starts with "question_"
            question_key = next((key for key in item if key.startswith("question_")), None)
            question = item.get(question_key)
            reason = item.get('reason')
            question_type = item.get('question_type')
            
            if question and reason and question_type:
                regen_prompt += f"\n{question_key.capitalize()}: {question}\nReason: {reason}\nQuestion Type: {question_type}\n"

        regen_prompt += f"""
        Remember to maintain your reputation for comprehensive and insightful questioning. Your questions should not only test the student's knowledge of the assignment content but also their ability to think critically about the subject and apply concepts to new situations. Pay special attention to key themes, methodologies, and arguments presented in the assignment.
        Please regenerate these questions based on the reasons provided, ensuring that the new questions address the concerns raised and fit within the context of the assignment content below. Only regenerate the question specified and no more.
        Present the questions in the following JSON format. {{ "question_type": {{"regenerated_question_n:...", "regenerated_question_x:..."}}, "question_type": {{"regenerated_question_n:...", "regenerated_question_X:..."}}......}} where the question types are the following: {ai_qn_cat}
        
        
        IMPORTANT INSTRUCTIONS:
        - You MUST strictly refer ONLY to the assignment content provided below for context regarding the assignment. 
        - The assignment details provided above are only for general context; do not rely solely on that information. 
        - You must adhere the regenerated_question_number to the original Question_number passed for the specific quesiton type
        
        Analyze the assignment content provided at the end of this prompt thoroughly to ensure that your questions are directly relevant and appropriately challenging for a university-level oral examination.
        Assignment Content: 
        """
        # print(regen_prompt)
        # OpenAI API Call for question regeneration
        completion = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": regen_prompt},
                {"role": "user", "content": f"{assignment_content}"}
            ],
            max_tokens=800,
            response_format={"type": "json_object"}
        )
        
        response = completion.choices[0].message.content

        
        return True, response
        
    except Exception as e:
        print(f"Error during question regeneration: {e}")

    ## -- Regen Reasons --
    # "Too vague"
    # "Too difficult for the given level"
    # "Not aligned with assignment content"
    # "Repetitive or redundant"
    # "Lack of critical thinking assessment"
    # "Grammatical or phrasing issues"
    # "Not challenging enough"
    ## --
    
    #Helper method to process response for backend:
def transform_questions(questions_input) -> dict:
    """
    Transform a list of VivaQuestions objects into a nested dictionary format
    where questions are organized by type and numbered sequentially starting from 1.
    
    Args:
        questions_input: List of VivaQuestions objects
        
    Returns:
        dict: Nested dictionary with question types as top-level keys and
             numbered questions as sub-dictionaries
    """
    # Create a dict to group questions by type
    grouped_questions = {}
    
    # First pass: group questions by type
    for q in questions_input:
        
        question_type = str(q.question_type)
        question = str(q.question)
        
        if question_type not in grouped_questions:
            grouped_questions[question_type] = []
            
        grouped_questions[question_type].append(question)
    
    # Transform into the desired format with sequential numbering
    result = {}
    for q_type, questions_list in grouped_questions.items():
        # Create a new dict for this question type with sequential numbering
        questions_dict = {}
        for i, question in enumerate(questions_list, 1):  # Start counting from 1
            questions_dict[f"question_{i}"] = question
        result[q_type] = questions_dict
    
    return result
