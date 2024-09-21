AUTHOR = 'Grape'
SITENAME = 'YingJue Technology'
SITEURL = ""

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
    ("You can modify those links in your config file", "#"),
)

# Social widget
SOCIAL = (
    ("You can add links in your config file", "#"),
    ("Another social link", "#"),
)

DEFAULT_PAGINATION = 10

I18N_TEMPLATES_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
DISPLAY_PAGES_ON_MENU =False
MENUITEMS = (
			('Home','/pages/home/index.html'),
			)

THEME = "themes/bs3"
JINJA_ENVIRONMENT = {
  'extensions': ['jinja2.ext.i18n']
}
PYGMENTS_STYLE='default'
BOOTSTRAP_THEME='flatly'
DISPLAY_BREADCRUMBS=False
BOOTSTRAP_NAVBAR_INVERSE=False
DISPLAY_RECENT_POSTS_ON_SIDEBAR=True

TAG_CLOUD_STEPS = 4
TAG_CLOUD_BADGE = True  
DISPLAY_TAGS_ON_SIDEBAR=True
TAG_CLOUD_MAX_ITEMS=25
DISPLAY_TAGS_INLINE=True
HIDE_SIDEBAR=False
SHOW_SERIES = True
DISPLAY_SERIES_ON_SIDEBAR = True

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
}

GITALK_REPO_NAME = "gitalk_comments"
GITALK_REPO_OWNER = "yingjue2020"
GITALK_REPO_ADMIN = "yingjue2020"