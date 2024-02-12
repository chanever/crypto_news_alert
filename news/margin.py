from PIL import Image, ImageOps

# Load the generated image
image_path = '/mnt/data/Visualize_a_dynamic_and_optimistic_scene_depicting.png'
image = Image.open(image_path)

# Define the size of the white margin
margin_size = 300  # pixels

# Add white margin at the bottom
new_image = ImageOps.expand(image, border=(0, 0, 0, margin_size), fill='white')

# Save the modified image
modified_image_path = '/mnt/data/Modified_Bitcoin_Surge_Image.png'
new_image.save(modified_image_path)

modified_image_path
