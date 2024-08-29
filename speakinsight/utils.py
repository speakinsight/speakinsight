def read_file(file_path):
    """Read the contents of a file."""
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def evaluate_tenses(data, model, file_path, verbose):
    """Prompt for model to find tenses errors in the data provided."""
    messages = [
        # {'role':'system', 'content': 'You are a helpful teaching assistant. Your task is to evaluate a conversation or a piece of writing and provide feedback on the tenses used. You should identify any errors in the tenses and suggest corrections.Return a json for each user in the convo. Return in a json format with the following {"User1s Name":{mistakes:[{mistake: the mistake, correction: the correct word, tense misused: the actual problem}], most_troublesome_area: The area in which the user has the most problem}},{"User2s Name":{mistakes:[{mistake: the mistake, correction: the correct word, tense misused: the actual problem}], most_troublesome_area: The area in which the user has the most problem}}'},
        {'role': 'system', 'content': 'Please analyze the following dialogue for tense consistency. Identify any instances where the use of tense is incorrect or inconsistent, and suggest corrections. Provide a detailed explanation for each correction.Return in a json format with the following {"User1s Name":{mistakes:[{mistake: the mistake, correction: the correct word, tense misused: the actual problem}], most_troublesome_area: The area in which the user has the most problem}},{"User2s Name":{mistakes:[{mistake: the mistake, correction: the correct word, tense misused: the actual problem}], most_troublesome_area: The area in which the user has the most problem}}'},
        {'role':'user', 'content':f'{data}'}
    ]
    with open(file_path, 'a') as file:
        file.write('\n\n{')
        for chunks in model.stream(messages):
            delta = chunks['choices'][0]['delta']
            if 'role' in delta:
                if verbose:
                    print(delta['role'] + ': ', end='')
                file.write(delta['role'] + ': ')
            elif 'content' in delta:
                if verbose:
                    print(delta['content'], end='')
                file.write(delta['content'])
        file.write('}')


def evaluate_grammar(data, model, file_path, verbose):
    """Prompt for model to find tenses errors in the data provided."""
    messages = [
        {'role': 'system', 'content': 'Please analyze the following dialogue for grammatical correctness. Identify any grammatical errors, including sentence structure, subject-verb agreement, punctuation, and other syntax issues. Provide a correction for each error, along with a brief explanation..Return in a json format with the following {Name of User1:{mistakes:[{mistake: the mistake, correction: the correct word, problem: the actual problem}], most_troublesome_area: The area in which the user has the most problem}},{Name of User2:{mistakes:[{mistake: the mistake, correction: the correct word, problem: the actual problem}], most_troublesome_area: The area in which the user has the most problem}}'},
        {'role':'user', 'content':f'Dialogue {data}'}
    ]
    with open(file_path, 'a') as file:
        file.write('\n\n{')
        for chunks in model.stream(messages):
            delta = chunks['choices'][0]['delta']
            if 'role' in delta:
                if verbose:
                    print(delta['role'] + ': ', end='')
                file.write(delta['role'] + ': ')
            elif 'content' in delta:
                if verbose:
                    print(delta['content'], end='')
                file.write(delta['content'])
        file.write('}')

