import os
import zipfile
import requests

class FileProcessor:
    
    def __init__(self, extract_path ='text_files', file_types=['.txt', '.docx']):

        self.file_url = "https://github.com/msaricaumbc/DS601_Spring21/raw/main/Week10/homework/text_files.zip"
        self.extract_path = extract_path
        self.zip_filename = 'textfiles.zip'
        self.file_types = file_types
        
    def download_file(self):
        """
        download a file based on a URL, save to filename
        """
        r = requests.get(self.file_url , allow_redirects=True)
        open(self.zip_filename, 'wb').write(r.content)

    def extract_zip(self):
        with zipfile.ZipFile(self.zip_filename, "r") as zip_ref:
            zip_ref.extractall()    
    
    def find_all_files(self):
        paths = []
        for root, dirs, files in os.walk(self.extract_path):
            for file in files:
                if any([file.endswith(ft) for ft in self.file_types]):
                    path = (os.path.join(root, file), file)
                    # print(path)
                    paths.append(path)
        # print(paths)
        return paths

    def save_obj(self, obj, file_name):
        with open(file_name, "w") as f:
            for key in obj.keys():
                line = key + ':\t' + ','.join(obj[key]) + '\n'
                f.write(line)
    
    def start(self):
        """
        Entry point for the class
        """
        self.download_file()
        
        self.extract_zip()
        
        files = self.find_all_files()
        
        obj = {}
        
        for path, file in files:
            print ('Processing: ', file)
            obj[file] = self.process_file(path)
    
        print('Saving File')
        self.save_obj(obj, 'output.dat')
        
        print('Process Finished')
        
    def process_file(self, file_name):
        """
        abstract method
        
        Parameters: file_name
        Returns: List of unique words ['test', 'hair']
        """
        raise NotImplemented('process_file method not implemented')