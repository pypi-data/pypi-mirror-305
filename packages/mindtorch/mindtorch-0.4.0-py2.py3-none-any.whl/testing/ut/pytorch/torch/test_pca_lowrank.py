import mindtorch.torch as torch
from mindtorch.torchvision.datasets.mnist import MNIST
from mindtorch.torch.utils.data import DataLoader
import mindtorch.torchvision.transforms as transforms
import mindspore as ms

## You can open these comments when running offline
# import matplotlib.pyplot as plt
#
# color = ['yellow', 'black', 'aqua', 'green', 'teal', 'orange', 'navy', 'pink', 'purple', 'red']
#
#
# def show(v2, y):
#     for i in range(len(v2)):
#         plt.scatter(v2[i][0], v2[i][1], color=color[y[i]])
#     plt.savefig("2dfig_ms.png")
#
#
# def show3d(v3, y):
#     fig = plt.figure()
#     ax = fig.add_subplot(111, projection='3d')
#     for i in range(len(v3)):
#         ax.scatter(v3[i][0], v3[i][1], v3[i][2], color=color[y[i]])
#     plt.savefig("3dfig_ms.png")

data_train = MNIST('./data/mnist',
                   download=True,
                   transform=transforms.Compose([
                       transforms.Resize((32, 32)),
                       transforms.ToTensor()]))
data_train_loader = DataLoader(data_train, batch_size=128, num_workers=0)

if __name__ == '__main__':
    ms.context.set_context(mode=ms.PYNATIVE_MODE)

    for i,(x, y) in enumerate(data_train_loader):
        x = torch.squeeze(x)

        print(x.shape)
        # pca
        v3 = []
        for i in range(len(x)):
            v3.append(torch.pca_lowrank(x[i], q=3)[1].numpy())  # 3dim
        v2 = []
        for i in range(len(x)):
            v2.append(torch.pca_lowrank(x[i], q=2)[1].numpy())  # 2dim
        print(v2)

        ## You can open these comments when running offline
        # show(v2, y)
        # show3d(v3, y)
        break
