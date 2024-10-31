try:
    from mindspore.hal import Stream as Stream_MS
    from mindspore.hal import Event as Event_MS

    all = [
        "Event",
        "Stream"
    ]

    class Stream(Stream_MS):
        # rewrite __init__ because MindSpore.hal.Stream not support 'device' args.
        def __init__(self, device=None, priority=0, **kwargs):
            if device is not None:
                raise NotImplementedError("'cuda.Stream' can not support 'device'. "
                                        "For now, can only create stream on the current device.")
            if 'stream' in kwargs:
                super().__init__(stream=kwargs['stream'])
            elif 'stream_id' in kwargs:
                super().__init__(priority, kwargs['stream_id'])
            else:
                super().__init__(priority)

    class Event(Event_MS):
        # rewrite __init__ because MindSpore.hal.Event not support 'interprocess' args.
        def __init__(self, enable_timing=False, blocking=False, interprocess=False):
            super().__init__(enable_timing, blocking)
            if interprocess:
                raise NotImplementedError("'cuda.Event' can not support parameter 'interprocess'.")

        @classmethod
        def from_ipc_handle(cls, device, handle):
            raise NotImplementedError()

        def ipc_handle(self):
            raise NotImplementedError
except ImportError:
    # when mindspore.hal not support, just do not define Stream/Event
    ...
