import nltk
import os
from tqdm import tqdm
from collections import Counter
import math

class Preprocessor:
    """
    A class for text preprocessing tasks such as tokenization, stemming, and filtering stop words.

    Attributes:
        stop_words (set): A set of common stop words to be filtered out during tokenization.
        ps (nltk.stem.PorterStemmer): An instance of the Porter Stemmer for word stemming.
    """
    def __init__(self,stop_words=None, stemmer=nltk.stem.PorterStemmer()):
        """
        Initializes the Preprocessor object by defining the set of stop words and creating a Porter Stemmer instance.
        """
        if stop_words is None:
            self.stop_words = { 'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 
                                'for', 'from', 'has', 'he', 'in', 'is', 'it', 'its',
                                'of', 'on', 'that', 'the', 'to', 'was', 
                                'were', 'will', 'with'}
        else:
            self.stop_words = stop_words
        self.stemmer = stemmer
    
    def tokenize(self, text):
        """
        This function tokenizes the input text into words using the NLTK (Natural Language Toolkit) 
        word tokenizer. The NLTK word tokenizer is capable of handling various types of text, 
        including contractions and punctuations, and produces a list of individual words.
        
        Parameters:
            text (str): The input text to be tokenized.
            
        Returns:
            list: A list of tokens obtained by splitting the input text into words.
          
        """
        ## START YOU CODE HERE
        pass
        ## END
        return tokenized_text
    
    def stem(self, token):
        """
        This function utilizes the Porter Stemmer algorithm to reduce the input token
        to its root or base form. Stemming is a common text processing technique that 
        helps in simplifying words to their common base, enhancing the efficiency and 
        effectiveness of text analysis tasks.
        
        Parameters:
            token (str): The token to be stemmed.
            
        Returns:
            str: The stemmed version of the input token.
       
        """
        ## START YOU CODE HERE
        pass
        ## END
        return stemmed_token
        
    
    def is_apt_word(self, token):
        """
        This function determines the appropriateness of a token based on two criteria:
            1. It should consist of letters only (not include punctuation, numbers, or dates).
            2. It should not be a common stop word.
        
        Parameters:
            token (str): The token to be checked.
        
        Returns:
            bool: True if the token consists of letters only and is not a stop word, 
                  False otherwise.
        """
        if token.isalpha() and token.lower() not in self.stop_words:
            return True
        else:
            return False

    
    def preprocess(self, text, lower=True):
        """
        This function preprocesses the input text by first tokenizing it and optionally converting
        it to lowercase. Then, it removes any inappropriate words (stop words, non-letter characters)
        and applies stemming to the remaining tokens.
        
        Parameters:
            text (str): The input text to be preprocessed.
            lower (bool, optional): If True, converts the text to lowercase before processing.
                                     Default is True.
                                     
        Returns:
            list: A list of preprocessed and tokenized words, after removing stop words and stemming.
       
        """
        if lower:
            tokens = self.tokenize(text.lower())
        else:
            tokens = self.tokenize(text)
        if self.stemmer!= None:
            return [self.stem(token) for token in tokens if self.is_apt_word(token)]
        else:
            return [token for token in tokens if self.is_apt_word(token)]
        
class Indexer:
    """
    The Indexer class is responsible for managing document indexing.

    Attributes:
    - collection_path (str): The path to the document collection.
    - doc_id_to_filename (dict): Dictionary mapping document IDs to filenames.
    - filename_to_doc_id (dict): Dictionary mapping filenames to document IDs.
    - inverted_index (dict): Inverted index containing terms and their corresponding postings lists.
    - document_term_vector (dict): Vector representation of document terms.
    - collection_freq (dict): Dictionary storing the frequency of terms in the entire collection.
    - doc_freq (dict): Dictionary storing the document frequency of terms.
    - doc_lengths (dict): Dictionary storing the length of each document.
    - prep (Preprocessor): Preprocessor instance for text processing.

    Methods:
    - __init__(self, collection_path): Initializes the Indexer with the path to the document collection.
    """

    def __init__(self, collection_path):   
        # Initialize attributes
        self.collection_path = collection_path
        self.doc_id_to_filename = {} 
        self.filename_to_doc_id = {} 
        self.inverted_index = {}
        self.document_term_vector = {}
        self.collection_freq = {}    
        self.doc_freq = {}    
        self.doc_lengths = {}
        # Instantiate a Preprocessor for text processing
        self.prep = Preprocessor()
        
    
    def index(self):
        """
        Recursively read all files in the given directory and its subdirectories.
        """
        total_files = sum([len(files) for _, _, files in os.walk(self.collection_path)])
        with tqdm(total=total_files, desc="Processing Files") as pbar:
            for foldername, subfolders, filenames in os.walk(self.collection_path):
                for filename in filenames:
                    if filename.endswith('.txt'):
                        file_path = os.path.join(foldername, filename)
                        with open(file_path, 'r') as file:
                            text = file.read()
                            doc_id = len(self.doc_id_to_filename)
                            self.doc_id_to_filename[doc_id] = os.path.splitext(filename)[0]
                            self.filename_to_doc_id[filename] = doc_id
                            self.index_doc(text, doc_id)
                   
                pbar.update(len(filenames))
                
        for token in self.inverted_index.keys():
            sorted_posting = dict(sorted(self.inverted_index[token].items(), key=lambda item: item[0]))
            self.inverted_index[token] = sorted_posting

        
    def index_doc(self, text, doc_id):
        """
        Indexes a document by preprocessing its text and updating the index stuctures.

        Parameters:
        - text (str): The text content of the document.
        - doc_id (str): The unique identifier for the document.

        """
        ## START YOU CODE HERE
        pass
        ## END


def vsm_log_freq(indexer, query_tokens, docs):
    """
    Calculate the Vector Space Model (VSM) scores using Log Frequency Ranking for a query and a given set of documents.

    Args:
        indexer (Indexer): An instance of the Indexer class containing the inverted index.
        query_tokens (dict): A dictionary representing the query with terms as keys and their frequencies as values.
        docs (list): A list of document IDs for which the scores need to be calculated.

    Returns:
        dict: A dictionary containing document IDs as keys and their corresponding scores as values.
    """
    results = {}

    ## START YOU CODE HERE
    pass
    ## END

    return results


def vsm_jaccard(indexer, query_tokens, docs):
    """
    Calculate the Jaccard similarity coefficients for a given set of documents using the Vector Space Model (VSM).

    Args:
        indexer (Indexer): An instance of the Indexer class containing the inverted index.
        query_tokens (dict): A dictionary representing the query with terms as keys and their frequencies as values.
        docs (list): A list of document IDs for which the scores need to be calculated.

    Returns:
        dict: A dictionary containing document IDs as keys and their corresponding scores as values.
    """
    results = {}
    
    ## START YOU CODE HERE
    pass
    ## END
    
    return results


def vsm_cosine(indexer, query_tokens, docs):
    """
    Calculate Vector Space Model (VSM) scores using the Cosine Similarity measure for a given set of documents.

    Args:
        indexer (Indexer): An instance of the Indexer class containing the inverted index.
        query_tokens (dict): A dictionary representing the query with terms as keys and their frequencies as values.
        docs (list): A list of document IDs for which the scores need to be calculated.

    Returns:
        dict: A dictionary containing document IDs as keys and their corresponding scores as values.
    """
    results = {}
    
    ## START YOU CODE HERE
    pass
    ## END
    
    return results


class Retrieval:

    def __init__(self, indexer, prep):
        """
        Constructor for the Retrieval class.

        Parameters:
        - indexer: The inverted index and document frequency indexer.
        - prep: The preprocessor for query and document text.
        """
        self.indexer = indexer
        self.prep = prep
    
    def prepare_query(self, raw_query):
        """
        Preprocesses the raw query using the preprocessor and counts token frequencies.

        Parameters:
        - raw_query: The raw query string.

        Returns:
        A dictionary with token frequencies in the query.
        """
        # Pre-process query the same way as documents
        query = self.prep.preprocess(raw_query)
        # Count frequency
        return dict(Counter(query))

    def intersect_two_postings(self, posting_1, posting_2):
        """
        Computes the intersection between two posting lists.

        Parameters:
        - posting_1: The first posting list.
        - posting_2: The second posting list.

        Returns:
        A list containing the common elements between posting_1 and posting_2.
        """
        answer = []
        ## START YOU CODE HERE
        pass
        ## END
        return answer

    def intersect_postings(self, postings, doc_freq):
        """
        Computes the intersection of multiple posting lists.

        Parameters:
        - postings: A dictionary of posting lists for each token.
        - doc_freq: A dictionary of document frequencies for each token.

        Returns:
        A sorted list of documents that satisfy the intersection condition.
        """
        sorted_docs = sorted(doc_freq, key=doc_freq.get)
        merge = list(postings[sorted_docs[0]].keys())           
        for token in sorted_docs[1:]:
            merge = self.intersect_two_postings(merge, list(postings[token].keys()))
        return sorted(merge)

    def union_postings(self, postings):
        """
        Computes the union of multiple posting lists.

        Parameters:
        - postings: A dictionary of posting lists for each token.

        Returns:
        A sorted list of documents that satisfy the union condition.
        """
        answer = []
        ## START YOU CODE HERE
        pass
        ## END
        return answer

    def boolean_retrieval(self, query, ir_model='boolean', operator='OR'):
        """
        Performs boolean retrieval for the given query.

        Parameters:
        - query: The user query string.
        - ir_model: The information retrieval model to be used.
        - operator: The boolean operator ('AND' or 'OR') for combining query terms.

        Returns:
        A dictionary of sorted documents based on the relevance score.
        """
        query_tokens = self.prepare_query(query)
        postings = {}
        doc_freq = {}
        retrieved_docs = []
        for token in query_tokens.keys():
            if token in self.indexer.inverted_index.keys():
                postings[token] = self.indexer.inverted_index[token]
                doc_freq[token] = self.indexer.doc_freq[token]
            else:
                postings[token] = {}
                doc_freq[token] = 0
        if operator.lower() == 'and':
            retrieved_docs = self.intersect_postings(postings, doc_freq)            
        elif operator.lower() == 'or':       
            retrieved_docs =  self.union_postings(postings)
        else:
            raise ValueError('Incorrect Boolean operator.')

        if ir_model.lower() == 'boolean':
            return retrieved_docs



