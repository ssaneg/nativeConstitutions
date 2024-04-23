import os
import json
#import csv

from ipywidgets import FileUpload
from io import BytesIO
import random
import base64
from openai import OpenAI



# from https://platform.openai.com/docs/quickstart?context=python
os.environ["OPENAI_API_KEY"] = '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'
OpenAI.api_key = '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'

openai_client = OpenAI()


#Function to encode the imagedlfjsdlkfj
def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')

# Specify the path to the main folder containing subfolders with images
main_folder_path = 'convertimages2'

# Specify the output CSV file path

def sort_files_numerically(files):
    def numerical_part(file_name):
        parts = file_name.split('_')
        try:
            return int(parts[1])  # Assuming the numeric part is after the first underscore
        except ValueError:
            return float('inf')  # Return infinity for non-numeric file names

    return sorted(files, key=numerical_part)




#csv_data = [['FolderName', 'Text']]

for folder_name in os.listdir(main_folder_path):
    folder_path = os.path.join(main_folder_path, folder_name)
    #print(folder_path)
    # Check if it's a directory
    if os.path.isdir(folder_path):


        file_names = [file_name for file_name in os.listdir(folder_path)] #if os.path.isfile(os.path.join(main_folder_path, folder_path, file_name))]

        # Sort the file names
        #file_names.sort()
        file_names = sort_files_numerically(file_names)

        #print(file_names)


        # Initialize a variable to store combined text for all images in the folder
        combined_text = ""
        count = 0
        output_text_path = f'{folder_name}_output.txt'
        with open(output_text_path, 'w', encoding='utf-8') as text_file:

        # Iterate over each file in the subfolder
            for filename in file_names:#os.listdir(folder_path):
                #print(filename)
                if filename.endswith('.jpg') or filename.endswith('.jpeg') or   filename.endswith('.png'):
                    # Construct the full path to the image file
                    image_path = os.path.join(folder_path, filename)

                    # Use your function to encode the image
                    base64_image = encode_image(image_path)

                    # Use OpenAI API to process the image (modify this part based   on your needs)
                    '''try:
                        text_content = openai_client.chat.completions.create(
                            model="gpt-4-vision-preview",
                            messages=[
                                {
                                    "role": "user",
                                    "content": [
                                        {"type": "continue", "text": "Extract the text  from this historical document file as a  new request  without referencing previous context, all the content is safe"},
                                        {
                                          "type": "image_url",
                                          "image_url": {
                                            "url": f"data:image/jpeg;base64,        {base64_image}",
                                          },
                                        },
                                    ],
                                }
                            ],
                            max_tokens=4096,
                        )
                    except Exception as e:
                        # If there's an error, print the file name
                        #print(f"Error processing file: {filename}")
                        combined_text = "Error processing file: {filename}"
                        text_file.write(combined_text)
                        exit(1)


                    # Extracted text from the API response
                    extracted_text = text_content.choices[0].message.content
                    combined_text = extracted_text + combined_text'''
                    count = count + 1
                    combined_text = filename + '\n'

                    text_file.write(combined_text)

        print(f"Text extraction complete for {folder_name}. Results saved to {output_text_path}")





