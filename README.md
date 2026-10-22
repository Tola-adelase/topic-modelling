# Topic modelling on Medium titles

**Question:** how do LDA, LSA and HDP compare when extracting themes from short titles?

[Visual case study](https://tola-adelase.github.io/topic-modelling-case-study.html) · [Original notebook](Topic%20Modelling_Medium%20Articles.ipynb)

A personal/academic exploration using Python, Gensim, text preparation and coherence evaluation. Original analysis is preserved; saved evidence and unvalidated claims are distinguished below.

## Saved evidence

126,418 source records; an 8,000-title sample; a 9,585-token dictionary.

| Method | Saved c_v coherence |
|---|---:|
| LDA | 0.512878 |
| LSA | 0.419377 |
| HDP | 0.742783 |

Coherence is **not accuracy**. HDP's higher value does not establish human usefulness or a deployment winner. No controlled latency/throughput benchmark supports a speed ranking.

## Audit the saved outputs

Python 3.9+, no third-party packages. Run from the repository root:

```bash
python3 scripts/audit_saved_outputs.py
```

This extracts printed coherence values and flags the unseeded sample. It was executed on 22 October 2026; see [saved-output-audit.json](saved-output-audit.json). **It is an output audit, not retraining.**

## Data and reproducibility status

The original `medium_post_titles.csv` is **not bundled**. The notebook reads an author-specific absolute path; original package versions were not retained. A full rerun is blocked by the missing input and unvalidated legacy environment.

To produce a new run: obtain an authorised dataset with `title` and `category` columns; change the input path; fix the title sample's random state; seed applicable models; record package versions; run cells top-to-bottom; save fresh outputs separately. Install NLTK stopwords and WordNet resources. Core packages include Jupyter, pandas, NumPy, NLTK, Gensim and compatible SciPy. Later/import-only cells also reference TensorFlow, spaCy, TextBlob, pyLDAvis, scikit-learn, Bokeh, wordcloud, seaborn, matplotlib and `stop-words`. No exact validated lockfile can be claimed without the original environment.

## Method and limits

Alphabetic tokenisation, lowercasing, English/custom stopword filtering, lemmatisation and removal of one-character tokens precede modelling. LDA and LSA use 10 topics on a count corpus; HDP uses defaults. This is not a matched-topic-count comparison. LSA is not run on TF–IDF here.

`df.sample(8000)` has no fixed random state. One sample does not show stability or downstream utility. Later visualisations contain character/word-count confusion, repeated full-sample clouds, character-level counting and a topic-ID mapping problem in t-SNE; those plots are excluded from the portfolio evidence. Next: deterministic preparation, repeated-seed comparisons, representative-title review and an explicit content-discovery evaluation.
