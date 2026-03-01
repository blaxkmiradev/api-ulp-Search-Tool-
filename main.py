import json
import os
import requests
from datetime import datetime
from api_ulp import ApiUlp

# ── Configuration ─────────────────────────────────────────────
API_KEY    = "YOUR_API_KEY"   # Replace with your real API key
QUERY      = "example.com"    # Replace with your search target
LIMIT      = 100              # Max number of results to return
OUTPUT_DIR = "results"        # Folder where results will be saved
# ──────────────────────────────────────────────────────────────


def save_results(query: str, results: dict) -> str:
    """Save results to a timestamped .txt file and return the file path."""
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    timestamp  = datetime.now().strftime("%Y%m%d_%H%M%S")
    safe_query = "".join(c if c.isalnum() or c in "-_." else "_" for c in query)
    filepath   = os.path.join(OUTPUT_DIR, f"{safe_query}_{timestamp}.txt")

    with open(filepath, "w", encoding="utf-8") as f:
        f.write("ULP API Search Results\n")
        f.write("=" * 40 + "\n")
        f.write(f"Query     : {query}\n")
        f.write(f"Limit     : {LIMIT}\n")
        f.write(f"Timestamp : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write("=" * 40 + "\n\n")
        f.write(json.dumps(results, indent=2, ensure_ascii=False))
        f.write("\n")

    return filepath


def main():
    client = ApiUlp(api_key=API_KEY)

    try:
        print(f"[*] Searching for: '{QUERY}' (limit={LIMIT}) ...")
        results = client.search(query=QUERY, limit=LIMIT)

        print("[+] Success! Results:")
        print(json.dumps(results, indent=2, ensure_ascii=False))

        filepath = save_results(QUERY, results)
        print(f"\n[+] Results saved to: {filepath}")

    except ValueError as e:
        print(f"[!] Input Error: {e}")

    except requests.exceptions.HTTPError as e:
        print(f"[!] API Error: {e}")

    except requests.exceptions.ConnectionError as e:
        print(f"[!] Connection Error: {e}")

    except requests.exceptions.Timeout as e:
        print(f"[!] Timeout: {e}")


if __name__ == "__main__":
    main()
