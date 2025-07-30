!!! abstract "Episodes in module: **{{ page.meta.module }}**"

    {% for p in module_posts(page) %}
    - Episode {{ loop.index }} - {{ p.meta.date.date() }} - [{{ p.title }}]({{ '../../../' + p.file.src_uri }})
    {% endfor %}
