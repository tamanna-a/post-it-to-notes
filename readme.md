This project is a way to convert an image of post-it notes and extract the texts.

The machine learning component involves a number of Computer Vision tasks, namely **line segmentation** and **Handwriting Text Recognition.** 
The front-end of the app is built in flask, it allows the user to upload a post it note.

**ML-Sub-Problems**
I separated the ML problem into 3 components.

1. Pre-Processing Post-It notes into a similar format as the training data
2. Segmenting lines in the post-it into lines 
3. Lines to text —> Easter2 Model

For Pre-processing, I used OpenCV's functions.
The line to text part was built by applying the Easter2 model, which is currently the SOTA non-transformer model. 

Below are some resources used to aid in the project. 

**Dataset**:
IAM (IAM Handwriting)
- 13,353 images of handwritten lines of text created by 657 writers
- writers transcribed text from Lancaster-Oslo/Bergen Corpus of British English
- total of 1,539 handwritten pages 
- 115,320 words
- The database is labeled at the sentence, line, and word levels
- Dataset paper: The IAM-database: an English sentence database for offline handwriting recognition

Accessing dataset:
- You need to register first at https://fki.tic.heia-fr.ch/databases/iam-handwriting-database
- Github repo with data download python notebook: https://github.com/kartikgill/Easter2/blob/main/notebooks/iam_dataset_download.ipynb
- Train-test split: wget https://www.openslr.org/resources/56/splits.zip

The papers can be found under model/papers directory.

Citation:
@article{chaudhary2022easter2,
  title={Easter2. 0: Improving convolutional models for handwritten text recognition},
  author={Chaudhary, Kartik and Bali, Raghav},
  journal={arXiv preprint arXiv:2205.14879},
  year={2022}
}


Other <br>
Flask:
https://roytuts.com/upload-and-display-image-using-python-flask/

Terminologies:
HTR- Handwriting Text Recognition
Squeeze and Excitation (SE) module
Youtube lecture: https://www.youtube.com/watch?v=BSZqvObJVMg&ab_channel=MaziarRaissi

CTC- Connectionist Temporal Classification
https://www.youtube.com/watch?v=c86gfVGcvh4&ab_channel=CarnegieMellonUniversityDeepLearning

Dense Residual Connection

CER- Character Error Rate
