import sys
import argparse
from speakinsight.utils import read_file, evaluate_tenses, evaluate_grammar
from speakinsight.ModelManager import ModelManager

def main():
    parser = argparse.ArgumentParser(description="Speak Insight. Get insights from your chats and never make a mistake again.")
    parser.add_argument("-f", "--filepath",type=str, help="The path to the file to read.")

    args = parser.parse_args()
    data = read_file(args.filepath)

    model = ModelManager()
    evaluate_tenses(data, model, "output/tenses_analysis.json", verbose=False)
    evaluate_grammar(data, model, "output/grammar_analysis.json", verbose=False)


if __name__ == "__main__":
    main()
