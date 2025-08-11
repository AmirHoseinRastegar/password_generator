from abc import ABC, abstractmethod
import string
import random
from typing import List, Optional

import nltk

class PasswordGenerator(ABC):
    '''
    base class for generating passwords
    '''
    @abstractmethod
    
    def generate(self)-> str:
        '''
        abstract methode of password generating that get inherited by 
        other classes
        '''
        pass
    
    
class random_pass(PasswordGenerator) :
    '''
       generates a random password
    '''
    
    def __init__(self, include_number: bool = False, include_symboles: bool = False, length: int = 8) :
        self.length=length
        self.charachters= string.ascii_letters
        if include_number:
            self.charachters += include_number
        if include_symboles:
            self.charachters += include_symboles
        
    def generate(self) -> str:
        
        '''
        generate from specific charachters
        '''
        return ''.join(random.choice(self.charachters) for _ in range (self.length)) 
          


class MemorablePassword(PasswordGenerator):
    '''
      Generates some chosen words as password
    '''
    
    def __init__(self,
                 seperator: str = '_',
                 vocabulary: Optional[List[str]] = None,
                 words_count = 5,
                 caps = False,
                 ):
      if vocabulary is None:
          vocabulary= nltk.corpus.words.words()
          
      self.caps = caps
      self.seperator=seperator
      self.vocabulary = vocabulary
      self.words_count=words_count
      
      
    def generate(self):
      '''
      genearetes the password
      '''
      password_words= [random.choice(self.vocabulary ) for _ in range (self.words_count) ]
       
      if self.caps:
        password_words= [word.upper() for word in password_words]
      
      return self.seperator.join(password_words)



class PinPass(PasswordGenerator):
    '''
    generates a numeric PIN
    '''
    
    def __init__(self, length= 8):
        
        self.length=length
    
    def generate(self):
        
        pin= (random.choice(string.digits) for _ in range(self.length))
        return ''.join(pin)