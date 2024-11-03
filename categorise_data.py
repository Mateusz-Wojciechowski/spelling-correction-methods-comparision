from nltk.corpus import words
from metaphone import doublemetaphone
import pandas as pd
import Levenshtein


english_words = set(words.words())
spelling_errors = pd.read_csv('data/spelling_errors.csv', index_col=None)

# categorise data as described in the report

context_errors = spelling_errors[spelling_errors['wrong_spelling'].isin(english_words)]
context_errors.to_csv('data/context_errors.csv', index=False)
spelling_errors = spelling_errors[~spelling_errors['wrong_spelling'].isin(english_words)]

transposition_data = spelling_errors[
    spelling_errors.apply(
        lambda row: Levenshtein.distance(str(row['correct_spelling']), str(row['wrong_spelling'])) == 2 and
                    sorted(str(row['correct_spelling'])) == sorted(str(row['wrong_spelling'])),
        axis=1
    )
]
transposition_data.to_csv('data/transposition_errors.csv', index=False)
spelling_errors = spelling_errors[~spelling_errors.index.isin(transposition_data.index)]

small_typos = spelling_errors[
    spelling_errors.apply(
        lambda row: Levenshtein.distance(str(row['correct_spelling']), str(row['wrong_spelling'])) <= 3,
        axis=1
    )
]
small_typos.to_csv('data/small_typo_errors.csv', index=False)
spelling_errors = spelling_errors[~spelling_errors.index.isin(small_typos.index)]

fonetic_data = spelling_errors[
    spelling_errors.apply(
        lambda row: doublemetaphone(str(row['correct_spelling']))[0] == doublemetaphone(str(row['wrong_spelling']))[0],
        axis=1
    )
]
fonetic_data.to_csv('data/phonetic_errors.csv', index=False)
spelling_errors = spelling_errors[~spelling_errors.index.isin(fonetic_data.index)]

spelling_errors.to_csv('data/other_errors.csv', index=False)


