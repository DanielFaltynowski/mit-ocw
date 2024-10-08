"""
  @author: Daniel Faltynowski
"""

import string
from ps4a import get_permutations

### HELPER CODE ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    
    print("Loading word list from file...")
    # inFile: file
    inFile = open(file_name, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.extend([word.lower() for word in line.split(' ')])
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list


### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'

# you may find these constants helpful
VOWELS_LOWER = 'aeiou'
VOWELS_UPPER = 'AEIOU'
CONSONANTS_LOWER = 'bcdfghjklmnpqrstvwxyz'
CONSONANTS_UPPER = 'BCDFGHJKLMNPQRSTVWXYZ'

class SubMessage(object):
    def __init__(self, text):
        '''
        Initializes a SubMessage object
                
        text (string): the message's text

        A SubMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.__messsage_text = text
        self.__valid_words = load_words(WORDLIST_FILENAME)
    
    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.__messsage_text

    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class.
        This helps you avoid accidentally mutating class attributes.
        
        Returns: a COPY of self.valid_words
        '''
        return self.__valid_words
                
    def build_transpose_dict(self, vowels_permutation):
        '''
        vowels_permutation (string): a string containing a permutation of vowels (a, e, i, o, u)
        
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to an
        uppercase and lowercase letter, respectively. Vowels are shuffled 
        according to vowels_permutation. The first letter in vowels_permutation 
        corresponds to a, the second to e, and so on in the order a, e, i, o, u.
        The consonants remain the same. The dictionary should have 52 
        keys of all the uppercase letters and all the lowercase letters.

        Example: When input "eaiuo":
        Mapping is a->e, e->a, i->i, o->u, u->o
        and "Hello World!" maps to "Hallu Wurld!"

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        
        response = {}
        response[vowels_permutation[-1]] = vowels_permutation[0]
        for i in range(len(vowels_permutation) - 1):
            response[vowels_permutation[i]] = vowels_permutation[i + 1]
        return response
    
    def apply_transpose(self, transpose_dict):
        '''
        transpose_dict (dict): a transpose dictionary
        
        Returns: an encrypted version of the message text, based 
        on the dictionary
        '''
        
        ans = ''
        for letter in self.__messsage_text:
            if letter not in transpose_dict:
                ans = ans + letter
            else:
                ans = ans + transpose_dict[letter]
        return ans
        
class EncryptedSubMessage(SubMessage):
    def __init__(self, text):
        '''
        Initializes an EncryptedSubMessage object

        text (string): the encrypted message text

        An EncryptedSubMessage object inherits from SubMessage and has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''

        SubMessage.__init__(self, text)
        


    def decrypt_message(self):
        '''
        Attempt to decrypt the encrypted message 
        
        Idea is to go through each permutation of the vowels and test it
        on the encrypted message. For each permutation, check how many
        words in the decrypted text are valid English words, and return
        the decrypted message with the most English words.
        
        If no good permutations are found (i.e. no permutations result in 
        at least 1 valid word), return the original string. If there are
        multiple permutations that yield the maximum number of words, return any
        one of them.

        Returns: the best decrypted message    
        
        Hint: use your function from Part 4A
        '''
        
        ans = []
        index = None
        best_score = 0
        vowels_permutation = get_permutations(VOWELS_UPPER) + get_permutations(VOWELS_LOWER)

        for i in range(len(vowels_permutation)):
            actual_score = 0
            transpose_dict = self.build_transpose_dict(vowels_permutation[i])
            decrypted_message = self.apply_transpose(transpose_dict)
            ans.append(decrypted_message)
            decrypted_message = decrypted_message.split()
            for word in decrypted_message:
                if is_word(self.get_valid_words(), word):
                    actual_score = actual_score + 1
            if actual_score > best_score:
                best_score = actual_score
                index = i
        
        if index == None:
            print('This is incorrect message!')
        else:
            return ans[index]

            

                

    

if __name__ == '__main__':

    # Example test case
    # message = SubMessage("Hello World!")
    # permutation = "eaiuo"
    # enc_dict = message.build_transpose_dict(permutation)
    # print("Original message:", message.get_message_text(), "Permutation:", permutation)
    # print("Expected encryption:", "Hallu Wurld!")
    # print("Actual encryption:", message.apply_transpose(enc_dict))
    # enc_message = EncryptedSubMessage(message.apply_transpose(enc_dict))
    # print("Decrypted message:", enc_message.decrypt_message())
     

    # cip = SubMessage('my husband works hard')
    # print(cip.build_transpose_dict(VOWELS_LOWER))
    # print(cip.apply_transpose(cip.build_transpose_dict(VOWELS_LOWER)))

    # dip = EncryptedSubMessage('my hasbend wurks herd')
    # print(dip.decrypt_message())

    test1 = SubMessage("hello my friends")
    test1_e = test1.apply_transpose(test1.build_transpose_dict(VOWELS_LOWER))
    print(test1_e)
    test1_d = EncryptedSubMessage(test1_e)
    print(test1_d.decrypt_message())

    test2 = SubMessage("working hard is a good thing when you are younger than your parents")
    test2_e = test2.apply_transpose(test2.build_transpose_dict(VOWELS_LOWER))
    print(test2_e)
    test2_d = EncryptedSubMessage(test2_e)
    print(test2_d.decrypt_message())

    test3 = SubMessage("this is the part when i say i do not want it")
    test3_e = test3.apply_transpose(test3.build_transpose_dict(VOWELS_LOWER))
    print(test3_e)
    test3_d = EncryptedSubMessage(test3_e)
    print(test3_d.decrypt_message())
