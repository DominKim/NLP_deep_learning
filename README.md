# NLP_deep_learning


## Python
- 콜백함수(callback) : 내가 함수를 호출하는 것이 아니라 다른 함수에서 호출하는 
``` python3
def call_10_times(func):
  for i in range(10):
    func()
    
def print_hello():
  print("안녕하세요")
  
call_10_times(print_hello)
```
