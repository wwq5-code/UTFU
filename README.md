# UIAF-U

# User-side Influence Approximation Forgetting with Utility Preservation (UIAF-U) for Federated Unlearning


### Overview
This repository is the official implementation of UIAF-U, and the corresponding paper is under review.


### Prerequisites

```
python = 3.10.10
torch==2.0.0
torchvision==0.15.1
matplotlib==3.7.1
numpy==1.23.5
```

### Running the experiments

1. To run the URF and UIAF-U on MNIST
```
python /Federated_learning/BackdoorFedUnl/BackdoorFedAvg.py
```

2. To run the URF and UIAF-U on CIFAR10
```
python /Federated_learning/BackdoorFedUnl/backdoorUnl_cifar_er/CIFAR10_er02_3ke.py
```

3. To run our reproduced and improved HFU on MNIST
```
python /Federated_learning/Unl-subtract_hessian/backdoor_FedHessian.py
```

4. To run our reproduced and improved HFU on CIFAR
```
python /Federated_learning/Unl-subtract_hessian/Hessian_backddor_CIFAR/cifar_hessian_u/hessian_cifar_temp.py
```
### Results
Our model achieves a better performance than state-of-the-art federated unlearning methods