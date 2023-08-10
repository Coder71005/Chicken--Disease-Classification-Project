#!/usr/bin/env python
# coding: utf-8

# In[11]:


import os
from pathlib import Path
import logging


# In[13]:


logging.basicConfig(level = logging.INFO, format = '[%(asctime)s]: %(message)s:')


# In[6]:


project_name = 'cnnClassifier'

lis_of_files = [
    ".guthib/workflos/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yamil",
    "params.ymal",
    "requirements.txt",
    "setup.py",
    "research/trials/ipynb"
]


# In[ ]:


for filepath in list_of_files:
    filepath = Path(filepath)
    filedir,filename = os.path.split(filepath)
    
    
    if filedir != "":
        os.makedirs(filedir,exist_ok = True)
        logging.info(f"Creating directiory;{filedir} for the file: {filename}")
        
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) ==0):
        with open(filepath,"w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filename} is already exist")


# In[10]:





# In[ ]:




