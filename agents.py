from llama_index.core.agent import ReActAgent
from llama_index.core.tools import FunctionTool
from llama_index.llms.gemini import Gemini
from llama_index.core.settings import Settings
from llama_index.core.memory import ChatMemoryBuffer
from dotenv import load_dotenv
import os
import requests
import json
from typing import Dict, Any, List
from datetime import datetime, timezone
import pytz

load_dotenv()

# Configure Gemini 2.0 as the default LLM
Settings.llm = Gemini(
    model="models/gemini-2.0-flash-lite",
    api_key=os.getenv("GOOGLE_API_KEY"),
    temperature=0.1,
    max_tokens=4096
)

# Current date and time tool
def get_current_datetime() -> str:
    """
    Get the current date and time in multiple timezones for financial markets.
    
    Returns:
        JSON string containing current datetime information
    """
    # Get current UTC time
    utc_now = datetime.now(timezone.utc)
    
    # Define major financial market timezones
    timezones = {
        "UTC": timezone.utc,
        "EST": pytz.timezone("America/New_York"),  # US Eastern Time
        "PST": pytz.timezone("America/Los_Angeles"),  # US Pacific Time
        "IST": pytz.timezone("Asia/Kolkata"),  # Indian Standard Time
        "GMT": pytz.timezone("Europe/London"),  # London Time
        "JST": pytz.timezone("Asia/Tokyo"),  # Japan Standard Time
        "HKT": pytz.timezone("Asia/Hong_Kong"),  # Hong Kong Time
        "SGT": pytz.timezone("Asia/Singapore"),  # Singapore Time
    }
    
    datetime_info = {
        "current_datetime": {
            "utc": utc_now.strftime("%Y-%m-%d %H:%M:%S UTC"),
            "formatted": utc_now.strftime("%A, %B %d, %Y at %I:%M:%S %p UTC"),
            "timestamp": utc_now.timestamp(),
            "date": utc_now.strftime("%Y-%m-%d"),
            "time": utc_now.strftime("%H:%M:%S")
        },
        "market_times": {}
    }
    
    # Get times in different market timezones
    for market, tz in timezones.items():
        market_time = utc_now.astimezone(tz)
        datetime_info["market_times"][market] = {
            "datetime": market_time.strftime("%Y-%m-%d %H:%M:%S"),
            "formatted": market_time.strftime("%A, %B %d, %Y at %I:%M:%S %p"),
            "timezone": str(tz),
            "is_market_open": _is_market_open(market_time, market)
        }
    
    # Add market session information
    datetime_info["market_sessions"] = _get_market_sessions(utc_now)
    
    return json.dumps(datetime_info, indent=2)

def _is_market_open(market_time: datetime, market: str) -> bool:
    """
    Determine if a specific market is currently open based on time.
    """
    weekday = market_time.weekday()  # Monday = 0, Sunday = 6
    hour = market_time.hour
    
    # Weekend check
    if weekday >= 5:  # Saturday or Sunday
        return False
    
    # Market-specific hours (simplified)
    market_hours = {
        "EST": (9, 16),  # 9 AM - 4 PM EST
        "PST": (6, 13),  # 6 AM - 1 PM PST
        "IST": (9, 16),  # 9 AM - 4 PM IST
        "GMT": (8, 16),  # 8 AM - 4 PM GMT
        "JST": (9, 15),  # 9 AM - 3 PM JST
        "HKT": (9, 16),  # 9 AM - 4 PM HKT
        "SGT": (9, 17),  # 9 AM - 5 PM SGT
    }
    
    if market in market_hours:
        start_hour, end_hour = market_hours[market]
        return start_hour <= hour < end_hour
    
    return True  # Default to open for other timezones

def _get_market_sessions(utc_now: datetime) -> Dict[str, Any]:
    """
    Get information about current and upcoming market sessions.
    """
    sessions = {
        "current_session": None,
        "upcoming_sessions": [],
        "recent_sessions": []
    }
    
    # Major market sessions (simplified)
    market_sessions = [
        {"name": "US Markets", "timezone": "EST", "hours": (9, 16)},
        {"name": "European Markets", "timezone": "GMT", "hours": (8, 16)},
        {"name": "Indian Markets", "timezone": "IST", "hours": (9, 16)},
        {"name": "Asian Markets", "timezone": "JST", "hours": (9, 15)},
    ]
    
    for session in market_sessions:
        tz = pytz.timezone("America/New_York" if session["timezone"] == "EST" else 
                          "Europe/London" if session["timezone"] == "GMT" else
                          "Asia/Kolkata" if session["timezone"] == "IST" else
                          "Asia/Tokyo")
        
        session_time = utc_now.astimezone(tz)
        start_hour, end_hour = session["hours"]
        
        if start_hour <= session_time.hour < end_hour and session_time.weekday() < 5:
            sessions["current_session"] = {
                "name": session["name"],
                "timezone": session["timezone"],
                "start_time": f"{start_hour:02d}:00",
                "end_time": f"{end_hour:02d}:00",
                "current_time": session_time.strftime("%H:%M:%S")
            }
    
    return sessions

# Web search tool using Serper API with reliable source filtering
def web_search(query: str) -> str:
    """
    Search the web for information using Serper API, prioritizing reliable financial sources.
    
    Args:
        query: The search query string
        
    Returns:
        JSON string containing search results from trusted sources
    """
    serper_api_key = os.getenv("SERPER_API_KEY")
    if not serper_api_key:
        return "Error: SERPER_API_KEY not found in environment variables"
    
    # Add reliable source keywords to query
    reliable_sources = [
        "Bloomberg", "Reuters", "Financial Times", "Wall Street Journal", 
        "CNBC", "MarketWatch", "Yahoo Finance", "Seeking Alpha",
        "Economic Times", "Business Standard", "Moneycontrol", "Livemint",
        "NDTV Profit", "CNBC TV18", "Business Today"
    ]
    
    # Enhance query with reliable source keywords
    enhanced_query = f"{query} site:bloomberg.com OR site:reuters.com OR site:ft.com OR site:wsj.com OR site:cnbc.com OR site:marketwatch.com OR site:finance.yahoo.com OR site:seekingalpha.com OR site:economictimes.indiatimes.com OR site:business-standard.com OR site:moneycontrol.com OR site:livemint.com OR site:ndtv.com OR site:cnbctv18.com OR site:businesstoday.in"
    
    url = "https://google.serper.dev/search"
    headers = {
        'X-API-KEY': serper_api_key,
        'Content-Type': 'application/json'
    }
    
    payload = {
        'q': enhanced_query,
        'num': 15
    }
    
    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return json.dumps(response.json(), indent=2)
    except requests.exceptions.RequestException as e:
        return f"Error performing web search: {str(e)}"

# Create function tools
datetime_tool = FunctionTool.from_defaults(
    fn=get_current_datetime,
    name="get_current_datetime",
    description="Get the current date and time in multiple timezones, including major financial market times and session information"
)

search_tool = FunctionTool.from_defaults(
    fn=web_search,
    name="web_search",
    description="Search the web for current information from reliable financial sources including Bloomberg, Reuters, Financial Times, and trusted Indian financial publications"
)

# Research Analyst Agent with Chain of Thought prompting
research_analyst_agent = ReActAgent.from_tools(
    tools=[search_tool, datetime_tool],
    llm=Settings.llm,
    memory=ChatMemoryBuffer.from_defaults(token_limit=16000),
    system_prompt="""
You are a seasoned Research Analyst with a strong background in financial markets and data analysis. 
Your expertise lies in uncovering valuable insights from vast amounts of financial data and market information. 
You have a keen eye for spotting trends and identifying undervalued assets. 
Your analysis is crucial for informing the Portfolio Manager's investment decisions.

CRITICAL REQUIREMENTS:
1. ONLY source information from reliable financial sources including:
   - International: Bloomberg, Reuters, Financial Times, Wall Street Journal, CNBC, MarketWatch, Yahoo Finance, Seeking Alpha
   - Indian Markets: Economic Times, Business Standard, Moneycontrol, Livemint, NDTV Profit, CNBC TV18, Business Today
2. NEVER include disclaimers about financial advice in your analysis
3. Use Chain of Thought reasoning - always explain your analytical process step by step
4. Communicate seamlessly with Portfolio Manager and Risk Manager using clear, actionable language
5. ALWAYS check current date/time before conducting research to ensure you're working with the most recent information

ANALYTICAL PROCESS (Chain of Thought):
1. THINK: What specific information do I need to answer this research question?
2. TIMESTAMP: Use get_current_datetime to establish the current temporal context
3. SEARCH: Use web_search to gather data from reliable sources only, considering market hours and session timing
4. ANALYZE: Break down the information systematically:
   - What are the key facts and figures?
   - What trends or patterns emerge?
   - What are the underlying drivers?
   - How does this compare to historical data or benchmarks?
   - How recent is this information relative to current market conditions?
5. SYNTHESIZE: Combine insights into coherent analysis
6. RECOMMEND: Provide clear, actionable insights for the Portfolio Manager

Your role is to:
- Conduct in-depth fundamental and technical research on markets, companies, and asset classes
- Utilize financial models, industry reports, and market trends to identify potential investment opportunities
- Generate detailed research reports including valuation metrics, growth prospects, and risk factors
- Deliver comprehensive insights to the Portfolio Manager for strategy development

RESPONSE FORMAT:
Always structure your responses with clear sections:
1. Research Question/Objective
2. Current Market Context (date/time, market sessions)
3. Data Sources Used (with specific URLs when available)
4. Key Findings (with specific metrics and data points)
5. Analysis & Reasoning (step-by-step thought process)
6. Investment Implications
7. Next Steps for Portfolio Manager

Always provide thorough, data-driven analysis with specific metrics and concrete evidence to support your findings.
""",
    verbose=True,
    max_iterations=10
)

# Portfolio Manager Agent with Chain of Thought prompting
portfolio_manager_agent = ReActAgent.from_tools(
    tools=[datetime_tool],  # Portfolio manager needs datetime but not web search
    llm=Settings.llm,
    memory=ChatMemoryBuffer.from_defaults(token_limit=16000),
    system_prompt="""
As an experienced Portfolio Manager, you have a proven track record of successful investment strategies. 
Your strength lies in synthesizing complex market information and making decisive investment choices. 
You work closely with both the Research Analyst and Risk Manager to optimize the fund's performance while managing risk.

CRITICAL REQUIREMENTS:
1. NEVER include disclaimers about financial advice in your strategies
2. Use Chain of Thought reasoning - always explain your decision-making process step by step
3. Communicate seamlessly with Research Analyst and Risk Manager
4. Build upon the Research Analyst's findings and incorporate Risk Manager's assessments
5. ALWAYS check current date/time to ensure your strategies are relevant to current market conditions

DECISION-MAKING PROCESS (Chain of Thought):
1. THINK: What is the core investment opportunity or challenge?
2. TIMESTAMP: Use get_current_datetime to understand current market context and timing
3. ANALYZE: Review Research Analyst's findings systematically:
   - What are the key investment drivers?
   - What are the potential risks and rewards?
   - How does this fit with current portfolio positioning?
   - How does the current market timing affect this decision?
4. EVALUATE: Consider Risk Manager's input:
   - What risk factors need to be addressed?
   - How does this affect overall portfolio risk?
5. DECIDE: Make clear investment decisions with rationale
6. EXECUTE: Provide specific implementation steps

Your role is to:
- Develop and implement investment strategies based on research provided by the Research Analyst
- Assess market conditions, valuation, expected returns, and overall risk appetite
- Make decisions on capital allocation and trade execution
- Adjust strategies for both short-term and long-term goals
- Communicate with the Risk Manager to ensure risk factors are adequately considered before trade execution

RESPONSE FORMAT:
Always structure your responses with clear sections:
1. Strategy Overview
2. Current Market Context (date/time, market sessions)
3. Analysis of Research Findings (with specific references)
4. Risk Assessment Integration
5. Investment Decision & Rationale (step-by-step reasoning)
6. Implementation Plan
7. Expected Outcomes & Monitoring Points

Focus on creating actionable investment strategies with clear reasoning and specific allocation recommendations.
""",
    verbose=True,
    max_iterations=10
)

# Risk Manager Agent with Chain of Thought prompting
risk_manager_agent = ReActAgent.from_tools(
    tools=[datetime_tool],  # Risk manager needs datetime but not web search
    llm=Settings.llm,
    memory=ChatMemoryBuffer.from_defaults(token_limit=16000),
    system_prompt="""
You are a meticulous Risk Manager with a deep understanding of financial markets and risk assessment techniques. 
Your role is critical in safeguarding the fund's assets and ensuring compliance with risk management protocols. 
You work closely with the Portfolio Manager to balance risk and reward in all investment decisions.

CRITICAL REQUIREMENTS:
1. NEVER include disclaimers about financial advice in your assessments
2. Use Chain of Thought reasoning - always explain your risk analysis process step by step
3. Communicate seamlessly with Portfolio Manager and Research Analyst
4. Provide quantitative risk metrics whenever possible
5. ALWAYS check current date/time to assess risk in the context of current market conditions

RISK ASSESSMENT PROCESS (Chain of Thought):
1. THINK: What specific risks am I evaluating?
2. TIMESTAMP: Use get_current_datetime to understand current market timing and session context
3. ANALYZE: Break down risk factors systematically:
   - What are the market risks?
   - What are the company-specific risks?
   - What are the portfolio concentration risks?
   - What are the liquidity risks?
   - How do current market conditions affect these risks?
4. QUANTIFY: Assign specific risk metrics where possible:
   - VaR (Value at Risk) estimates
   - Beta calculations
   - Correlation analysis
   - Stress test scenarios
5. EVALUATE: Compare against risk limits and benchmarks
6. RECOMMEND: Provide clear risk mitigation strategies

Your role is to:
- Evaluate risks of proposed trades by analyzing portfolio exposure and conducting stress tests
- Ensure the fund stays within defined risk limits
- Monitor ongoing risks after trade execution
- Adjust risk limits based on market changes    
- Report potential issues to the Portfolio Manager that might require portfolio rebalancing or adjustments
- Minimize downside risks while maximizing potential returns

RESPONSE FORMAT:
Always structure your responses with clear sections:
1. Risk Assessment Overview
2. Current Market Context (date/time, market sessions)
3. Quantitative Risk Metrics (with specific calculations)
4. Risk Factor Analysis (step-by-step breakdown)
5. Portfolio Impact Assessment
6. Risk Mitigation Recommendations
7. Monitoring & Alert Thresholds

Provide detailed risk assessments with quantitative analysis and clear recommendations for risk mitigation.
""",
    verbose=True,
    max_iterations=10
)
