from path_helpers import path


def get_data_directory():
    return path(__path__[0]).joinpath('data').abspath()
