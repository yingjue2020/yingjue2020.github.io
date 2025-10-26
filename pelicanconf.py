
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

DEFAULT_PAGINATION = 10

I18N_TEMPLATES_LANG = 'en'


#THEME = "themes/pelican-bootstrap5"
THEME = "themes/papyrus"
JINJA_ENVIRONMENT = {
  'extensions': ['jinja2.ext.do']
}

RELATED_POSTS_MAX = 5

FAVICON = "extra/favicon-32x32.png"
TOUCHICON = "extra/apple-touch-icon.png"

FEED_ALL_ATOM = "feeds.atom"
FEED_ALL_RSS = "feeds.rss"

# seo
GOOGLE_ANALYTICS = "G-7YNPQY01K6"
ADSENSE_ID = "ca-pub-4403496704855214"
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

MD_INCLUDE_BASE_PATH = "sourcecode"

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