class script(object):
    START_TXT = """<b>HELLO</b> {} 💐,
 <i>My Name Is 🦋 𝙅𝞐𝙎𝞛𝞘𝞜𝞝 🦋 & I Can Provide Movies, Just Add Me To Your Groups And Enjoy...🤓</i>
 
 <i>I Have Some Additional Cool Features...🥳 Hit Help To Find Out My Commands...🔍</i>
 
 <b><u>More Updates</u> :-</b>
 ╔══❖•ೋ° °ೋ•❖══╗       
🖇 @adhologam_official🖇
🖇 @adhologam_series 🖇
╚══❖•ೋ° °ೋ•❖══╝"""
    HELP_TXT = """<b>HELLO</b> {}
    
⚙ <i>My Commands</i> ⚙

<b><u>More Updates</u> :-</b>
╔══❖•ೋ° °ೋ•❖══╗       
🖇 @adhologam_official🖇
🖇 @adhologam_series 🖇
╚══❖•ೋ° °ೋ•❖══╝"""
    ABOUT_TXT = """<b> ABOUT ME 🔍</b>

🕵‍♂ <i>MY NAME :-</i> 🦋 𝙅𝞐𝙎𝞛𝞘𝞜𝞝 🦋

🕵‍♂ <i>CREATOR :-</i> <a href=https://t.me/STEPHEN_OF_TELEGRAM>☞ͥ͟⋆ͣ͟⋆ͫ°»Ꮢ๏ʟєχ𓅇꙰</a>

🕵‍♂ <i>DATA BASE :-</i> <b>Mongo Db</b>

🕵‍♂ <i>BOT SERVER :- </i> <b>Vps</b>"""
    SOURCE_TXT = """<b>NOTE:</b>
- Eva Maria is a open source project. 
- Source - https://github.com/EvamariaTG/EvaMaria  

<b>DEVS:</b>
- <a href=https://t.me/TeamEvamaria>Team Eva Maria</a>"""
    MANUELFILTER_TXT = """<b>📄 <u>MANUAL FILTERS</u> :</b>

🔘 <i>Filter Is The Feature Were Users Can Set Automated Replies For a Particular Keyword And 🦋 Jasmine 🦋 Will Respond Whenever a Keyword Is Found The Message, This bot Supports Both Url And Alert Inline Buttons.</i>

<b>⚠️ <u>NOTE</u> :</b>

🔘 <i>🦋 Jasmine 🦋 Should Have Admin Privillage.</i>
🔘 <i>Only Admins Can Add Filters In a Chat.</i>
🔘 <i>Alert Buttons Have a Limit Of 64 Characters.</i>

📚 <b><u>COMMANDS AND USAGE</u> :</b>

➠ <b>/filter -</b> <code>Add a Filter In Chat</code>

➠ <b>/filters -</b> <code>List All The Filters Of a Chat</code>

➠ <b>/del -</b> <code>Delete a Specific Filter In Chat</code>

➠ <b>/delall -</b> <code>Delete The Whole Filters In a Chat (chat owner only)</code>"""
    BUTTON_TXT = """<b>📄 <u>FORMATION</u> :</b>

<i>🦋 Jasmine 🦋 Supports Both Url And Alert Inline Buttons.</i>

<b>⚠️ <u>NOTE</u> :</b>

🔘 <i>Telegram Will Not Allows You To Send Buttons Without Any Content, So Content Is Mandatory.</i>
🔘 <i>🦋 Jasmine 🦋 Supports Buttons With Any Telegram Media Type.</i>
🔘 <i>Buttons Should Be Properly Parsed As Markdown Format.</i>

<b>📄 <u>URL BUTTONS</u> :</b>

🔘 <code>[Button Text](buttonurl:https://t.me/EvaMariaBot)</code>

<b>📄 <u>ALERT BUTTONS</u> :</b>

🔘 <code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
• /connect  - <code>connect a particular chat to your PM</code>
• /disconnect  - <code>disconnect from a chat</code>
• /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of Eva Maria

<b>Commands and Usage:</b>
• /id - <code>get id of a specified user.</code>
• /info  - <code>get information about a user.</code>
• /imdb  - <code>get the film information from IMDb source.</code>
• /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
• /logs - <code>to get the rescent errors</code>
• /stats - <code>to get status of files in db.</code>
• /delete - <code>to delete a specific file from db.</code>
• /users - <code>to get list of my users and ids.</code>
• /chats - <code>to get list of the my chats and ids </code>
• /leave  - <code>to leave from a chat.</code>
• /disable  -  <code>do disable a chat.</code>
• /ban  - <code>to ban a user.</code>
• /unban  - <code>to unban a user.</code>
• /channel - <code>to get list of total connected channels</code>
• /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """★ 𝚃𝙾𝚃𝙰𝙻 𝙵𝙸𝙻𝙴𝚂: <code>{}</code>
★ 𝚃𝙾𝚃𝙰𝙻 𝚄𝚂𝙴𝚁𝚂: <code>{}</code>
★ 𝚃𝙾𝚃𝙰𝙻 𝙲𝙷𝙰𝚃𝚂: <code>{}</code>
★ 𝚄𝚂𝙴𝙳 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝚒𝙱
★ 𝙵𝚁𝙴𝙴 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝚒𝙱"""
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""
