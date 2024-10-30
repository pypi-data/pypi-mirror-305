import asyncio
import aiohttp
from datetime import datetime, timedelta, timezone
from dotenv import load_dotenv
from updater.utils.db_handler import db_get_google_api_key_num
import os
from typing import List, Dict, Optional

load_dotenv()

google_search_engine_id = os.environ['google_searchengine_id']


async def fetch_google_results(search_query: str, search_site: str, search_range_days: Optional[int], max_results: int) -> List[Dict[str, str]]:
  # each call returns 10 results
  if search_range_days:
    date_restriction = f'd{search_range_days}'
  else:
    date_restriction = ""
  
  results_fetched = 0
  start_index = 1
  all_items = []

  async with aiohttp.ClientSession() as session:
    while results_fetched < max_results:
      api_key = get_google_api_key()
      
      # Construct api call url with parameters
      if search_site:
        url = f"https://www.googleapis.com/customsearch/v1?q={search_query}&cx={google_search_engine_id}&key={api_key}&dateRestrict={date_restriction}&siteSearch={search_site}&siteSearchFilter=i&start={start_index}"
      else:
        url = f"https://www.googleapis.com/customsearch/v1?q={search_query}&cx={google_search_engine_id}&key={api_key}&dateRestrict={date_restriction}&start={start_index}"

      async with session.get(url) as response:
        data = await response.json()
        
        # Handle Google API errors
        if 'error' in data:
          error = data['error']
          if error.get('code') == 429 or 'quotaExceeded' in error.get('message', ''):
            raise Exception("Google API quota exceeded")
          elif error.get('code') == 400:
            raise Exception(f"Invalid Google API request: {error.get('message')}")
          else:
            raise Exception(f"Google API error: {error.get('message')}")

      items = data.get('items', [])
      all_items.extend(items)

      results_fetched += len(items)
      start_index += len(items)

      # Break if no more results are returned
      if not items:
        break

  return all_items[:max_results]


def get_google_api_key() -> str:
  today = datetime.now(timezone.utc).date().isoformat()
  max_num = 16
  
  key_num = db_get_google_api_key_num(today, max_num)
  
  api_key = os.environ[f'google_api_key_{key_num}']

  return api_key


# For testing purposes
if __name__ == "__main__":
  search_query = "best M2 Max"
  search_range_days = None
  search_site = None
  max_results = 10

  results = asyncio.run(fetch_google_results(search_query, search_site, search_range_days, max_results))
  print(results)
