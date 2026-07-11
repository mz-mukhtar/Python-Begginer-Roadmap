# 📘 Week Eight – Session One: Working With APIs

Welcome back! 👋

Welcome to **Week Eight**—the final week of the Python Beginner to Practical Developer Roadmap! 🎉

Up until now, our applications only worked with local data stored on your own laptop (`students.json` or `students.csv`). But what if your application needs live weather data, real-time currency exchange rates, or up-to-date country profiles?

You do not need to download the entire world's database onto your hard drive! Instead, your application can talk to web servers across the internet using an **API (Application Programming Interface)**. In this session, you will learn how web requests work, install the industry-standard **`requests`** library, handle JSON responses and status codes, and build our interactive **Country Information Application**!

---

## 🎯 Learning Objectives

By the end of this session, you will be able to:
- Explain what an API is using real-world analogies (Restaurant Waiter analogy)
- Understand web communication flows (Client Requests vs. Server Responses)
- Identify HTTP request methods (`GET`, `POST`, `PUT`, `DELETE`) and HTTP status codes (`200`, `404`, `500`)
- Install and use Python's `requests` library inside a virtual environment
- Send `GET` requests to public web endpoints with safe timeouts (`timeout=10`)
- Parse live JSON payloads into Python lists and dictionaries using `.json()`
- Handle network failures and HTTP errors cleanly using `try-except` and `.raise_for_status()`
- Build, run, and explain the **Country Information Application** project

---

## 📌 1. Introduction: The Restaurant Analogy

Imagine sitting at a restaurant table.
- **You (The Customer)**: You want food, but you do not walk into the kitchen to cook it yourself.
- **The Kitchen (The Server)**: The kitchen prepares the food, but the chefs do not walk out to your table.
- **The Waiter (The API)**: The waiter takes your order, carries it to the kitchen, and delivers your prepared meal back to your table!

In software engineering:
```text
Your Python Application (Customer)
  ↓ [Sends Request via API]
Web Server / Database (Kitchen)
  ↓ [Returns JSON Response via API]
Your Python Application
```

An **API** is simply a standardized messenger that allows two different software applications to exchange data safely over the internet.

---

## 🌐 2. Request and Response & Endpoints

Every API conversation consists of two parts:
1. **Request**: Your Python program asks a web server at a specific web address (**URL / Endpoint**) for information.
2. **Response**: The server answers with an **HTTP Status Code** and a data payload (usually formatted as JSON!).

---

## 📬 3. HTTP Methods

When communicating with APIs, standard **HTTP Methods** tell the server what action you want to perform:

| HTTP Method | Action | Example Analogy |
| :---: | :--- | :--- |
| **`GET`** | Retrieve data from server | Inspecting a restaurant menu |
| **`POST`** | Submit new data to server | Submitting a new order |
| **`PUT`** | Update existing data | Modifying your meal choice |
| **`DELETE`** | Remove data from server | Canceling your order |

In this session, we focus exclusively on **`GET`** requests to fetch live information!

---

## 🚦 4. HTTP Status Codes

Every response includes a 3-digit number called a **Status Code** indicating whether the request succeeded:

| Status Code | Meaning | Explanation |
| :---: | :--- | :--- |
| **`200`** | **OK** | Request succeeded perfectly! Data is attached. |
| **`201`** | **Created** | New resource created successfully on server. |
| **`400`** | **Bad Request** | Server could not understand the request formatting. |
| **`401`** | **Unauthorized** | Missing authentication credentials or API key. |
| **`403`** | **Forbidden** | You are authenticated, but lack permission to access this resource. |
| **`404`** | **Not Found** | The URL endpoint or requested item does not exist. |
| **`500`** | **Internal Server Error** | The web server crashed on its end. |

---

## 📦 5. Installing the `requests` Library

Let us put our Week Seven virtual environment skills to work! Open your terminal inside your project folder:

```bash
# Create and activate environment
python -m venv .venv
source .venv/bin/activate  # Or Windows: .venv\Scripts\Activate.ps1

# Install requests library
python -m pip install requests
```

---

## 🚀 6. Sending Your First GET Request

Let us send a live request to **JSONPlaceholder**—a free public educational API:

```python
import requests

url = "https://jsonplaceholder.typicode.com/users/1"

# Send GET request with a 10-second timeout safety guard
response = requests.get(url, timeout=10)

print("HTTP Status Code:", response.status_code)
```

### Example Output:
```text
HTTP Status Code: 200
```

---

## 📥 7. Reading JSON Responses (`.json()`)

Remember Week Four? JSON looks just like Python dictionaries! The `response.json()` method automatically converts the server's raw JSON text payload directly into Python dictionaries or lists:

```python
import requests

url = "https://jsonplaceholder.typicode.com/users/1"
response = requests.get(url, timeout=10)

# Convert API JSON response to Python dictionary
user_data = response.json()

print("Name:", user_data["name"])
print("Email:", user_data["email"])
print("City:", user_data["address"]["city"])
```

### Example Output:
```text
Name: Leanne Graham
Email: Sincere@april.biz
City: Gwenborough
```

---

## 🛡️ 8. Basic API Error Handling

What if the internet disconnects or the user searches for a missing resource (`404`)? We use `try-except` combined with `response.raise_for_status()` to catch network errors gracefully:

```python
import requests

api_url = "https://jsonplaceholder.typicode.com/users/999"  # User 999 does not exist!

try:
    response = requests.get(api_url, timeout=10)
    response.raise_for_status()  # Raises HTTPError for 4xx or 5xx status codes
    data = response.json()
    print("Success:", data)
except requests.exceptions.HTTPError as err:
    print(f"❌ HTTP Error occurred: {err}")
except requests.exceptions.RequestException as err:
    print(f"❌ Network connection error: {err}")
```

---

## 🛠️ 9. Weekly Project: Country Information Application

Let us combine API requests, JSON parsing, dictionary navigation, and error handling to build our **Country Information Application** using the public REST Countries API!

### 📋 Required Features
- Prompts the user to enter any country name.
- Sends a live `GET` request to `https://restcountries.com/v3.1/name/<country_name>`.
- Displays formatted facts: Official Name, Capital City, Population, Region, and Currency.
- Handles missing countries (`404`) and internet dropouts without crashing!

### Complete Runnable Code

```python
# ==========================================
# Project: Country Information Application
# Week Eight Session One Project
# ==========================================

import requests


def fetch_country_info(country_name):
    """Fetches live country data from public REST Countries API."""
    url = f"https://restcountries.com/v3.1/name/{country_name}"

    try:
        response = requests.get(url, timeout=10)

        # Check if country was not found
        if response.status_code == 404:
            print(f"\n❌ Country '{country_name}' not found. Please check spelling.")
            return None

        response.raise_for_status()
        data = response.json()

        # The API returns a list of matching countries; take the top match
        return data[0]

    except requests.exceptions.Timeout:
        print("\n⏳ Request timed out. Check your internet connection.")
        return None
    except requests.exceptions.RequestException as e:
        print(f"\n❌ Network error occurred: {e}")
        return None


def display_country_report(country_data):
    """Parses country dictionary and prints formatted report."""
    name = country_data.get("name", {}).get("official", "Unknown")

    capitals = country_data.get("capital", ["No Capital"])
    capital = capitals[0] if capitals else "No Capital"

    population = country_data.get("population", 0)
    region = country_data.get("region", "Unknown")

    # Extract first currency name safely
    currencies = country_data.get("currencies", {})
    currency_name = "Unknown"
    if currencies:
        first_currency_code = list(currencies.keys())[0]
        currency_name = currencies[first_currency_code].get("name", first_currency_code)

    print("\n==========================================")
    print("        COUNTRY INFORMATION REPORT        ")
    print("==========================================")
    print("Official Name:", name)
    print("Capital City :", capital)
    print("Region       :", region)
    print("Population   :", f"{population:,}")
    print("Currency     :", currency_name)
    print("==========================================")


def main():
    """Interactive controller loop."""
    print("=== Welcome to the Live Country Information Explorer ===")

    while True:
        query = input("\nEnter a country name (or type 'exit' to quit): ").strip()
        if query.lower() == "exit":
            print("\n👋 Thank you for exploring the world. Goodbye!")
            break

        if not query:
            print("Please enter a non-empty country name.")
            continue

        print(f"Searching API for '{query}'...")
        country_data = fetch_country_info(query)

        if country_data:
            display_country_report(country_data)


if __name__ == "__main__":
    main()
```

### Example Output:
```text
=== Welcome to the Live Country Information Explorer ===

Enter a country name (or type 'exit' to quit): Ethiopia
Searching API for 'Ethiopia'...

==========================================
        COUNTRY INFORMATION REPORT        
==========================================
Official Name: Federal Democratic Republic of Ethiopia
Capital City : Addis Ababa
Region       : Africa
Population   : 114,963,583
Currency     : Ethiopian birr
==========================================
```

---

## 📝 10. Practice Exercises

Try these API exercises!

### Beginner
1. **Status Code Check**: Send a `GET` request to `https://jsonplaceholder.typicode.com/posts/1` and print the HTTP status code.
2. **Title Extractor**: Convert the JSON response from Exercise 1 into a dictionary and print only the `"title"` key.

### Intermediate
3. **List of Posts**: Send a `GET` request to `https://jsonplaceholder.typicode.com/posts` (returns a list of 100 dictionaries). Loop through the first 5 posts and print their titles.
4. **404 Handler**: Write a script that requests `https://jsonplaceholder.typicode.com/missing_page`, inspects `response.status_code == 404`, and prints `"Page missing!"`.

### Challenge
5. **Random Quote Viewer**: Use any free public quote API to build a CLI script that fetches and displays a random motivational quote each time it runs!

---

## ❓ 11. Review Questions

1. What role does an API play between a client application and a remote server?
2. What is the difference between an HTTP `GET` request and an HTTP `POST` request?
3. What does HTTP status code `200` mean compared to status code `404`?
4. What method converts a raw JSON response body into Python dictionaries (`response.json()`)?
5. Why should every web request include a `timeout=10` parameter?

---

## ✅ 12. Learning Checklist

- [ ] I understand how APIs enable applications to communicate over the internet.
- [ ] I can install and import the `requests` library.
- [ ] I can send `GET` requests to public web endpoints.
- [ ] I can inspect status codes (`200`, `404`) and parse JSON payloads.
- [ ] I can handle network connection errors safely.
- [ ] I can build and explain the Country Information Application.

---

## 🏁 13. Session Summary

- **APIs** act as standardized messengers allowing Python apps to fetch live internet data.
- **`requests.get(url)`** retrieves server responses containing status codes and data bodies.
- **`.json()`** converts JSON responses into familiar Python dictionaries and lists.
- Combining live API requests with error safety allowed us to build our **Country Information Application**!
