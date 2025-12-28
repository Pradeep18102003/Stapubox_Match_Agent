import json
import pgeocode
import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate

dist_calc = pgeocode.GeoDistance('IN')

def get_distance(p1, p2):
    d = dist_calc.query_postal_code(p1, p2)
    return round(d, 2) if d is not None else 999

def find_match(user_query, user_pincode):
    with open("data/players.json", "r") as f:
        all_players = json.load(f)
    
    nearby_players = []
    for p in all_players:
        distance = get_distance(user_pincode, p['pincode'])
        if distance <= 10.0:
            p['distance_km'] = distance
            nearby_players.append(p)
            
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash", 
        google_api_key=st.secrets["GOOGLE_API_KEY"],
        temperature=0.5
    )
    
    prompt = ChatPromptTemplate.from_template("""
    You are the StapuBox AI Sports Concierge. 
    User Query: {query}
    User Pincode: {pincode}
    
    Filtered Players (within 10km): {data}
    
    Instructions:
    - Pick the best 1-2 matches based on sport and skill level.
    - If no exact sport matches, suggest the closest active player and explain why.
    - Keep the tone energetic and professional.
    """)
    
    chain = prompt | llm
    response = chain.invoke({
        "query": user_query, 
        "pincode": user_pincode, 
        "data": json.dumps(nearby_players[:5]) 
    })
    
    return response.content