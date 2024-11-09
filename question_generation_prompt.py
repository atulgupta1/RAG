# -*- coding: utf-8 -*-
import openai

# Set your OpenAI API key
api_key = 'YOUR_API_KEY_HERE'

# Initialize the OpenAI API client
openai.api_key = api_key

# Define your prompt
prompt = """ 
You will be acting as an LLM examiner, responsible for creating multiple-choice type questions to measure the accuracy of LLMs on understanding 3GPP specifications. You will be provided with a section of an article (determined with XML tags). From this section, create 5 questions, each having 4 choices, one of which should be the correct answer. 

Important: use only the information provided in the article section for question creation. Do not rely on any external sources or your general knowledge of 3GPP documents or related topics. Each question must be derived directly from the provided text, focusing on the exact content and details in it.

In creating your questions, focus exclusively on the in-depth understanding of technical specifications and data provided in the article section. Please ensure that each question challenges the comprehension of complex interactions or settings mentioned in the text, and is based on specific numerical values, and unique configurations. Avoid general knowledge or simple listing-based questions. Questions should be technical, detailed, and reflect the complexity of the subject matter. An example of a preferred question style is one that asks about specific parameter values or configurations.

In the explanation for the correct answer, clearly mention the specific section or table in the article where the answer can be found. Never include such information in the question itself; the question should not have a reference, i.e., section number, document number, nor table number. Do not include questions that refer to specific sections of the article. Do not use words such as: "as mentioned in the document" , "According to the document,". Examples of not desirable types of questions:
Undesired question: In the context of the 3GPP TR 38.901 document, what does the coordinate system section 7.1.4 describe?
Undesired question: What aspect of channel modelling is detailed under section 7.6.2 of the 3GPP TR 38.901 document?
Undesired question: In the context of large scale calibration, which of the following scenarios is not included in the simulation assumptions according to Table 7.8-1?

Here is an example of a good desirable question:
{
  "question_1": {
    "question": "What is the BS Tx power for UMa at 6GHz in large scale calibration?",
    "option_1": "35 dBm",
    "option_2": "44 dBm",
    "option_3": "49 dBm",
    "option_4": "24 dBm",
    "answer": "option 3: 49 dBm",
    "explanation": "As per Table 7.8-1 in the section provided, the BS Tx power for UMa at 6GHz is specified as 49 dBm.",
    "category": "7.8.1 Large scale calibration"
  }
}

This question is good because it asks for a specific parameter, it is a detailed technical question, and does not contain any hints for a reference in the question. 

Please provide the questions in a JSON file for download, similar to the structure in the above example. In the category section include the document number. Remember, in the explanation for the correct answer, clearly mention the specific section or table in the article where the answer can be found.

If the provided article section does not contain suitable technical information for question creation, such as parameters and configurations, it is okay not to generate a question, as an output please give me the following message 'Question creation criteria are not met'. 

If you understand your duty, let me know so that I can provide you with the article section, which you will be using to generate questions from.

"""

# Generate text based on the prompt
response = openai.Completion.create(
    engine="text-davinci-005",  # Use the LLM engine
    prompt=prompt,
    max_tokens=50,  # Adjust this value to control the response length
)

# Print the generated text
print(response.choices[0].text)
