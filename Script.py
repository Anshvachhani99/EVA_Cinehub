class script(object):
    START_TXT = """ℍ𝔼𝕃𝕃𝕆 {},
𝕀 𝔸𝕄 <a href=https://t.me/{}>{}</a>\n\n 𝕀 𝔻𝔼𝕃𝕀𝕍𝕀𝔼ℝ ℝ𝔼ℚ𝕌𝔼𝕊𝕋𝔼𝔻 𝕄𝔼𝔻𝕀𝔸 𝕋𝕆 ℙ𝔼𝕆ℙ𝕃𝔼.\n𝔻𝕆ℕ𝕋 𝔽𝕆ℝ𝔾𝔼𝕋 𝕋𝕆 𝔽𝕆𝕃𝕃𝕆𝕎 𝕄𝕐 𝕌𝕆𝔻𝔸𝕋𝔼𝕊 ℂℍ𝔸ℕℕ𝔼𝕃 𝔹𝔼𝔽𝕆ℝ𝔼 𝕌𝕊𝕀ℕ𝔾 𝕄𝔼."""
    HELP_TXT = """𝙷𝙴𝚈 {}
ℍ𝔼ℝ𝔼 𝕀𝕊 𝕄𝕐 ℂ𝕆𝕄𝕄𝔸ℕ𝔻𝕊."""
    ABOUT_TXT = """✯ 𝙼𝚈 𝙽𝙰𝙼𝙴: {}
✯ 𝙲𝚁𝙴𝙰𝚃𝙾𝚁: <a href= https://t.me/anonymous7205>🆂🅾️🆄🅼🅰️🅳🅸🅿️</a>
✯ 𝙻𝙸𝙱𝚁𝙰𝚁𝚈: 𝙿𝚈𝚁𝙾𝙶𝚁𝙰𝙼
✯ 𝙻𝙰𝙽𝙶𝚄𝙰𝙶𝙴: 𝙿𝚈𝚃𝙷𝙾𝙽 𝟹
✯ 𝙳𝙰𝚃𝙰 𝙱𝙰𝚂𝙴: 𝙼𝙾𝙽𝙶𝙾 𝙳𝙱
✯ 𝙱𝙾𝚃 𝚂𝙴𝚁𝚅𝙴𝚁: 𝙷𝙴𝚁𝙾𝙺𝚄
✯ 𝙱𝚄𝙸𝙻𝙳: v1.0.1 [ ℂ𝕀ℕ𝔼ℍ𝕌𝔹 𝕍𝔼ℝ𝕊𝕀𝕆ℕ ]"""
    SOURCE_TXT = """<b>NOTE:</b> 
- OWNER - <a href= https://t.me/anonymous7205>🆂🅾️🆄🅼🅰️🅳🅸🅿️</a>

<b>DEVS:</b>
- <a href= https://t.me/anonymous7205>🆂🅾️🆄🅼🅰️🅳🅸🅿️</a>"""
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and EvaMaria will respond whenever a keyword is found the message

<b>NOTE:</b>
𝟙. 𝕤𝕙𝕠𝕦𝕝𝕕 𝕙𝕒𝕧𝕖 𝕒𝕕𝕞𝕚𝕟 𝕡𝕣𝕚𝕧𝕚𝕝𝕝𝕒𝕘𝕖.
𝟚. 𝕠𝕟𝕝𝕪 𝕒𝕕𝕞𝕚𝕟𝕤 𝕔𝕒𝕟 𝕒𝕕𝕕 𝕗𝕚𝕝𝕥𝕖𝕣𝕤 𝕚𝕟 𝕒 𝕔𝕙𝕒𝕥.
𝟛. 𝕒𝕝𝕖𝕣𝕥 𝕓𝕦𝕥𝕥𝕠𝕟𝕤 𝕙𝕒𝕧𝕖 𝕒 𝕝𝕚𝕞𝕚𝕥 𝕠𝕗 𝟞𝟜 𝕔𝕙𝕒𝕣𝕒𝕔𝕥𝕖𝕣𝕤.

<b>Commands and Usage:</b>
• /filter - <code>add a filter in chat</code>
• /filters - <code>list all the filters of a chat</code>
• /del - <code>delete a specific filter in chat</code>
• /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- 𝔼𝕧𝕒 𝕄𝕒𝕣𝕚𝕒 𝕊𝕦𝕡𝕡𝕠𝕣𝕥𝕤 𝕓𝕠𝕥𝕙 𝕦𝕣𝕝 𝕒𝕟𝕕 𝕒𝕝𝕖𝕣𝕥 𝕚𝕟𝕝𝕚𝕟𝕖 𝕓𝕦𝕥𝕥𝕠𝕟𝕤.

<b>NOTE:</b>
𝟙. 𝕋𝕖𝕝𝕖𝕘𝕣𝕒𝕞 𝕨𝕚𝕝𝕝 𝕟𝕠𝕥 𝕒𝕝𝕝𝕠𝕨𝕤 𝕪𝕠𝕦 𝕥𝕠 𝕤𝕖𝕟𝕕 𝕓𝕦𝕥𝕥𝕠𝕟𝕤 𝕨𝕚𝕥𝕙𝕠𝕦𝕥 𝕒𝕟𝕪 𝕔𝕠𝕟𝕥𝕖𝕟𝕥, 𝕤𝕠 𝕔𝕠𝕟𝕥𝕖𝕟𝕥 𝕚𝕤 𝕞𝕒𝕟𝕕𝕒𝕥𝕠𝕣𝕪.
𝟚. 𝕤𝕦𝕡𝕡𝕠𝕣𝕥 𝕓𝕦𝕥𝕥𝕠𝕟𝕤 𝕨𝕚𝕥𝕙 𝕒𝕟𝕪 𝕥𝕖𝕝𝕖𝕘𝕣𝕒𝕞 𝕞𝕖𝕕𝕚𝕒 𝕥𝕪𝕡𝕖.
𝟛. 𝔹𝕦𝕥𝕥𝕠𝕟𝕤 𝕤𝕙𝕠𝕦𝕝𝕕 𝕓𝕖 𝕡𝕣𝕠𝕡𝕖𝕣𝕝𝕪 𝕡𝕒𝕣𝕤𝕖𝕕 𝕒𝕤 𝕞𝕒𝕣𝕜𝕕𝕠𝕨𝕟 𝕗𝕠𝕣𝕞𝕒𝕥

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/Bot)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
𝟙. 𝕄𝕒𝕜𝕖 𝕞𝕖 𝕥𝕙𝕖 𝕒𝕕𝕞𝕚𝕟 𝕠𝕗 𝕪𝕠𝕦𝕣 𝕔𝕙𝕒𝕟𝕟𝕖𝕝 𝕚𝕗 𝕚𝕥'𝕤 𝕡𝕣𝕚𝕧𝕒𝕥𝕖.
𝟚. 𝕞𝕒𝕜𝕖 𝕤𝕦𝕣𝕖 𝕥𝕙𝕒𝕥 𝕪𝕠𝕦𝕣 𝕔𝕙𝕒𝕟𝕟𝕖𝕝 𝕕𝕠𝕖𝕤 𝕟𝕠𝕥 𝕔𝕠𝕟𝕥𝕒𝕚𝕟𝕤 𝕔𝕒𝕞𝕣𝕚𝕡𝕤, 𝕡𝕠𝕣𝕟 𝕒𝕟𝕕 𝕗𝕒𝕜𝕖 𝕗𝕚𝕝𝕖𝕤.
𝟛. 𝔽𝕠𝕣𝕨𝕒𝕣𝕕 𝕥𝕙𝕖 𝕝𝕒𝕤𝕥 𝕞𝕖𝕤𝕤𝕒𝕘𝕖 𝕥𝕠 𝕞𝕖 𝕨𝕚𝕥𝕙 𝕢𝕦𝕠𝕥𝕖𝕤.
 𝕀'𝕝𝕝 𝕒𝕕𝕕 𝕒𝕝𝕝 𝕥𝕙𝕖 𝕗𝕚𝕝𝕖𝕤 𝕚𝕟 𝕥𝕙𝕒𝕥 𝕔𝕙𝕒𝕟𝕟𝕖𝕝 𝕥𝕠 𝕞𝕪 𝕕𝕓."""
    CONNECTION_TXT = """Help: <b>Connections</b>

- 𝕌𝕤𝕖𝕕 𝕥𝕠 𝕔𝕠𝕟𝕟𝕖𝕔𝕥 𝕓𝕠𝕥 𝕥𝕠 ℙ𝕄 𝕗𝕠𝕣 𝕞𝕒𝕟𝕒𝕘𝕚𝕟𝕘 𝕗𝕚𝕝𝕥𝕖𝕣𝕤 
- 𝕚𝕥 𝕙𝕖𝕝𝕡𝕤 𝕥𝕠 𝕒𝕧𝕠𝕚𝕕 𝕤𝕡𝕒𝕞𝕞𝕚𝕟𝕘 𝕚𝕟 𝕘𝕣𝕠𝕦𝕡𝕤.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
• /connect  - <code>connect a particular chat to your PM</code>
• /disconnect  - <code>disconnect from a chat</code>
• /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features

<b>Commands and Usage:</b>
• /id - <code>get id of a specified user.</code>
• /info  - <code>get information about a user.</code>
• /imdb  - <code>get the film information from IMDb source.</code>
• /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
𝕋𝕙𝕚𝕤 𝕞𝕠𝕕𝕦𝕝𝕖 𝕠𝕟𝕝𝕪 𝕨𝕠𝕣𝕜𝕤 𝕗𝕠𝕣 𝕞𝕪 𝕒𝕕𝕞𝕚𝕟𝕤


    STATUS_TXT = """★ 𝚃𝙾𝚃𝙰𝙻 𝙵𝙸𝙻𝙴𝚂: <code>{}</code>
★ 𝚃𝙾𝚃𝙰𝙻 𝚄𝚂𝙴𝚁𝚂: <code>{}</code>
★ 𝚃𝙾𝚃𝙰𝙻 𝙲𝙷𝙰𝚃𝚂: <code>{}</code>
★ 𝚄𝚂𝙴𝙳 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝚒𝙱
★ 𝙵𝚁𝙴𝙴 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝚒𝙱"""
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
𝕋𝕠𝕥𝕒𝕝 𝕄𝕖𝕞𝕓𝕖𝕣𝕤 = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
𝕀𝔻 - <code>{}</code>
Nᴀᴍᴇ - {}
"""