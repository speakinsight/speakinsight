import sys
import argparse
from speakinsight.utils import read_file, create_tenses_prompt
from speakinsight.ModelManager import ModelManager

def main():
    parser = argparse.ArgumentParser(description="Speak Insight. Get insights from your chats and never make a mistake again.")
    parser.add_argument("-f", "--filepath",type=str, help="The path to the file to read.")

    args = parser.parse_args()
    data = read_file(args.filepath)

    model = ModelManager()
    prompt = create_tenses_prompt(data)
    response = model.invoke(prompt)
    print(response)

if __name__ == "__main__":
    main()
