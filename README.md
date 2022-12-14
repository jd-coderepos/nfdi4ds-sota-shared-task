## SOTA? Tracking the State-of-the-Art Empirical Artificial Intelligence Research

The central activity around empirical AI research includes automated tasks defined via a task dataset for which machine learning models are developed whose performance can be evaluated by a standard set of evaluation metrics. Pushing the state-of-the-art boundaries in empirical AI research means optimizing the models developed for the tasks in terms of speed, accuracy, or storage. As such researchers in this domain often seem to ask the central question “What’s the state-of-the-art result for task XYZ right now?” 


Instead of seeking out the answer buried in the ranked list of documents via a search query made on traditional search engines, researchers instead look for the answer on community-curated leaderboards such as https://paperswithcode.com/ or https://orkg.org/benchmarks. These leaderboards are websites specifically designed to showcase the performance of all introduced machine learning models on a machine learning task dataset. As such researchers seeking to find out the best model performance on a task dataset can easily obtain this information on these websites via their performance trendline overviews showcasing various model performances over a task dataset over time.


In this Shared Task, we hope to go beyond the community curation of leaderboards and instead  realize the vision of obtaining the most efficient machine learning model capable of automatically detecting leaderboards. The efficiency of the submitted machine learning models as a solution to the shared task will be tested based on speed, model parameters, and leaderboard detection F1 measure.


### What this repository contains?

The repository is organized as follows:

```
README
[annotated-data]/				#released
     |--- [article-counter-folder]/
	 |    |--- [article-id].tei.xml
	 |    |--- annotations.txt
	 |    |--- code-link.txt				#optional - if a code link was found in the paper, this annotation file is created; if not, it is not part of the folder.
	 |___ ...
[zero-shot-data]/				#not released
     |--- [article-counter-folder]/
	 |    |--- [article-id].tei.xml
	 |    |--- annotations.txt
	 |    |--- code-link.txt				#optional	 
	 |___ ...
```

The dataset dump originates from [paperswithcode.com](https://paperswithcode.com/).

Each folder in the respective dump corresponds to a scholarly article
originally downloaded in `pdf` format from arXiv, whose contents were then
scrapped as `txt` data encoded in the [TEI](https://en.wikipedia.org/wiki/Text_Encoding_Initiative) XML format.

Of the 7449 papers in the annotated-data, only 814 papers reported their
code links as a mention within the text.

### Dataset statistics


### Rough Timeline:

January 15, 2023 - first version training dataset public release and test dataset private release

February 15, 2023 - second version dataset release incorporating any changes suggested for the first version

### License

Shield: [![CC BY-SA 4.0][cc-by-sa-shield]][cc-by-sa]

This work is licensed under a
[Creative Commons Attribution-ShareAlike 4.0 International License][cc-by-sa].

[![CC BY-SA 4.0][cc-by-sa-image]][cc-by-sa]

[cc-by-sa]: http://creativecommons.org/licenses/by-sa/4.0/
[cc-by-sa-image]: https://licensebuttons.net/l/by-sa/4.0/88x31.png
[cc-by-sa-shield]: https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg
