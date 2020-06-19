from zipfile import ZipFile
import os
from os.path import basename

dirName = '/media/profnick/F27CDC9F7CDC5FC1/Projects/nightingale-data/src/data/'
# create a ZipFile object
with ZipFile('/media/profnick/F27CDC9F7CDC5FC1/Projects/nightingale-data/src/compressed/sample.zip', 'w') as zipObj:
   # Iterate over all the files in directory
   for folderName, subfolders, filenames in os.walk(dirName):
       for filename in filenames:
           #create complete filepath of file in directory
           filePath = os.path.join(folderName, filename)
           # Add file to zip
           zipObj.write(filePath, basename(filePath))