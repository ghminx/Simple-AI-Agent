from utils import llm_call
import re 


def route_llm(user_input : str) -> str:
    select_prompt = f'''

    user_input : {user_input}


    당신은 AI 라우팅 시스템입니다.
    사용자의 요청을 보고 가장 적절한 AI 모델을 선택하세요.

    선택 가능한 모델:
    - gemma2-9b-it (요청이 매우 간단하거나 반복적인 경우)
    - llama3-70b-8192 (일반적인 질문이나 가벼운 생성 작업)
    - deepseek-r1-distill-llama-70b-specdec (복잡하거나 창의적 사고가 필요한 고급 요청)


    - 사용자의 질문에는 답변하지 않습니다.
    - 먼저 왜 해당 모델을 선택했는지 간단히 설명하고, 아래 형식으로 **반드시 그대로 출력**해주세요:


    출력 예시:

    선택 이유: 사용자의 요청이 어떤 유형이며, 어떤 모델이 그에 적합한지 설명.
    선택한 모델 이름 : "gemma2-9b-it"

    '''

    select = llm_call(select_prompt)
    
    reason = select.split('\n')[0]
    
    if not select:
        raise "No model selected"
    
    model_name = re.search(r'\"(.*?)\"', select).group(1)
    
    print(f'Reasoning Select Model : {reason}')
    print(f'selected model : {model_name}')
    
    response = llm_call(user_input, model_name)
    
    return response


user_input1 = '저녁메뉴 1개만 추천해줘'

user_input2 = "ChatGPT와 일반 챗봇의 차이점을 간단히 설명해줘."

user_input3 = "OverFitting의 개념을 알려주고 해결 방법에는 어떤 것들이 있는지 구체적인 예시를 들어서 상세히 알려줘"

if __name__ == '__main__':
    response = route_llm(user_input1)
    print(response)