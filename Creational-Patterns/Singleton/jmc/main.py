# 프린터 기능 싱글톤 구현

# 메타클래스 활용
class Singleton(type):
    _instance = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instance:
            instance = super().__call__(*args, **kwargs)
            cls._instance[cls] = instance
        return cls._instance[cls]
    

class Printer(metaclass=Singleton):
    def __init__(self) -> None:
        self._ready_docs = []

    def print_document(self, doc):
        self._ready_docs.append(doc)
        print(f"{doc} 문서의 인쇄가 대기열로 들어갑니다.")
    
    def get_ready_docs(self):
        print(self._ready_docs)


# 데코레이터 활용
        
def singleton(cls):
    instances = {}

    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance


@singleton
class Printer():
    def __init__(self) -> None:
        self._ready_docs = []

    def print_document(self, doc):
        self._ready_docs.append(doc)
        print(f"{doc} 문서의 인쇄가 대기열로 들어갑니다.")
    
    def get_ready_docs(self):
        print(self._ready_docs)


p = Printer()
doc1 = "1번 문서"
p.print_document(doc1)

p.get_ready_docs()
# ['1번 문서']


j = Printer()
doc2 = "2번 문서"
j.print_document(doc2)

j.get_ready_docs()
# ['2번 문서']