from openai import OpenAI
import json

# Initialize OpenAI client
client = None

def init_openai(openai_api_key, openai_org_key, openai_proj_key):
    """
    Initialize the OpenAI client with provided API credentials.

    Args:
        openai_api_key (str): The API key for OpenAI.
        openai_org_key (str): The organization key for OpenAI.
        openai_proj_key (str): The project key for OpenAI.

    Returns:
        None
    """
    global client
    client = OpenAI(
        api_key=openai_api_key,
        organization=openai_org_key,
        project=openai_proj_key
    )

def grammar_score(input_data):
    """
    Evaluate the grammar, structure, and spelling of the input document, and return a quality score.

    Args:
        input_data (str): The document content to be evaluated.

    Returns:
        tuple: (bool, str) indicating success status and the result or error message.
    """
    if not client:
        return False, "OpenAI client not initialized, refer to README.md"

    try:
        prompt = f"""
        Assessing the quality of the written submission in terms of structure, grammar, and spelling.
        Assess aspects such as structure, vocabulary, grammar, and spelling. 
        For example, a thesis is expected to include a title page, introduction, TOC, chapters, reference list, etc.
        Based on the document below, provide a single numeric score out of 100 in JSON.
        {input_data}
        """

        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "user", "content": prompt}
            ],
            max_tokens=800,
            response_format={"type": "json_object"}
        )

        response = completion.choices[0].message.content
        return process_ai_response(response)
    except Exception as e:
        return False, f"Error evaluating score: {str(e)}"

def process_ai_response(response):
    """
    Process the AI response by parsing the JSON format and returning the response or error.

    Args:
        response (str): The raw JSON response from the AI.

    Returns:
        tuple: (bool, str) where the first element indicates success status and the second is the parsed response or error message.
    """
    try:
        response_data = json.loads(response)
        if 'error' in response_data:
            return False, response_data['error']
        return True, response
    except json.JSONDecodeError:
        return False, "Invalid response from AI"

def struc_check(input_data):
    """
    Check the document for structural issues like missing sections or improper formatting.

    Args:
        input_data (str): The document content to be analyzed for structure.

    Returns:
        tuple: (bool, str) indicating success status and the response or error message.
    """
    if not client:
        return False, "OpenAI client not initialized, refer to README.md"

    try:
        prompt = f"""
        Analyze the structure of the document for missing sections, formatting issues, or other structural problems. 
        Provide feedback in JSON format, including details of flagged issues, reasons, and suggestions.
        {input_data}
        """

        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "user", "content": prompt}
            ],
            max_tokens=1000,
            response_format={"type": "json_object"}
        )

        response = completion.choices[0].message.content
        return process_ai_response(response)
    except Exception as e:
        return False, f"Error performing structure check: {str(e)}"

def spell_check(input_data):
    """
    Check the document for spelling mistakes, regardless of British or American English preferences.

    Args:
        input_data (str): The document content to be checked for spelling.

    Returns:
        tuple: (bool, str) indicating success status and the response or error message.
    """
    if not client:
        return False, "OpenAI client not initialized, refer to README.md"

    try:
        prompt = f"""
        Check the document for spelling mistakes and provide feedback in JSON format, including misspelled words and corrections.
        {input_data}
        """

        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "user", "content": prompt}
            ],
            max_tokens=800,
            response_format={"type": "json_object"}
        )

        response = completion.choices[0].message.content
        return process_ai_response(response)
    except Exception as e:
        return False, f"Error performing spell check: {str(e)}"
