import os
import ast
import json
import shutil

#class for iterate
class STRLIter:
  def __init__(self,STRL,f):
    self._STRL = STRL
    self._file = f

  #method for iteration
  def __next__(self):
    #[:-1]removes\n
    line = self._file.readline()[:-1]

    if not line:
      raise StopIteration
    #convert to original type
    item = ast.literal_eval(line)

    return item


class STRL:
  #making __strl__ dir
  def __init__(self,file_name,mode):
    if file_name[0:8] == "__temp__":
      raise ValueError("file name cannot start with '__temp__'")
    #create __sllist__ dir if not exist
    dir_existence = os.path.exists('./__strl__')
    if dir_existence == False:
      os.mkdir('./__strl__')
    #mode w resets the file
    if mode == "w":
      #reset the file content
      with open("./__strl__/"+ file_name,mode='w', encoding='utf-8') as f:
        f.write("")
    #mode l load the file. if not exist, create file.
    elif mode == "l":
      #create file if not exist
      file_existence = os.path.exists('./__strl__/'+file_name)
      if file_existence == False:
        with open("./__strl__/"+ file_name,mode='w', encoding='utf-8') as f:
          f.write("")
    else:
      raise AttributeError('Mode "' + mode + '" does not exist\nPlease use "w" or "l".\nw: delete existing file and rewrite. l: load the existing file.')

    self._filename = file_name

  #iterationg method
  def __iter__(self):
    f = open("./__strl__/"+ self._filename, encoding='utf-8')
    return STRLIter(self,f)
    f.close()


  #set up the data to write
  def __to_str(self,item):
    #dict causes error in some enviroments
    if type(item) == dict:
      item = json.dumps(item)
      write_item =  str(item)
    #str need quotation for ast.literal_eval(see StorageLustIter.__next__)
    elif type(item) == str:
      write_item = '"' + item + '"'
    else:
      write_item =  str(item)

    return write_item


  def get_text(self):
    with open("./__strl__/"+self._filename,mode='r', encoding='utf-8') as f:
      return f.read()


  #return the file data by list
  def get_list(self):
    return_list = []
    with open("./__strl__/"+self._filename,mode='r', encoding='utf-8') as f:
      for item in f:
        line = item[:-1] #remove\n

        if not line:
          raise StopIteration
        #convert to original class
        return_item = ast.literal_eval(line)
        return_list.append(return_item)
    return return_list


 #return the file data by list
  def get_filtered_list(self,func):
    if callable(func) == False:
      raise AttributeError('Please give lambda or function to func argument.')

    return_list = []
    with open("./__strl__/"+self._filename,mode='r', encoding='utf-8') as f:
      for item in f:
        line = item[:-1] #remove\n

        if not line:
          raise StopIteration
        #convert to original class
        return_item = ast.literal_eval(line)
        if func(return_item) == True:
          return_list.append(return_item)
    return return_list


  #return the data of given line
  def get_item(self,line_num):
    n = 0
    with open("./__strl__/"+self._filename,mode='r', encoding='utf-8') as read_f:
      for line in read_f:
        #if line_num matches line number n(starts 0), return the line
        if n == line_num:
          return ast.literal_eval(line)
        n += 1
      #When the line number doesn't exist
      return None

  #add all items of given list
  def append_list_items(self, rewrite_list):
    if type(rewrite_list) != list:
      raise AttributeError('Please give list to argument.')
    for item in rewrite_list:
      write_item = self.__to_str(item)
      with open("./__strl__/"+self._filename,mode='a', encoding='utf-8') as f:
        f.write( write_item + '\n')


  def append(self, item):
    write_item = self.__to_str(item)
    with open("./__strl__/"+self._filename,mode='a', encoding='utf-8') as f:
      f.write( write_item + '\n')


  #change the specific line
  def set(self,line_num,set_item):
    if line_num < 0:
      raise ValueError("line number cannnot be negative.")
    n = 0
    with open("./__strl__/"+self._filename,mode='r', encoding='utf-8') as read_f:
      #create temporary file
      with open("./__strl__/"+"__temp__"+self._filename,mode='a', encoding='utf-8') as write_f:
        for line in read_f:
          if n == line_num:
            #if line_num matches line number n(starts 0), write given set_item
            write_item = self.__to_str(set_item)
            write_f.write(write_item + "\n")
          else:
            # keep the other lines same
            write_f.write(line)
          n += 1
        #When line_num > lines in file
        if n < line_num:
          #until line_num, add None
          while n < line_num:
            write_item = self.__to_str(None)
            write_f.write(write_item + "\n")
            n += 1
          #when reach line_num, add set_item
          write_item = self.__to_str(set_item)
          write_f.write(write_item + "\n")


    #remove temporary file and copy to original
    shutil.move("./__strl__/"+"__temp__"+self._filename,"./__strl__/"+self._filename)

  #insert to the specific line
  def insert(self,line_num,set_item):
    if line_num < 0:
      raise ValueError("line number cannnot be negative.")

    n = 0
    with open("./__strl__/"+self._filename,mode='r', encoding='utf-8') as read_f:
      #create temporary file
      with open("./__strl__/"+"__temp__"+self._filename,mode='a', encoding='utf-8') as write_f:
        for line in read_f:
          if n == line_num:
            #if line_num matches line number n(starts 0), write given set_item
            write_item = self.__to_str(set_item)
            write_f.write(write_item + "\n")
            # keep the other lines same
            write_f.write(line)
          else:
            # keep the other lines same
            write_f.write(line)
          n += 1
        #When line_num > lines in file
        if n < line_num:
          #until line_num, add None
          while n < line_num:
            write_item = self.__to_str(None)
            write_f.write(write_item + "\n")
            n += 1
          #when reach line_num, add set_item
          write_item = self.__to_str(set_item)
          write_f.write(write_item + "\n")

    #remove temporary file and copy to original
    shutil.move("./__strl__/"+"__temp__"+self._filename,"./__strl__/"+self._filename)

  def remove(self, line_num_tuple):
    n = 0
    with open("./__strl__/"+self._filename,mode='r', encoding='utf-8') as read_f:
      #create temporary file
      with open("./__strl__/"+"__temp__"+self._filename,mode='a', encoding='utf-8') as write_f:
        for line in read_f:
          if n in line_num_tuple:
            write_f.write("")
          else:
            # keep the other lines same
            write_f.write(line)
          n += 1
    #remove temporary file and copy to original
    shutil.move("./__strl__/"+"__temp__"+self._filename,"./__strl__/"+self._filename)

  @classmethod
  def show_files(cls):
    try:
      files = os.listdir(path='./__strl__')
    except FileNotFoundError:
      return []
    return files

  def delete(self):
    os.remove("./__strl__/"+self._filename)



