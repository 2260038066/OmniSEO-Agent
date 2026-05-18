import os
from openai import OpenAI
import json

class CriticAgent:
    def __init__(self, seo_targets):
        self.client = OpenAI(
            api_key=os.getenv("LLM_API_KEY"),
            base_url=os.getenv("LLM_BASE_URL")
        )
        self.keywords = seo_targets['primary_keywords']

    def evaluate(self, content, language):
        prompt = f"""
        You are a strict QA and SEO Analyst. Evaluate the following product description.
        Target Language: {language}
        Required SEO Keywords: {', '.join(self.keywords)}
        
        Evaluate based on:
        1. Keyword Density (Are the keywords naturally integrated?)
        2. Readability & Flow
        3. Marketing Persuasiveness
        
        Respond ONLY with a JSON object containing 'score' (0-100) and 'feedback' (string with actionable advice).
        
        Content to evaluate:
        {content}
        """
        
        response = self.client.chat.completions.create(
            model="gpt-4o", # 建议这里使用推理能力强的模型
            messages=[{"role": "user", "content": prompt}],
            response_format={"type": "json_object"},
            temperature=0.2
        )
        
        try:
            result = json.loads(response.choices[0].message.content)
            return result.get('score', 0), result.get('feedback', "Parsing error.")
        except:
            return 0, "System error in Critic evaluation."