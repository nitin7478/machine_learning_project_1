import os
import sys 

class HousingException(Exception):
    # Exception is parent class , we are using inheritance here
    def __init__(self , error_message:Exception, error_detail:sys):
        # error_message is object of Exception which gives what is exception
        # details of error , which line causing error is given by sys to error_detail object
        
        #to pass error message informationation to Exception(Parent class)
        super().__init__(error_message) # use super to pass information to parent class
        self.error_message=HousingException.get_detailed_error_message(error_message=error_message,
                                                                        error_detail=error_detail)
        
        
    @staticmethod
    def get_detailed_error_message(error_message:Exception, error_detail:sys)->str: 
        """
        error_message: Exception object
        error_detail: object of sys module  
        """
        _,_ , exec_tb = error_detail.exc_info() #going to return most recent exception caught by except clause
        exception_block_line_number = exec_tb.tb_frame.f_lineno
        try_block_line_number = exec_tb.tb_lineno
        file_name = exec_tb.tb_frame.f_code.co_filename
        
        error_message = f"""
        Error occured in script: [{file_name}] 
        at try block line number: [{try_block_line_number}] and exception block line number : [{exception_block_line_number}]
        error message : [{error_message}]
        """
        return error_message
    
    def __str__(self):
        return self.error_message
    
    def __repr__(self)->str:
        return HousingException.__name__.str()
        
        
            
    
    
    
    