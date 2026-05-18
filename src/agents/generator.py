import os
from openai import OpenAI

class GeneratorAgent:
    def __init__(self, brand_settings, seo_targets):
        self.client = OpenAI(
            api_key=os.getenv("LLM_API_KEY"),
            base_url=os.getenv("LLM_BASE_URL")
        )
        self.brand_tone = brand_settings['tone_of_voice']
        self.keywords = seo_targets['primary_keywords'] + seo_targets['secondary_keywords']

    def generate(self, selling_points, language, feedback=""):
        prompt = f"""
        You are an expert SEO copywriter. Write a high-converting product description.
        Target Language: {language}
        Brand Tone of Voice: {self.brand_tone}
        Must Include SEO Keywords: {', '.join(self.keywords)}
        Product Selling Points (Extracted from competitors): {selling_points}
        
        Previous Critic Feedback (If any, you must fix these issues): {feedback}
        
        Output the response in Markdown format, including catchy H1, H2 tags and bullet points.
        """
        
        # 实际项目中这里可能消耗大量上下文 Token
        response = self.client.chat.completions.create(
            model="gpt-4o", # 可以根据实际使用的模型修改
            messages=[
                {"role": "system", "content": "You are a senior cross-border E-commerce content strategist."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )
        return response.choices[0].message.content