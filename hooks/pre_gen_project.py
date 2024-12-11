from datetime import datetime

def on_pre_gen(context):
    current_year = datetime.now().year
    context['cookiecutter']['year'] = current_year