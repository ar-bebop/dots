from colors import color

# these are defined global variables
c = c
config = config

color(c)

config.load_autoconfig(False)

c.colors.webpage.preferred_color_scheme = 'dark'
c.colors.webpage.darkmode.policy.images = 'never'

c.content.blocking.method = 'both'

c.content.javascript.clipboard = 'access'
c.content.javascript.can_open_tabs_automatically = True

c.content.autoplay = False
c.content.pdfjs = True
c.content.local_content_can_access_remote_urls = True

c.downloads.location.suggestion = 'both'
c.downloads.remove_finished = 8

c.hints.radius = 0
c.keyhint.radius = 0
c.prompt.radius = 0

c.tabs.show = 'multiple'

c.editor.command = ['nvim', '{file}']

c.url.searchengines = {'DEFAULT': 'https://duckduckgo.com/?q={}', 'google': 'https://google.com/search?hl=en&q={}'}

config.bind(',v', 'hint media spawn mpv {hint-url}')
config.bind(',m', 'hint media spawn nsxiv {hint-url}')
