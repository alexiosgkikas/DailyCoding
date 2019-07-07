# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 17:32:25 2019

@author: Alexios
"""
flat_dict={}

def flat_dict_fun(nested_dict,parent):
   for ele in nested_dict:
       if isinstance(nested_dict.get(ele),dict):    
           print("found nested: "+str(ele))
           parent+=(str(ele))+"."
           flat_dict_fun(nested_dict.get(ele),parent)
       else:
           flat_dict[parent +(str(ele))]=nested_dict.get(ele)
    
        
if __name__ == "__main__":
    nested_dict = {"key": 3,"foo": {"a": 5,"bar": {"baz": 8}}}
    print(nested_dict)
    flat_dict_fun(nested_dict,"")
    
    print(flat_dict)