from neuspell import BertChecker, CnnlstmChecker
import pandas as pd
from symspellpy import SymSpell
import os

symspell = SymSpell(max_dictionary_edit_distance=5, prefix_length=7)
symspell.load_dictionary('frequency_dictionary_en_82_765.txt', term_index=0, count_index=1)

checker_lstm_cnn = CnnlstmChecker()
checker_lstm_cnn.from_pretrained()
checker_bert = BertChecker()
checker_bert.from_pretrained()


def correct_with_symspell(text):
    print("corrected")
    suggestions = symspell.lookup_compound(str(text), max_edit_distance=2)
    return suggestions[0].term


def correct_with_bert(text):
    print("corrected")
    return checker_bert.correct(str(text))


def correct_with_lstm_cnn(text):
    return checker_lstm_cnn.correct(str(text))


articles_augmented = pd.read_csv('data/articles_augmented.csv')
# taking only 50 articles
articles_augmented = articles_augmented.iloc[:50]
print(articles_augmented.info())
articles_augmented['symspell_correction'] = articles_augmented['augmented_text'].apply(correct_with_symspell)
print("finished textblob")
articles_augmented['bert_correction'] = articles_augmented['augmented_text'].apply(correct_with_bert)
print("finished bert")
articles_augmented['lstm_cnn_correction'] = articles_augmented['augmented_text'].apply(correct_with_lstm_cnn)

output_folder = 'articles_corrected'
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

articles_augmented.to_csv('articles_corrected/articles_augmented_corrected.csv', index=False)
