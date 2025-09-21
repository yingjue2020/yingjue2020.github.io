# A static website
My website developed in pelican

This work is licensed under CC BY 4.0 

http://mindbending.org/en

```html
{% if 'brand' in SIDEBAR_ELEMENTS %}
                {% include 'sidebar/brand.html' %}
                {% do SIDEBAR_ELEMENTS.remove('brand') %}
            {% endif %}

            <section class="visible-lg visible-md" id="sidebar-content{% if SIDEBAR_POSITION == 'left' %}-left{% endif %}">
                <ul class="list-group list-group-flush">
                    {% for element in SIDEBAR_ELEMENTS %}
                        {% include SIDEBAR_MAP[element] %}
                    {% endfor %}
                </ul>
            </section>
```

## TODO
- GOOGLE_CSE_ID (https://programmablesearchengine.google.com/controlpanel/overview?cx=d1afdec03092141dc)
- GOOGLE_SITE_VERIFICATION
- index done
- categories category done
- tags tag
- article
- page
- authors author
- archives done

## Build local environment

```bash
pelican --autoreload --listen --ignore-cache
pelican -o output -s pelicanconf.py -v -e SITEURL='"http://127.0.0.1:8000"'
```