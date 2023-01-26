"""
*** This file communicates with WolframAlpha api.
    It contains all logic for the question and answers.

"""

from fastapi import APIRouter, HTTPException, status
from dotenv import load_dotenv
from api import schemas
from urllib import parse

import xml.etree.ElementTree as ET
import wolframalpha
import requests
import os

router = APIRouter(tags=['Question'])

# TODO: I CAN USE A REGEX TO REMOVE THE UNWANTED PIPES

load_dotenv()
WOLFRAM_APP_ID = os.getenv('WOLFRAM_APP_ID')

base_url = f"https://api.wolframalpha.com/v2/"

@router.post('/ask')
async def ask_question(request: schemas.Question): 
    # create a client class
    client = wolframalpha.Client(WOLFRAM_APP_ID)

    # Stores the response from 
    # wolframalpha
    res = client.query(request.question)
    
    # Includes only text from the response
    answer = next(res.results).text

    # Raise an exception in case something unexpected happens
    if not answer:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Something went wrong!"
        )

    return {'answer': answer}

@router.post('/ask-math')
async def ask_math_question(request: schemas.Question):
    
    # Get the question in raw string and make it url safe
    raw_question = request.question
    url_safe_question = parse.quote(raw_question)

    # Wolframalpha API query URL
    query = base_url + f"query?appid={WOLFRAM_APP_ID}&input={url_safe_question} \
            &podstate=Result__Step-by-step+solution&format=plaintext"
    
    # API call, and parse the result using xml ElementTree
    # since the API returns an xml response.
    response = requests.get(query)
    root = ET.fromstring(response.text)

    # Search for the pod and subpod elements holding the answers from the query result
    # and append both the short answer and the step-by-step answers in a list.
    pods = root.findall('.//pod/subpod')
    answers = []

    for pod in pods:
        plaintext = pod.find('.//plaintext')
        answers.append(plaintext.text)
    
    # Raise an exception in case something unexpected happens
    if not answers:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                detail="Something went wrong!")

    # Get the long answer from the answers list and split each steps into
    # different lines
    long_answer = str(answers[2]).splitlines()
    
    return {
        'short_nswer': answers[1],
        'long_nswer': long_answer
    }
