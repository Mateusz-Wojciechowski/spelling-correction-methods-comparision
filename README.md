# Comparision of spelling correction methods

This project focuses on comparing spelling correction approaches both on single words and texts.

## Spelling correction for single words
For this task I decided to use birkbeck dataset (https://www.dcs.bbk.ac.uk/~roger/corpora.html) which contains 36,133 misspellings of 6,136 words.
The dataset is provided in .dat format, so the first I did was a conversion to .csv format
Afterward, I divided the dataset into categories representing different types of spelling mistakes for a more detailed analysis.
Data preparation, the correction process, results, and additional information are provided in the report attached to this repository.
### To correct misspelled words, I chose three tools, each with unique characteristics:
#### Symspell from the symspellpy library
SymSpell is a dictionary-based approach that corrects spelling mistakes by using an efficient algorithm to find words within a predefined edit distance of the misspelled word. 
As it will be presented in the results section, it works well for straightforward misspellings.
It is known for its speed and efficiency.
#### CNNLSTM checker from neuspell library
This model combines Convolutional Neural Networks (CNN) and Long Short-Term Memory (LSTM) networks to correct spelling mistakes by learning contextual spelling patterns. It works well for more complex misspellings by taking into account the surrounding context of words, which helps improve accuracy on both simple and context-based errors.
#### BERT Checker from neuspell library
BERT (Bidirectional Encoder Representations from Transformers) is a pre-trained language model. It is based on a state-of-the-art Transformers architecture.

I chose these approaches to leverage their diverse methodologies and strengths: Symspell provides a classic, dictionary-based algorithm; the CNNLSTM checker applies neural networks to capture contextual patterns; and the BERT Checker utilizes the Transformer architecture for deep contextual understanding

### Metrics for performance evaluation
#### Cosine Similarity
Cosine Similarity measures the similarity between two text vectors by calculating the cosine of the angle between them. It’s particularly useful for capturing the degree of similarity between the corrected and correct versions of words, it ranges from -1 (opposite) to 1 (identical).
#### Jaro-Winkler Similarity
Jaro-Winkler Similarity is a metric that evaluates the similarity between two strings by focusing on the number and order of matching characters. It’s especially sensitive to small differences and character transpositions, making it valuable for measuring the similarity between words with slight typographical errors.
#### Levenshtein Distance
Levenshtein Distance calculates the minimum number of single-character edits (insertions, deletions, substitutions) required to change one word into another. It is a direct measure of how far two words are in terms of character edits, making it ideal for evaluating correction performance on single words.
#### Accuracy
Accuracy calculates the percentage of words correctly corrected by the tool, based on a perfect match between the corrected and correct word forms. It provides a straightforward measure of how many words were fully and accurately corrected by each tool.

## Correction for long articles
For this part of the project I used medium articles dataset (https://www.kaggle.com/datasets/hsankesara/medium-articles?resource=download). Since articles were quite long I decided to use only 50 of them for evaluation.
I had to do some data preprocessing, firstly I removed unnecessary columns and then I used my self-implemented simple text augmentation algorithm to apply misspellings in the article.

I used the same tools as in the case of correcting single words, the only difference being, utilizing text (not single word) mode for SymSpell

### Metrics for performance evaluation
As this type of task required, I had to change some matrix. I once again used Levenshtein but this time I additionaly calculated Jaccard-Similarity
#### Jaccard-Similarity
Jaccard Similarity is a metric that measures the similarity between two sets by comparing the overlap between them. For text analysis, it is commonly used to evaluate how similar two sets of words are by calculating the ratio of the intersection (common words) to the union (total unique words) of the two sets. Jaccard Similarity ranges from 0 to 1, where 0 means no overlap and 1 means the sets are identical. This metric is particularly useful for evaluating text similarity in longer texts, as it accounts for the presence or absence of words rather than their order, making it effective for identifying partial matches and shared vocabulary in corrected and original texts.

## How to locally reproduce results?
NOTE!!!!
There will most likely be a problem with neuspell library as its current version is missing some key files. I solved this problem taking the steps described on this forum: https://github.com/neuspell/neuspell/issues/36 by ftarin-supership 

```
git clone <repository-url>
cd <repository-folder>
```
I strongly suggest using conda enviroment as for example metaphone library is unavailable throug pip
Download datasets described above and place them in data folder if you didn't collect them from github.

### Generating corrections for words

#### Option 1
Run generate_csv.py to create a csv file with the data for correction, Run categorise_data.py to categorise your dataset and save each category to a seperate file, Run convert_to_lowercase.py, Run generate_corrections.py to obtain corrections

#### Option 2 
Run run_pipeline_word_correction.py file that contains the whole pipeline.
It may take a while !!!

Generating Text corrections

#### Option 1
Run synthetically_augment_articles.py to read the article data and apply augmentation, Run generate_text_corrections.py to obtain text corrections

#### Option 2
Run run_pipeline_text_correction.py
It may take a while !!!




