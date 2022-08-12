import yaml


def print_args(args):
    args = vars(args)
    for k in args:
        print(f'{k}: {args[k]}')


def try_catch(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(e)
    return wrapper


def get_config(file: str) -> dict:
    with open(file, 'r', encoding='utf-8') as f:
        cfg = yaml.load(f, yaml.Loader)
    return cfg


if __name__ == '__main__':
    conf = 'configs/test.yaml'
    config = get_config(conf)
    print(config)
    print(type(config))