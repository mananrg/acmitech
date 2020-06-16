#import content_selection
from google.cloud import vision
from google.cloud.vision import types
import os
import io
from getpostsfromjson import
os.environ['GOOGLE_APPLICATION_CREDENTIALS']=r'gcp_cloud_vision.json'
client=vision.ImageAnnotatorClient()
import os
with os.scandir('/var/www/html/down_images/') as entries:
    for entry in entries:
      try:
        file_name=entry.name
        print("file name is")
        print(file_name)
        #file_name=r'o2lvjfgeydch80my_1577675741.jpeg'
        image_path=f'{file_name}'
        with io.open(image_path,'rb') as image_file:
           content=image_file.read()
        image=vision.types.Image(content=content)
        response=client.label_detection(image=image)
        print("for file_name")
        print(file_name)
        print("response is")
        print(response)
      except:
        print("error in opening file")
#x=[]

#x=content_selection.ret_html()
#print(type(x))

