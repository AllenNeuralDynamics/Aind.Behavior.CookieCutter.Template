from datetime import datetime

def on_pre_gen(context):
    # Set the current year
    context['cookiecutter']['year'] = datetime.now().year