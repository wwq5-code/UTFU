

import numpy as np
import matplotlib.pyplot as plt

epsilon = 3
beta = 1 / epsilon


x=[1, 2, 3, 4, 5]
# validation_for_plt =[97,95.8600, 94.9400, 93.5400, 93.2400]
# attack_for_plt=[0, 0.3524, 0, 0.1762, 0.1762]
# basic_for_plt=[99.8, 99.8, 99.8, 99.8, 99.8]

labels = ['0.05', '0.1', '0.15', '0.2', '0.25']

unl_fr = [80.4, 80.4, 80.4, 80.4, 80.4]
unl_br = [80.02, 78.95, 79.26, 79.15, 78.01]
unl_self_r = [80.05, 80.18, 79.69, 79.75, 79.61]
unl_hess_r = [78.6,  78.6, 78.6, 78.6, 78.6]


plt.figure()
#plt.figure(figsize=(8, 5.3))
plt.plot(x, unl_fr, color='blue', marker='^', label='Retrain',linewidth=4, markersize=10)
plt.plot(x, unl_br, color='orange',  marker='x',  label='UIAF',linewidth=4,  markersize=10)
plt.plot(x, unl_self_r, color='g',  marker='*',  label='UIAF-U',linewidth=4, markersize=10)
#plt.plot(x, unl_hess_r, color='r',  marker='p',  label='HFU',linewidth=4, markersize=10)
# plt.plot(x, y_sa03, color='r',  marker='2',  label='AAAI21 A_acc, pr=0.3',linewidth=3, markersize=8)
# plt.plot(x, y_sa05, color='darkblue',  marker='4',  label='AAAI21 A_acc, pr=0.5',linewidth=3, markersize=8)
# plt.plot(x, y_ma03, color='darkviolet',  marker='3',  label='FedMC A_acc, pr=0.3',linewidth=3, markersize=8)
# plt.plot(x, y_ma05, color='cyan',  marker='p',  label='FedMC A_acc, pr=0.5',linewidth=3, markersize=8)


# plt.grid()
leg = plt.legend(fancybox=True, shadow=True)
# plt.xlabel('Malicious Client Ratio (%)' ,fontsize=16)
plt.ylabel('Accuracy (%)' ,fontsize=20)
my_y_ticks = np.arange(72 ,83,2)
plt.yticks(my_y_ticks,fontsize=20)

plt.xlabel('$\\beta_u$' ,fontsize=20)
plt.xticks(x, labels, fontsize=20)
# plt.title('CIFAR10 IID')
plt.legend(loc='best',fontsize=20)
plt.tight_layout()
#plt.title("MNIST")
plt.rcParams['figure.figsize'] = (2.0, 1)
plt.rcParams['image.interpolation'] = 'nearest'
plt.rcParams['figure.subplot.left'] = 0.11
plt.rcParams['figure.subplot.bottom'] = 0.08
plt.rcParams['figure.subplot.right'] = 0.977
plt.rcParams['figure.subplot.top'] = 0.969
plt.savefig('cifar_acc_ur_curve.pdf', format='pdf', dpi=200)
plt.show()