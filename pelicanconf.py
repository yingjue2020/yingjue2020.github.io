from datetime import datetime
NOW = datetime.now()

def custom_page_range(current_page_num, page_count):
    if page_count <=5:
        return range(1, page_count + 1)
    start = current_page_num - 2
    delta_s = 0
    if start <= 0:
        delta_s = 2 - current_page_num + 1
        start = 1
    end = current_page_num + 2 + delta_s
    delta_e = 0
    if end > page_count:
        delta_e = end - page_count
        end = page_count
    start = start - delta_e
    return list(range(start, end + 1))

JINJA_GLOBALS = {
    'rose_page_range': custom_page_range,
}

AUTHOR = 'Grape'
SITENAME = 'YINGJUE'
SITEURL = ""
ORGNIZATION = "YINGJUE"

PATH = "content"

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = 'en'

AUTHORS = {
  'Grape': {
    'avatar': '/images/avatars/grape.png',
    'bio': "Graduated in Computer Science and Engineering, but currently working with GNU/Linux infrastructure and in the spare time I'm an Open Source programmer (Python and C), a drawer and author in the YINGJUE Blog.",
    'links': [
        ("GitHub", "github", "#"),
        ("Twitter", "twitter", "#"),
        ("Google Plus", "google-plus", "#"),
        ("Facebook", "facebook", "#"),
    ]
  },
  'Apple': {'avatar': '/images/avatars/apple.png',
  'bio': "Graduated in Computer Science and Engineering, but currently working with GNU/Linux infrastructure and in the spare time I'm an Open Source programmer (Python and C), a drawer and author in the YINGJUE Blog.",
  'links': [
        ("GitHub", "github", "#"),
        ("Twitter", "twitter", "#"),
        ("Google Plus", "google-plus", "#"),
        ("Facebook", "facebook", "#"),
    ]
  }
}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

RELATED_POSTS_CAROUSEL = False

ARTICLE_URL = 'categories/{category}/{slug}'
ARTICLE_SAVE_AS = 'categories/{category}/{slug}/index.html'

PAGE_URL = '{slug}'
PAGE_SAVE_AS = '{slug}/index.html'

AUTHORS_URL = "authors"
AUTHOR_URL = 'authors/{slug}'
AUTHOR_SAVE_AS = 'authors/{slug}/index.html'

CATEGORIES_URL = "categories"
CATEGORY_URL = 'categories/{slug}'
CATEGORY_SAVE_AS = 'categories/{slug}/index.html'

TAGS_URL = "tags"
TAG_URL = 'tags/{slug}'
TAG_SAVE_AS = 'tags/{slug}/index.html'

# Blogroll
LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    # ("TATAMOBILE", "https://tatamobile.net"),
)

# Social widget
SOCIAL = (
    ("E-mail", "envelope"),
    ("GitHub", "github"),
    ("Twitter", "twitter"),
    ("Google Plus", "google-plus"),
    ("Facebook", "facebook"),
    ("Stackoverflow", "stack-overflow"),
    ("GitTip", "gittip"),
    ("Linux User", "linux"),
    ("Feeds", "rss"),
)

DEFAULT_PAGINATION = 10

I18N_TEMPLATES_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None


#THEME = "themes/pelican-bootstrap5"
THEME = "themes/papyrus"
JINJA_ENVIRONMENT = {
  'extensions': ['jinja2.ext.i18n', 'jinja2.ext.do']
}

RELATED_POSTS_MAX = 10
SHOW_DATE_MODIFIED = True
SHOW_ARTICLE_AUTHOR = True
SHOW_ARTICLE_CATEGORY = True

FAVICON = "extra/favicon-32x32.png"
TOUCHICON = "extra/apple-touch-icon.png"

# css
TYPOGRIFY = False
CUSTOM_CSS = "extra/custom.css"
CUSTOM_JS = "extra/custom.js"
FEED_ALL_ATOM = "feeds.atom"
FEED_ALL_RSS = "feeds.rss"

PYGMENTS_STYLE='monokai'
BOOTSTRAP_THEME='zephyr'

# navbar
NAVBAR_ELEMENTS = ['menu-items', 'brand-simple']
DISPLAY_PAGES_ON_MENU =False
DISPLAY_CATEGORIES_ON_MENU = False
SUMMARY_MAX_LENGTH = 64
SUMMARY_MAX_PARAGRAPHS = 2
SITE_LINKS = [
    ('Home', ''),
    ('Authors', 'authors'),
    ('Archives', 'archives'),
    ('Categories', 'categories'),
    ('Tags', 'tags'),
    # ('RSS', 'feeds.rss'),
]
MENUITEMS = (
            ('Archives', 'archives'),
            ('Categories', 'categories'),
            ('Tags', 'tags'),
            ('Authors', 'authors'),
            # ('RSS', 'feeds.rss'),
)
# seo
# GOOGLE_CSE_ID = "d1afdec03092141dc"
GOOGLE_ANALYTICS = "G-7YNPQY01K6"
ADSENSE_ID = "ca-pub-4403496704855214"
# ADSENSE_SLOT_ID = "5654114561"
# SITEMAP = {
#     "format": "xml",
#     "priorities": {
#         "articles": 0.5,
#         "indexes": 0.5,
#         "pages": 0.5
#     },
#     "changefreqs": {
#         "articles": "monthly",
#         "indexes": "daily",
#         "pages": "monthly"
#     }
# }
EXTENDED_SITEMAP_PLUGIN = {
    'priorities': {
        'index': 1.0,
        'articles': 0.8,
        'pages': 0.5,
        'others': 0.4
    },
    'changefrequencies': {
        'index': 'daily',
        'articles': 'weekly',
        'pages': 'monthly',
        'others': 'monthly',
    }
}

MARKDOWN = {
    "extension_configs": {
        # Needed for code syntax highlighting
        "markdown.extensions.codehilite": {"css_class": "highlight"},
        "markdown.extensions.extra": {},
        "markdown.extensions.meta": {},
        # This is for enabling the TOC generation
        "markdown.extensions.toc": {"title": "Table of Contents"},
    },
    "output_format": "html5",
}

# site banner
HIDE_SITE_BANNER = True
SHOW_SITE_BANNER_IN = ['all']
SITE_BANNER_ELEMENTS = ['logo', 'name', 'social']
SITE_BANNER_BACKGROUND_COLOR = "#eeeeec; background-image: url('/images/background_banner.jpg'); background-position: center top;"
SITELOGO = "images/logo.png"

# sidebar
SIDEBAR_ELEMENTS = ["condensed", "links", "adsense"]
# SIDE_BRAND_ELEMENTS = ['logo', 'name', 'links', 'social', 'search']
SIDE_BRAND_ELEMENTS = ['logo', 'name', 'social']
CONDENSED_SIDEBAR_ITEMS = ['categories', 'tagcloud', 'recent']

DISPLAY_BREADCRUMBS = False
DISPLAY_CATEGORY_IN_BREADCRUMBS = True

BOOTSTRAP_FLUID = False
# BOOTSTRAP_NAVBAR_INVERSE=False
# DISPLAY_RECENT_POSTS_ON_SIDEBAR=True

TAG_CLOUD_STEPS = 4
TAG_CLOUD_BADGE = True
TAG_CLOUD_MAX_ITEMS=25
# DISPLAY_TAGS_ON_SIDEBAR=True

# DISPLAY_TAGS_INLINE=True
# HIDE_SIDEBAR=False
# SHOW_SERIES = True
# DISPLAY_SERIES_ON_SIDEBAR = True
# CC_LICENSE = "CC-BY-SA"
# CC_LICENSE_COMMERCIAL = "yes"
# CC_LICENSE_DERIVATIVES = "yes"
# CUSTOM_LICENSE = '<p xmlns:cc="http://creativecommons.org/ns#" >This work is licensed under <a href="https://creativecommons.org/licenses/by-sa/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">CC BY-SA 4.0<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1" alt=""><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1" alt=""><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/sa.svg?ref=chooser-v1" alt=""></a></p>'

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

MD_INCLUDE_BASE_PATH = "sourcecode"
# MATH_JAX = {'color':'black','align':'left'}

STATIC_PATHS = [
    'images',
    'extra',  # this
]

EXTRA_PATH_METADATA = {
    'extra/favicon.png': {'path': 'favicon.png'},  # and this
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/CNAME': {'path': 'CNAME'},
    'extra/app-ads.txt': {'path': 'app-ads.txt'},
    'extra/ads.txt': {'path': 'ads.txt'},
    'extra/terms.txt': {'path': 'terms.html'},
    'extra/privacy.txt': {'path': 'privacy.html'},
}

GISGUS_REPO_NAME = "yingjue2020/yingjue2020.github.io"
GISGUS_REPO_ID = "MDEwOlJlcG9zaXRvcnkxODE5OTg4NTc="
GISGUS_CATEGORY_NAME = "Announcements"
GISGUS_CATEGORY_ID = "DIC_kwDOCtkVCc4Culyf"

SUBTITLE = "Yingjue's Blog"
SUBTEXT = "I'm a drawer and author in the YINGJUE Blog."
COPYRIGHT = "© 2025 YINGJUE. All rights reserved."