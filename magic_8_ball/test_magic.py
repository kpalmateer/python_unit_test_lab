""" TODO create a test case to test each of the following functions,

generate_url_for_question
 - check that the expected URL is returned for an example question. 

extract_answer_from_response
 - one test should create some example dictionaries that match the expected response from the API,
 and check that the correct answer is extracted and returned.
 - another test should create example dictionaries with a different structure to the one returned from the API, 
 and check that the function returns None. 

 
 TODO to think about - what else could you test about this program? 
 What types of expected and unexpected behavior might happen? You may be able to write tests for some 
 of your ideas now. We'll talk about ways to test other aspects of this program in class.

"""
import requests
import unittest
from unittest import TestCase
from functions_magic import generate_url_for_question, extract_answer_from_response

class Test8Ball(TestCase):
    def test_generate_url_for_question(self):
        question = 'Will I live to be 100?'
        expected_url = 'https://magic-8-ball-mctc.uc.r.appspot.com/magic/JSON/' + question
        actual_url = generate_url_for_question('Will I live to be 100?')
        self.assertEqual(expected_url, actual_url)

if __name__ == '__main__':
    unittest.main()
