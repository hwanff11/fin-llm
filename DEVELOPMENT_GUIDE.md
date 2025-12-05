# 법률 질의응답 AI 시스템 개발 가이드

## 🎯 프로젝트 목표

여러 법령 PDF 파일을 입력받아 법률적 질문에 대한 정확한 답변을 제공하는 RAG 기반 AI 시스템 개발

---

## 📋 개발 단계

### Phase 1: 기본 시스템 구축 ✅

**완료된 작업:**
- ✅ 프로젝트 노트북 생성 (`[PROJECT]_Legal_QA_RAG.ipynb`)
- ✅ README 문서 작성
- ✅ 기본 RAG 파이프라인 구현
  - PDF 문서 로드
  - 텍스트 분할
  - 임베딩 생성
  - 벡터 DB 구축
  - 검색 및 답변 생성

**다음 단계:**
1. 노트북 실행 및 테스트
2. 실제 법령 PDF로 시스템 검증
3. 답변 품질 평가

---

### Phase 2: 시스템 개선 (권장)

#### 2.1 성능 향상
- [ ] 더 나은 임베딩 모델 적용 (`text-embedding-3-large`)
- [ ] 더 강력한 LLM 사용 (`gpt-4o`)
- [ ] 재순위화(Reranking) 추가
- [ ] 쿼리 확장(Query Expansion) 구현

#### 2.2 법률 특화 기능
- [ ] 법령 조문 번호 자동 추출
- [ ] 관련 판례 검색 기능
- [ ] 법령 개정 이력 추적
- [ ] 법률 용어 사전 통합

#### 2.3 사용자 경험 개선
- [ ] Gradio/Streamlit 웹 인터페이스 구축
- [ ] 대화 히스토리 관리
- [ ] 북마크 및 저장 기능
- [ ] PDF 하이라이트 기능

---

### Phase 3: 프로덕션 준비

#### 3.1 품질 보증
- [ ] RAG 평가 지표 측정
  - Faithfulness (충실도)
  - Answer Relevancy (답변 관련성)
  - Context Relevancy (컨텍스트 관련성)
- [ ] 테스트 케이스 작성
- [ ] 오답 분석 및 개선

#### 3.2 배포 준비
- [ ] API 서버 구축 (FastAPI)
- [ ] 도커 컨테이너화
- [ ] 클라우드 배포 (AWS/GCP/Azure)
- [ ] 모니터링 시스템 구축

#### 3.3 보안 및 규정 준수
- [ ] 개인정보 보호 조치
- [ ] 로그 관리
- [ ] 사용 제한 및 인증
- [ ] 면책조항 명시

---

## 🔧 즉시 시작하기

### 1단계: 노트북 열기

```bash
# VS Code에서 열기
code "[PROJECT]_Legal_QA_RAG.ipynb"

# 또는 Jupyter에서 열기
jupyter notebook "[PROJECT]_Legal_QA_RAG.ipynb"
```

### 2단계: 셀 순서대로 실행

노트북의 셀을 위에서부터 순서대로 실행하세요:

1. ✅ 환경 설정
2. ✅ PDF 문서 로드
3. ✅ 텍스트 분할
4. ✅ 임베딩 모델 설정
5. ✅ 벡터 DB 구축
6. ✅ 검색기 설정
7. ✅ 프롬프트 설계
8. ✅ RAG 체인 구성
9. ✅ 테스트 실행

### 3단계: 질문하기

```python
# 질문 입력
my_question = "임대차 계약 기간 중 임대료를 인상할 수 있나요?"

# 답변 받기
answer = ask_legal_question(my_question)
```

---

## 📚 추가 법령 PDF 추가 방법

### 방법 1: 파일 직접 추가

1. PDF 파일을 `./data/` 폴더에 복사
2. 노트북의 "2. PDF 문서 로드" 섹션에서 파일 경로 추가:

```python
legal_pdf_files = [
    os.path.join(DATA_DIR, 'housing_leasing_law.pdf'),
    os.path.join(DATA_DIR, '새로운_법령.pdf'),  # 추가
]
```

3. 해당 셀부터 다시 실행

### 방법 2: 동적 추가 (기존 DB 유지)

```python
# 새로운 PDF 추가 (벡터 DB에 추가)
new_pdfs = [
    './data/새로운_법령1.pdf',
    './data/새로운_법령2.pdf',
]
add_new_legal_documents(new_pdfs)
```

---

## 🎨 커스터마이징 가이드

### 프롬프트 수정

법률 전문성을 더 강화하려면:

```python
system_prompt = """당신은 대한민국 법률 전문 AI 어시스턴트입니다.

<추가 지침>
- 판례를 참고하여 답변하세요
- 법률 용어를 쉽게 풀어서 설명하세요
- 실무적인 조언도 포함하세요
</추가 지침>

...
"""
```

### 검색 전략 변경

더 많은 문서를 검색하려면:

```python
retriever = vector_store.as_retriever(
    search_type="mmr",
    search_kwargs={
        "k": 10,           # 10개 문서 검색
        "fetch_k": 30,     # 30개 후보에서 선택
        "lambda_mult": 0.5,  # 다양성 증가
    }
)
```

### LLM 모델 변경

더 정확한 답변을 위해:

```python
llm = ChatOpenAI(
    model="gpt-4o",      # GPT-4o 사용
    temperature=0.0,     # 완전 결정적 답변
)
```

---

## 🐛 문제 해결

### 문제 1: `vector_store` 정의되지 않음

**원인**: 셀을 순서대로 실행하지 않음

**해결**:
1. 노트북을 처음부터 다시 실행
2. "Restart Kernel and Run All" 실행

### 문제 2: PDF 로드 실패

**원인**: 파일 경로가 잘못됨

**해결**:
```python
# 파일 존재 확인
import os
pdf_path = './data/housing_leasing_law.pdf'
print(f"파일 존재: {os.path.exists(pdf_path)}")
```

### 문제 3: OpenAI API 오류

**원인**: API 키가 설정되지 않음

**해결**:
```bash
# .env 파일 확인
cat .env

# API 키 설정
echo "OPENAI_API_KEY=your-key-here" >> .env
```

### 문제 4: 메모리 부족

**원인**: 너무 많은 문서 처리

**해결**:
```python
# 청크 크기 증가 (청크 수 감소)
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1500,  # 기본 800에서 증가
    chunk_overlap=200,
)
```

---

## 📊 성능 벤치마크

### 기본 설정
- **임베딩**: text-embedding-3-small
- **LLM**: gpt-4o-mini
- **검색**: MMR (k=5)

**예상 성능**:
- 답변 생성 시간: 3-5초
- 답변 정확도: 85-90%
- 비용: 질문당 약 $0.01

### 고성능 설정
- **임베딩**: text-embedding-3-large
- **LLM**: gpt-4o
- **검색**: MMR + Rerank (k=10)

**예상 성능**:
- 답변 생성 시간: 5-8초
- 답변 정확도: 92-95%
- 비용: 질문당 약 $0.05

---

## 🚀 다음 단계 추천

### 즉시 실행 가능
1. ✅ 노트북 실행 및 기본 테스트
2. ✅ 실제 법령 PDF 추가
3. ✅ 다양한 질문으로 테스트

### 단기 목표 (1-2주)
1. 📊 RAG 평가 수행 (`[LLM]_08_RAG_Evalution.ipynb` 참고)
2. 🎨 Gradio 웹 인터페이스 구축
3. 📈 성능 개선 (Reranking, Query Expansion)

### 중기 목표 (1-2개월)
1. 🌐 웹 애플리케이션 배포
2. 📱 모바일 친화적 UI
3. 🔐 사용자 인증 시스템

### 장기 목표 (3-6개월)
1. 🏢 프로덕션 서비스 런칭
2. 📊 사용자 피드백 수집 및 개선
3. 🤖 AI 모델 파인튜닝

---

## 💡 유용한 리소스

### LangChain 문서
- [LangChain RAG Tutorial](https://python.langchain.com/docs/tutorials/rag/)
- [Vector Stores](https://python.langchain.com/docs/integrations/vectorstores/)
- [Retrievers](https://python.langchain.com/docs/how_to/#retrievers)

### RAG 최적화
- [Advanced RAG Techniques](https://blog.langchain.dev/deconstructing-rag/)
- [RAG Evaluation](https://docs.ragas.io/)
- [Query Expansion](https://python.langchain.com/docs/how_to/MultiQueryRetriever/)

### 법률 AI 참고
- [Legal AI Best Practices](https://www.lawgeex.com/resources/legal-ai-best-practices/)
- [AI in Legal Tech](https://www.artificiallawyer.com/)

---

## 📞 지원

### 질문이 있으신가요?

1. **노트북 내 주석 확인**: 각 셀에 상세한 설명이 있습니다
2. **README 참고**: 기본 사용법과 FAQ
3. **이슈 등록**: GitHub Issues에 질문 등록
4. **학습 노트북**: `[LLM]_07_RAG.ipynb` 등 참고

---

**행운을 빕니다! 🎉**

법률 AI 시스템 개발을 시작하세요!
