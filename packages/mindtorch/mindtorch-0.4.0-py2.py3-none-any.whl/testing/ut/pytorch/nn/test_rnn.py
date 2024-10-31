#!/usr/bin/env python
# -*- coding: utf-8 -*-
import mindtorch
import mindtorch.torch as ms_torch
from mindtorch.torch import tensor
import mindtorch.torch.nn.utils.rnn as rnn_utils

from mindspore import context
import mindspore as ms
import numpy as np
import torch
from ...utils import SKIP_ENV_GRAPH_MODE, set_mode_by_env_config, param_compare, is_test_under_ascend_context
set_mode_by_env_config()


def test_rnn_relu():
    input = np.random.random((5, 3, 2)).astype(np.float32)
    ms_tensor = tensor(input)
    ms_rnn = mindtorch.torch.nn.RNN(input_size=2, hidden_size=2, num_layers=1, nonlinearity='relu', bias=True, batch_first=False, dropout=0, bidirectional=False)
    ms_output, ms_h= ms_rnn(ms_tensor)

    torch_rnn = torch.nn.RNN(input_size=2, hidden_size=2, num_layers=1, nonlinearity='relu', bias=True, batch_first=False, dropout=0, bidirectional=False)
    for i in ms_rnn.parameters():
        torch_rnn.__setattr__(i.name, torch.nn.Parameter(torch.Tensor(i.asnumpy())))
    torch_tensor = torch.tensor(input)
    torch_output, torch_h = torch_rnn(torch_tensor)

    param_compare(ms_output, torch_output.detach(), atol=1e-6)
    param_compare(ms_h, torch_h.detach(), atol=1e-6)

def test_rnn_relu_input_2_dim():
    input = np.random.random((5, 2)).astype(np.float32)
    ms_tensor = tensor(input)
    ms_rnn = mindtorch.torch.nn.RNN(input_size=2, hidden_size=2, num_layers=1, nonlinearity='relu', bias=True, batch_first=False, dropout=0, bidirectional=False)
    ms_output, ms_h= ms_rnn(ms_tensor)

    torch_rnn = torch.nn.RNN(input_size=2, hidden_size=2, num_layers=1, nonlinearity='relu', bias=True, batch_first=True, dropout=0, bidirectional=False)
    for i in ms_rnn.parameters():
        torch_rnn.__setattr__(i.name, torch.nn.Parameter(torch.Tensor(i.asnumpy())))
    torch_tensor = torch.tensor(input)
    torch_output, torch_h = torch_rnn(torch_tensor)

    param_compare(ms_output, torch_output.detach(), atol=1e-6)
    param_compare(ms_h, torch_h.detach(), atol=1e-6)

def test_rnn_tanh():
    input = np.random.random((5, 3, 2)).astype(np.float32)
    h0 =  np.random.random((4, 5, 2)).astype(np.float32)
    ms_tensor = tensor(input)
    ms_h0 = tensor(h0)
    ms_rnn = mindtorch.torch.nn.RNN(input_size=2, hidden_size=2, num_layers=2, nonlinearity='tanh', bias=True, batch_first=True, dropout=0, bidirectional=True)
    ms_output, ms_h= ms_rnn(ms_tensor, ms_h0)

    torch_rnn = torch.nn.RNN(input_size=2, hidden_size=2, num_layers=2, nonlinearity='tanh', bias=True, batch_first=True, dropout=0, bidirectional=True)
    for i in ms_rnn.parameters():
        torch_rnn.__setattr__(i.name, torch.nn.Parameter(torch.Tensor(i.asnumpy())))
    torch_tensor = torch.tensor(input)
    torch_h0 = torch.tensor(h0)
    torch_output, torch_h = torch_rnn(torch_tensor, torch_h0)

    param_compare(ms_output, torch_output.detach(), atol=1e-6)
    param_compare(ms_h, torch_h.detach(), atol=1e-6)


@SKIP_ENV_GRAPH_MODE(reason='class PackedSequence can not be recognize in graph. it is treated as tuple in graph.')
def test_rnn_packed_sequence():
    data = [ms_torch.tensor([[1], [2.], [3]]),ms_torch.tensor([[4.], [5]]), ms_torch.tensor([[6.], [7], [8]])]
    x = rnn_utils.pad_sequence(data, batch_first=True, padding_value=0)
    lengths = [3, 2, 3]
    packed = rnn_utils.pack_padded_sequence(x, lengths, batch_first=True, enforce_sorted=False)
    ms_rnn = mindtorch.torch.nn.RNN(input_size=1, hidden_size=3, num_layers=1, nonlinearity='tanh', bias=True, dropout=0, bidirectional=False)
    ms_output, ms_h = ms_rnn(packed)

    data = [torch.tensor([[1], [2.], [3]]),torch.tensor([[4.], [5]]), torch.tensor([[6.], [7], [8]])]
    x = torch.nn.utils.rnn.pad_sequence(data, batch_first=True, padding_value=0)
    lengths = [3, 2, 3]
    packed = torch.nn.utils.rnn.pack_padded_sequence(x, lengths, batch_first=True, enforce_sorted=False)
    tr_rnn = torch.nn.RNN(input_size=1, hidden_size=3, num_layers=1, nonlinearity='tanh', bias=True, dropout=0, bidirectional=False)
    for i in ms_rnn.parameters():
        tr_rnn.__setattr__(i.name, torch.nn.Parameter(torch.Tensor(i.asnumpy())))
    torch_output, torch_h = tr_rnn(packed)

    param_compare(ms_output.data, torch_output.data.detach(), atol=1e-4)
    param_compare(ms_h, torch_h.detach(), atol=1e-4)

@SKIP_ENV_GRAPH_MODE(reason='class PackedSequence can not be recognize in graph. it is treated as tuple in graph.')
def test_rnn_packed_sequence_batch_first_hx():
    data = [ms_torch.tensor([[1], [2.], [3]]),ms_torch.tensor([[4.], [5]]), ms_torch.tensor([[6.], [7], [8]])]
    x = rnn_utils.pad_sequence(data, batch_first=True, padding_value=0)
    lengths = [3, 2, 3]
    packed = rnn_utils.pack_padded_sequence(x, lengths, batch_first=True, enforce_sorted=False)
    ms_rnn = mindtorch.torch.nn.RNN(input_size=1, hidden_size=3, num_layers=1, nonlinearity='tanh',
                                      bias=True, dropout=0, bidirectional=False, batch_first=True)
    hx = ms_torch.zeros((1, 3, 3))
    ms_output, ms_h = ms_rnn(packed, hx)

    data = [torch.tensor([[1], [2.], [3]]),torch.tensor([[4.], [5]]), torch.tensor([[6.], [7], [8]])]
    x = torch.nn.utils.rnn.pad_sequence(data, batch_first=True, padding_value=0)
    lengths = [3, 2, 3]
    packed = torch.nn.utils.rnn.pack_padded_sequence(x, lengths, batch_first=True, enforce_sorted=False)
    tr_rnn = torch.nn.RNN(input_size=1, hidden_size=3, num_layers=1, nonlinearity='tanh',
                          bias=True, dropout=0, bidirectional=False, batch_first=True)
    for i in ms_rnn.parameters():
        tr_rnn.__setattr__(i.name, torch.nn.Parameter(torch.Tensor(i.asnumpy())))
    hx = torch.zeros((1, 3, 3))
    torch_output, torch_h = tr_rnn(packed, hx)

    param_compare(ms_output.data, torch_output.data.detach(), atol=1e-4)
    param_compare(ms_h, torch_h.detach(), atol=1e-4)

@SKIP_ENV_GRAPH_MODE(reason='class PackedSequence can not be recognize in graph. it is treated as tuple in graph.')
def test_rnn_packed_sequence_enforce_sorted_true():
    data = [ms_torch.tensor([[1], [2.], [3]]), ms_torch.tensor([[6.], [7], [8]]), ms_torch.tensor([[4.], [5]])]
    x = rnn_utils.pad_sequence(data, batch_first=True, padding_value=0)
    lengths = [3, 3, 2]
    packed = rnn_utils.pack_padded_sequence(x, lengths, batch_first=True, enforce_sorted=True)
    ms_rnn = mindtorch.torch.nn.RNN(input_size=1, hidden_size=3, num_layers=1, nonlinearity='tanh', bias=True, dropout=0, bidirectional=False)
    ms_output, ms_h = ms_rnn(packed)

    data = [torch.tensor([[1], [2.], [3]]), torch.tensor([[6.], [7], [8]]), torch.tensor([[4.], [5]])]
    x = torch.nn.utils.rnn.pad_sequence(data, batch_first=True, padding_value=0)
    lengths = [3, 3, 2]
    packed = torch.nn.utils.rnn.pack_padded_sequence(x, lengths, batch_first=True, enforce_sorted=True)
    tr_rnn = torch.nn.RNN(input_size=1, hidden_size=3, num_layers=1, nonlinearity='tanh', bias=True, dropout=0, bidirectional=False)
    for i in ms_rnn.parameters():
        tr_rnn.__setattr__(i.name, torch.nn.Parameter(torch.Tensor(i.asnumpy())))
    torch_output, torch_h = tr_rnn(packed)

    param_compare(ms_output.data, torch_output.data.detach(), atol=1e-4)
    param_compare(ms_h, torch_h.detach(), atol=1e-4)

@SKIP_ENV_GRAPH_MODE(reason='class PackedSequence can not be recognize in graph. it is treated as tuple in graph.')
def test_rnn_packed_sequence_bidirectional():
    data = [ms_torch.tensor([[1], [2.], [3]]),ms_torch.tensor([[4.], [5]]), ms_torch.tensor([[6.], [7], [8]])]
    x = rnn_utils.pad_sequence(data, batch_first=True, padding_value=0)
    lengths = [3, 2, 3]
    packed = rnn_utils.pack_padded_sequence(x, lengths, batch_first=True, enforce_sorted=False)
    ms_rnn = mindtorch.torch.nn.RNN(input_size=1, hidden_size=3, num_layers=2, nonlinearity='tanh', bias=True, dropout=0, bidirectional=True)
    ms_output, ms_h = ms_rnn(packed)

    data = [torch.tensor([[1], [2.], [3]]),torch.tensor([[4.], [5]]), torch.tensor([[6.], [7], [8]])]
    x = torch.nn.utils.rnn.pad_sequence(data, batch_first=True, padding_value=0)
    lengths = [3, 2, 3]
    packed = torch.nn.utils.rnn.pack_padded_sequence(x, lengths, batch_first=True, enforce_sorted=False)
    tr_rnn = torch.nn.RNN(input_size=1, hidden_size=3, num_layers=2, nonlinearity='tanh', bias=True, dropout=0, bidirectional=True)
    for i in ms_rnn.parameters():
        tr_rnn.__setattr__(i.name, torch.nn.Parameter(torch.Tensor(i.asnumpy())))
    torch_output, torch_h = tr_rnn(packed)

    if is_test_under_ascend_context():
        param_compare(ms_output.data, torch_output.data.detach(), atol=1e-3, rtol=1e-3)
        param_compare(ms_h, torch_h.detach(), atol=1e-3, rtol=1e-3)
    else:
        param_compare(ms_output.data, torch_output.data.detach(), atol=1e-4)
        param_compare(ms_h, torch_h.detach(), atol=1e-4)

def test_gru1():
    input = np.random.random((5, 3, 2)).astype(np.float32)
    h0 =  np.random.random((4, 3, 16)).astype(np.float32)

    ms_tensor = tensor(input)
    ms_h0 = tensor(h0)
    ms_gru = mindtorch.torch.nn.GRU(input_size=2, hidden_size=16, num_layers=2, bias=True, batch_first=False, dropout=0, bidirectional=True)
    ms_output, ms_h = ms_gru(ms_tensor, ms_h0)

    torch_tensor = torch.tensor(input)
    torch_h0 = torch.tensor(h0)
    torch_gru = torch.nn.GRU(input_size=2, hidden_size=16, num_layers=2, bias=True, batch_first=False, dropout=0, bidirectional=True)
    for i in ms_gru.parameters():
        torch_gru.__setattr__(i.name, torch.nn.Parameter(torch.Tensor(i.asnumpy())))

    torch_output, torch_h = torch_gru(torch_tensor, torch_h0)

    if is_test_under_ascend_context():
        param_compare(ms_output, torch_output.detach(), atol=1e-3, rtol=1e-3)
        param_compare(ms_h, torch_h.detach(), atol=1e-3, rtol=1e-3)
    else:
        param_compare(ms_output, torch_output.detach(), atol=1e-6)
        param_compare(ms_h, torch_h.detach(), atol=1e-6)

def test_gru2():
    input = np.random.random((3, 5, 2)).astype(np.float32)

    ms_tensor = tensor(input)
    ms_gru = mindtorch.torch.nn.GRU(input_size=2, hidden_size=16, num_layers=1, bias=False, batch_first=False, dropout=0, bidirectional=False)
    ms_output, ms_h = ms_gru(ms_tensor)

    torch_tensor = torch.tensor(input)
    torch_gru = torch.nn.GRU(input_size=2, hidden_size=16, num_layers=1, bias=False, batch_first=False, dropout=0, bidirectional=False)
    for i in ms_gru.parameters():
        torch_gru.__setattr__(i.name, torch.nn.Parameter(torch.Tensor(i.asnumpy())))
    torch_output, torch_h = torch_gru(torch_tensor)

    if is_test_under_ascend_context():
        param_compare(ms_output, torch_output.detach(), atol=1e-3, rtol=1e-3)
        param_compare(ms_h, torch_h.detach(), atol=1e-3, rtol=1e-3)
    else:
        param_compare(ms_output, torch_output.detach(), atol=1e-6)
        param_compare(ms_h, torch_h.detach(), atol=1e-6)

@SKIP_ENV_GRAPH_MODE(reason='class PackedSequence can not be recognize in graph. it is treated as tuple in graph.')
def test_gru_packed_sequence():
    data = [ms_torch.tensor([[1], [2.], [3]]),ms_torch.tensor([[4.], [5]]), ms_torch.tensor([[6.], [7], [8]])]
    x = rnn_utils.pad_sequence(data, batch_first=True, padding_value=0)
    lengths = [3, 2, 3]
    packed = rnn_utils.pack_padded_sequence(x, lengths, batch_first=True, enforce_sorted=False)
    ms_rnn = mindtorch.torch.nn.GRU(input_size=1, hidden_size=16, num_layers=1, bias=True, dropout=0, bidirectional=False)
    ms_output, ms_h = ms_rnn(packed)

    data = [torch.tensor([[1], [2.], [3]]),torch.tensor([[4.], [5]]), torch.tensor([[6.], [7], [8]])]
    x = torch.nn.utils.rnn.pad_sequence(data, batch_first=True, padding_value=0)
    lengths = [3, 2, 3]
    packed = torch.nn.utils.rnn.pack_padded_sequence(x, lengths, batch_first=True, enforce_sorted=False)
    tr_rnn = torch.nn.GRU(input_size=1, hidden_size=16, num_layers=1, bias=True, dropout=0, bidirectional=False)
    for i in ms_rnn.parameters():
        tr_rnn.__setattr__(i.name, torch.nn.Parameter(torch.Tensor(i.asnumpy())))
    torch_output, torch_h = tr_rnn(packed)

    if is_test_under_ascend_context():
        param_compare(ms_output.data, torch_output.data.detach(), atol=1e-3, rtol=1e-3)
        param_compare(ms_h, torch_h.detach(), atol=1e-3, rtol=1e-3)
    else:
        param_compare(ms_output.data, torch_output.data.detach(), atol=1e-6)
        param_compare(ms_h, torch_h.detach(), atol=1e-6)

def test_lstm1():
    input = np.random.random((5, 3, 2)).astype(np.float32)
    h0 = np.random.random((4, 3, 2)).astype(np.float32)
    c0 = np.random.random((4, 3, 2)).astype(np.float32)
    ms_tensor = tensor(input)
    ms_h0 = tensor(h0)
    ms_c0 = tensor(c0)
    ms_lstm = mindtorch.torch.nn.LSTM(input_size=2, hidden_size=2, num_layers=2, bias=True, batch_first=False, dropout=0, bidirectional=True)
    ms_output, ms_hc = ms_lstm(ms_tensor, (ms_h0, ms_c0))

    torch_tensor = torch.tensor(input)
    torch_h0 = torch.tensor(h0)
    torch_c0 = torch.tensor(c0)
    torch_lstm = torch.nn.LSTM(input_size=2, hidden_size=2, num_layers=2, bias=True, batch_first=False, dropout=0, bidirectional=True)
    for i in ms_lstm.parameters():
        torch_lstm.__setattr__(i.name, torch.nn.Parameter(torch.Tensor(i.asnumpy())))
    torch_output, torch_hc = torch_lstm(torch_tensor, (torch_h0, torch_c0))

    if is_test_under_ascend_context():
        param_compare(ms_output, torch_output.detach(), atol=1e-3, rtol=1e-3)
        param_compare(ms_hc[0], torch_hc[0].detach(), atol=1e-3, rtol=1e-3)
        param_compare(ms_hc[1], torch_hc[1].detach(), atol=1e-3, rtol=1e-3)
    else:
        param_compare(ms_output, torch_output.detach(), atol=1e-6)
        param_compare(ms_hc[0], torch_hc[0].detach(), atol=1e-6)
        param_compare(ms_hc[1], torch_hc[1].detach(), atol=1e-6)

def test_lstm2():
    input = np.random.random((3, 5, 2)).astype(np.float32)

    ms_tensor = tensor(input)
    ms_lstm = mindtorch.torch.nn.LSTM(input_size=2, hidden_size=2, num_layers=1, bias=False, batch_first=True, dropout=0, bidirectional=False)
    ms_output, ms_hc = ms_lstm(ms_tensor)

    torch_tensor = torch.tensor(input)
    torch_lstm = torch.nn.LSTM(input_size=2, hidden_size=2, num_layers=1, bias=False, batch_first=True, dropout=0, bidirectional=False)
    for i in ms_lstm.parameters():
        torch_lstm.__setattr__(i.name, torch.nn.Parameter(torch.Tensor(i.asnumpy())))
    torch_output, torch_hc = torch_lstm(torch_tensor)

    if is_test_under_ascend_context():
        param_compare(ms_output, torch_output.detach(), atol=1e-3, rtol=1e-3)
        param_compare(ms_hc[0], torch_hc[0].detach(), atol=1e-3, rtol=1e-3)
        param_compare(ms_hc[1], torch_hc[1].detach(), atol=1e-3, rtol=1e-3)
    else:
        param_compare(ms_output, torch_output.detach(), atol=1e-6)
        param_compare(ms_hc[0], torch_hc[0].detach(), atol=1e-6)
        param_compare(ms_hc[1], torch_hc[1].detach(), atol=1e-6)

def test_lstm_proj_size():
    input = np.random.random((3, 5, 2)).astype(np.float32)

    ms_tensor = tensor(input)
    ms_lstm = mindtorch.torch.nn.LSTM(input_size=2, hidden_size=3, num_layers=1, bias=False, batch_first=True, dropout=0, bidirectional=False, proj_size=2)

    ms_output, ms_hc = ms_lstm(ms_tensor)

    torch_tensor = torch.tensor(input)
    torch_lstm = torch.nn.LSTM(input_size=2, hidden_size=3, num_layers=1, bias=False, batch_first=True, dropout=0, bidirectional=False, proj_size=2)

    for i in ms_lstm.parameters():
        torch_lstm.__setattr__(i.name, torch.nn.Parameter(torch.Tensor(i.asnumpy())))
    torch_output, torch_hc = torch_lstm(torch_tensor)

    param_compare(ms_output, torch_output.detach(), atol=1e-6)
    param_compare(ms_hc[0], torch_hc[0].detach(), atol=1e-6)
    param_compare(ms_hc[1], torch_hc[1].detach(), atol=1e-6)

def test_lstm_proj_size_bidirectional():
    input = np.random.random((3, 5, 2)).astype(np.float32)

    ms_tensor = tensor(input)
    ms_lstm = mindtorch.torch.nn.LSTM(input_size=2, hidden_size=3, num_layers=2, bias=True, batch_first=True, dropout=0, bidirectional=True, proj_size=2)
    ms_output, ms_hc = ms_lstm(ms_tensor)

    torch_tensor = torch.tensor(input)
    torch_lstm = torch.nn.LSTM(input_size=2, hidden_size=3, num_layers=2, bias=True, batch_first=True, dropout=0, bidirectional=True, proj_size=2)
    for i in ms_lstm.parameters():
        torch_lstm.__setattr__(i.name, torch.nn.Parameter(torch.Tensor(i.asnumpy())))
    torch_output, torch_hc = torch_lstm(torch_tensor)

    param_compare(ms_output, torch_output.detach(), atol=1e-6)
    param_compare(ms_hc[0], torch_hc[0].detach(), atol=1e-6)
    param_compare(ms_hc[1], torch_hc[1].detach(), atol=1e-6)

@SKIP_ENV_GRAPH_MODE(reason='class PackedSequence can not be recognize in graph. it is treated as tuple in graph.')
def test_lstm_packed_sequence():
    data = [ms_torch.tensor([[1], [2.], [3]]),ms_torch.tensor([[4.], [5]]), ms_torch.tensor([[6.], [7], [8]])]
    x = rnn_utils.pad_sequence(data, batch_first=True, padding_value=0)
    lengths = [3, 2, 3]
    packed = rnn_utils.pack_padded_sequence(x, lengths, batch_first=True, enforce_sorted=False)
    ms_lstm = mindtorch.torch.nn.LSTM(input_size=1, hidden_size=3, num_layers=1, bias=True, dropout=0, bidirectional=False)
    ms_output, (ms_h, ms_c) = ms_lstm(packed)

    data = [torch.tensor([[1], [2.], [3]]),torch.tensor([[4.], [5]]), torch.tensor([[6.], [7], [8]])]
    x = torch.nn.utils.rnn.pad_sequence(data, batch_first=True, padding_value=0)
    lengths = [3, 2, 3]
    packed = torch.nn.utils.rnn.pack_padded_sequence(x, lengths, batch_first=True, enforce_sorted=False)
    tr_lstm = torch.nn.LSTM(input_size=1, hidden_size=3, num_layers=1, bias=True, dropout=0, bidirectional=False)
    for i in ms_lstm.parameters():
        tr_lstm.__setattr__(i.name, torch.nn.Parameter(torch.Tensor(i.asnumpy())))
    torch_output, (torch_h, torch_c) = tr_lstm(packed)

    if is_test_under_ascend_context():
        param_compare(ms_output.data, torch_output.data.detach(), atol=1e-3, rtol=1e-3)
        param_compare(ms_h, torch_h.detach(), atol=1e-3, rtol=1e-3)
        param_compare(ms_c, torch_c.detach(), atol=1e-3, rtol=1e-3)
    else:
        param_compare(ms_output.data, torch_output.data.detach(), atol=1e-5)
        param_compare(ms_h, torch_h.detach(), atol=1e-4)
        param_compare(ms_c, torch_c.detach(), atol=3e-4)

@SKIP_ENV_GRAPH_MODE(reason='class PackedSequence can not be recognize in graph. it is treated as tuple in graph.')
def test_lstm_packed_sequence_batch_first_hx():
    data = [ms_torch.tensor([[1], [2.], [3]]),ms_torch.tensor([[4.], [5]]), ms_torch.tensor([[6.], [7], [8]])]
    x = rnn_utils.pad_sequence(data, batch_first=True, padding_value=0)
    lengths = [3, 2, 3]
    packed = rnn_utils.pack_padded_sequence(x, lengths, batch_first=True, enforce_sorted=False)
    ms_lstm = mindtorch.torch.nn.LSTM(input_size=1, hidden_size=3, num_layers=1,
                                        bias=True, dropout=0, bidirectional=False, batch_first=True)
    hx = ms_torch.zeros((1, 3, 3))
    cx = ms_torch.zeros((1, 3, 3))
    ms_output, (ms_h, ms_c) = ms_lstm(packed, (hx, cx))

    data = [torch.tensor([[1], [2.], [3]]),torch.tensor([[4.], [5]]), torch.tensor([[6.], [7], [8]])]
    x = torch.nn.utils.rnn.pad_sequence(data, batch_first=True, padding_value=0)
    lengths = [3, 2, 3]
    packed = torch.nn.utils.rnn.pack_padded_sequence(x, lengths, batch_first=True, enforce_sorted=False)
    tr_lstm = torch.nn.LSTM(input_size=1, hidden_size=3, num_layers=1,
                            bias=True, dropout=0, bidirectional=False, batch_first=True)
    for i in ms_lstm.parameters():
        tr_lstm.__setattr__(i.name, torch.nn.Parameter(torch.Tensor(i.asnumpy())))
    hx = torch.zeros((1, 3, 3))
    cx = torch.zeros((1, 3, 3))
    torch_output, (torch_h, torch_c) = tr_lstm(packed, (hx, cx))

    if is_test_under_ascend_context():
        param_compare(ms_output.data, torch_output.data.detach(), atol=1e-3, rtol=1e-3)
        param_compare(ms_h, torch_h.detach(), atol=1e-3, rtol=1e-3)
        param_compare(ms_c, torch_c.detach(), atol=1e-3, rtol=1e-3)
    else:
        param_compare(ms_output.data, torch_output.data.detach(), atol=1e-5)
        param_compare(ms_h, torch_h.detach(), atol=1e-4)
        param_compare(ms_c, torch_c.detach(), atol=2e-4)

@SKIP_ENV_GRAPH_MODE(reason='class PackedSequence can not be recognize in graph. it is treated as tuple in graph.')
def test_lstm_packed_sequence_enforce_sorted_true():
    data = [ms_torch.tensor([[1], [2.], [3]]),ms_torch.tensor([[6.], [7], [8]]), ms_torch.tensor([[4.], [5]])]
    x = rnn_utils.pad_sequence(data, batch_first=True, padding_value=0)
    lengths = [3, 3, 2]
    packed = rnn_utils.pack_padded_sequence(x, lengths, batch_first=True, enforce_sorted=True)
    ms_lstm = mindtorch.torch.nn.LSTM(input_size=1, hidden_size=3, num_layers=1, bias=True, dropout=0, bidirectional=False)
    ms_output, (ms_h, ms_c) = ms_lstm(packed)

    data = [torch.tensor([[1], [2.], [3]]), torch.tensor([[6.], [7], [8]]), torch.tensor([[4.], [5]])]
    x = torch.nn.utils.rnn.pad_sequence(data, batch_first=True, padding_value=0)
    lengths = [3, 3, 2]
    packed = torch.nn.utils.rnn.pack_padded_sequence(x, lengths, batch_first=True, enforce_sorted=True)
    tr_lstm = torch.nn.LSTM(input_size=1, hidden_size=3, num_layers=1, bias=True, dropout=0, bidirectional=False)
    for i in ms_lstm.parameters():
        tr_lstm.__setattr__(i.name, torch.nn.Parameter(torch.Tensor(i.asnumpy())))
    torch_output, (torch_h, torch_c) = tr_lstm(packed)

    if is_test_under_ascend_context():
        param_compare(ms_output.data, torch_output.data.detach(), atol=1e-3, rtol=1e-3)
        param_compare(ms_h, torch_h.detach(), atol=1e-3, rtol=1e-3)
        param_compare(ms_c, torch_c.detach(), atol=1e-3, rtol=1e-3)
    else:
        param_compare(ms_output.data, torch_output.data.detach(), atol=1e-5)
        param_compare(ms_h, torch_h.detach(), atol=1e-4)
        param_compare(ms_c, torch_c.detach(), atol=1e-4)

@SKIP_ENV_GRAPH_MODE(reason='class PackedSequence can not be recognize in graph. it is treated as tuple in graph.')
def test_lstm_packed_sequence_bidirectional():
    data = [ms_torch.tensor([[1], [2.], [3]]),ms_torch.tensor([[4.], [5]]), ms_torch.tensor([[6.], [7], [8]])]
    x = rnn_utils.pad_sequence(data, batch_first=True, padding_value=0)
    lengths = [3, 2, 3]
    packed = rnn_utils.pack_padded_sequence(x, lengths, batch_first=True, enforce_sorted=False)
    ms_lstm = mindtorch.torch.nn.LSTM(input_size=1, hidden_size=3, num_layers=2, bias=True, dropout=0, bidirectional=True)
    ms_output, (ms_h, ms_c) = ms_lstm(packed)

    data = [torch.tensor([[1], [2.], [3]]),torch.tensor([[4.], [5]]), torch.tensor([[6.], [7], [8]])]
    x = torch.nn.utils.rnn.pad_sequence(data, batch_first=True, padding_value=0)
    lengths = [3, 2, 3]
    packed = torch.nn.utils.rnn.pack_padded_sequence(x, lengths, batch_first=True, enforce_sorted=False)
    tr_lstm = torch.nn.LSTM(input_size=1, hidden_size=3, num_layers=2, bias=True, dropout=0, bidirectional=True)
    for i in ms_lstm.parameters():
        tr_lstm.__setattr__(i.name, torch.nn.Parameter(torch.Tensor(i.asnumpy())))
    torch_output, (torch_h, torch_c) = tr_lstm(packed)

    if is_test_under_ascend_context():
        param_compare(ms_output.data, torch_output.data.detach(), atol=1e-3, rtol=1e-3)
        param_compare(ms_h, torch_h.detach(), atol=1e-3, rtol=1e-3)
        param_compare(ms_c, torch_c.detach(), atol=1e-3, rtol=1e-3)
    else:
        param_compare(ms_output.data, torch_output.data.detach(), atol=1e-4)
        param_compare(ms_h, torch_h.detach(), atol=1e-4)
        param_compare(ms_c, torch_c.detach(), atol=1e-4)

@SKIP_ENV_GRAPH_MODE(reason='class PackedSequence can not be recognize in graph. it is treated as tuple in graph.')
def test_lstm_packed_sequence_bidirectional_proj_size():
    data = [ms_torch.tensor([[1], [2.], [3]]),ms_torch.tensor([[4.], [5]]), ms_torch.tensor([[6.], [7], [8]])]
    x = rnn_utils.pad_sequence(data, batch_first=True, padding_value=0)
    lengths = [3, 2, 3]
    packed = rnn_utils.pack_padded_sequence(x, lengths, batch_first=True, enforce_sorted=False)
    ms_lstm = mindtorch.torch.nn.LSTM(input_size=1, hidden_size=3, num_layers=2, bias=True, dropout=0, bidirectional=True, proj_size=2)
    ms_output, (ms_h, ms_c) = ms_lstm(packed)

    data = [torch.tensor([[1], [2.], [3]]),torch.tensor([[4.], [5]]), torch.tensor([[6.], [7], [8]])]
    x = torch.nn.utils.rnn.pad_sequence(data, batch_first=True, padding_value=0)
    lengths = [3, 2, 3]
    packed = torch.nn.utils.rnn.pack_padded_sequence(x, lengths, batch_first=True, enforce_sorted=False)
    tr_lstm = torch.nn.LSTM(input_size=1, hidden_size=3, num_layers=2, bias=True, dropout=0, bidirectional=True, proj_size=2)
    for i in ms_lstm.parameters():
        tr_lstm.__setattr__(i.name, torch.nn.Parameter(torch.Tensor(i.asnumpy())))
    torch_output, (torch_h, torch_c) = tr_lstm(packed)

    param_compare(ms_output.data, torch_output.data.detach(), atol=1e-4)
    param_compare(ms_h, torch_h.detach(), atol=1e-4)
    param_compare(ms_c, torch_c.detach(), atol=1e-4)

def test_rnncell1():
    _data = np.random.random((2, 3, 2)).astype(np.float32)
    _hx = np.random.random((3, 4)).astype(np.float32)

    ms_rnn = ms_torch.nn.RNNCell(2, 4)
    input = ms_torch.tensor(_data)
    hx = ms_torch.tensor(_hx)
    output = []
    for i in range(2):
        hx = ms_rnn(input[i], hx)
        output.append(hx)
    ms_output = ms_torch.stack(output, dim=0)

    tr_rnn = torch.nn.RNNCell(2, 4)
    for i in ms_rnn.parameters():
        tr_rnn.__setattr__(i.name, torch.nn.Parameter(torch.Tensor(i.asnumpy())))
    input = torch.tensor(_data)
    hx = torch.tensor(_hx)
    output = []
    for i in range(2):
        hx = tr_rnn(input[i], hx)
        output.append(hx)
    torch_output = torch.stack(output, dim=0)

    param_compare(ms_output, torch_output.detach(), atol=1e-6)

def test_rnncell2():
    _data = np.random.random((2, 2)).astype(np.float32)
    _hx = np.random.random((4,)).astype(np.float32)

    ms_rnn = ms_torch.nn.RNNCell(2, 4)
    input = ms_torch.tensor(_data)
    hx = ms_torch.tensor(_hx)
    output = []
    for i in range(2):
        hx = ms_rnn(input[i], hx)
        output.append(hx)
    ms_output = ms_torch.stack(output, dim=0)

    tr_rnn = torch.nn.RNNCell(2, 4)
    for i in ms_rnn.parameters():
        tr_rnn.__setattr__(i.name, torch.nn.Parameter(torch.Tensor(i.asnumpy())))
    input = torch.tensor(_data)
    hx = torch.tensor(_hx)
    output = []
    for i in range(2):
        hx = tr_rnn(input[i], hx)
        output.append(hx)
    torch_output = torch.stack(output, dim=0)

    param_compare(ms_output, torch_output.detach(), atol=1e-6)

def test_rnncell3():
    _data = np.random.random((2, 2)).astype(np.float32)

    ms_rnn = ms_torch.nn.RNNCell(2, 4)
    input = ms_torch.tensor(_data)
    output = []
    for i in range(2):
        hx = ms_rnn(input[i])
        output.append(hx)
    ms_output = ms_torch.stack(output, dim=0)

    tr_rnn = torch.nn.RNNCell(2, 4)
    for i in ms_rnn.parameters():
        tr_rnn.__setattr__(i.name, torch.nn.Parameter(torch.Tensor(i.asnumpy())))
    input = torch.tensor(_data)
    output = []
    for i in range(2):
        hx = tr_rnn(input[i])
        output.append(hx)
    torch_output = torch.stack(output, dim=0)

    param_compare(ms_output, torch_output.detach(), atol=1e-6)

def test_grucell1():
    _data = np.random.random((2, 3, 2)).astype(np.float32)
    _hx = np.random.random((3, 4)).astype(np.float32)

    ms_gru = ms_torch.nn.GRUCell(2, 4)
    input = ms_torch.tensor(_data)
    hx = ms_torch.tensor(_hx)
    output = []
    for i in range(2):
        hx = ms_gru(input[i], hx)
        output.append(hx)
    ms_output = ms_torch.stack(output, dim=0)

    tr_gru = torch.nn.GRUCell(2, 4)
    for i in ms_gru.parameters():
        tr_gru.__setattr__(i.name, torch.nn.Parameter(torch.Tensor(i.asnumpy())))
    input = torch.tensor(_data)
    hx = torch.tensor(_hx)
    output = []
    for i in range(2):
        hx = tr_gru(input[i], hx)
        output.append(hx)
    torch_output = torch.stack(output, dim=0)

    param_compare(ms_output, torch_output.detach(), atol=1e-6)

def test_grucell2():
    _data = np.random.random((2, 2)).astype(np.float32)
    _hx = np.random.random((4,)).astype(np.float32)

    ms_gru = ms_torch.nn.GRUCell(2, 4)
    input = ms_torch.tensor(_data)
    hx = ms_torch.tensor(_hx)
    output = []
    for i in range(2):
        hx = ms_gru(input[i], hx)
        output.append(hx)
    ms_output = ms_torch.stack(output, dim=0)

    tr_gru = torch.nn.GRUCell(2, 4)
    for i in ms_gru.parameters():
        tr_gru.__setattr__(i.name, torch.nn.Parameter(torch.Tensor(i.asnumpy())))
    input = torch.tensor(_data)
    hx = torch.tensor(_hx)
    output = []
    for i in range(2):
        hx = tr_gru(input[i], hx)
        output.append(hx)
    torch_output = torch.stack(output, dim=0)

    param_compare(ms_output, torch_output.detach(), atol=1e-6)

def test_grucell3():
    _data = np.random.random((2, 2)).astype(np.float32)

    ms_gru = ms_torch.nn.GRUCell(2, 4)
    input = ms_torch.tensor(_data)
    output = []
    for i in range(2):
        hx = ms_gru(input[i])
        output.append(hx)
    ms_output = ms_torch.stack(output, dim=0)

    tr_gru = torch.nn.GRUCell(2, 4)
    for i in ms_gru.parameters():
        tr_gru.__setattr__(i.name, torch.nn.Parameter(torch.Tensor(i.asnumpy())))
    input = torch.tensor(_data)
    output = []
    for i in range(2):
        hx = tr_gru(input[i])
        output.append(hx)
    torch_output = torch.stack(output, dim=0)

    param_compare(ms_output, torch_output.detach(), atol=1e-6)

def test_grucell_bias_false():
    _data = np.random.random((2, 3, 2)).astype(np.float32)
    _hx = np.random.random((3, 4)).astype(np.float32)

    ms_gru = ms_torch.nn.GRUCell(2, 4, bias=False)
    input = ms_torch.tensor(_data)
    hx = ms_torch.tensor(_hx)
    output = []
    for i in range(2):
        hx = ms_gru(input[i], hx)
        output.append(hx)
    ms_output = ms_torch.stack(output, dim=0)

    tr_gru = torch.nn.GRUCell(2, 4, bias=False)
    for i in ms_gru.parameters():
        tr_gru.__setattr__(i.name, torch.nn.Parameter(torch.Tensor(i.asnumpy())))
    input = torch.tensor(_data)
    hx = torch.tensor(_hx)
    output = []
    for i in range(2):
        hx = tr_gru(input[i], hx)
        output.append(hx)
    torch_output = torch.stack(output, dim=0)

    param_compare(ms_output, torch_output.detach(), atol=1e-6)

def test_lstmcell1():
    _data = np.random.random((2, 3, 2)).astype(np.float32)
    _hx = np.random.random((3, 4)).astype(np.float32)
    _cx = np.random.random((3, 4)).astype(np.float32)

    ms_lstm = ms_torch.nn.LSTMCell(2, 4) # (input_size, hidden_size)
    input = ms_torch.tensor(_data) # (time_steps, batch, input_size)
    hx = ms_torch.tensor(_hx) # (batch, hidden_size)
    cx = ms_torch.tensor(_cx)
    output = []
    cx_out = []
    for i in range(input.shape[0]):
        hx, cx = ms_lstm(input[i], (hx, cx))
        output.append(hx)
        cx_out.append(cx)
    ms_output = ms_torch.stack(output, dim=0)
    ms_cx = ms_torch.stack(cx_out, dim=0)

    tr_lstm = torch.nn.LSTMCell(2, 4) # (input_size, hidden_size)
    for i in ms_lstm.parameters():
        tr_lstm.__setattr__(i.name, torch.nn.Parameter(torch.Tensor(i.asnumpy())))
    input = torch.tensor(_data) # (time_steps, batch, input_size)
    hx = torch.tensor(_hx) # (batch, hidden_size)
    cx = torch.tensor(_cx)
    output = []
    cx_out = []
    for i in range(input.size()[0]):
        hx, cx = tr_lstm(input[i], (hx, cx))
        output.append(hx)
        cx_out.append(cx)
    torch_output = torch.stack(output, dim=0)
    torch_cx = torch.stack(cx_out, dim=0)

    param_compare(ms_output, torch_output.detach(), atol=1e-6)
    param_compare(ms_cx, torch_cx.detach(), atol=1e-6)

def test_lstmcell2():
    _data = np.random.random((2, 2)).astype(np.float32)
    _hx = np.random.random((4,)).astype(np.float32)
    _cx = np.random.random((4,)).astype(np.float32)

    ms_lstm = ms_torch.nn.LSTMCell(2, 4) # (input_size, hidden_size)
    input = ms_torch.tensor(_data) # (time_steps, batch, input_size)
    hx = ms_torch.tensor(_hx) # (batch, hidden_size)
    cx = ms_torch.tensor(_cx)
    output = []
    cx_out = []
    for i in range(input.shape[0]):
        hx, cx = ms_lstm(input[i], (hx, cx))
        output.append(hx)
        cx_out.append(cx)
    ms_output = ms_torch.stack(output, dim=0)
    ms_cx = ms_torch.stack(cx_out, dim=0)

    tr_lstm = torch.nn.LSTMCell(2, 4) # (input_size, hidden_size)
    for i in ms_lstm.parameters():
        tr_lstm.__setattr__(i.name, torch.nn.Parameter(torch.Tensor(i.asnumpy())))
    input = torch.tensor(_data) # (time_steps, batch, input_size)
    hx = torch.tensor(_hx) # (batch, hidden_size)
    cx = torch.tensor(_cx)
    output = []
    cx_out = []
    for i in range(input.size()[0]):
        hx, cx = tr_lstm(input[i], (hx, cx))
        output.append(hx)
        cx_out.append(cx)
    torch_output = torch.stack(output, dim=0)
    torch_cx = torch.stack(cx_out, dim=0)

    param_compare(ms_output, torch_output.detach(), atol=1e-6)
    param_compare(ms_cx, torch_cx.detach(), atol=1e-6)

def test_lstmcell3():
    _data = np.random.random((2, 3, 2)).astype(np.float32)

    ms_lstm = ms_torch.nn.LSTMCell(2, 4) # (input_size, hidden_size)
    input = ms_torch.tensor(_data) # (time_steps, batch, input_size)
    output = []
    cx_out = []
    for i in range(input.shape[0]):
        hx, cx = ms_lstm(input[i])
        output.append(hx)
        cx_out.append(cx)
    ms_output = ms_torch.stack(output, dim=0)
    ms_cx = ms_torch.stack(cx_out, dim=0)

    tr_lstm = torch.nn.LSTMCell(2, 4) # (input_size, hidden_size)
    for i in ms_lstm.parameters():
        tr_lstm.__setattr__(i.name, torch.nn.Parameter(torch.Tensor(i.asnumpy())))
    input = torch.tensor(_data) # (time_steps, batch, input_size)
    output = []
    cx_out = []
    for i in range(input.size()[0]):
        hx, cx = tr_lstm(input[i])
        output.append(hx)
        cx_out.append(cx)
    torch_output = torch.stack(output, dim=0)
    torch_cx = torch.stack(cx_out, dim=0)

    param_compare(ms_output, torch_output.detach(), atol=1e-6)
    param_compare(ms_cx, torch_cx.detach(), atol=1e-6)

@SKIP_ENV_GRAPH_MODE(reason="[CI] ms2.4.0 0920 not pass, timeout.")
def test_gru_2d_input_batch_first_check_hidden_size():
    # GRU only support hidden size to be divisible by 16 on ascend, so here we use 16 hidden_size, 32 input_size.
    data = np.random.rand(32, 32).astype(np.float32)

    ms_input = ms_torch.tensor(data)
    ms_gru = ms_torch.nn.GRU(32, 32 // 2, num_layers=2, batch_first=True, dropout=0, bidirectional=True)
    ms_output, ms_h = ms_gru(ms_input)

    pt_input = torch.tensor(data)
    pt_gru = torch.nn.GRU(32, 32 // 2, num_layers=2, batch_first=True, dropout=0, bidirectional=True)
    for i in ms_gru.parameters():
        pt_gru.__setattr__(i.name, torch.nn.Parameter(torch.Tensor(i.asnumpy())))
    pt_output, pt_h = pt_gru(pt_input)

    if is_test_under_ascend_context():
        _atol = 1e-3
    else:
        _atol = 1e-6
    param_compare(ms_output, pt_output.detach(), atol=_atol)
    param_compare(ms_h, pt_h.detach(), atol=_atol)

def test_lstm_2d_input_batch_first_check_hidden_size():
    input = np.random.random((3, 2)).astype(np.float32)

    ms_tensor = tensor(input)
    ms_lstm = mindtorch.torch.nn.LSTM(input_size=2, hidden_size=2, num_layers=1, bias=False, batch_first=True, dropout=0, bidirectional=False)
    ms_output, ms_hc = ms_lstm(ms_tensor)

    torch_tensor = torch.tensor(input)
    torch_lstm = torch.nn.LSTM(input_size=2, hidden_size=2, num_layers=1, bias=False, batch_first=True, dropout=0, bidirectional=False)
    for i in ms_lstm.parameters():
        torch_lstm.__setattr__(i.name, torch.nn.Parameter(torch.Tensor(i.asnumpy())))
    torch_output, torch_hc = torch_lstm(torch_tensor)

    if is_test_under_ascend_context():
        param_compare(ms_output, torch_output.detach(), atol=1e-3, rtol=1e-3)
        param_compare(ms_hc[0], torch_hc[0].detach(), atol=1e-3, rtol=1e-3)
        param_compare(ms_hc[1], torch_hc[1].detach(), atol=1e-3, rtol=1e-3)
    else:
        param_compare(ms_output, torch_output.detach(), atol=1e-6)
        param_compare(ms_hc[0], torch_hc[0].detach(), atol=1e-6)
        param_compare(ms_hc[1], torch_hc[1].detach(), atol=1e-6)

if __name__ == '__main__':
    set_mode_by_env_config()
    test_rnn_relu()
    test_rnn_tanh()
    test_rnn_relu_input_2_dim()
    test_rnn_packed_sequence()
    test_rnn_packed_sequence_bidirectional()
    test_gru1()
    test_gru2()
    test_gru_packed_sequence()
    test_lstm1()
    test_lstm2()
    test_lstm_packed_sequence()
    test_lstm_packed_sequence_bidirectional()
    test_lstm_proj_size()
    test_lstm_proj_size_bidirectional()
    test_lstm_packed_sequence_bidirectional_proj_size()
    test_rnncell1()
    test_rnncell2()
    test_rnncell3()
    test_grucell1()
    test_grucell2()
    test_grucell3()
    test_lstmcell1()
    test_lstmcell2()
    test_lstmcell3() 
    test_rnn_packed_sequence_enforce_sorted_true()
    test_lstm_packed_sequence_enforce_sorted_true()
    test_grucell_bias_false()
    test_gru_2d_input_batch_first_check_hidden_size()