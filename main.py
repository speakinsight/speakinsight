import sys
import argparse
from speakinsight.utils import read_file, evaluate_tenses, evaluate_grammar, evaluate_vocabulary, evaluate_sentence_structure_and_clarity
from speakinsight.ModelManager import LlamaModelManager, GroqModelManager
from collections import defaultdict

def main():
    parser = argparse.ArgumentParser(description="Speak Insight. Get insights from your chats and never make a mistake again.")
    parser.add_argument("-f", "--filepath",type=str, help="The path to the file to read.")

    args = parser.parse_args()
    data = read_file(args.filepath)
    dialouges = data.split("\n\n")
    dialouges_dict = defaultdict(list)
    for dialouge in dialouges:
        user, text = dialouge.split("\n")
        dialouges_dict[user].append(text)
    
    print(dialouges_dict)
    model = GroqModelManager()
    print("Evaluating tenses")
    evaluate_tenses(dialouges_dict, model, "output/tenses_analysis.json", verbose=False)
    # evaluate_grammar(dialouges_dict, model, "output/grammar_analysis.json", verbose=False)
    # evaluate_vocabulary(dialouges_dict, model, "output/vocabulary_analysis.json", verbose=False)
    # evaluate_sentence_structure_and_clarity(data, model, "output/sentence_structure_analysis.json", verbose=False)


if __name__ == "__main__":
    main()
