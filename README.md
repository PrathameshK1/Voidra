

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)


---

## 🎯 Overview

Voidra is an advanced AI-powered investment research platform that combines the expertise of specialized AI agents to deliver comprehensive, data-driven investment analysis. Built for quantitative analysts, portfolio managers, and investment professionals, Voidra provides institutional-grade research capabilities with the speed and accuracy of modern AI.

### Key Features

- Multi-Agent AI System: Three specialized AI agents working in concert
- Real-time Market Data**: Live financial data from trusted sources
- Chain of Thought Analysis: Systematic reasoning with step-by-step insights
- Flexible Workflows: Customizable analysis types for different needs
- Multi-language Support: Reports in 25+ languages
- Professional Reporting: Institutional-grade analysis reports

---

## 🏗️ Architecture

### AI Agent Ecosystem

Voidra operates through three specialized AI agents, each with distinct expertise:

#### 🔍 Research Analyst Agent
- **Purpose**: Comprehensive market and company research
- **Capabilities**:
  - Fundamental and technical analysis
  - Industry trend analysis
  - Competitive landscape assessment
  - Valuation metrics calculation
  - Growth catalyst identification
- **Data Sources**: Bloomberg, Reuters, Financial Times, WSJ, CNBC, Economic Times, Business Standard

#### 💼 Portfolio Manager Agent
- **Purpose**: Investment strategy development and capital allocation
- **Capabilities**:
  - Strategic investment planning
  - Capital allocation optimization
  - Trade execution planning
  - Performance expectation modeling
  - Risk-adjusted positioning

#### ⚠️ Risk Manager Agent
- **Purpose**: Quantitative risk assessment and stress testing
- **Capabilities**:
  - VaR (Value at Risk) calculations
  - Stress testing and scenario analysis
  - Portfolio impact assessment
  - Risk mitigation strategies
  - Buy/Don't Buy recommendations

### 🔄 Workflow Integration

```
User Query → Research Analysis → Portfolio Strategy → Risk Assessment → Final Report
     ↓              ↓                    ↓                    ↓              ↓
  Input         Market Data        Investment Plan      Risk Metrics    Actionable
Validation      & Insights         & Allocation         & Alerts        Insights
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- Google Gemini API key
- Serper API key (for web search)
- Internet connection for real-time data

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-org/voidra.git
   cd voidra
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your API keys
   ```

4. **Run the system**
   ```bash
   python crew.py
   ```



## 🎯 Use Cases

### For Quantitative Analysts
- **Data-driven research**: Comprehensive market analysis with reliable sources
- **Valuation modeling**: Multiple valuation approaches and metrics
- **Risk quantification**: VaR, stress testing, and scenario analysis
- **Performance attribution**: Detailed factor analysis and insights

### For Portfolio Managers
- **Strategic planning**: Investment thesis development and capital allocation
- **Risk management**: Portfolio-level risk assessment and mitigation
- **Performance optimization**: Risk-adjusted return maximization
- **Execution planning**: Trade timing and implementation strategies

### For Investment Professionals
- **Due diligence**: Comprehensive company and market analysis
- **Client reporting**: Professional-grade investment reports
- **Multi-language support**: Global client communication
- **Regulatory compliance**: Transparent analysis methodology

---

## 📈 Sample Output

### Executive Summary
```
VOIDRA AI INVESTMENT ANALYSIS REPORT
APPLE INC.

Analysis Timestamp: 2024-12-15 14:30:22 UTC
Original Query: iPhone market share and growth prospects

EXECUTIVE SUMMARY

Analysis conducted in response to: 'iPhone market share and growth prospects'. 
This comprehensive investment analysis of Apple Inc. provides actionable insights 
for portfolio management decisions. The analysis incorporates research insights, 
portfolio strategy recommendations, and quantitative risk assessment. All findings 
are based on current market data and reliable financial sources.
```

### Key Insights
- **Research Insights**: Key findings from comprehensive market and company analysis
- **Portfolio Strategy**: Optimal investment approach and allocation recommendations
- **Risk Assessment**: Quantitative risk metrics and mitigation strategies

### Investment Recommendation
- **FINAL RECOMMENDATION**: BUY
- **CONFIDENCE LEVEL**: High (85%)
- **KEY RISK FACTORS**: Supply chain disruptions, regulatory scrutiny
- **PRIMARY CATALYSTS**: iPhone 15 success, services growth, AI integration

---

## 🔧 Configuration

### Environment Variables

```bash
# Required
GOOGLE_API_KEY=your_gemini_api_key
SERPER_API_KEY=your_serper_api_key

# Optional
LOG_LEVEL=INFO
MAX_TOKENS=4096
TEMPERATURE=0.1
```

### Customization Options

- **Model Configuration**: Adjust LLM parameters for different use cases
- **Data Sources**: Add or modify reliable financial sources
- **Workflow Types**: Create custom analysis workflows
- **Report Formats**: Customize report structure and styling

---

## 🌍 International Support

### Supported Languages
Voidra supports 25+ languages across three regions:

**Global Markets**
- Spanish, French, German, Italian, Portuguese
- Russian, Arabic, Chinese (Simplified/Traditional)
- Japanese, Korean

**Asia-Pacific**
- Hindi, Thai, Vietnamese, Indonesian, Malay
- Hebrew, Turkish

**Europe**
- Dutch, Swedish, Norwegian, Danish, Finnish, Polish

### Usage Example
```python
# Translate report to Spanish
translated_file = voidra.translate_report("report.md", "es")
```

---

## 📊 Data Sources

### Primary Sources
- **Bloomberg**: Market data and financial news
- **Reuters**: Global financial information
- **Financial Times**: European market insights
- **Wall Street Journal**: US market analysis
- **CNBC**: Real-time market coverage

### Indian Markets
- **Economic Times**: Indian financial news
- **Business Standard**: Indian market analysis
- **Moneycontrol**: Indian financial data
- **Livemint**: Indian business insights
- **NDTV Profit**: Indian market coverage

### Additional Sources
- **MarketWatch**: Market data and analysis
- **Yahoo Finance**: Financial information
- **Seeking Alpha**: Investment research

---

## 🔒 Security & Compliance

### Data Security
- **API Key Management**: Secure environment variable handling
- **Data Privacy**: No user data storage or transmission
- **Source Verification**: Only trusted financial sources
- **Audit Trail**: Complete analysis logging and tracking

### Compliance Features
- **Transparent Methodology**: Clear analysis framework
- **Source Attribution**: All data sources properly cited
- **Risk Disclosures**: Comprehensive risk assessment
- **Professional Standards**: Institutional-grade reporting

---

## 🚀 Performance & Scalability

### Performance Metrics
- **Analysis Speed**: 3-5 minutes for full analysis
- **Data Accuracy**: 95%+ source reliability
- **Report Quality**: Professional-grade output
- **Scalability**: Handles multiple concurrent analyses

### Optimization Features
- **Caching**: Intelligent result caching
- **Parallel Processing**: Multi-agent concurrent execution
- **Memory Management**: Efficient token usage
- **Error Handling**: Robust error recovery

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

# ⚠️ IMPORTANT DISCLAIMER

## 🚨 NOT FOR ACTUAL TRADING OR INVESTMENT DECISIONS

**Voidra is an educational and research tool designed for learning, experimentation, and academic purposes only.**

---

## 📋 DISCLAIMER OF LIABILITY

### **NO FINANCIAL ADVICE**
This software and its outputs do not constitute financial advice, investment recommendations, or trading signals. The analysis provided by Voidra is for educational and research purposes only.

### **NOT FOR ACTUAL TRADING**
- ❌ **DO NOT** use this tool for actual trading decisions
- ❌ **DO NOT** rely on its outputs for real investment choices
- ❌ **DO NOT** use it to manage real money or portfolios
- ❌ **DO NOT** consider it a substitute for professional financial advice

### **EDUCATIONAL PURPOSE ONLY**
- ✅ Use for learning about investment analysis concepts
- ✅ Use for understanding AI applications in finance
- ✅ Use for academic research and experimentation
- ✅ Use for developing programming and AI skills

---

## 🔒 LIMITATION OF LIABILITY

### **NO WARRANTIES**
This software is provided "AS IS" without any warranties, express or implied. The developers make no representations about the accuracy, reliability, or suitability of the analysis for any purpose.

### **NO RESPONSIBILITY FOR LOSSES**
The developers and contributors are not responsible for any financial losses, damages, or consequences that may result from:
- Using this software for actual trading
- Relying on the analysis for investment decisions
- Any misinterpretation of the results
- Technical issues or bugs in the software

### **USER RESPONSIBILITY**
By using this software, you acknowledge that:
- You understand this is for educational purposes only
- You will not use it for actual trading or investment decisions
- You accept all risks associated with using the software
- You are responsible for your own actions and decisions

---

## 📚 INTENDED USE CASES

### **Appropriate Uses:**
- 🎓 **Academic Research**: Studying AI applications in finance
- 🔬 **Experimentation**: Testing AI models and algorithms
- 💻 **Programming Practice**: Learning Python and AI development
- 📊 **Educational Demonstrations**: Understanding investment concepts
- 🧪 **Prototype Development**: Building and testing ideas

### **Inappropriate Uses:**
- 💰 **Actual Trading**: Making real buy/sell decisions
- 📈 **Portfolio Management**: Managing real investment portfolios
- 🎯 **Investment Recommendations**: Advising others on investments
- 📊 **Financial Planning**: Planning real financial strategies
- 🏦 **Professional Services**: Using in professional financial services

---

## ⚖️ LEGAL NOTICES

### **Regulatory Compliance**
This software is not registered with any financial regulatory authority and should not be used in regulated financial activities.

### **Professional Standards**
The analysis does not meet professional standards for financial advice and should not be used in professional contexts.

### **Data Accuracy**
While the software uses reliable data sources, the analysis may contain errors, inaccuracies, or outdated information.

---

## 🛡️ SAFETY GUIDELINES

### **Before Using This Software:**
1. **Understand the Purpose**: This is for learning, not trading
2. **Consult Professionals**: Seek real financial advice from qualified professionals
3. **Do Your Research**: Verify any information independently
4. **Start Small**: Begin with educational experiments only
5. **Stay Informed**: Keep learning about proper investment practices

### **If You Want to Start Real Trading:**
1. **Get Professional Advice**: Consult with licensed financial advisors
2. **Use Regulated Platforms**: Use official, regulated trading platforms
3. **Start with Paper Trading**: Practice with simulated trading first
4. **Understand Risks**: Learn about market risks and volatility
5. **Follow Regulations**: Comply with all applicable financial regulations



## ✅ ACKNOWLEDGMENT

By using Voidra, you acknowledge that you have read, understood, and agree to this disclaimer. You understand that this software is for educational and research purposes only and should not be used for actual trading or investment decisions.

---

**Remember: This is a tool for learning and experimentation, not for making real money decisions!**


