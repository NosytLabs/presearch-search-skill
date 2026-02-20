import os
import json
import sys
from presearch_python import PresearchSkill

def run_search(name, params):
    print(f"\n🔍 Searching: {name}")
    print(f"   Params: {json.dumps(params, indent=2)}")
    
    api_key = os.getenv("PRESEARCH_API_KEY")
    if not api_key:
        print("❌ Error: PRESEARCH_API_KEY environment variable not set.")
        return

    try:
        with PresearchSkill(api_key) as skill:
            query = params.pop("q")
            # Map params to method args
            ip = params.get("ip", "127.0.0.1")
            lang = params.get("lang", "en-US")
            time_filter = params.get("time", "any")
            page = params.get("page", 1)
            safe = params.get("safe", "1")
            location = params.get("location", None)
            
            response = skill.search(query, ip=ip, lang=lang, time_filter=time_filter, page=page, safe=safe, location=location)
            
            print(f"✅ Success! Found {len(response.results)} results.")
            if response.results:
                top_result = response.results[0]
                print(f"   Top: {top_result.title}")
                print(f"   Link: {top_result.link}")
                print(f"   Desc: {top_result.description[:100]}...")
            
            if response.info_section:
                print(f"ℹ️  Info Section: {response.info_section.get('title')}")
            
            if response.special_sections:
                print(f"🌟 Special Sections: {list(response.special_sections.keys())}")
                
    except Exception as e:
        print(f"❌ Failed: {e}")

def main():
    print("🚀 Presearch Skill - Advanced Features Demo")
    print("=" * 50)
    
    # 1. Date Filter: Past Day
    run_search("News from Last 24h", {
        "q": "latest technology news",
        "time": "day"
    })
    
    # 2. Date Filter: Past Month
    run_search("Crypto Trends Last Month", {
        "q": "bitcoin price trends",
        "time": "month"
    })
    
    # 3. Location Filter (San Francisco)
    run_search("Local Search (SF)", {
        "q": "weather",
        "location": '{"lat": 37.77, "long": -122.41}'
    })
    
    # 4. Safe Search OFF
    run_search("Safe Search OFF", {
        "q": "linux kernel unfiltered",
        "safe": "0"
    })
    
    # 5. Pagination (Page 2)
    run_search("Pagination Page 2", {
        "q": "python tutorials",
        "page": 2
    })

if __name__ == "__main__":
    main()