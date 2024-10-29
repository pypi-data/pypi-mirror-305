import json
import time
import asyncio
import os
from openai import AsyncOpenAI
import requests
from dotenv import load_dotenv
import instructor

load_dotenv()  
PERPLEXITY_API_KEY = os.getenv("PERPLEXITY_API_KEY")

async def get_openai_response_instr(sys_prompt, user_prompt, model, temp, response_model):
  client_instr = instructor.from_openai(AsyncOpenAI())
  try:
    response = await asyncio.wait_for(client_instr.chat.completions.create(
      model=model,
      response_model=response_model,
      temperature=temp,
      messages=[
        {'role': 'system', 'content': sys_prompt},
        {'role': 'user', 'content': user_prompt}
      ]
    ), timeout=600)
    if response:
      return response
  except asyncio.TimeoutError:
    print("OpenAI request timed out")
    return None
  except Exception as e:
    print(f"Error in get_openai_response, model {model}: {str(e)}")
    return None


# Returns json object
async def get_openai_response(sys_prompt, user_prompt, model, response_format, caller):
  client = AsyncOpenAI()
  start_time = time.time()
  try:
    completion = await asyncio.wait_for(client.chat.completions.create(
      model=model,
      response_format=response_format,
      temperature=0,
      messages=[
        {'role': 'system', 'content': sys_prompt},
        {'role': 'user', 'content': user_prompt}
      ]
    ), timeout=600)
    duration = time.time() - start_time
    if completion:
      prompt_tokens = completion.usage.prompt_tokens
      completion_tokens = completion.usage.completion_tokens
      total_tokens = completion.usage.total_tokens
      return json.loads(completion.choices[0].message.content)
  except asyncio.TimeoutError:
    print("OpenAI request timed out")
    return None
  except Exception as e:
    print(f"Error in get_openai_response for fn {caller}, model {model}: {str(e)}")
    return None


async def get_openai_response_struct(sys_prompt, user_prompt, model, response_format, caller):
  client = AsyncOpenAI()
  start_time = time.time()
  try:
    completion = await asyncio.wait_for(client.beta.chat.completions.parse(
      model=model,
      response_format=response_format,
      temperature=0,
      messages=[
        {'role': 'system', 'content': sys_prompt},
        {'role': 'user', 'content': user_prompt}
      ]
    ), timeout=600)
    duration = time.time() - start_time
    if completion:
      prompt_tokens = completion.usage.prompt_tokens
      completion_tokens = completion.usage.completion_tokens
      total_tokens = completion.usage.total_tokens
      return completion.choices[0].message.parsed
  except asyncio.TimeoutError:
    print("OpenAI request timed out")
    return None
  except Exception as e:
    print(f"Error in get_openai_response: {str(e)}")
    return None
          

def get_perplexity_response(sys_prompt, user_prompt, model, temp):
  url = "https://api.perplexity.ai/chat/completions"  
  headers = {
    "Authorization": f"Bearer {PERPLEXITY_API_KEY}",
    "Content-Type": "application/json"
  }
  
  payload = {
    "model": model,
    "temperature": temp,
    "return_citations": True,
    "messages": [
      {"role": "system", "content": sys_prompt},
      {"role": "user", "content": user_prompt}
    ]
  }
  
  response = requests.request("POST", url, json=payload, headers=headers)
  if response.status_code == 200:
    return response.json()['choices'][0]['message']['content']
  else:
    print(f"Error in get_perplexity_response: {response.status_code} {response.text}")
    return None
  