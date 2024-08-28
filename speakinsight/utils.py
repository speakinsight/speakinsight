def read_file(file_path):
    """Read the contents of a file."""
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def create_tenses_prompt(data):
    """Prompt for model to find tenses errors in the data provided."""
    messages = [
        {'role':'system', 'content': 'You are a helpful teaching assistant. Your task is to evaluate a conversation or a piece of writing and provide feedback on the tenses used. You should identify any errors in the tenses and suggest corrections. Return in a json format with the following {mistakes:[{mistake: the mistake, correction: the correct word, tense misused: the actual problem}], most_troublesome_area: The area in which the user has the most problem} If there are multiple Users, Return Different jsons for each'} ,
        {'role':'user', 'content':f'{data}'}
    ]
    return messages
