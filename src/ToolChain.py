from factory import Factory
from utils import get_config


class ToolChain:
    def __init__(self, factory: Factory, config: str) -> None:
        self.factory = factory
        self.cfg = get_config(config)

    def _parse_args(self, tool: dict, outs: list):
        outs = outs
        args = tool.get('args', None)
        if args is not None and isinstance(args, list):
            for i in range(len(args)):
                args[i] = eval(args[i]) if isinstance(args[i], str) else args[i]

        kwargs = tool.get('kwargs', None)
        if kwargs is not None and isinstance(kwargs, dict):
            for k in kwargs:
                kwargs[k] = eval(kwargs[k]) if isinstance(kwargs[k], str) else kwargs[k]
        return args, kwargs

    def run(self):
        outs = []
        for tool in self.cfg:
            name = list(tool.keys())[0]
            func = self.factory.get_func(name)
            args, kwargs = self._parse_args(tool[name], outs)
            if args is None and kwargs is None:
                out = func()
            elif kwargs is None:
                out = func(*args)
            elif args is None:
                out = func(**kwargs)
            else:
                out = func(*args, **kwargs)
            outs.append(out)


if __name__ == '__main__':
    from toolhub import factory
    chain = ToolChain(factory, '/Users/yinxu/Documents/GitHub/ToolChain/configs/list_files.yaml')
    chain.run()
