#!/usr/bin/python3
"""Base Model"""
import uuid
import datetime

class BaseModel:
    """Base Model Class"""
    
    def __init__(self):
        """Initialization generating id and datetime"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at
        
    def update_timestamp(self):
        """Update datetime"""
        self.updated_at = datetime.now()