AUTHOR = 'Grape'
SITENAME = 'YINGJUE'
SITEURL = ""
ORGNIZATION = "Yingjue Technology (Shenzhen) Co., Ltd."

PATH = "content"

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = 'en'

# THEME = "themes/zend"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

ARTICLE_URL = 'posts/{category}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{category}/{slug}/index.html'

PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'

AUTHOR_URL = 'author/{slug}/'
AUTHOR_SAVE_AS = 'author/{slug}/index.html'

CATEGORY_URL = 'category/{slug}/'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'

TAG_URL = 'tag/{slug}/'
TAG_SAVE_AS = 'tag/{slug}/index.html'

# Blogroll
LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    ("TATAMOBILE", "https://tatamobile.net"),
)

# Social widget
SOCIAL = (
    ("E-mail", "envelope", "#"),
    ("GitHub", "github", "https://github.com/yingjue2020"),
    ("Twitter", "twitter", "#"),
    ("Google Plus", "google-plus", "#"),
    ("Facebook", "facebook", "#"),
    ("Stackoverflow", "stack-overflow", "#"),
    ("GitTip", "gittip", "#"),
    ("Linux User", "linux", "#"),
    ("Feeds", "rss", "feeds.atom"),
)

DEFAULT_PAGINATION = 10

I18N_TEMPLATES_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None


THEME = "themes/pelican-bootstrap3"
JINJA_ENVIRONMENT = {
  'extensions': ['jinja2.ext.i18n', 'jinja2.ext.do']
}

FAVICON = "extra/favicon-32x32.png"
TOUCHICON = "extra/apple-touch-icon.png"

# css
TYPOGRIFY = False
CUSTOM_CSS = "extra/custom.css"
FEED_ALL_ATOM = "feeds.atom"
FEED_ALL_RSS = "feeds.rss"

PYGMENTS_STYLE='monokai'
BOOTSTRAP_THEME='readable'

# navbar
NAVBAR_ELEMENTS = ['menu-items', 'search', 'brand-dropdown']
DISPLAY_PAGES_ON_MENU =False
DISPLAY_CATEGORIES_ON_MENU = False
SITE_LINKS = [
    ('Home', ''),
    ('Authors', 'authors'),
    ('Archives', 'archives'),
    ('Categories', 'categories'),
    ('Tags', 'tags'),
    ('RSS', 'feeds.rss'),
]
MENUITEMS = (
            ('About','pages/about'),
            ('Projects','pages/projects'),
            # ('Series',[
            #     ('Bending Gnome Keyring with Python', 'pages/series/series1'),
            #     ('PyCon Highlights', 'pages/series/series2'),
            #     ('Python and UDisks', 'pages/series/series3'),
            # ]),
            ('Contact','pages/contact'),
            
			)
# seo
GOOGLE_CSE_ID = "d1afdec03092141dc"
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

# site banner
SHOW_SITE_BANNER_IN = ['all']
SITE_BANNER_ELEMENTS = ['logo', 'name', 'social']
SITE_BANNER_BACKGROUND_COLOR = "#eeeeec; background-image: url('/images/background_banner.jpg'); background-position: center top;"
SITELOGO = "images/logo.png"

# sidebar
SIDEBAR_ELEMENTS = ["condensed", "links"]
# SIDE_BRAND_ELEMENTS = ['logo', 'name', 'links', 'social', 'search']
SIDE_BRAND_ELEMENTS = ['logo', 'name', 'social']
CONDENSED_SIDEBAR_ITEMS = ['categories', 'tagcloud', 'recent']

DISPLAY_BREADCRUMBS = True

BOOTSTRAP_FLUID = True
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
CUSTOM_LICENSE = '<p xmlns:cc="http://creativecommons.org/ns#" >This work is licensed under <a href="https://creativecommons.org/licenses/by-sa/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">CC BY-SA 4.0<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1" alt=""><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1" alt=""><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/sa.svg?ref=chooser-v1" alt=""></a></p>'

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
    'extra/app-ads.txt': {'path': 'app-ads.txt'}
}

GITALK_REPO_NAME = "gitalk_comments"
GITALK_REPO_OWNER = "yingjue2020"
GITALK_REPO_ADMIN = "yingjue2020"