import pandas as pd
from symspellpy import SymSpell, Verbosity
from neuspell import BertChecker, CnnlstmChecker
import os


symspell = SymSpell(max_dictionary_edit_distance=5, prefix_length=7)
# load dictionary for symspell
symspell.load_dictionary('frequency_dictionary_en_82_765.txt', term_index=0, count_index=1)

checker_lstm_cnn = CnnlstmChecker()
checker_lstm_cnn.from_pretrained()
checker_bert = BertChecker()
checker_bert.from_pretrained()


files = ["data_lowercase/small_typo_errors_lowercase.csv", "data_lowercase/transposition_errors_lowercase.csv",  "data_lowercase/phonetic_errors_lowercase.csv", "data/other_errors_lowercase.csv"]


def correct_with_symspell(word):
    suggestions = symspell.lookup(str(word), Verbosity.CLOSEST, max_edit_distance=2)
    return suggestions[0].term if suggestions else str(word)


def correct_with_bert(word):
    return checker_bert.correct(str(word))


def correct_with_lstm_cnn(word):
    return checker_lstm_cnn.correct(str(word))


output_folder = 'words_corrected'
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# generate corrections for each type of errors and save them to csv
for file in files:
    df = pd.read_csv(file)
    df['wrong_spelling'] = df['wrong_spelling'].str.lower()
    df['symspell_correction'] = df['wrong_spelling'].apply(correct_with_symspell)
    df['bert_correction'] = df['wrong_spelling'].apply(correct_with_bert)
    df['lstm_cnn_correction'] = df['wrong_spelling'].apply(correct_with_lstm_cnn)

    filename = os.path.basename(file).replace(".csv", "_corrected.csv")
    output_file = os.path.join(output_folder, filename)
    df.to_csv(output_file, index=False)
    print(f"File saved as: {output_file}")
