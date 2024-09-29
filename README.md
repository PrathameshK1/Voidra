# Voidra
Your own locally hosted and private Pocket Hedge Fund (HFT) Quant analyst 


# Financial Market Analysis and Investment Management System

## Overview

Voidra implements an advanced investment management system using three specialized AI agents. These agents work collaboratively to identify investment opportunities, develop strategies, and manage risks in the financial markets.

## Agents

1. **Research Analyst Agent**
2. **Portfolio Manager Agent**
3. **Risk Manager Agent**

## Agent Details and Workflow

### 1. Research Analyst Agent

- **Role**: Research Analyst
- **Goal**:
  - Conduct in-depth fundamental and technical research on markets, companies, and asset classes.
  - Utilize financial models, industry reports, and market trends to identify potential investment opportunities.
  - Generate detailed research reports including valuation metrics, growth prospects, and risk factors.
- **Workflow**:
  - Identifies potential investment opportunities through comprehensive market research.
  - Generates detailed research reports with asset valuations, market trends, risk factors, and growth prospects.
  - Passes the research report to the Portfolio Manager Agent for further analysis.

### 2. Portfolio Manager Agent

- **Role**: Portfolio Manager
- **Goal**:
  - Develop and implement investment strategies based on research provided by the Research Analyst.
  - Assess market conditions, valuation, expected returns, and overall risk appetite.
  - Make decisions on capital allocation and trade execution.
- **Workflow**:
  - Reviews research reports from the Research Analyst Agent.
  - Develops investment strategies based on the fund's goals and market conditions.
  - Determines capital allocation and trade types (e.g., long/short, derivatives, options).
  - Sends proposed trades to the Risk Manager Agent for approval before execution.

### 3. Risk Manager Agent

- **Role**: Risk Manager
- **Goal**:
  - Evaluate risks of proposed trades by analyzing portfolio exposure and conducting stress tests.
  - Ensure the fund stays within defined risk limits.
  - Monitor ongoing risks after trade execution.
- **Workflow**:
  - Performs detailed risk assessments on proposed trades.
  - Uses stress testing and scenario analysis to evaluate trade impact on the portfolio.
  - Approves trades within acceptable risk limits or suggests modifications.
  - Continues to monitor portfolio exposure and performance post-trade.

## System Workflow

1. **Idea Generation**: Research Analyst Agent identifies investment opportunities and creates detailed reports.
2. **Strategy Development**: Portfolio Manager Agent reviews research and develops investment strategies.
3. **Risk Assessment**: Risk Manager Agent evaluates proposed trades and provides risk clearance or suggests adjustments.
4. **Trade Execution**: Portfolio Manager Agent executes approved trades in the market.
5. **Post-Trade Monitoring**: Risk Manager Agent monitors portfolio performance and risk levels continuously.
6. **Feedback Loop**: All agents collaborate to refine strategies based on new data and trade outcomes.

This workflow ensures a comprehensive approach to investment management, balancing profit maximization with robust risk management throughout the trading lifecycle.

it generates a report after complettion and gives you the option to create a translated version of it in 243 different languages for catering to geopgrahical specific needs 

## How to Run the Project

### Requirements

- [X] Python 3.8+
- [X] Dependencies listed in `requirements.txt`
- [X] SERPER_API_KEY in the .env file

### Installation

1. Clone the repository:

   ```
   git clone https://github.com/brprado/CrewAI-Investiment-Risk.git
   cd CrewAI-Investiment-Risk
   ```

2. Install requirements:

   ```
   pip install -r requirements.txt
   ```

3. Run the project:

   ```python
   python crew.py
   ```

This will initiate the AI-driven investment management process, leveraging the collaborative efforts of the Research Analyst, Portfolio Manager, and Risk Manager agents.
