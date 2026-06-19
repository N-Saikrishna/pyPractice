import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s  -  %(levelname)s  -  %(message)s')
logging.debug('Start of Progeam')

def factorial(n):
    assert isinstance(n, int), 'Input must be a integer' #isinstance checks if a variable is of the specified class or not
    assert n >= 0, 'Input must be non-negative'

    logging.debug('Start of Factorial(' + str(n) + ')')
    total = 1
    for i in range(1, n + 1): 
        total *= i
        logging.debug('i is ' + str(i) + ', total is ' + str(total))
    
    logging.debug('End of Factorial(' + str(n) + ')')
    return total

fact_num = int(input('Factorial of? '))
print(factorial(fact_num))
logging.debug('End of program')

