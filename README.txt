Image to Text for my dad's optical. He has around 910 receipts that needs inputting into Google Drive. (I do it manually)
=========
Tried my hand at PyTesseract, but to no avail because Tesseract can only handle high-res images and the receipts that was provided is really blurry and ilegible, even I can't understand the handwriting.
=========
This might be useful for future projects so I'm pushing it here.

=========
Steps:
pip install pyTesseract
import Tesseract as shown in code and edit the file path for the image
=========
Need to figure out how to make a loop to loop through my whole folder of receipts of 910 images then selecting specific index using tuples or dictionaries
Then push to SQL
