import os
from buildbot.www.hooks import AuthenticatedResource
from dotenv import load_dotenv
# --- Load admin users from .env.local ---
load_dotenv(dotenv_path=".env.local")
ADMIN_USERS = os.getenv("ADMIN_USERS", "admin").split(",")

# --- Supercharged defaults ---
SUPERCHARGED_UI_DEFAULTS = { 
    # ... (paste the full previous config here)
}

ROLE_OVERRIDES = {
    'admin': {
        'Console.showFullLog': True,
        'autoRefresh': 10,
        'Grid.collapse_inactive_builders': False,
        'Builders.collapse_inactive': False,
        'Workers.collapse_inactive': False,
        'Theme': 'dark',
    },
    'user': {
        'Console.showFullLog': False,
        'autoRefresh': 30,
        'Grid.collapse_inactive_builders': True,
        'Builders.collapse_inactive': True,
        'Workers.collapse_inactive': True,
        'Theme': 'light',
    }
}

# --- Helper to merge defaults, role-based, and cookie overrides ---
def get_ui_config_for_user(username: str, cookie_overrides=None):
    role = 'admin' if username in ADMIN_USERS else 'user'
    config = SUPERCHARGED_UI_DEFAULTS.copy()
    config.update(ROLE_OVERRIDES.get(role, {}))
    if cookie_overrides:
        config.update(cookie_overrides)
    return config

class DynamicUIResource(AuthenticatedResource):
    """
    Apply UI config dynamically per user, including cookie overrides.
    """
    def get_ui_default_config(self, request):
        user = getattr(request, 'user', None)
        username = getattr(user, 'username', 'guest')

        # Example cookie overrides: 'theme', 'autoRefresh', 'showFullLog'
        cookie_overrides = {}
        theme = request.getCookie('theme')
        if theme:
            cookie_overrides['Theme'] = theme
        auto_refresh = request.getCookie('autoRefresh')
        if auto_refresh:
            try:
                cookie_overrides['autoRefresh'] = int(auto_refresh)
            except ValueError:
                pass
        show_log = request.getCookie('showFullLog')
        if show_log:
            cookie_overrides['Console.showFullLog'] = show_log.lower() == 'true'

        return get_ui_config_for_user(username, cookie_overrides)

# --- Apply dynamic UI to Buildbot ---
c['www']['ui_default_config'] = DynamicUIResource()
