from utils import llm_call
from typing import List

# 단계적으로 LLM이 사용자의 질문에 대답하는 프롬프트 체인
def chain(input: str, prompts: List[str]) -> List[str]:
    
    responses = []
    result = input
    
    for i, prompt in enumerate(prompts, 1):
        print(f"==================Step {i}=================")
        print(f"{i}번째 Prompt : {result}")
        
        result = llm_call(f"Prompt: {prompt}\nUser_input: {result}\n")
        responses.append(result)
        
        print(f"================{i}번째 답변================\n")
        print(result)
        
    return responses    


user_input = '''

AI 기술이나 최신 소식에 대해 블로그를 작성하고 싶어
AI와 관련된 흥미롭고 유익한 블로그 글을 작성하고 싶은데
어떤 주제로 블로그를 쓰면 좋을까?'

'''

# 단계적으로 LLM이 사용자의 질문에 대답하는 프롬프트 체인
prompts = [
    
# 사용자의 질문을 이해하고 적절한 주제 제안
"""
사용자의 요청 바탕으로 적합한 블로그 글 주제를 3가지 제안해주세요
- 사용자의 요청을 이해하고 요약하세요
- 각 주제는 명확하고 구체적으로 제안하세요
- 사람들이 관심 가질 만한 이유도 함께 설명하세요 
""",

# 주제를 선택하고 이 주제에서 나올수 있는 추가적인 요소들 5가지 제안
"""
다음 주제 중 하나를 선택하고, 어떤 주제를 선택했는지 명시, 그리고 선택한 이유 설명하세요
- 해당 주제에서 다룰 수 있는 추가적인 요소 5가지를 제안해주세요
- 다양한 관점에서 주제를 다룰 수 있도록 다양한 요소를 제안하세요
""",

# 주제를 바탕으로 블로그 글을 작성
"""
선택한 주제를 바탕으로 블로그 글을 작성해주고, 포맷은 다음의 양식을 따라주세요

- 도입: 주제에 대한 배경이나 중요성 소개  
- 본문: 2~3개의 핵심 소제목으로 내용을 전개  
- 결론: 요약 및 독자에게 던지는 질문이나 통찰

문체는 친절하고 명확하게, 일반 독자도 이해할 수 있게 써야 합니다
""",
]

if __name__ == '__main__':
    chain(user_input, prompts)