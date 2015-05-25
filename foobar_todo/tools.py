# -*- coding: utf-8 -*-
import os

from django.conf import settings


def compile_sass():
    """
    Функция, компилирует sass и записывает стили в сжатом виде
    """
    try:
        import sass
    except ImportError:
        print("Libsass not installed")
    sass_path = os.path.join(settings.STATICFILES_DIRS[0], 'sass')
    css_path = os.path.join(settings.STATICFILES_DIRS[0], 'css')

    if not os.path.isdir(sass_path):
        return

    if not os.path.isdir(css_path):
        os.mkdir(css_path)

    sass_file = os.path.join(sass_path, 'base.scss')
    css_file = os.path.join(css_path, 'base.min.css')
    output_style = 'compressed'

    try:
        css = sass.compile(
            filename=sass_file,
            output_style=output_style,
        )
    except sass.CompileError as error:
        print(error)
    else:
        with open(css_file, 'w') as styles_file:
            styles_file.write(css)
