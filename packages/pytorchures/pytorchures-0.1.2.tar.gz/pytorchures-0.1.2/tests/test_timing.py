import torch
import torch.nn as nn
import torch.nn.functional as F

from pytorchures import TimedModule


def test_conv_layer_wrapping():
    model = nn.Conv2d(in_channels=1, out_channels=16, kernel_size=3, padding=1)
    model = TimedModule(model)
    input_tensor = torch.randn(1, 1, 28, 28)

    output = model(input_tensor)

    assert output is not None
    assert model.get_timings()["module_name"] == "Conv2d"


def test_sequential_wrapping():
    model = nn.Sequential(nn.Conv2d(in_channels=1, out_channels=16, kernel_size=3, padding=1))

    model = TimedModule(model)

    layers = model._module.named_children()

    _, timed_conv = next(layers)

    assert isinstance(timed_conv, TimedModule)
    assert isinstance(timed_conv._module, nn.Conv2d)


def test_nested_sequential_wrapping():
    model = nn.Sequential(
        nn.Sequential(
            nn.Conv2d(in_channels=1, out_channels=16, kernel_size=3, padding=1),
        ),
        nn.Conv2d(in_channels=1, out_channels=16, kernel_size=3, padding=1),
    )

    model = TimedModule(model)

    layers = model._module.named_children()

    _, timed_seq = next(layers)
    _, nested_conv = next(timed_seq._module.named_children())

    assert isinstance(nested_conv, TimedModule)
    assert isinstance(nested_conv._module, nn.Conv2d)


class SimpleCNN(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = nn.Conv2d(in_channels=1, out_channels=16, kernel_size=3, padding=1)
        self.conv2 = nn.Conv2d(in_channels=16, out_channels=32, kernel_size=3, padding=1)
        self.fc1 = nn.Linear(32 * 7 * 7, 128)
        self.fc2 = nn.Linear(128, 10)
        self.NR_LAYERS = 4

    def forward(self, x):
        x = F.relu(self.conv1(x))
        x = F.max_pool2d(x, 2)
        x = F.relu(self.conv2(x))
        x = F.max_pool2d(x, 2)
        x = x.view(-1, 32 * 7 * 7)
        x = F.relu(self.fc1(x))
        x = self.fc2(x)

        return x


def test_named_model_fields_are_wrapped():
    model = SimpleCNN()
    input_tensor = torch.randn(1, 1, 28, 28)
    model = TimedModule(model)

    output = model(input_tensor)

    assert isinstance(model.conv1, TimedModule)
    assert isinstance(model.conv2, TimedModule)
    assert isinstance(model.fc1, TimedModule)
    assert isinstance(model.fc2, TimedModule)
    assert output is not None


def test_model_sublayer_timings_are_retrieved():
    model = SimpleCNN()
    input_tensor = torch.randn(1, 1, 28, 28)
    model = TimedModule(model)

    _ = model(input_tensor)
    timings_dict = model.get_timings()

    assert isinstance(model, TimedModule)
    assert len(timings_dict) == 6
    assert len(timings_dict["sub_modules"]) == model.NR_LAYERS
    assert timings_dict["module_name"] == "SimpleCNN"
    assert timings_dict["device_type"] == "cpu"
    assert timings_dict["sub_modules"][0]["module_name"] == "Conv2d"
    assert timings_dict["sub_modules"][2]["module_name"] == "Linear"


def test_3_time_measurements_are_available_when_model_is_called_3_times():
    model = SimpleCNN()
    input_tensor = torch.randn(1, 1, 28, 28)
    model = TimedModule(model)

    _ = model(input_tensor)
    _ = model(input_tensor)
    _ = model(input_tensor)
    timings_dict = model.get_timings()

    assert len(timings_dict["execution_times_ms"]) == 3
    for i in range(4):
        assert len(timings_dict["sub_modules"][i]["execution_times_ms"]) == 3


def test_measurements_are_cleared():
    model = SimpleCNN()
    input_tensor = torch.randn(1, 1, 28, 28)
    model = TimedModule(model)

    _ = model(input_tensor)
    model.clear_timings()
    timings_dict = model.get_timings()

    assert "execution_times_ms" not in timings_dict


def test_2_measurements_are_available_after_clearing():
    model = SimpleCNN()
    input_tensor = torch.randn(1, 1, 28, 28)
    model = TimedModule(model)

    _ = model(input_tensor)
    model.clear_timings()
    _ = model(input_tensor)
    _ = model(input_tensor)
    timings_dict = model.get_timings()

    assert len(timings_dict["execution_times_ms"]) == 2
    for i in range(4):
        assert len(timings_dict["sub_modules"][i]["execution_times_ms"]) == 2


class MyCustomLayer(nn.Conv2d):
    """This class is to demonstrate call on a non-existent method"""

    def custom_method(self):
        self.called = True


class SimpleCNNWithCustomMethodCall(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = MyCustomLayer(in_channels=1, out_channels=16, kernel_size=3, padding=1)
        self.conv2 = nn.Conv2d(in_channels=16, out_channels=32, kernel_size=3, padding=1)
        self.fc1 = nn.Linear(32 * 7 * 7, 128)
        self.fc2 = nn.Linear(128, 10)

    def forward(self, x):
        x = F.relu(self.conv1(x))
        x = F.max_pool2d(x, 2)
        x = F.relu(self.conv2(x))
        x = F.max_pool2d(x, 2)
        x = x.view(-1, 32 * 7 * 7)
        x = F.relu(self.fc1(x))
        x = self.fc2(x)

        # when wrapped with TimedModule, this will raise an error if not handled properly
        self.conv1.custom_method()

        return x


def test_method_of_wrapped_layer_can_be_accessed_through_timed_layer():
    conv = MyCustomLayer(in_channels=1, out_channels=2, kernel_size=3)
    timed_conv = TimedModule(conv)

    method = timed_conv._module.custom_method
    forwarded_method = timed_conv.custom_method

    assert method == forwarded_method


def test_method_of_wrapper_layer_is_called_during_model_execution():
    model = SimpleCNNWithCustomMethodCall()
    input_tensor = torch.randn(1, 1, 28, 28)
    model = TimedModule(model)

    _ = model(input_tensor)

    assert isinstance(model.conv1, TimedModule)
    assert model.conv1.called is True
