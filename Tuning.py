
import os
import app
import google.generativeai as genai
#import PIL.Image





os.environ['GOOGLE_API_KEY'] = "AIzaSyAhJ41L42PQLRRsIaGns8eXnkx0hPA0Q88"

genai.configure(api_key=os.environ['GOOGLE_API_KEY'])

model= genai.GenerativeModel('gemini-1.5-flash')





def answer_asked_question(ask_question):
    request_answer = " show me the correct detailed solution of  ) ", ask_question
    api_response_answer = model.generate_content(request_answer)
    return api_response_answer.text


def image_asked_question(questions_image):
    request_image_solution= "Show me the solution of question shown in the image", questions_image
    api_response_image_solution = model.generate_content(request_image_solution)
    return api_response_image_solution

def get_solution(question):
    request_solution= " show me the correct detailed solution of  ) ",question
    api_response_sol= model.generate_content(request_solution)
    return api_response_sol.text

def generate_hint(question):
    request_hint = " show me only the hint needed to solve this  ) ", question
    api_response_hint = model.generate_content(request_hint)
    return api_response_hint.text

def get_formulae(question):
    request_formulae=" Analyze the following problem statement and provide the relevant formula(s) for solving it:don't give me the solution ",question
    api_response_formulae=model.generate_content(request_formulae)
    return api_response_formulae.text



