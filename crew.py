from deep_translator import GoogleTranslator
from agents import research_analyst_agent, portfolio_manager_agent, risk_manager_agent
from tasks import TaskManager
import os
import logging
from typing import Optional, Dict, Any, List
from datetime import datetime
import json

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class VoidraInvestmentSystem:
    """
    Advanced Voidra Investment Management System with enhanced AI agent coordination
    """
    
    def __init__(self):
        self.task_manager = TaskManager(
            research_agent=research_analyst_agent,
            portfolio_agent=portfolio_manager_agent,
            risk_agent=risk_manager_agent
        )
        self.analysis_history = []
        self.current_analysis = None
        
    def analyze_company(self, company: str, query: str = None, additional_context: str = None, workflow_type: str = "full") -> Dict[str, Any]:
        """
        Perform comprehensive company analysis with enhanced workflow management
        
        Args:
            company: Company name to analyze
            query: Specific research query or focus area
            additional_context: Additional context or constraints
            workflow_type: Type of analysis ('full', 'research_only', 'portfolio_only', 'risk_only', 'research_portfolio')
            
        Returns:
            Dictionary containing analysis results and metadata
        """
        logger.info(f"Starting enhanced analysis for {company}")
        logger.info(f"Query: {query}")
        logger.info(f"Workflow type: {workflow_type}")
        
        # Create analysis metadata
        analysis_metadata = {
            "company": company,
            "query": query,
            "workflow_type": workflow_type,
            "start_time": datetime.now().isoformat(),
            "additional_context": additional_context,
            "status": "in_progress"
        }
        
        try:
            # Execute appropriate workflow
            if workflow_type == "full":
                results = self.task_manager.execute_sequential_workflow(company, query, additional_context)
            else:
                results = self.task_manager.execute_custom_workflow(company, workflow_type, query, additional_context=additional_context)
            
            # Generate enhanced report
            report = self.task_manager.generate_enhanced_combined_report(company, results, query)
            
            # Update metadata
            analysis_metadata.update({
                "end_time": datetime.now().isoformat(),
                "status": "completed",
                "workflow_context": results.get('workflow_context', {}),
                "results_keys": list(results.keys())
            })
            
            # Store analysis
            self.current_analysis = {
                "metadata": analysis_metadata,
                "results": results,
                "report": report
            }
            
            self.analysis_history.append(self.current_analysis)
            
            logger.info(f"Enhanced analysis completed for {company}")
            return {
                "metadata": analysis_metadata,
                "results": results,
                "report": report
            }
            
        except Exception as e:
            analysis_metadata.update({
                "end_time": datetime.now().isoformat(),
                "status": "failed",
                "error": str(e)
            })
            logger.error(f"Error during enhanced analysis: {str(e)}")
            raise
    
    def get_analysis_status(self) -> Dict[str, Any]:
        """
        Get current analysis status and workflow context
        
        Returns:
            Dictionary containing current analysis status
        """
        if not self.current_analysis:
            return {"status": "no_analysis_running"}
        
        return {
            "current_analysis": self.current_analysis["metadata"],
            "workflow_status": self.task_manager.get_workflow_status()
        }
    
    def get_analysis_history(self) -> List[Dict[str, Any]]:
        """
        Get analysis history
        
        Returns:
            List of previous analyses
        """
        return [analysis["metadata"] for analysis in self.analysis_history]
    
    def save_report(self, report: str, filename: str = None, format_type: str = "markdown") -> str:
        """
        Save report to file with enhanced formatting options
        
        Args:
            report: Report content
            filename: Output filename (auto-generated if None)
            format_type: Report format ('markdown', 'txt')
            
        Returns:
            Path to saved file
        """
        try:
            if filename is None:
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                filename = f"voidra_analysis_{timestamp}.{format_type}"
            
            # Ensure proper file extension
            if not filename.endswith(f".{format_type}"):
                filename = f"{filename}.{format_type}"
            
            with open(filename, "w", encoding="utf-8") as file:
                file.write(report)
            
            logger.info(f"Enhanced report saved to {filename}")
            return filename
            
        except Exception as e:
            logger.error(f"Error saving enhanced report: {str(e)}")
            raise
    
    def export_analysis_data(self, filename: str = None, format_type: str = "json") -> str:
        """
        Export complete analysis data including metadata and results
        
        Args:
            filename: Output filename (auto-generated if None)
            format_type: Export format ('json', 'txt')
            
        Returns:
            Path to exported file
        """
        if not self.current_analysis:
            raise ValueError("No analysis data available for export")
        
        try:
            if filename is None:
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                company = self.current_analysis["metadata"]["company"]
                filename = f"voidra_analysis_data_{company}_{timestamp}.{format_type}"
            
            export_data = {
                "voidra_version": "2.0",
                "export_timestamp": datetime.now().isoformat(),
                "analysis": self.current_analysis
            }
            
            if format_type == "json":
                with open(filename, "w", encoding="utf-8") as file:
                    json.dump(export_data, file, indent=2, ensure_ascii=False)
            else:
                with open(filename, "w", encoding="utf-8") as file:
                    file.write(str(export_data))
            
            logger.info(f"Analysis data exported to {filename}")
            return filename
            
        except Exception as e:
            logger.error(f"Error exporting analysis data: {str(e)}")
            raise
    
    def translate_report(self, file_path: str, target_language: str) -> Optional[str]:
        """
        Translate report to target language with enhanced error handling
        
        Args:
            file_path: Path to original report
            target_language: Target language code
            
        Returns:
            Path to translated file or None if error
        """
        if not os.path.exists(file_path):
            logger.error(f"File '{file_path}' does not exist")
            return None
        
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                content = file.read()
            
            # Initialize translator
            translator = GoogleTranslator(source="en", target=target_language)
            
            # Translate content in chunks to handle large reports
            translated_content = self._translate_in_chunks(content, translator)
            
            # Save translated report with timestamp
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            translated_file_path = f"voidra_analysis_{target_language}_{timestamp}.md"
            
            with open(translated_file_path, "w", encoding="utf-8") as file:
                file.write(translated_content)
            
            logger.info(f"Enhanced translation completed and saved to {translated_file_path}")
            return translated_file_path
            
        except Exception as e:
            logger.error(f"Error during enhanced translation: {str(e)}")
            return None
    
    def _translate_in_chunks(self, text: str, translator: GoogleTranslator, chunk_size: int = 4500) -> str:
        """
        Translate text in chunks to handle large content with improved chunking
        
        Args:
            text: Text to translate
            translator: GoogleTranslator instance
            chunk_size: Size of each chunk
            
        Returns:
            Translated text
        """
        if len(text) <= chunk_size:
            return translator.translate(text)
        
        # Split text into chunks with better boundary detection
        chunks = []
        for i in range(0, len(text), chunk_size):
            chunk = text[i:i + chunk_size]
            # Try to break at sentence boundaries
            if i + chunk_size < len(text):
                last_period = chunk.rfind('.')
                last_newline = chunk.rfind('\n')
                last_colon = chunk.rfind(':')
                break_point = max(last_period, last_newline, last_colon)
                if break_point > chunk_size * 0.7:  # Only break if it's not too early
                    chunk = chunk[:break_point + 1]
            chunks.append(chunk)
        
        # Translate each chunk with progress tracking
        translated_chunks = []
        total_chunks = len(chunks)
        
        for i, chunk in enumerate(chunks):
            try:
                translated_chunk = translator.translate(chunk)
                translated_chunks.append(translated_chunk)
                logger.info(f"Translated chunk {i+1}/{total_chunks} ({((i+1)/total_chunks)*100:.1f}%)")
            except Exception as e:
                logger.warning(f"Error translating chunk {i+1}: {str(e)}")
                translated_chunks.append(chunk)  # Keep original if translation fails
        
        return ''.join(translated_chunks)
    
    def get_supported_languages(self) -> dict:
        """
        Get dictionary of supported languages with enhanced categorization
        
        Returns:
            Dictionary of language codes and names categorized by region
        """
        return {
            'global': {
                'es': 'Spanish',
                'fr': 'French',
                'de': 'German',
                'it': 'Italian',
                'pt': 'Portuguese',
                'ru': 'Russian',
                'ar': 'Arabic',
                'zh': 'Chinese (Simplified)',
                'zh-tw': 'Chinese (Traditional)',
                'ja': 'Japanese',
                'ko': 'Korean'
            },
            'asia_pacific': {
                'hi': 'Hindi',
                'th': 'Thai',
                'vi': 'Vietnamese',
                'id': 'Indonesian',
                'ms': 'Malay',
                'he': 'Hebrew',
                'tr': 'Turkish'
            },
            'europe': {
                'nl': 'Dutch',
                'sv': 'Swedish',
                'no': 'Norwegian',
                'da': 'Danish',
                'fi': 'Finnish',
                'pl': 'Polish'
            }
        }
    
    def get_workflow_options(self) -> Dict[str, str]:
        """
        Get available workflow options with descriptions
        
        Returns:
            Dictionary of workflow types and descriptions
        """
        return {
            "full": "Complete analysis (Research → Portfolio → Risk)",
            "research_only": "Research analysis only",
            "portfolio_only": "Portfolio strategy only (requires research context)",
            "risk_only": "Risk assessment only (requires research and portfolio context)",
            "research_portfolio": "Research and portfolio strategy (no risk assessment)"
        }
    
    def validate_company_input(self, company: str) -> Dict[str, Any]:
        """
        Validate company input and provide suggestions
        
        Args:
            company: Company name to validate
            
        Returns:
            Dictionary with validation results and suggestions
        """
        validation = {
            "is_valid": True,
            "suggestions": [],
            "warnings": []
        }
        
        if not company or len(company.strip()) < 2:
            validation["is_valid"] = False
            validation["warnings"].append("Company name is too short")
        
        if len(company) > 100:
            validation["warnings"].append("Company name is very long - consider using official name")
        
        # Common company name patterns
        if company.lower() in ['apple', 'aapl']:
            validation["suggestions"].append("Consider using 'Apple Inc.' for more comprehensive results")
        elif company.lower() in ['microsoft', 'msft']:
            validation["suggestions"].append("Consider using 'Microsoft Corporation' for more comprehensive results")
        elif company.lower() in ['google', 'alphabet', 'googl']:
            validation["suggestions"].append("Consider using 'Alphabet Inc.' for more comprehensive results")
        
        return validation

def main():
    """
    Enhanced main function to run the Voidra Investment System
    """
    print("=" * 70)
    print("🚀 Welcome to Voidra 2.0 - Advanced AI Investment Management System")
    print("=" * 70)
    print("📊 Powered by Chain of Thought AI Agents with Real-time Market Data")
    print("🔍 Research Analyst | 💼 Portfolio Manager | ⚠️ Risk Manager")
    print("=" * 70)
    print()
    
    # Initialize system
    voidra = VoidraInvestmentSystem()
    
    try:
        # Get company input with validation
        company = input("💼 What company would you like Voidra to analyze? ").strip()
        
        if not company:
            print("❌ Please enter a valid company name.")
            return
        
        # Validate input
        validation = voidra.validate_company_input(company)
        if not validation["is_valid"]:
            print(f"❌ Invalid input: {validation['warnings'][0]}")
            return
        
        if validation["warnings"]:
            print(f"⚠️  Warning: {validation['warnings'][0]}")
        
        if validation["suggestions"]:
            print(f"💡 Suggestion: {validation['suggestions'][0]}")
        
        # Get specific query
        print("\n🎯 What specific aspect would you like to focus on?")
        print("   (Press Enter for comprehensive analysis)")
        query = input("   Query: ").strip()
        
        # Get workflow type
        print("\n⚙️  Select analysis type:")
        workflow_options = voidra.get_workflow_options()
        for key, description in workflow_options.items():
            print(f"   {key}: {description}")
        
        workflow_type = input("\n   Workflow type (default: full): ").strip().lower()
        if not workflow_type or workflow_type not in workflow_options:
            workflow_type = "full"
        
        # Get additional context
        print("\n📝 Any additional context or constraints?")
        print("   (e.g., 'Focus on Indian market', 'Conservative risk profile')")
        additional_context = input("   Context: ").strip()
        
        print(f"\n🔍 Starting {workflow_type} analysis for {company}...")
        if query:
            print(f"   Focus: {query}")
        if additional_context:
            print(f"   Context: {additional_context}")
        
        print("⏳ This may take a few minutes as our AI agents work together...")
        print("   📊 Research Analyst: Gathering market data...")
        print("   💼 Portfolio Manager: Developing strategies...")
        print("   ⚠️ Risk Manager: Assessing risks...")
        
        # Analyze company
        analysis_result = voidra.analyze_company(company, query, additional_context, workflow_type)
        
        # Save original report
        original_file = voidra.save_report(analysis_result["report"])
        print(f"✅ Analysis complete! Report saved to '{original_file}'")
        
        # Show analysis status
        status = voidra.get_analysis_status()
        print(f"📈 Analysis Status: {status['current_analysis']['status']}")
        print(f"⏱️  Duration: {status['current_analysis']['end_time']}")
        
        # Offer data export
        print("\n💾 Would you like to export the complete analysis data?")
        export_choice = input("   Export data? (y/n, default: n): ").strip().lower()
        
        if export_choice in ['y', 'yes']:
            export_file = voidra.export_analysis_data()
            print(f"✅ Analysis data exported to '{export_file}'")
        
        # Offer translation
        print("\n🌍 Would you like to translate this report to another language?")
        supported_langs = voidra.get_supported_languages()
        
        print("\nSupported languages:")
        for category, languages in supported_langs.items():
            print(f"\n{category.upper().replace('_', ' ')}:")
            for code, name in list(languages.items())[:5]:  # Show first 5 per category
                print(f"  {code}: {name}")
            if len(languages) > 5:
                print(f"  ... and {len(languages) - 5} more")
        
        translate_choice = input("\nEnter language code (or 'skip' to finish): ").strip().lower()
        
        if translate_choice and translate_choice != 'skip':
            # Check if language is supported
            is_supported = False
            for category, languages in supported_langs.items():
                if translate_choice in languages:
                    is_supported = True
                    language_name = languages[translate_choice]
                    break
            
            if is_supported:
                print(f"\n🔄 Translating report to {language_name}...")
                translated_file = voidra.translate_report(original_file, translate_choice)
                
                if translated_file:
                    print(f"✅ Translation complete! Saved to '{translated_file}'")
                else:
                    print("❌ Translation failed. Please check the logs for details.")
            else:
                print(f"❌ Language code '{translate_choice}' not supported.")
        
        print("\n🎉 Analysis complete! Thank you for using Voidra 2.0.")
        print("📊 Your AI-powered investment insights are ready!")
        
    except KeyboardInterrupt:
        print("\n\n⏹️  Analysis interrupted by user.")
    except Exception as e:
        logger.error(f"Error in enhanced main execution: {str(e)}")
        print(f"\n❌ An error occurred: {str(e)}")
        print("Please check the logs for more details.")

if __name__ == "__main__":
    main()
