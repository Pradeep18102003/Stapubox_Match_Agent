# StapuBox AI Matchmaker

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Powered by Gemini](https://img.shields.io/badge/AI-Gemini%203%20Flash-orange.svg)](https://aistudio.google.com/)

**StapuBox AI Matchmaker** is a proactive "Social Sports Assistant" built to solve the primary friction point for working professionals: finding the right sports partner at the right time and place. 

By combining **Geospatial Intelligence** (pincode-based distance math) with **Generative AI** (Gemini 3 Flash), this agent moves beyond simple search filters to provide intelligent, contextual matchmaking.

---

## Live Demo
**Try the App here:** [Stapubox Match Agent](https://stapuboxmatchagent-8jvnzeqmr5radntrtxjumd.streamlit.app/)

> **Note:** Enter your Pincode in the sidebar to find matches within a 10km radius.

---

## Key Features
* **Proactive Matchmaking:** Uses Gemini 2.5 Flash to understand natural language requests (e.g., *"Looking for a competitive 7 AM cricket match near Noida Sector 62"*).
* **Geospatial Optimization:** Implements `pgeocode` for high-speed, offline distance calculations between Indian pincodes to ensure partners are feasible.
* **Smart "Gym Buddy" Logic:** Differentiates between competitive opponents (Badminton/Tennis) and motivational partners (Gym/Workout).
* **Synthetic Data Scale:** Tested against a custom-built dataset of 200+ localized player profiles across Delhi-NCR.

---

## Performance & Logic
I focused on building an efficient **Hybrid RAG (Retrieval-Augmented Generation)** pipeline. Instead of sending all data to the LLM, the system performs a pre-filter using mathematical distance checks.


### App Preview
<img width="1920" height="1080" alt="Screenshot 2025-12-28 114756" src="https://github.com/user-attachments/assets/c77e91f2-be73-4a5b-80a1-a54bd73f7707" />

<img width="1920" height="1080" alt="Screenshot 2025-12-28 114756" src="https://github.com/user-attachments/assets/68124063-837b-4e76-a5fc-a4d932f172b4" />


---

## Tech Stack & Architecture
* **LLM:** Gemini 2.5 Flash (via LangChain)
* **Frontend:** Streamlit
* **Geospatial:** Pgeocode (India dataset)
* **Data Generation:** Python Faker (Localized `en_IN` profiles)

### Project Structure
```text
stapubox-match-agent/
├── data/               # Synthetic player database (200+ profiles)
├── scripts/            # Data generation and utility scripts
├── src/                # Core AI logic and geospatial engine
└── app.py              # Streamlit UI & Session state management
```
---

## ⚙️ Local Setup

Follow these steps to get the StapuBox AI Matchmaker running on your local machine:

1. **Clone the Repository:**
   ```bash
   git clone [https://github.com/Pradeep18102003/Stapubox_Match_Agent.git](https://github.com/Pradeep18102003/Stapubox_Match_Agent.git)
   cd Stapubox_Match_Agent
   ```
2. **Create a Virtual Environment:**
   ```bash
   python -m venv venv
   # Activate on Windows:
   .\venv\Scripts\activate
   # Activate on Mac/Linux:
   source venv/bin/activate
   ```
3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Configure Your API Key:**
   Create a directory named `.streamlit` in the root folder and add a `secrets.toml` file inside it and add your Google Gemini API key inside that file
5. **Generate Synthetic Data:**
   Run the data generation script to create your local database of 200 players
   ```bash
   python scripts/gen_data.py
   ```
6. **Launch the application**

### Contact me
- Name: Pradeep Kumar S
- Email: pradeep18kumar10@gmail.com
- LinkedIn: [Pradeep Kumar](https://www.linkedin.com/in/pradeep-kumar-bba090320/)
- Github: [Pradeep18102003](https://github.com/Pradeep18102003)
   
   
