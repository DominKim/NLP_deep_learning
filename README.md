# NLP_deep_learning
- colab 멈춤 방지
``` json
function ClickConnect(){
    console.log("코랩 연결 끊김 방지"); 
    document.querySelector("colab-toolbar-button#connect").click() 
}
setInterval(ClickConnect, 60 * 1000)
```

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
- 람다(lambda) : 매개변수로 함수를 전달하기 위해 함수 구문을 작성하는 것이 번거롭고, 코드 낭비라는 생각이 들 때 함수를 간단하고 쉽게 선언하는 방법 = 짧게 쓸 수 있는 문법

- filter(함수(=func), 리스트(=반복요소=iterables)) : 리스트의 요소를 함수에 넣고 리턴된 값이 True인 것으로 새로운 리스트를 구성해주는 함수

- map(함수(=func), 리스트(=반복요소=iterables)) : 기존 리스트 기반으로 신규 리스트 만들 때 사용

- transfomrs.ToTensor() : 0 ~ 1 사이로 스케일링


 
| Model | train_loss | valid_loss | RMSE |
| -------------| ------------- | ------------- | ------------- |
| transfer_learing_resnet34-use_trained_freeze_epoch20-batch8| 1.4222e+04 | 1.2300e+04	| 105.03642 |
| transfer_learing_densnet121-use_trained_freeze_epoch20-batch8 | 1.4091e+04 | 1.2923e+04   | 103.90428 |
| densenet121-use_trained-freeze-epoch20-batch8 | 1.7068e+02 | 1.3420e+02   | 103.90428 |
| densenet121-use_trained-freeze-epoch20-batch8_albumentation_normalize_hori_random_vertical_motion_gaussnoise | 3.9548e+02 | 2.0384e+02   | 98.06773  |
| densenet121-use_trained-freeze-epoch50-batch32_albumentation_normalize_hori_random_vertical_motion_gaussnoise.pth | 3.5934e+02 | 1.6615e+02 | 98.06773 |
| densenet121-use_trained-freeze-epoch50-batch32_albumentation_hori_random_vertical_motion_gaussnoise.pth | 3.4917e+02 | 1.7434e+02 | 98.06773 |
| keypoint-rcnn-e50-bs8-albu | - | - | 81.30218 |
| keypointrcnn_resnet50e10-bs8-newalbu.pth | - | - | 53.3512 |
| keypointrcnn_resnet50e20-bs8-newalbu-swa-lr.pth | 2.8293 | - | 42.36044 |
| keypointrcnn_resnet50e20-bs16-newalbu-swa-lr.pth | 2.6189 | - | 42.36044 |
| keypointrcnn_resnet101e30-bs8-newalbu-swa-lr.pth | 2.15212 | ~  | 42.36044 |
| keypointrcnn_resnet101e50-bs8-newalbu-swa-lr.pth | 2.6395 | 2.2781e+01  | 42.36044 |
