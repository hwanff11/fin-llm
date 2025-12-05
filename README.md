# 🤖 법률 질의응답 AI 시스템 (Legal QA with RAG)

법령 PDF 파일을 기반으로 법률적 질문에 정확한 답변을 제공하는 RAG(Retrieval-Augmented Generation) 시스템

---

## 📋 프로젝트 개요

이 프로젝트는 **여러 법령 PDF 파일**을 입력받아 **법률 질문에 대한 정확한 답변**을 제공하는 AI 시스템입니다.

### 주요 기능

- 📄 **다중 PDF 문서 처리**: 여러 법령 PDF 파일 동시 로드 및 처리
- ✂️ **법률 조문 최적화 분할**: 법률 문서 구조에 맞춘 텍스트 분할
- 🔢 **고품질 임베딩**: OpenAI 임베딩 모델 활용 (한국어 최적화)
- 🗄️ **벡터 데이터베이스**: Chroma DB 기반 효율적인 검색
- 🤖 **법률 전문 프롬프트**: 법률 자문에 특화된 프롬프트 설계
- 📊 **출처 명시**: 답변의 근거가 되는 법령 조문 및 페이지 표시

---

## 🚀 빠른 시작

### 1. 환경 설정

```bash
# 프로젝트 클론
git clone <repository-url>
cd fin-llm

# 가상환경 활성화 (이미 설정되어 있음)
source .venv/bin/activate

# 필요한 패키지 설치 (uv 사용)
uv sync
```

### 2. 환경 변수 설정

`.env` 파일에 OpenAI API 키를 설정하세요:

```bash
OPENAI_API_KEY=your-api-key-here
```

### 3. 노트북 실행

```bash
jupyter notebook "[PROJECT]_Legal_QA_RAG.ipynb"
```

또는 VS Code에서 노트북을 직접 열어서 실행하세요.

---

## 📁 프로젝트 구조

```
fin-llm/
├── [PROJECT]_Legal_QA_RAG.ipynb    # 메인 법률 QA 시스템 노트북
├── [LLM]_07_RAG.ipynb              # RAG 기초 학습 노트북
├── [LLM]_08_RAG_Evalution.ipynb    # RAG 평가 노트북
├── data/
│   ├── housing_leasing_law.pdf     # 주택임대차보호법 (예시)
│   └── *.pdf                       # 추가 법령 PDF 파일
├── chroma_db_legal/                # 벡터 데이터베이스 저장소
├── .env                            # 환경 변수 (API 키)
└── README.md                       # 이 파일
```

---

## 💡 사용 방법

### 기본 사용

1. **노트북 열기**: `[PROJECT]_Legal_QA_RAG.ipynb` 파일을 엽니다.

2. **순서대로 실행**: 셀을 위에서부터 순서대로 실행합니다.

3. **질문하기**: 마지막 섹션에서 법률 질문을 입력하고 답변을 받습니다.

```python
# 질문 예시
my_question = "임대차 계약 기간 중 임대료를 인상할 수 있나요?"
answer = ask_legal_question(my_question)
```

### 새로운 PDF 추가

```python
# 새로운 법령 PDF 추가
new_pdfs = [
    './data/새로운_법령1.pdf',
    './data/새로운_법령2.pdf',
]
add_new_legal_documents(new_pdfs)
```

---

## 🔧 시스템 구성

### 1. 문서 로드 및 처리
- **PyPDFLoader**: PDF 파일 로드
- **RecursiveCharacterTextSplitter**: 법률 조문에 최적화된 텍스트 분할

### 2. 임베딩 및 벡터화
- **OpenAI Embeddings**: `text-embedding-3-small` 모델 사용
- **Chroma DB**: 벡터 저장 및 검색

### 3. 검색 전략
- **MMR (Maximal Marginal Relevance)**: 관련성과 다양성의 균형
- **유사도 검색**: 코사인 유사도 기반

### 4. 답변 생성
- **LLM**: GPT-4o-mini (또는 GPT-4o)
- **프롬프트**: 법률 전문 시스템 프롬프트
- **출력**: 구조화된 답변 (핵심 답변 + 법적 근거 + 추가 설명)

---

## 📊 예시 질문 및 답변

### 질문 1
**Q**: "주택 임대차 계약의 최소 기간은 얼마인가요?"

**A**: 
```
핵심 답변:
주택 임대차 계약의 최소 기간은 2년입니다.

법적 근거:
주택임대차보호법 제4조(임대차기간 등)에 따르면, 
"기간을 정하지 아니하거나 2년 미만으로 정한 임대차는 
그 기간을 2년으로 본다"고 규정하고 있습니다.

추가 설명:
계약서에 1년으로 작성되어 있어도 법적으로는 2년으로 
보호받을 수 있습니다.

주의사항:
본 답변은 법률 정보 제공 목적이며, 구체적인 사안은 
변호사와 상담하시기 바랍니다.
```

---

## ⚙️ 성능 개선 방법

### 1. 더 나은 임베딩 모델
```python
embeddings = OpenAIEmbeddings(model="text-embedding-3-large")
```

### 2. 더 강력한 LLM
```python
llm = ChatOpenAI(model="gpt-4o", temperature=0.1)
```

### 3. 검색 개수 조정
```python
retriever = vector_store.as_retriever(
    search_type="mmr",
    search_kwargs={"k": 10}  # 더 많은 문서 검색
)
```

### 4. 재순위화(Reranking) 추가
- Cohere Rerank API
- Cross-Encoder 모델

### 5. 쿼리 확장(Query Expansion)
- Multi-Query Retriever
- HyDE (Hypothetical Document Embeddings)

---

## 📚 학습 자료

프로젝트에 포함된 학습 노트북:

1. **[LLM]_07_RAG.ipynb**: RAG 시스템 기초
   - 문서 로더
   - 텍스트 분할
   - 임베딩
   - 벡터 저장소
   - RAG 체인 구성

2. **[LLM]_08_RAG_Evalution.ipynb**: RAG 평가
   - 평가 데이터셋 구축
   - 평가 지표 (Faithfulness, Relevancy, etc.)
   - 성능 측정

3. **[LLM]_09_Query_Expansion.ipynb**: 쿼리 확장
   - Multi-Query
   - RAG-Fusion

4. **[LLM]_10_Rerank_Compression.ipynb**: 재순위화
   - Cohere Rerank
   - Contextual Compression

---

## ⚠️ 주의사항

### 법률 자문 아님
이 시스템은 **법률 정보 제공 목적**이며, 공식적인 법률 자문이 아닙니다.

### 전문가 상담 필요
구체적인 법률 문제는 반드시 **변호사 등 법률 전문가**와 상담하세요.

### 최신성 확인
법령은 수시로 개정되므로, **최신 법령**을 확인해야 합니다.

### 정확성 검증
AI의 답변은 참고용이며, 중요한 결정 전에는 **원문을 직접 확인**하세요.

### 개인정보 보호
실제 사건이나 개인정보를 입력하지 마세요.

---

## 🛠️ 기술 스택

- **Python**: 3.12+
- **LangChain**: RAG 파이프라인 구축
- **OpenAI**: LLM 및 임베딩 모델
- **Chroma DB**: 벡터 데이터베이스
- **PyPDF**: PDF 문서 처리
- **Jupyter**: 노트북 환경

---

## 📝 라이선스

이 프로젝트는 교육 목적으로 제작되었습니다.

---

## 🤝 기여

버그 리포트, 기능 제안, 풀 리퀘스트를 환영합니다!

---

## 📧 문의

프로젝트 관련 문의사항이 있으시면 이슈를 등록해주세요.

---

**Made with ❤️ for Legal Tech Innovation**
