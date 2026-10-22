from litellm import get_agent
from calendar import Day
import os
from datetime import date
from google.adk.agents import Agent

#환경변수로 에이전트가 사용할 모델을 고른다
def get_model() :
    """MODEL 값으로 GEMINI <-> Local LLM(ex.ollama) 로 전환"""
    if os.getenv("MODEL_PROVIDER", "gemini") == "ollama":
        from google.adk.models.lite_llm import LiteLLM
        local = os.getenv("LOCAL_MODEL", "llama3.2")
        return LiteLLM(model=f"ollama_chat/{local}")
    return os.environ["GEMINI_MODEL"]

#에이전트가 호출할 도구(함수) 선언
def calc_annual_leave(hire_date : str) -> dict:
    """입사일(YYYY-MM-DD) 기준 올해 법정 연차 일수를 계산한다.

    근로기준법 기준: 1년 미만은 개근 1개월당 1일(최대 11일),
    1년 이상 15일, 3년 이상부터 2년마다 1일 가산(최대 25일).
    """
    start = date.fromisoformat(hire_date)
    today = date.today()
    month = (today.year - start.year) * 12 + (today.month - start.month)
    
    if today.day < start.day:
        month -= 1
    
    years = month // 12
    
    if years < 1:
        days = min(month, 11)
    else:
        days = min(15 + (years -1) // 2, 25)

    return {"근속 년": years, "근속 개월": month, "법정 연차 일수":days}

root_agent = Agent(
    name="hr_policy_agent",
    model=get_model(),
    description="인사 규정 질문에 답하고 연차 일수를 계산하는 사내 HR 도우미",
    instruction=(
        "너는 사내 HR 도우미다. 연차 일수 질문에는 반드시 calc_annual_leave 도구를 호출한다."
        "규정 해석이 애매하면 단정하지 말고 인사팀 확인을 권한다. 답변은 한국어로 간결하게."
    ),
    tools=[calc_annual_leave],
)