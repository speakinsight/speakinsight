


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
        {'role': 'system', 'content': 'Please analyze the following dialogue for tense consistency. Identify any instances where the use of tense is incorrect or inconsistent, and suggest corrections. Provide a detailed explanation for each correction.Return in a json format with the  names of conversation persons according to following {"User1s Name":{mistakes:[{mistake: the mistake, correction: the correct word, tense misused: the actual problem}], most_troublesome_area: The area in which the user has the most problem}},{"User2s Name":{mistakes:[{mistake: the mistake, correction: the correct word, tense misused: the actual problem}], most_troublesome_area: The area in which the user has the most problem}}'},
        {'role':'user', 'content':f'{data}'}
    ]
    evaluate(messages, model, file_path, verbose)

def evaluate_grammar(data, model, file_path, verbose):
    """Prompt for model to find tenses errors in the data provided."""
    messages = [
        {'role': 'system', 'content': 'Please analyze the following dialogue for grammatical correctness. Identify any grammatical errors, including sentence structure, subject-verb agreement, punctuation, and other syntax issues. Provide a correction for each error, along with a brief explanation..Return in a json format with names of conversation persons according to  the following {"User1s Name":{mistakes:[{mistake: the mistake, correction: the correct word, problem: the actual problem}], most_troublesome_area: The area in which the user has the most problem}},{"User2s Name":{mistakes:[{mistake: the mistake, correction: the correct word, problem: the actual problem}], most_troublesome_area: The area in which the user has the most problem}}'},
        {'role':'user', 'content':f'Dialogue {data}'}
    ]
    evaluate(messages, model, file_path, verbose)

def evaluate_vocabulary(data, model, file_path, verbose):
    messages = [
        {'role': 'system', 'content': 'Please analyze the following dialogue for vocabulary errors. Identify any instances where the use of vocabulary is incorrect or inappropriate, and suggest corrections. Provide a detailed explanation for each correction.Return in a json format with the names of conversation persons according to following {"User1s Name":{mistakes:[{mistake: the mistake, correction: the correct word, problem: the actual problem}], most_troublesome_area: The area in which the user has the most problem}},{"User2s Name":{mistakes:[{mistake: the mistake, correction: the correct word, problem: the actual problem}], most_troublesome_area: The area in which the user has the most problem}}'},
        {'role':'user', 'content':f'{data}'}
    ]
    evaluate(messages, model, file_path, verbose)

def evaluate_sentence_structure_and_clarity(data, model, file_path, verbose):
    messages = [
        {'role': 'Please carefully analyze the following dialogue for sentence structure and clarity. Identify any sentences that are unclear, overly complex, or poorly structured. Provide suggestions to improve the clarity and flow of each sentence. Return in a json format with the names of conversation persons according to following {"User1s Name":{mistakes:[{mistake: the mistake, correction: the correct word, problem: the actual problem}], most_troublesome_area: The area in which the user has the most problem}},{"User2s Name":{mistakes:[{mistake: the mistake, correction: the correct word, problem: the actual problem}], most_troublesome_area: The area in which the user has the most problem}}'},
        {'role':'user', 'content':f'{data}'}
    ]
    evaluate(messages, model, file_path, verbose)

def evaluate(messages, model, file_path, verbose):
    with open(file_path, 'a') as file:
        file.write('\n\n{')
        for chunks in model.stream(messages):
            print(chunks)
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
