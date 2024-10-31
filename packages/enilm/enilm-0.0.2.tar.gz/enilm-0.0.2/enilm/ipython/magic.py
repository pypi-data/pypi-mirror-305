def autoreload():
    return '''
    %load_ext autoreload
    %autoreload 2
    '''

def fix_autocomplete():
    return '''
    # fix tab autocomplete
    # https://github.com/jupyterlab/jupyterlab/issues/9620
    %config Completer.use_jedi = False
    '''
