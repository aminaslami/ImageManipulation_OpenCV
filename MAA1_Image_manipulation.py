import cv2

# Load the image
image = cv2.imread('input_image.jpg')

# Resize the image
resized_image = cv2.resize(image, (500, 500))

# Convert the image to grayscale
gray_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)

# Save the grayscale image
cv2.imwrite('output_image.jpg', gray_image)

# Display the original and modified images
cv2.imshow('Original Image', image)
cv2.imshow('Grayscale Image', gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
