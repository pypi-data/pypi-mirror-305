import mindtorch.torch as msa_torch

from ...utils import set_mode_by_env_config, param_compare
set_mode_by_env_config()

def test_float_functional_add():
    f_add = msa_torch.nn.quantized.FloatFunctional()
    a = msa_torch.tensor(3.0)
    b = msa_torch.tensor(4.0)
    f_add_out = f_add.add(a, b)
    add_out = msa_torch.add(a, b)
    param_compare(f_add_out, add_out)

def test_float_functional_graph():
    class FFModel(msa_torch.nn.Module):
        def __init__(self,):
            super(FFModel, self).__init__()
            self.ff = msa_torch.nn.quantized.FloatFunctional()

        def forward(self, x, y):
            out = self.ff.add_relu(x, y)
            return out

    ff_net = FFModel()
    a = msa_torch.tensor(3.0)
    b = msa_torch.tensor(4.0)
    f_add_out = ff_net(a, b)
    add_out = msa_torch.add(a, b)
    add_out = msa_torch.nn.functional.relu(add_out)
    param_compare(f_add_out, add_out)

if __name__ == '__main__':
    set_mode_by_env_config()
    test_float_functional_add()
    test_float_functional_graph()
