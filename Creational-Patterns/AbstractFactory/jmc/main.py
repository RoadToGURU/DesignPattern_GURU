from abc import ABC, abstractmethod

# GPT, LLaMA 객체 생성 추상팩토리
class LLMFactory(ABC):
    @abstractmethod
    def create_gpt(self) -> GPT:
        pass

    @abstractmethod
    def create_llama(self) -> LLaMA:
        pass

# 특정 라이브러리에 맞는 모델 객체 생성 팩토리
class LangchainFactory(LLMFactory):
    def create_gpt(self) -> GPT:
        return LangchainGPT()

    def create_llama(self) -> LLaMA:
        return LangchainLLaMA()

class LlamaIndexFactory(LLMFactory):
    def create_gpt(self) -> GPT:
        return LlamaIndexGPT()

    def create_llama(self) -> LLaMA:
        return LlamaIndexLLaMA()
    
# GPT, LLaMA 모델 추상 클래스
class GPT(ABC):
    @abstractmethod
    def infer(self) -> str:
        pass

class LLaMA(ABC):
    @abstractmethod
    def infer(self) -> str:
        pass

# 특정 라이브러리의 GPT 및 LLaMA 모델 구체 클래스
class LangchainGPT(GPT):
    def infer(self) -> str:
        return "infer with GPT, Langchain Wrapper"

class LlamaIndexGPT(GPT):
    def infer(self) -> str:
        return "infer with GPT, LlamaIndex Wrapper"

class LangchainLLaMA(LLaMA):
    def infer(self) -> str:
        return "infer with LLaMA, Langchain Wrapper"

class LlamaIndexLLaMA(LLaMA):
    def infer(self) -> str:
        return "infer with LLaMA, LlamaIndex Wrapper"
    

def client_code(factory: LLMFactory) -> None:
    gpt = factory.create_gpt()
    llama = factory.create_llama()

    print(gpt.infer())
    print(llama.infer())

client_code(LangchainFactory())