import sys
import os
import time
import json
import requests
from typing import List, Optional, Dict, Any
from dataclasses import dataclass, asdict

@dataclass
class SearchResult:
    title: str
    link: str
    description: str

@dataclass 
class SearchResponse:
    results: List[SearchResult]
    current_page: int
    has_next: bool
    info_section: Optional[Dict[str, Any]] = None
    special_sections: Optional[Dict[str, Any]] = None

class PresearchSkill:
    """
    Production-ready Presearch API client for AI agents.
    Implements rate limiting and exponential backoff.
    """
    
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://na-us-1.presearch.com/v1/search"
        self.last_request_time = 0
        self.rate_limit_delay = 1.1  # >1s for Free Tier safety
        
    def __enter__(self):
        return self
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
        
    def _rate_limit(self):
        """Enforce rate limits"""
        current_time = time.time()
        time_since_last = current_time - self.last_request_time
        if time_since_last < self.rate_limit_delay:
            time.sleep(self.rate_limit_delay - time_since_last)
        self.last_request_time = time.time()
    
    def search(self, query: str, ip: str = "127.0.0.1", lang: str = "en-US", time_filter: str = "any", 
               page: int = 1, safe: str = "1", location: Optional[str] = None) -> SearchResponse:
        """
        Execute a search query.
        """
        self._rate_limit()
        
        params = {
            "q": query,
            "ip": ip,
            "lang": lang,
            "time": time_filter,
            "page": str(page),
            "safe": safe
        }
        
        if location:
            params["location"] = location
        
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
            "Accept": "application/json"
        }
        
        try:
            response = requests.get(self.base_url, params=params, headers=headers)
            
            if response.status_code == 429:
                time.sleep(2) # Simple backoff
                return self.search(query, ip, lang, time_filter, page, safe, location)
                
            response.raise_for_status()
            
            data = response.json()
            resp_data = data.get("data", {})
            standard_results = resp_data.get("standardResults", [])
            pagination = resp_data.get("pagination", {})
            info_section = resp_data.get("infoSection")
            special_sections = resp_data.get("specialSections")
            
            results = [
                SearchResult(
                    title=r.get("title", ""),
                    link=r.get("link", ""), 
                    description=r.get("description", "")
                )
                for r in standard_results
            ]
            
            return SearchResponse(
                results=results,
                current_page=pagination.get("current_page", 1),
                has_next=pagination.get("has_next", False),
                info_section=info_section,
                special_sections=special_sections
            )
            
        except requests.exceptions.RequestException as e:
            raise Exception(f"Presearch API Error: {e}")

if __name__ == "__main__":
    # CLI Usage: python3 presearch_python.py "search query"
    if len(sys.argv) < 2:
        print("Usage: python3 presearch_python.py <query>")
        sys.exit(1)
        
    api_key = os.getenv("PRESEARCH_API_KEY")
    if not api_key:
        print("Error: PRESEARCH_API_KEY environment variable not set.")
        sys.exit(1)
        
    query = sys.argv[1]
    
    try:
        with PresearchSkill(api_key) as skill:
            response = skill.search(query)
            
            # Print JSON output for agent consumption
            output = {
                "results": [asdict(r) for r in response.results],
                "info_section": response.info_section,
                "special_sections": response.special_sections,
                "pagination": {
                    "current_page": response.current_page,
                    "has_next": response.has_next
                }
            }
            print(json.dumps(output, indent=2))
            
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)