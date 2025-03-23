#%%
import os 
from openai import AsyncOpenAI, OpenAI
from groq import Groq, AsyncGroq
import asyncio

api_key = os.getenv('GROQ_API_KEY')

client = Groq(api_key = api_key)

def llm_call(prompt: str, system_prompt: str = "", model = 'gemma2-9b-it') -> str:
    
    completion = client.chat.completions.create(
        model = model,
        temperature = 0.1,
        max_tokens = 1024,
    
        messages = [
            {'role' : 'system', 'content' : system_prompt},
            {'role' : 'user', 'content' : prompt},
            
        ]
    )
    
    return completion.choices[0].message.content

# open_api_key = os.getenv('OPENAI_API_KEY')
async_client = AsyncGroq(api_key = api_key)


async def llm_call_async(prompt: str, system_prompt: str = "", model = 'gemma2-9b-it') -> str:

    completion = await async_client.chat.completions.create(
        model=model,
        temperature = 0.1,
        max_tokens = 1024,
        
    
        messages = [
            {'role' : 'system', 'content' : system_prompt},
            {'role' : 'user', 'content' : prompt},
            
        ]
    )
    
    return completion.choices[0].message.content


# if __name__ == '__main__':
    # print(llm_call("안녕"))
    
if __name__ == '__main__':
    # 비동기 함수를 실행하기 위한 이벤트 루프 생성
    async def main():
        result = await llm_call_async("안녕")
        print(result)
    
    # 비동기 함수 실행
    asyncio.run(main())

    
