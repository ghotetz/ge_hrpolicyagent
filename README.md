# 📌 Google ADK HR Policy Agent
> 입사 연차 별 연차 일수 자동 계산 에이전트

## ⚡ 주요 기능 (Features)
> 법적 제공 연차(최대 25일, 최소 11일) 을 자동으로 계산

## 🛠 기술 스택 (Tech Stack)
- Google ADK, Python

## 💻 시작 가이드 (Getting Started)
- Google Cloud 인증
'''gcloud auth login
gcloud auth application-default login
gcloud config set project ax-gemini-lab'''

- Google ADK 설치
'''python -m venv .venv && source .venv/bin/activate
pip install google-adk litellm'''

- ADK 검증
'''adk web
127.0.0.1:8000'''
