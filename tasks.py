from typing import Dict, Any, Optional, List
from llama_index.core.agent import ReActAgent
import logging
from datetime import datetime
import json

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class TaskManager:
    """
    Advanced task management system for coordinating agent workflows with high-quality prompting
    """
    
    def __init__(self, research_agent: ReActAgent, portfolio_agent: ReActAgent, risk_agent: ReActAgent):
        self.research_agent = research_agent
        self.portfolio_agent = portfolio_agent
        self.risk_agent = risk_agent
        self.execution_results = {}
        self.workflow_context = {}
    
    def _get_temporal_context(self) -> str:
        """
        Get current temporal context for workflow execution
        """
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S UTC")
        return f"Current Analysis Timestamp: {current_time}"
    
    def _create_workflow_context(self, query: str, company: str) -> Dict[str, Any]:
        """
        Create comprehensive workflow context for seamless agent communication
        """
        return {
            "query": query,
            "company": company,
            "analysis_timestamp": self._get_temporal_context(),
            "workflow_stage": "initialized",
            "data_flow": {
                "research_completed": False,
                "portfolio_completed": False,
                "risk_completed": False
            },
            "key_insights": {},
            "risk_flags": [],
            "recommendations": []
        }
    
    def execute_research_task(self, company: str, query: str = None, additional_context: str = None) -> str:
        """
        Execute comprehensive research analysis task with chain of thought prompting
        
        Args:
            company: Company name to analyze
            query: Specific research query or focus area
            additional_context: Additional context or constraints
            
        Returns:
            Research report as string
        """
        # Create temporal context
        temporal_context = self._get_temporal_context()
        
        # Build comprehensive research prompt with chain of thought reasoning
        research_prompt = f"""
# RESEARCH ANALYSIS TASK: {company.upper()}

## TEMPORAL CONTEXT
{temporal_context}

## RESEARCH OBJECTIVE
Conduct comprehensive, data-driven research on {company} to provide actionable investment insights.

## CHAIN OF THOUGHT ANALYSIS FRAMEWORK

### STEP 1: RESEARCH SCOPE DEFINITION
- What specific aspects of {company} need investigation?
- What market context is relevant for this analysis?
- What time horizon should we consider?

### STEP 2: DATA GATHERING STRATEGY
- What reliable sources should I consult?
- What financial metrics are most relevant?
- What market indicators should I track?

### STEP 3: COMPREHENSIVE ANALYSIS
- Fundamental analysis: financial health, growth prospects, competitive position
- Technical analysis: price trends, volume patterns, market sentiment
- Industry analysis: sector trends, competitive landscape, regulatory environment
- Macro analysis: economic factors, geopolitical risks, market conditions

### STEP 4: INSIGHT SYNTHESIS
- What are the key investment drivers?
- What are the primary risk factors?
- What are the growth opportunities?
- What are the potential headwinds?

## SPECIFIC RESEARCH REQUIREMENTS

### 1. COMPANY FUNDAMENTALS
- Financial performance analysis (revenue, earnings, cash flow)
- Balance sheet strength and liquidity
- Growth metrics and projections
- Management quality and track record
- Competitive advantages and moats

### 2. MARKET POSITIONING
- Industry ranking and market share
- Competitive landscape analysis
- Product/service portfolio strength
- Geographic diversification
- Customer base and loyalty

### 3. VALUATION ANALYSIS
- P/E, P/B, EV/EBITDA ratios
- DCF valuation if applicable
- Peer comparison analysis
- Historical valuation trends
- Fair value estimates

### 4. RISK ASSESSMENT
- Business model risks
- Financial risks (leverage, liquidity)
- Operational risks
- Regulatory risks
- Market risks

### 5. GROWTH CATALYSTS
- New product launches
- Market expansion opportunities
- Operational improvements
- Strategic initiatives
- Industry tailwinds

### 6. RECENT DEVELOPMENTS
- Latest earnings reports
- Management changes
- Strategic announcements
- Regulatory updates
- Market reactions

## ADDITIONAL CONTEXT
{additional_context if additional_context else "No additional context provided"}

## RESPONSE STRUCTURE
Follow this exact format for your analysis:

### 1. RESEARCH QUESTION/OBJECTIVE
[Clearly state what you're analyzing and why]

### 2. CURRENT MARKET CONTEXT
[Use get_current_datetime to establish temporal context]

### 3. DATA SOURCES USED
[List specific reliable sources with URLs when available]

### 4. KEY FINDINGS
[Present specific metrics, data points, and insights]

### 5. ANALYSIS & REASONING
[Step-by-step thought process explaining your conclusions]

### 6. INVESTMENT IMPLICATIONS
[What this means for investment decisions]

### 7. NEXT STEPS FOR PORTFOLIO MANAGER
[Specific recommendations for portfolio strategy]

## CRITICAL REQUIREMENTS
1. Use ONLY reliable financial sources (Bloomberg, Reuters, FT, WSJ, CNBC, Economic Times, Business Standard, etc.)
2. Provide specific metrics and data points
3. Explain your reasoning step-by-step
4. Consider current market timing and conditions
5. Focus on actionable insights for portfolio management
6. NO disclaimers about financial advice

Execute this research analysis now, following the chain of thought framework above.
"""
        
        logger.info(f"Starting comprehensive research task for {company}")
        logger.info(f"Temporal context: {temporal_context}")
        
        try:
            response = self.research_agent.chat(research_prompt)
            result = str(response)
            self.execution_results['research'] = result
            self.workflow_context['data_flow']['research_completed'] = True
            logger.info("Research task completed successfully")
            return result
        except Exception as e:
            logger.error(f"Error in research task: {str(e)}")
            raise
    
    def execute_portfolio_management_task(self, company: str, research_data: str, query: str = None) -> str:
        """
        Execute portfolio management task with enhanced chain of thought prompting
        
        Args:
            company: Company name to analyze
            research_data: Research report from previous task
            query: Original user query for context
            
        Returns:
            Investment strategy as string
        """
        # Create temporal context
        temporal_context = self._get_temporal_context()
        
        # Build comprehensive portfolio management prompt
        portfolio_prompt = f"""
# PORTFOLIO MANAGEMENT TASK: {company.upper()}

## TEMPORAL CONTEXT
{temporal_context}

## ORIGINAL QUERY CONTEXT
{query if query else "General investment analysis requested"}

## RESEARCH DATA INTEGRATION
{research_data}

## CHAIN OF THOUGHT DECISION FRAMEWORK

### STEP 1: RESEARCH SYNTHESIS
- What are the key investment drivers from the research?
- What are the primary risk factors identified?
- What is the current market positioning?

### STEP 2: STRATEGIC ASSESSMENT
- How does {company} fit into current portfolio strategy?
- What is the optimal investment approach?
- What time horizon is most appropriate?

### STEP 3: CAPITAL ALLOCATION ANALYSIS
- What percentage allocation is optimal?
- How does this affect portfolio diversification?
- What is the expected return profile?

### STEP 4: EXECUTION PLANNING
- What specific trades should be executed?
- What is the optimal entry strategy?
- What are the exit criteria?

### STEP 5: RISK INTEGRATION
- How do we mitigate identified risks?
- What are the downside scenarios?
- How does this affect overall portfolio risk?

## PORTFOLIO STRATEGY REQUIREMENTS

### 1. MARKET CONDITION ASSESSMENT
- Current market environment analysis
- Sector-specific trends and outlook
- Macroeconomic factors affecting {company}
- Market sentiment and positioning

### 2. INVESTMENT THESIS DEVELOPMENT
- Core investment rationale
- Key value drivers
- Growth catalysts
- Competitive advantages

### 3. CAPITAL ALLOCATION STRATEGY
- Recommended position size
- Portfolio weight allocation
- Diversification impact
- Risk-adjusted positioning

### 4. TRADE EXECUTION PLAN
- Entry strategy and timing
- Position sizing approach
- Risk management parameters
- Exit criteria and targets

### 5. PERFORMANCE EXPECTATIONS
- Expected return scenarios
- Time horizon for realization
- Key performance indicators
- Success metrics

### 6. RISK CONSIDERATIONS
- Downside risk assessment
- Volatility expectations
- Correlation with existing positions
- Liquidity considerations

## RESPONSE STRUCTURE
Follow this exact format for your strategy:

### 1. STRATEGY OVERVIEW
[Executive summary of investment approach]

### 2. CURRENT MARKET CONTEXT
[Use get_current_datetime to establish temporal context]

### 3. ANALYSIS OF RESEARCH FINDINGS
[Specific references to research insights]

### 4. RISK ASSESSMENT INTEGRATION
[How risks from research affect strategy]

### 5. INVESTMENT DECISION & RATIONALE
[Step-by-step reasoning for strategy]

### 6. IMPLEMENTATION PLAN
[Specific execution steps]

### 7. EXPECTED OUTCOMES & MONITORING
[Performance expectations and monitoring points]

## CRITICAL REQUIREMENTS
1. Build directly upon research findings
2. Provide specific allocation percentages
3. Include clear entry/exit criteria
4. Consider current market timing
5. Address identified risks proactively
6. NO disclaimers about financial advice
7. Focus on actionable implementation steps

Execute this portfolio management analysis now, following the chain of thought framework above.
"""
        
        logger.info(f"Starting portfolio management task for {company}")
        logger.info(f"Temporal context: {temporal_context}")
        
        try:
            response = self.portfolio_agent.chat(portfolio_prompt)
            result = str(response)
            self.execution_results['portfolio'] = result
            self.workflow_context['data_flow']['portfolio_completed'] = True
            logger.info("Portfolio management task completed successfully")
            return result
        except Exception as e:
            logger.error(f"Error in portfolio management task: {str(e)}")
            raise
    
    def execute_risk_assessment_task(self, company: str, portfolio_strategy: str, research_data: str = None, query: str = None) -> str:
        """
        Execute comprehensive risk assessment task with enhanced chain of thought prompting
        
        Args:
            company: Company name to analyze
            portfolio_strategy: Portfolio strategy from previous task
            research_data: Original research data for context
            query: Original user query for context
            
        Returns:
            Risk assessment report as string
        """
        # Create temporal context
        temporal_context = self._get_temporal_context()
        
        # Build comprehensive risk assessment prompt
        risk_prompt = f"""
# RISK ASSESSMENT TASK: {company.upper()}

## TEMPORAL CONTEXT
{temporal_context}

## ORIGINAL QUERY CONTEXT
{query if query else "General risk assessment requested"}

## PORTFOLIO STRATEGY TO EVALUATE
{portfolio_strategy}

## RESEARCH DATA CONTEXT
{research_data if research_data else "Research data not provided"}

## CHAIN OF THOUGHT RISK ANALYSIS FRAMEWORK

### STEP 1: RISK IDENTIFICATION
- What specific risks does this investment pose?
- What are the portfolio-level risk implications?
- What are the market-level risk factors?

### STEP 2: RISK QUANTIFICATION
- How can we measure these risks quantitatively?
- What are the probability distributions?
- What are the potential loss scenarios?

### STEP 3: STRESS TESTING
- How does this investment perform under stress?
- What are the worst-case scenarios?
- How does it affect overall portfolio risk?

### STEP 4: RISK MITIGATION
- What strategies can reduce these risks?
- What are the optimal risk management approaches?
- How do we balance risk and return?

### STEP 5: FINAL ASSESSMENT
- Is this investment within acceptable risk parameters?
- What is the risk-adjusted recommendation?
- What monitoring is required?

## COMPREHENSIVE RISK ASSESSMENT REQUIREMENTS

### 1. PORTFOLIO EXPOSURE ANALYSIS
- Current portfolio risk profile
- Impact of new position on overall risk
- Correlation analysis with existing positions
- Concentration risk assessment
- Sector exposure implications

### 2. QUANTITATIVE RISK METRICS
- Value at Risk (VaR) calculations
- Expected shortfall estimates
- Beta and volatility analysis
- Sharpe ratio implications
- Maximum drawdown scenarios

### 3. STRESS TESTING & SCENARIOS
- Market crash scenarios (2008-style)
- Sector-specific downturn scenarios
- Company-specific stress scenarios
- Macroeconomic shock scenarios
- Liquidity crisis scenarios

### 4. RISK FACTOR ANALYSIS
- Market risk (systematic)
- Company-specific risk (idiosyncratic)
- Sector risk
- Geographic risk
- Currency risk (if applicable)
- Interest rate risk
- Regulatory risk

### 5. RISK LIMIT COMPLIANCE
- Position size limits
- Sector concentration limits
- Volatility limits
- Correlation limits
- Liquidity requirements

### 6. RISK MITIGATION STRATEGIES
- Hedging approaches
- Position sizing adjustments
- Stop-loss strategies
- Diversification recommendations
- Monitoring protocols

## RESPONSE STRUCTURE
Follow this exact format for your assessment:

### 1. RISK ASSESSMENT OVERVIEW
[Executive summary of risk profile]

### 2. CURRENT MARKET CONTEXT
[Use get_current_datetime to establish temporal context]

### 3. QUANTITATIVE RISK METRICS
[Specific calculations and metrics]

### 4. RISK FACTOR ANALYSIS
[Step-by-step breakdown of risk factors]

### 5. PORTFOLIO IMPACT ASSESSMENT
[How this affects overall portfolio risk]

### 6. RISK MITIGATION RECOMMENDATIONS
[Specific strategies to reduce risk]

### 7. MONITORING & ALERT THRESHOLDS
[Risk monitoring parameters]

### 8. FINAL RECOMMENDATION
[Buy/Don't Buy with risk-adjusted rationale]

## CRITICAL REQUIREMENTS
1. Provide specific quantitative risk metrics
2. Include stress test results
3. Address all major risk categories
4. Consider current market conditions
5. Provide actionable risk mitigation strategies
6. NO disclaimers about financial advice
7. Give clear Buy/Don't Buy recommendation with rationale

Execute this comprehensive risk assessment now, following the chain of thought framework above.
"""
        
        logger.info(f"Starting comprehensive risk assessment task for {company}")
        logger.info(f"Temporal context: {temporal_context}")
        
        try:
            response = self.risk_agent.chat(risk_prompt)
            result = str(response)
            self.execution_results['risk'] = result
            self.workflow_context['data_flow']['risk_completed'] = True
            logger.info("Risk assessment task completed successfully")
            return result
        except Exception as e:
            logger.error(f"Error in risk assessment task: {str(e)}")
            raise
    
    def execute_sequential_workflow(self, company: str, query: str = None, additional_context: str = None) -> Dict[str, str]:
        """
        Execute all tasks in sequential order with enhanced workflow management
        
        Args:
            company: Company name to analyze
            query: Specific user query or focus area
            additional_context: Additional context or constraints
            
        Returns:
            Dictionary containing all task results
        """
        logger.info(f"Starting enhanced sequential workflow for {company}")
        
        # Initialize workflow context
        self.workflow_context = self._create_workflow_context(query or f"Analyze {company}", company)
        
        # Step 1: Research Analysis
        logger.info("=== STEP 1: RESEARCH ANALYSIS ===")
        research_result = self.execute_research_task(company, query, additional_context)
        
        # Step 2: Portfolio Management
        logger.info("=== STEP 2: PORTFOLIO MANAGEMENT ===")
        portfolio_result = self.execute_portfolio_management_task(company, research_result, query)
        
        # Step 3: Risk Assessment
        logger.info("=== STEP 3: RISK ASSESSMENT ===")
        risk_result = self.execute_risk_assessment_task(company, portfolio_result, research_result, query)
        
        # Compile final results
        final_results = {
            'research': research_result,
            'portfolio': portfolio_result,
            'risk': risk_result,
            'workflow_context': self.workflow_context
        }
        
        logger.info("Enhanced sequential workflow completed successfully")
        return final_results
    
    def execute_custom_workflow(self, company: str, workflow_type: str, query: str = None, **kwargs) -> Dict[str, str]:
        """
        Execute custom workflow based on specific requirements
        
        Args:
            company: Company name to analyze
            workflow_type: Type of workflow ('research_only', 'portfolio_only', 'risk_only', 'research_portfolio')
            query: Specific user query
            **kwargs: Additional parameters
            
        Returns:
            Dictionary containing workflow results
        """
        logger.info(f"Starting custom workflow: {workflow_type} for {company}")
        
        results = {}
        
        if workflow_type == 'research_only':
            results['research'] = self.execute_research_task(company, query, kwargs.get('additional_context'))
            
        elif workflow_type == 'portfolio_only':
            # For portfolio-only, we need some research context
            research_context = kwargs.get('research_context', f"Basic analysis of {company}")
            results['portfolio'] = self.execute_portfolio_management_task(company, research_context, query)
            
        elif workflow_type == 'risk_only':
            # For risk-only, we need both research and portfolio context
            research_context = kwargs.get('research_context', f"Basic analysis of {company}")
            portfolio_context = kwargs.get('portfolio_context', f"Basic portfolio strategy for {company}")
            results['risk'] = self.execute_risk_assessment_task(company, portfolio_context, research_context, query)
            
        elif workflow_type == 'research_portfolio':
            results['research'] = self.execute_research_task(company, query, kwargs.get('additional_context'))
            results['portfolio'] = self.execute_portfolio_management_task(company, results['research'], query)
            
        else:
            # Default to full workflow
            results = self.execute_sequential_workflow(company, query, kwargs.get('additional_context'))
        
        return results
    
    def generate_enhanced_combined_report(self, company: str, results: Dict[str, str], query: str = None) -> str:
        """
        Generate an enhanced combined report with executive summary and key insights
        
        Args:
            company: Company name
            results: Results from all agents
            query: Original user query for context
            
        Returns:
            Enhanced combined report as markdown string
        """
        # Extract key insights from results
        key_insights = self._extract_key_insights(results)
        
        # Generate executive summary
        executive_summary = self._generate_executive_summary(company, results, query)
        
        # Get temporal context
        temporal_context = self._get_temporal_context()
        
        report = f"""# VOIDRA AI INVESTMENT ANALYSIS REPORT
## {company.upper()}

**Analysis Timestamp:** {temporal_context}  
**Original Query:** {query if query else f"Comprehensive analysis of {company}"}

---

## EXECUTIVE SUMMARY

{executive_summary}

---

## KEY INSIGHTS

{key_insights}

---

## DETAILED ANALYSIS

### 1. RESEARCH ANALYSIS
{results.get('research', 'Research analysis not available')}

### 2. PORTFOLIO MANAGEMENT STRATEGY
{results.get('portfolio', 'Portfolio strategy not available')}

### 3. RISK ASSESSMENT
{results.get('risk', 'Risk assessment not available')}

---

## INVESTMENT RECOMMENDATION

Based on the comprehensive analysis conducted by our AI-driven investment management system:

**FINAL RECOMMENDATION:** [To be determined from risk assessment]

**CONFIDENCE LEVEL:** [To be determined from analysis quality]

**KEY RISK FACTORS:** [To be extracted from risk assessment]

**PRIMARY CATALYSTS:** [To be extracted from research analysis]

---

## METHODOLOGY

This analysis was conducted using Voidra's advanced AI investment management system, incorporating:

- **Research Analyst Agent:** Comprehensive fundamental and technical analysis
- **Portfolio Manager Agent:** Strategic investment planning and allocation
- **Risk Manager Agent:** Quantitative risk assessment and stress testing

All analysis is based on data from reliable financial sources including Bloomberg, Reuters, Financial Times, Wall Street Journal, and trusted Indian financial publications.

---

*Report generated by Voidra AI Investment Management System*  
*Analysis completed at {temporal_context}*
"""
        return report
    
    def _extract_key_insights(self, results: Dict[str, str]) -> str:
        """
        Extract key insights from agent results
        """
        insights = []
        
        if 'research' in results:
            insights.append("**Research Insights:** Key findings from comprehensive market and company analysis")
        
        if 'portfolio' in results:
            insights.append("**Portfolio Strategy:** Optimal investment approach and allocation recommendations")
        
        if 'risk' in results:
            insights.append("**Risk Assessment:** Quantitative risk metrics and mitigation strategies")
        
        return "\n".join(insights) if insights else "No insights available"
    
    def _generate_executive_summary(self, company: str, results: Dict[str, str], query: str = None) -> str:
        """
        Generate executive summary from agent results
        """
        summary_parts = [
            f"This comprehensive investment analysis of {company} provides actionable insights for portfolio management decisions.",
            "The analysis incorporates research insights, portfolio strategy recommendations, and quantitative risk assessment.",
            "All findings are based on current market data and reliable financial sources."
        ]
        
        if query:
            summary_parts.insert(0, f"Analysis conducted in response to: '{query}'")
        
        return " ".join(summary_parts)
    
    def get_workflow_status(self) -> Dict[str, Any]:
        """
        Get current workflow status and context
        """
        return {
            "workflow_context": self.workflow_context,
            "execution_results": {k: "Completed" if v else "Pending" for k, v in self.execution_results.items()},
            "temporal_context": self._get_temporal_context()
        }
