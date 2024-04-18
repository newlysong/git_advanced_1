from typing import List

# Skeleton code for even_list
def even_list(int_list: List[int]) -> List[int]:
    
    """
    Determines if a number is even and return an even list.    
    
    Args:        
    int_list: A list of integer. 
       
    Returns:        
    A list of even integers.    
    """
    
    # TODO: Implement even_list    
    return [num for num in int_list if num % 2 == 0]