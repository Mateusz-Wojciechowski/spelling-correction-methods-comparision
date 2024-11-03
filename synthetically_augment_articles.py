import pandas as pd
import random

articles = pd.read_csv('data/articles.csv', index_col=None)

articles = articles.drop(['author', 'claps', 'reading_time', 'link', 'title'], axis=1)
articles.rename(columns={'text': 'correct_text'}, inplace=True)

articles['correct_text'] = articles['correct_text'].astype(str).fillna("")


# introduce random char manipulations on the articles
def simulate_typos_manually(text, typo_prob=0.05):
    text = list(text)
    for i in range(len(text)):
        if random.random() < typo_prob:
            if text[i].isalpha():
                typo_type = random.choice(['swap', 'delete', 'replace'])
                if typo_type == 'swap' and i < len(text) - 1:
                    text[i], text[i + 1] = text[i + 1], text[i]
                elif typo_type == 'delete':
                    text[i] = ''
                elif typo_type == 'replace':
                    text[i] = random.choice('abcdefghijklmnopqrstuvwxyz')
    return ''.join(text)


articles['augmented_text'] = articles['correct_text'].apply(simulate_typos_manually)

articles.to_csv("data/articles_augmented.csv", index=False)


