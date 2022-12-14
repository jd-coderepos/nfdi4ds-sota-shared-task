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
	 |    |--- code-link.txt		#optional - if a code link was found in the paper, this annotation file is created; if not, it is not part of the folder.
	 |___ ...
[zero-shot-data]/				#not released
     |--- [article-counter-folder]/
	 |    |--- [article-id].tei.xml
	 |    |--- annotations.txt
	 |    |--- code-link.txt		#optional	 
	 |___ ...
```

The dataset dump originates from [paperswithcode.com](https://paperswithcode.com/).

Each folder in the respective dump corresponds to a scholarly article
originally downloaded in `pdf` format from arXiv, whose contents were then
scrapped as `txt` data encoded in the [TEI](https://en.wikipedia.org/wiki/Text_Encoding_Initiative) XML format.

Of the 7449 papers in the `annotated-data`, only 840 papers reported their
code links as a mention within the paper's text. Whereever found, the code link
annotations are included in the file `code-link.txt`.

<!-- Of the 3183 papers in the annotated-data, only 117 papers reported their code links as a mention within the text.  -->

### Dataset statistics

| Parameter | Count |
| --- | --- |
| unique tasks | 826 |
| unique datasets | 2,986 |
| unique metrics | 1,482 |
| unique (task, dataset, metric) tuples | 6,805 |
| avg. (task, dataset, metric) tuples overall | 5.32 |

Ten most common Tasks

| Task name | Count |
| --- | --- |
| Atari Games | 2,122 |
| Image Classification | 2,015 |
| Object Detection | 1,574 |
| Image Super-Resolution | 961 |
| Link Prediction | 880 |
| Question Answering | 708 |
| Semantic Segmentation | 676 |
| Neural Architecture Search | 652 |
| Node Classification | 641 |
| Few-Shot Image Classification | 641 |

Ten most common Datasets

| Dataset name | Count |
| --- | --- |
| COCO test-dev | 1,429 |
| ImageNet | 1,399 |
| COCO minival | 646 |
| CIFAR-10 | 620 |
| Human3.6M | 345 |
| DAVIS 2016 | 312 |
| CIFAR-100 | 247 |
| CNN / Daily Mail | 227 |
| FB15k-237 | 223 |
| Cityscapes test | 222 |

Ten most common Metrics

| Metric name | Count |
| --- | --- |
| Accuracy | 4,457 |
| Score | 2,189 |
| F1 | 1,376 |
| PSNR | 1,039 |
| Top 1 Accuracy | 710 |
| SSIM | 675 |
| AP | 565 |
| mIoU | 527 |
| MAP | 504 |
| FID | 503 |

Ten most common (Task, Dataset, Metric) tuples

| (Task, Dataset, Metric) | Count |
| --- | --- |
| (Image Classification, ImageNet, Top 1 Accuracy) | 425 |
| (Image Classification, ImageNet, Number of params) | 243 |
| (Image Classification, ImageNet, Top 5 Accuracy) | 200 |
| (Object Detection, COCO test-dev, box AP) | 178 |
| (Image Classification, CIFAR-10, Percentage correct) | 166 |
| (Object Detection, COCO test-dev, AP50) | 137 |
| (Image Classification, CIFAR-100, Percentage correct) | 137 |
| (Object Detection, COCO test-dev, AP75) | 134 |
| (Object Detection, COCO test-dev, APM) | 134 |
| (Object Detection, COCO test-dev, APS) | 133 |


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
