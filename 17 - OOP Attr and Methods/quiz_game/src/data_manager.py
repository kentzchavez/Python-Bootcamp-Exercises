import requests
import json
import html

def get_questions_from_opentdb_url(url):
    """Gets data from response URL"""
    print('[!] Gathering questions...\n')
    response = requests.get(url)
    data = response.json()
    questions = []
    for question in data['results']:
        questions.append({
            'text': html.unescape(question['question']), # some questions contains html entities, so to convert those into normal characters, I'll use this html function
            'answer': question['correct_answer']  
            })
    return questions
