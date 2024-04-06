from PIL import Image

# Open the original image
image = Image.open('images/alien2small.png')

# Define the new width and height for the smaller image
new_width = image.width // 2
new_height = image.height // 2

# Resize the image
smaller_image = image.resize((new_width, new_height))

# Save the smaller image
smaller_image.save('images/alien3small.png')

# Close the original image
image.close()