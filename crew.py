from deep_translator import GoogleTranslator
from crewai import Process, Crew
from agents import (
    research_analyst_agent,
    portfolio_manager_agent,
    risk_manager_agent,
)
from tasks import research_task, portfolio_management_task, risk_assessment_task
import os

crew = Crew(
    agents=[
        research_analyst_agent,
        portfolio_manager_agent,
        risk_manager_agent,
    ],
    tasks=[research_task, portfolio_management_task, risk_assessment_task],
    process=Process.sequential,  # Execute tasks sequentially
)


def translate_md(file_path, target_language):
    if not os.path.exists(file_path):
        print(f"Error: The file '{file_path}' does not exist.")
        return

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()

        translator = GoogleTranslator(source="en", target=target_language)
        translated_content = translator.translate(content)

        translated_file_path = f"investment_risk_analysis_{target_language}.md"
        with open(translated_file_path, "w", encoding="utf-8") as file:
            file.write(translated_content)

        print(f"The translation has been completed and saved in '{translated_file_path}'.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    company = str(input("What company do you want to Voidra to analyze? "))
    result = crew.kickoff(inputs={"empresa": company})
    
    # Save the original report
    original_file_path = "investment_risk_analysis.md"
    with open(original_file_path, "w", encoding="utf-8") as file:
        file.write(result)
    print(f"The original report has been saved in '{original_file_path}'.")
    
    # Translate the report
    target_language = input("Enter the target language for translation (e.g., 'es' for Spanish, 'fr' for French): ")
    translate_md(original_file_path, target_language)
    
    # Create a separate translated file
    translated_file_path = f"investment_risk_analysis_{target_language}.md"
    with open(translated_file_path, "r", encoding="utf-8") as file:
        translated_content = file.read()
    
    print(f"A separate translated file has been created: '{translated_file_path}'.")
