# We begin with importing the required python libraries that include cv2, pytesseract and a module called as re

import cv2

import pytesseract

import re

# The first step involves following the path of the picture that is uploaded to check for validity

picture_track = r"C:\Users\Sreelu\OneDrive\Documents\New folder\pancardexample.jpeg"

# Now the second step is about reading the picture to pass it for conversion into text

picture = cv2.imread(picture_track)

# After reading the third step involves the  process of converting the picture to textual data

content= pytesseract.picture_to_string(picture)

# Now, it checks whether the above textual data matches the required pattern

model = re.compile(r'[A-Z]{5}[0-9]{4}[A-Z]')

# Here follows the searching of number in the PAN card is being processed from that extracted data

equal = model.search(content)

# Printing the number of the PAN card if the match is successful where it qualifies all the requirements accordingly

if equal:

  print("PAN Card Number:", equal.group())

# If there exists no proper match, then return an empty string in that case

else:

  print("")