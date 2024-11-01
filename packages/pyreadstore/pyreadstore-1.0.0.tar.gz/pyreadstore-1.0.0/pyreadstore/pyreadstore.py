# pyreadstore/pyreadstore.py

# Copyright 2024 EVOBYTE Digital Biology Dr. Jonathan Alles
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import configparser
import pandas as pd
from pydantic import BaseModel
from typing import List

from pyreadstore import rsclient
from pyreadstore import rsexceptions
from pyreadstore import rsdataclasses


class Client():
    
    RETURN_TYPES = ['pandas', 'json']
    
    def __init__(self,
                 config_dir: str = '~/.readstore',
                 username: str | None = None, 
                 token : str | None = None,
                 host: str = 'http://localhost',
                 return_type: str = 'pandas',
                 port: int = 8000,
                 fastq_extensions: List[str] = ['.fastq','.fastq.gz','.fq','.fq.gz']):
        
        # Check valid return types
        self._check_return_type(return_type)
        self.return_type = return_type
        
        # If username & token provided, use them to initialize the client
        if username and token:
            endpoint_url  = f'{host}:{port}'
            
        elif username or token:
            raise rsexceptions.ReadStoreError('Both Username and Token must be provided')
        # Case load config from files
        else:
            if '~' in config_dir:
                config_dir = os.path.expanduser(config_dir)
            else:
                config_dir = os.path.abspath(config_dir)
            
            config_path = os.path.join(config_dir, 'config')
            if not os.path.exists(config_path):
                raise rsexceptions.ReadStoreError(f'Config file not found at {config_dir}')
            
            rs_config = configparser.ConfigParser()
            rs_config.read(config_path)
        
            username = rs_config.get('credentials', 'username', fallback=None)
            token = rs_config.get('credentials', 'token', fallback=None)
            endpoint_url = rs_config.get('general', 'endpoint_url', fallback=None)
            fastq_extensions = rs_config.get('general', 'fastq_extensions', fallback=None)
            fastq_extensions = fastq_extensions.split(',')
            
        # Check if ENV variables are set
        # Overwrite config if found
        if 'READSTORE_USERNAME' in os.environ:
            username = os.environ['READSTORE_USERNAME']
        if 'READSTORE_TOKEN' in os.environ:
            token = os.environ['READSTORE_TOKEN']
        if 'READSTORE_ENDPOINT_URL' in os.environ:
            endpoint_url = os.environ['READSTORE_ENDPOINT_URL']
        if 'READSTORE_FASTQ_EXTENSIONS' in os.environ:
            fastq_extensions = os.environ['READSTORE_FASTQ_EXTENSIONS']
            fastq_extensions = fastq_extensions.split(',')
        
        self.fastq_extensions = fastq_extensions
        
        # Initialize the client
        self.rs_client = rsclient.RSClient(username,
                                            token,
                                            endpoint_url,
                                            output_format='csv')
        
        
    def _convert_json_to_pandas(self,
                            json_data: List[dict] | dict,
                            validation_class: BaseModel) -> pd.DataFrame | pd.Series:
        
        if isinstance(json_data, dict):
            if json_data == {}:
                return pd.Series()
            else:
                data = validation_class(**json_data)
                return pd.Series(data.model_dump())
            
        elif isinstance(json_data, list):
            # Data validation using pydantic
            data = [validation_class(**ele) for ele in json_data]
            
            if data == []:
                df = pd.DataFrame(columns=validation_class.model_fields.keys())    
            else:
                df = pd.DataFrame([ele.model_dump() for ele in data])
                
            return df
        else:
            raise rsexceptions.ReadStoreError('Invalid JSON data')
    
    def _check_return_type(self, return_type: str):
        if return_type not in Client.RETURN_TYPES:
            raise rsexceptions.ReadStoreError(f'Invalid return type. Must be in {Client.RETURN_TYPES}')
        
    def get_return_type(self) -> str:
        return self.return_type
     
    def list(self,
             project_id: int | None = None,
             project_name: str | None = None,
             return_type: str | None = None) -> pd.DataFrame | List[dict]:
        
        if return_type:
            self._check_return_type(return_type)
            return_type = return_type
        else:
            return_type = self.return_type
        
        fq_datasets = self.rs_client.list_fastq_datasets(project_id=project_id,
                                                         project_name=project_name)
        
        if return_type == 'pandas':
            fq_datasets = self._convert_json_to_pandas(fq_datasets, rsdataclasses.RSFqDataset)
        
        return fq_datasets
    
    # TODO: Function to explode metadata
    
    def get(self,
            dataset_id: int| None = None,
            dataset_name: str | None = None,
            return_type: str | None = None) -> pd.Series | dict:
        
        if (dataset_id is None) and (dataset_name is None):
            raise rsexceptions.ReadStoreError('Either dataset_id or dataset_name must be provided')
            
        if return_type:
            self._check_return_type(return_type)
            return_type = return_type
        else:
            return_type = self.return_type
        
        fq_dataset = self.rs_client.get_fastq_dataset(dataset_id = dataset_id,
                                                      dataset_name = dataset_name)
        
        if return_type == 'pandas':
            fq_dataset = self._convert_json_to_pandas(fq_dataset, rsdataclasses.RSFqDatasetDetail)
        
        return fq_dataset
    
    def get_fastq(self,
                dataset_id: int | None = None,
                dataset_name: str | None = None,
                return_type: str | None = None) -> pd.DataFrame | List[dict]:
        
        if (dataset_id is None) and (dataset_name is None):
            raise rsexceptions.ReadStoreError('Either id or name must be provided')
        
        if return_type:
            self._check_return_type(return_type)
            return_type = return_type
        else:
            return_type = self.return_type
        
        fq_dataset = self.rs_client.get_fastq_dataset(dataset_id = dataset_id,
                                                      dataset_name = dataset_name)
        
        # Check if the dataset was found
        if fq_dataset == {}:
            if return_type == 'pandas':
                return_cols = rsdataclasses.RSFqFile.model_fields.keys()
                return pd.DataFrame(columns=return_cols)
            else:
                return []
        else:
            fq_dataset = rsdataclasses.RSFqDatasetDetail(**fq_dataset)
            
            fq_file_ids = [fq_dataset.fq_file_r1,
                           fq_dataset.fq_file_r2,
                           fq_dataset.fq_file_i1,
                           fq_dataset.fq_file_i2]
            
            fq_file_ids = [int(e) for e in fq_file_ids if not e is None]
            fq_files = [self.rs_client.get_fq_file(fq_file_id) for fq_file_id in fq_file_ids]
            
            if return_type == 'pandas':
                fq_files = self._convert_json_to_pandas(fq_files, rsdataclasses.RSFqFile)

            return fq_files
        
    def download_attachment(self,
                            attachment_name: str,
                            dataset_id: int | None = None,
                            dataset_name: str | None = None,
                            outpath: str | None = None):
        
        if (dataset_id is None) and (dataset_name is None):
            raise rsexceptions.ReadStoreError('Either id or name must be provided')
        
        fq_dataset = self.rs_client.get_fastq_dataset(dataset_id = dataset_id,
                                                      dataset_name = dataset_name)
        
        # Check if the dataset was found
        if fq_dataset == {}: 
            raise rsexceptions.ReadStoreError('Dataset not found')
        
        fq_dataset = rsdataclasses.RSFqDatasetDetail(**fq_dataset)
        attachments = fq_dataset.attachments
        
        if attachment_name not in attachments:
            raise rsexceptions.ReadStoreError('Attachment not found')
        else:
            if outpath is None:
                outpath = os.getcwd()
                outpath = os.path.join(outpath, attachment_name)
            
            output_dirname = os.path.dirname(outpath)
            if (output_dirname != '') and (not os.path.exists(output_dirname)):
                raise rsexceptions.ReadStoreError(f'Output directory {output_dirname} does not exist')
            
            self.rs_client.download_fq_dataset_attachment(attachment_name,
                                                        outpath,
                                                        dataset_id,
                                                        dataset_name)
    
    
    def list_projects(self,
                      return_type: str | None = None) -> pd.DataFrame | List[dict]:
        
        if return_type:
            self._check_return_type(return_type)
            return_type = return_type
        else:
            return_type = self.return_type
        
        projects = self.rs_client.list_projects()
        
        if return_type == 'pandas':
            projects = self._convert_json_to_pandas(projects, rsdataclasses.RSProject)
        
        return projects
    
    
    def get_project(self,
                    project_id: int | None = None,
                    project_name: str | None = None,
                    return_type: str | None = None) -> pd.DataFrame | dict:
        
        if (project_id is None) and (project_name is None):
            raise rsexceptions.ReadStoreError('Either project_id or project_name must be provided')
        
        if return_type:
            self._check_return_type(return_type)
            return_type = return_type
        else:
            return_type = self.return_type
        
        project = self.rs_client.get_project(project_id = project_id,
                                            project_name = project_name)
        
        if return_type == 'pandas':
            project = self._convert_json_to_pandas(project, rsdataclasses.RSProjectDetail)
        
        return project
    
    def download_project_attachment(self,
                                   attachment_name: str,
                                   project_id: int | None = None,
                                   project_name: str | None = None,
                                   outpath: str | None = None):
        
        if (project_id is None) and (project_name is None):
            raise rsexceptions.ReadStoreError('Either id or name must be provided')
        
        project = self.rs_client.get_project(project_id = project_id,
                                            project_name = project_name)
        
        # Check if the project was found
        if project == {}: 
            raise rsexceptions.ReadStoreError('Project not found')
        
        project = rsdataclasses.RSProjectDetail(**project)
        attachments = project.attachments
        
        if attachment_name not in attachments:
            raise rsexceptions.ReadStoreError('Attachment not found')
        else:
            if outpath is None:
                outpath = os.getcwd()
                outpath = os.path.join(outpath, attachment_name)
            
            output_dirname = os.path.dirname(outpath)
            if (output_dirname != '') and (not os.path.exists(output_dirname)):
                raise rsexceptions.ReadStoreError(f'Output directory {output_dirname} does not exist')
            
            self.rs_client.download_project_attachment(attachment_name,
                                                        outpath,
                                                        project_id,
                                                        project_name)
            
    def upload_fastq(self, fastq : List[str] | str):
        
        if isinstance(fastq, str):
            fastq = [fastq]
        
        fq_files = []
        for fq in fastq:
            if not os.path.exists(fq):
                raise rsexceptions.ReadStoreError(f'File {fq} not found')
            if not fq.endswith(tuple(self.fastq_extensions)):
                raise rsexceptions.ReadStoreError(f'File {fq} is not a valid FASTQ file')
            fq_files.append(os.path.abspath(fq))
        
        self.rs_client.upload_fastq(fq_files)
        
            
    