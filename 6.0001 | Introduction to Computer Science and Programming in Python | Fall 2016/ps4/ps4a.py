"""
  @author: Daniel Faltynowski
"""

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''

    if len(sequence) == 1:
        return [sequence]
    elif len(sequence) == 2:
        reversed_sequence = list(sequence)
        reversed_sequence.reverse()
        reversed_sequence = ''.join(reversed_sequence)
        return [sequence, reversed_sequence]
    else:
        ans = []
        for letter in sequence:
            ans = ans + [letter + permutation for permutation in get_permutations(sequence.replace(letter, ''))]
        return ans
        
        

if __name__ == '__main__':
#    #EXAMPLE
   example_input = 'abc'
   print('Actual Output:', get_permutations(example_input))

   example_input = 'bust'
   print('Actual Output:', get_permutations(example_input))

   example_input = 'daniel'
   print('Actual Output:', get_permutations(example_input))

#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)

    

