from ddgs import DDGS

def web_search_egw(topic):

    query = f"site:egwwritings.org Ellen White {topic}"

    results = []

    try:
        with DDGS() as ddgs:
            search_results = ddgs.text(query, max_results=5)

            for r in search_results:
                results.append({
                    "title": r.get("title", ""),
                    "body": r.get("body", ""),
                    "link": r.get("href", "")
                })

    except Exception as e:
        print("Search error:", e)

        # fallback so API doesn't crash
        return [{
            "title": "Search unavailable",
            "body": "Please try again later",
            "link": ""
        }]

    return results