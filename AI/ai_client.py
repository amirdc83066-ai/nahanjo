#وصل کردن AI

#کتابخانه های مورد نیاز

import requests
from dotenv import load_dotenv
import os

# مدیریت ارتباط با مدل هوش مصنوعی
class AIClient:

    def __init__(self):
        
        load_dotenv()

        self.api_key = os.getenv("API_KEY")

        self.base_url = os.getenv("BASE_URL")

    # ارسال پرامپت و دریافت تحلیل هوشمند
    
    def analyze(self, prompt_file):

        with open(prompt_file, "r", encoding="utf-8") as f:
            full_prompt = f.read()

        url = f"{self.base_url}/chat/completions"

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        # تنظیم پارامترهای درخواست AI
        
        payload = {
            "model": "gpt-4o",
            "messages": [
                {
                    "role": "user",
                    "content": full_prompt
                }
            ],
            "temperature": 0,
            "top_p": 1

        }
        # ارسال درخواست به API
        
        response = requests.post(
            url,
            headers=headers,
            json=payload,
            timeout=120
        )
        # بررسی صحت پاسخ API
        
        if response.status_code != 200:
            raise Exception(response.text)

        result = response.json()
        
        # استخراج متن تحلیل از پاسخ مدل
        
        ai_text = result["choices"][0]["message"]["content"]

        return ai_text
