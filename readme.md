upload and display images in flask:
https://roytuts.com/upload-and-display-image-using-python-flask/

Text detection from images:
1. EasyOCR- 
   1. https://www.analyticsvidhya.com/blog/2021/06/text-detection-from-images-using-easyocr-hands-on-guide/
   2. https://www.youtube.com/watch?v=ZVKaWPW9oQY&ab_channel=NicholasRenotte
2. Tesseract- open source ocr engine
   1. https://www.youtube.com/watch?v=PY_N1XdFp4w&ab_channel=NeuralNine
   2. Medium article on Tesseract vs google- https://joseurena.medium.com/tesseract-ocr-evaluating-handwritten-text-recognition-1c6db85b2e7f
   3. youtube tesseract for handwritten text- https://www.youtube.com/watch?v=a5oeEhTf6_M&ab_channel=JoseM.Urena

Dataset:
IAM (IAM Handwriting)
- 13,353 images of handwritten lines of text created by 657 writers
- writers transcribed text from Lancaster-Oslo/Bergen Corpus of British English
- total of 1,539 handwritten pages 
- 115,320 words
- The database is labeled at the sentence, line, and word levels
- Dataset paper: The IAM-database: an English sentence database for offline handwriting recognition

Accessing dataset:
- You need to register first at https://fki.tic.heia-fr.ch/databases/iam-handwriting-database
- Email- ta2642, password- MachineReadM3
- Github repo with data download python notebook: https://github.com/kartikgill/Easter2/blob/main/notebooks/iam_dataset_download.ipynb
- Train-test split: wget https://www.openslr.org/resources/56/splits.zip

Citation:
@article{chaudhary2022easter2,
  title={Easter2. 0: Improving convolutional models for handwritten text recognition},
  author={Chaudhary, Kartik and Bali, Raghav},
  journal={arXiv preprint arXiv:2205.14879},
  year={2022}
}

Paper:
Terms:
HTR- Handwriting Text Recognition
Squeeze and Excitation (SE) module
Youtube lecture: https://www.youtube.com/watch?v=BSZqvObJVMg&ab_channel=MaziarRaissi

CTC- Connectionist Temporal Classification
https://www.youtube.com/watch?v=c86gfVGcvh4&ab_channel=CarnegieMellonUniversityDeepLearning

Dense Residual Connection

CER- Character Error Rate
