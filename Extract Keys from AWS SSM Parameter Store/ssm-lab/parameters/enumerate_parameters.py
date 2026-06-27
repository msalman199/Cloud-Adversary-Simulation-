#!/usr/bin/env python3
"""
SSM Parameter Enumeration Tool
Students: Complete the TODO sections to implement parameter discovery
"""

import json
import os
import glob

class SSMParameterEnumerator:
    def __init__(self, parameters_dir="parameters"):
        self.parameters_dir = parameters_dir
        self.found_parameters = []
    
    def list_all_parameters(self):
        """
        Enumerate all parameters in the simulated Parameter Store
        
        TODO: Implement the following:
        1. Use glob to find all .json files in parameters_dir
        2. Load each JSON file and parse the parameter data
        3. Append each parameter to self.found_parameters
        4. Print parameter name, type, and version
        5. Return the list of parameters
        """
        print("[+] Enumerating SSM Parameters...")
        
        # TODO: Implement parameter enumeration
        pass
    
    def filter_by_path(self, path_prefix):
        """
        Filter parameters by path prefix (e.g., /myapp/database/)
        
        TODO: Implement filtering logic
        Args:
            path_prefix: The path prefix to filter by
        Returns:
            List of matching parameters
        """
        # TODO: Filter parameters where Name starts with path_prefix
        pass
    
    def filter_by_type(self, param_type):
        """
        Filter parameters by type (String or SecureString)
        
        TODO: Implement type filtering
        Args:
            param_type: The parameter type to filter by
        Returns:
            List of matching parameters
        """
        # TODO: Filter parameters by Type field
        pass

if __name__ == "__main__":
    enumerator = SSMParameterEnumerator()
    # TODO: Call list_all_parameters()
    # TODO: Test filter_by_path() with "/myapp/database/"
    # TODO: Test filter_by_type() with "SecureString"
