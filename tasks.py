from crewai import Task
from agents import (
    research_analyst_agent,
    portfolio_manager_agent,
    risk_manager_agent,
)

research_task = Task(
    description="""
    Conduct comprehensive research on the company {empresa}. This includes:
    - Analyzing historical stock prices, trading volumes, and other relevant financial indicators.
    - Examining industry reports, market trends, and competitive landscape.
    - Evaluating the company's financial statements, growth prospects, and potential risks.
    - Considering any recent news or developments that might impact the company's valuation.
    Provide a detailed research report with your findings and analysis.
    """,
    expected_output="""
    A comprehensive research report on {empresa} including:
    - Historical financial data analysis
    - Industry positioning and market trends
    - Company valuation metrics
    - Growth prospects and potential risks
    - Recent news impact assessment
    """,
    agent=research_analyst_agent,
)

portfolio_management_task = Task(
    description="""
    Based on the research report provided for {empresa}, develop an investment strategy. Your task includes:
    - Assessing the current market conditions and how they relate to {empresa}.
    - Evaluating the potential returns and risks associated with investing in {empresa}.
    - Determining the appropriate capital allocation for {empresa} within the portfolio.
    - Proposing specific trade execution plans (e.g., long/short positions, options strategies).
    - Considering both short-term and long-term investment goals.
    Prepare a detailed investment strategy proposal.
    """,
    expected_output="""
    An investment strategy proposal for {empresa} including:
    - Market condition assessment
    - Return potential and risk analysis
    - Recommended capital allocation
    - Specific trade execution plans
    - Alignment with short-term and long-term goals
    """,
    agent=portfolio_manager_agent,
)

risk_assessment_task = Task(
    description="""
    Evaluate the risks associated with the proposed investment in {empresa}. Your assessment should include:
    - Analyzing the portfolio exposure if the proposed trade is executed.
    - Conducting stress tests and scenario analyses to evaluate potential impacts.
    - Assessing how the trade aligns with current risk limits and overall risk appetite.
    - Identifying any macroeconomic or company-specific risks that could affect the investment.
    - Providing recommendations on risk mitigation strategies if necessary.
    Prepare a comprehensive risk assessment report.
    """,
    expected_output="""
    A comprehensive risk assessment report for investing in {empresa} including:
    - Portfolio exposure analysis
    - Stress test and scenario analysis results
    - Alignment with risk limits and appetite
    - Identified macro and micro risks
    - Risk mitigation recommendations
    - Final risk-adjusted investment recommendation (Buy or Don't Buy)
    """,
    agent=risk_manager_agent,
    output_file="investment_risk_analysis.md",
)
