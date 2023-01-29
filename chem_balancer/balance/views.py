import cv2
import pytesseract
import re

from django.shortcuts import render, redirect

def parse_equation(text):
    elements = re.findall('[A-Z][a-z]?\d*', text)
    coefficients = re.findall('\d+', text)
    equation = dict(zip(elements, coefficients))
    return parse_equation

def balance_equation(equation):
    #balance coefficients for each element to determine overall equation

def index(request):
    if request.method == 'POST':
        image = request.FILES['image']
        #convert to numpy array
        image = cv2.imdecode(np.frombuffer(image.read(), np.uint8), cv2.IMREAD_UNCHANGED
        #to grayscale
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        #apply thresholding to make the text more clear
        thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU[1])

        #pass through to pytesseract

        text = pytesseract.image_to_string(thresh)

        #parse the chemical parse_equation
        equation = parse_equation(text)

        balanced_equation = balance_equation(equation)

        return render(request, 'balance/index.html', {'balanced_equation': balanced_equation})
    else:
        return render(request, 'balance/index.html')
