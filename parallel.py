# 비동기 함수를 사용하여 여러 모델에 대한 요청을 병렬로 처리하는 예제입니다.
from utils import llm_call_async
import asyncio

user_input = '''
업무적 피로감으로 인해 편하게힐링 할 수 있는 곳으로 여행을 가고 싶어 
여행지를 2가지만 추천해줘 추천 여행지, 여행 코스를 알려주고 그 이유도 알려줘
나는 여러 관광지를 돌아다는것 보다는 경치좋고 특색있는 명소를 찾아다니는것을 좋아해
아래 포맷대로 작성해줘 

추천 여행지 :
1. OO

추천 코스:
OO => OO => OO

추천 이유:
OO
'''


async def parallel_agent(prompt):
    tasks = []
    for prom in prompt:
        tasks.append(llm_call_async(prom['user'], prom['model']))
        
    responses = []
    for task in asyncio.as_completed(tasks):
        result = await task
        responses.append(result)
    
    return responses


async def main(user_input):
    
    prompt = [
    
    {'user' : user_input, 'model' : 'gemma2-9b-it'},
    {'user' : user_input, 'model' : 'llama3-70b-8192'},
    {'user' : user_input, 'model' : 'deepseek-r1-distill-llama-70b-specdec'}
    
    ]
    
    responses = await parallel_agent(prompt)
    
    ensemble_prompt = f'''
입력된 텍스트은 사용자의 요청에 따라 출력한 여러가지 결과입니다. 
이 결과들을 종합하고 요약하여 사용자의 질문에 맞는 최종 결과를 출력해주세요.

사용자 질문:
    {user_input}

모델별 응답:
'''
                    
    for i in range(len(prompt)):
        ensemble_prompt += f'model :{prompt[i]["model"]}\n모델 응답: {responses[i]}\n'
        
    result = await llm_call_async(ensemble_prompt, model="gemma2-9b-it")
    
    print("=========================프롬프트==========================\n")
    print(ensemble_prompt)
    
    print("=========================출력 결과=========================")
    print(result)

# 비동기 함수 실행
asyncio.run(main(user_input))