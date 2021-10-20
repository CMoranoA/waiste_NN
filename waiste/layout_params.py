# Background image
background_image = """
.stApp {
  background-image: linear-gradient(rgba(255,255,255,0.7),rgba(255,255,255,1)), url("https://static.vecteezy.com/system/resources/previews/000/168/278/non_2x/waste-basket-vector-pack.jpg");
  padding: 8px;
}
"""

# Title
title = '<h1 style="font-family: courier; color:#1D8ADB; font-size: 104px; text-align: center;text-shadow: 0 0 black;">w<span style="color:rgb(71 152 55);">AI</span>ste</h1>'

# How it works
title1 = '<h2 style="font-family: sans-serif; color:rgb(71 152 55); font-size: 64px; text-align: center;text-shadow: 0 0 black;">1</h2>'
title2 = '<h2 style="font-family: sans-serif; color:rgb(71 152 55); font-size: 64px; text-align: center;text-shadow: 0 0 black;">2</h2>'
title3 = '<h2 style="font-family: sans-serif; color:rgb(71 152 55); font-size: 64px; text-align: center;text-shadow: 0 0 black;">3</h2>'

subtitle1 = '<h2 style="font-family: sans-serif; color:#1D8ADB; font-size: 32px; text-align: center; padding-bottom: 40px;text-shadow: 0 0 black;">Upload an <span style="color:rgb(71 152 55);">image</span> of your waste</h2>'
subtitle2 = '<h2 style="font-family: sans-serif; color:#1D8ADB; font-size: 32px; text-align: center; padding-bottom: 40px;text-shadow: 0 0 black;">Get your waste <span style="color:rgb(71 152 55);">category</span></h2>'
subtitle3 = '<h2 style="font-family: sans-serif; color:#1D8ADB; font-size: 32px; text-align: center; padding-bottom: 40px;text-shadow: 0 0 black;">Find the <span style="color:rgb(71 152 55);">closest</span> location</h2>'

# User uploads photo

upload_photo = '<h2 style="color: #1c6ca5; opacity: 1; font-family: sans-serif; font-size: 16px; font-weight: 400; padding-top: 8px; padding-bottom: 8px; padding-right: 8px; padding-left: 8px; background-color: rgb(71, 152,55, 0.5);text-shadow: 0 0 black;">Upload image</h2>'

# Categories

enter_data = '<h2 style="font-family: sans-serif; color: rgba(17, 63, 8, 0.959); text-align: center; text-shadow: 0 0 black; padding: 16px;">Enter your data</h2>'

bin_locations = '<h2 style="font-family: sans-serif; color: rgba(17, 63, 8, 0.959); text-align: center; text-shadow: 0 0 black; padding: 16px;">Bin Locations</h2>'

paper_title = '<h2 style="font-family: sans-serif; color:#338ED3; font-size: 14px; text-align: center; text-shadow: 0 0 black;">PAPER</h2>'
paper_bin = """
<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" role="img" width="104" height="104" preserveAspectRatio="xMidYMid meet" viewBox="0 0 16 16"><rect x="0" y="0" width="16" height="16" fill="none" stroke="none" /><path d="M2 5v10c0 .55.45 1 1 1h9c.55 0 1-.45 1-1V5H2zm3 9H4V7h1v7zm2 0H6V7h1v7zm2 0H8V7h1v7zm2 0h-1V7h1v7z" fill="#338ED3"/><path d="M13.25 2H10V.75A.753.753 0 0 0 9.25 0h-3.5A.753.753 0 0 0 5 .75V2H1.75a.752.752 0 0 0-.75.75V4h13V2.75a.752.752 0 0 0-.75-.75zM9 2H6v-.987h3V2z" fill="#338ED3"/></svg></div>
"""

cardboard_title = '<h2 style="font-family: sans-serif; color:#FED400; font-size: 14px; text-align: center; text-shadow: 0 0 black;">CARDBOARD</h2>'
cardboard_bin = """
<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" role="img" width="104" height="104" preserveAspectRatio="xMidYMid meet" viewBox="0 0 16 16"><rect x="0" y="0" width="16" height="16" fill="none" stroke="none" /><path d="M2 5v10c0 .55.45 1 1 1h9c.55 0 1-.45 1-1V5H2zm3 9H4V7h1v7zm2 0H6V7h1v7zm2 0H8V7h1v7zm2 0h-1V7h1v7z" fill="#FED400"/><path d="M13.25 2H10V.75A.753.753 0 0 0 9.25 0h-3.5A.753.753 0 0 0 5 .75V2H1.75a.752.752 0 0 0-.75.75V4h13V2.75a.752.752 0 0 0-.75-.75zM9 2H6v-.987h3V2z" fill="#FED400"/></svg></div>
"""

metal_title = '<h2 style="font-family: sans-serif; color:rgb(38,126,41); font-size: 14px; text-align: center; text-shadow: 0 0 black;">METAL</h2>'
metal_bin = """
<div style="text-align: center;"><svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" role="img" width="104" height="104" preserveAspectRatio="xMidYMid meet" viewBox="0 0 16 16"><rect x="0" y="0" width="16" height="16" fill="none" stroke="none" /><path d="M2 5v10c0 .55.45 1 1 1h9c.55 0 1-.45 1-1V5H2zm3 9H4V7h1v7zm2 0H6V7h1v7zm2 0H8V7h1v7zm2 0h-1V7h1v7z" fill="rgb(38,126,41)"/><path d="M13.25 2H10V.75A.753.753 0 0 0 9.25 0h-3.5A.753.753 0 0 0 5 .75V2H1.75a.752.752 0 0 0-.75.75V4h13V2.75a.752.752 0 0 0-.75-.75zM9 2H6v-.987h3V2z" fill="rgb(38,126,41)"/></svg></div>
"""

plastic_title = '<h2 style="font-family: sans-serif; color:#FE9C00; font-size: 14px; text-align: center; text-shadow: 0 0 black;">PLASTIC</h2>'
plastic_bin = """
<div style="text-align: center;"><svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" role="img" width="104" height="104" preserveAspectRatio="xMidYMid meet" viewBox="0 0 16 16"><rect x="0" y="0" width="16" height="16" fill="none" stroke="none" /><path d="M2 5v10c0 .55.45 1 1 1h9c.55 0 1-.45 1-1V5H2zm3 9H4V7h1v7zm2 0H6V7h1v7zm2 0H8V7h1v7zm2 0h-1V7h1v7z" fill="#FE9C00"/><path d="M13.25 2H10V.75A.753.753 0 0 0 9.25 0h-3.5A.753.753 0 0 0 5 .75V2H1.75a.752.752 0 0 0-.75.75V4h13V2.75a.752.752 0 0 0-.75-.75zM9 2H6v-.987h3V2z" fill="#FE9C00"/></svg></div>
"""

glass_title = '<h2 style="font-family: sans-serif; color:#52B1BE; font-size: 14px; text-align: center; text-shadow: 0 0 black;">GLASS</h2>'
glass_bin = """
<div style="text-align: center;"><svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" role="img" width="104" height="104" preserveAspectRatio="xMidYMid meet" viewBox="0 0 16 16"><rect x="0" y="0" width="16" height="16" fill="none" stroke="none" /><path d="M2 5v10c0 .55.45 1 1 1h9c.55 0 1-.45 1-1V5H2zm3 9H4V7h1v7zm2 0H6V7h1v7zm2 0H8V7h1v7zm2 0h-1V7h1v7z" fill="#52B1BE"/><path d="M13.25 2H10V.75A.753.753 0 0 0 9.25 0h-3.5A.753.753 0 0 0 5 .75V2H1.75a.752.752 0 0 0-.75.75V4h13V2.75a.752.752 0 0 0-.75-.75zM9 2H6v-.987h3V2z" fill="#52B1BE"/></svg></div>
"""

organic_title = '<h2 style="font-family: sans-serif; color:#28DB03; font-size: 14px; text-align: center; text-shadow: 0 0 black;">ORGANIC</h2>'
organic_bin = """
<div style="text-align: center;"><svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" role="img" width="104" height="104" preserveAspectRatio="xMidYMid meet" viewBox="0 0 16 16"><rect x="0" y="0" width="16" height="16" fill="none" stroke="none" /><path d="M2 5v10c0 .55.45 1 1 1h9c.55 0 1-.45 1-1V5H2zm3 9H4V7h1v7zm2 0H6V7h1v7zm2 0H8V7h1v7zm2 0h-1V7h1v7z" fill="#28DB03"/><path d="M13.25 2H10V.75A.753.753 0 0 0 9.25 0h-3.5A.753.753 0 0 0 5 .75V2H1.75a.752.752 0 0 0-.75.75V4h13V2.75a.752.752 0 0 0-.75-.75zM9 2H6v-.987h3V2z" fill="#28DB03"/></svg></div>
"""

electronics_title = '<h2 style="font-family: sans-serif; color:#922DCD; font-size: 14px; text-align: center; text-shadow: 0 0 black;">E-WASTE</h2>'
electronics_bin = """
<div style="text-align: center;"><svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" role="img" width="104" height="104" preserveAspectRatio="xMidYMid meet" viewBox="0 0 16 16"><rect x="0" y="0" width="16" height="16" fill="none" stroke="none" /><path d="M2 5v10c0 .55.45 1 1 1h9c.55 0 1-.45 1-1V5H2zm3 9H4V7h1v7zm2 0H6V7h1v7zm2 0H8V7h1v7zm2 0h-1V7h1v7z" fill="#922DCD"/><path d="M13.25 2H10V.75A.753.753 0 0 0 9.25 0h-3.5A.753.753 0 0 0 5 .75V2H1.75a.752.752 0 0 0-.75.75V4h13V2.75a.752.752 0 0 0-.75-.75zM9 2H6v-.987h3V2z" fill="#922DCD"/></svg></div>
"""

bricks_title = '<h2 style="font-family: sans-serif; color:rgb(206,173,73); font-size: 14px; text-align: center; text-shadow: 0 0 black;">BRICKS</h2>'
bricks_bin = """
<div style="text-align: center;"><svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" role="img" width="104" height="104" preserveAspectRatio="xMidYMid meet" viewBox="0 0 16 16"><rect x="0" y="0" width="16" height="16" fill="none" stroke="none" /><path d="M2 5v10c0 .55.45 1 1 1h9c.55 0 1-.45 1-1V5H2zm3 9H4V7h1v7zm2 0H6V7h1v7zm2 0H8V7h1v7zm2 0h-1V7h1v7z" fill="rgb(206,173,73)"/><path d="M13.25 2H10V.75A.753.753 0 0 0 9.25 0h-3.5A.753.753 0 0 0 5 .75V2H1.75a.752.752 0 0 0-.75.75V4h13V2.75a.752.752 0 0 0-.75-.75zM9 2H6v-.987h3V2z" fill="rgb(206,173,73)"/></svg></div>
"""

telgopor_title = '<h2 style="font-family: sans-serif; color:rgb(126,123,123); font-size: 14px; text-align: center ;text-shadow: 0 0 black;">TELGOPOR</h2>'
telgopor_bin = """
<div style="text-align: center;"><svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" role="img" width="104" height="104" preserveAspectRatio="xMidYMid meet" viewBox="0 0 16 16"><rect x="0" y="0" width="16" height="16" fill="none" stroke="none" /><path d="M2 5v10c0 .55.45 1 1 1h9c.55 0 1-.45 1-1V5H2zm3 9H4V7h1v7zm2 0H6V7h1v7zm2 0H8V7h1v7zm2 0h-1V7h1v7z" fill="rgb(126,123,123)"/><path d="M13.25 2H10V.75A.753.753 0 0 0 9.25 0h-3.5A.753.753 0 0 0 5 .75V2H1.75a.752.752 0 0 0-.75.75V4h13V2.75a.752.752 0 0 0-.75-.75zM9 2H6v-.987h3V2z" fill="rgb(126,123,123)"/></svg></div>
"""

non_recyclable_title = '<h2 style="font-family: sans-serif; color:#423432; font-size: 14px; text-align: center; text-shadow: 0 0 black;">NON-REC</h2>'
non_recyclable_bin = """
<div style="text-align: center;"><svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" role="img" width="104" height="104" preserveAspectRatio="xMidYMid meet" viewBox="0 0 16 16"><rect x="0" y="0" width="16" height="16" fill="none" stroke="none" /><path d="M2 5v10c0 .55.45 1 1 1h9c.55 0 1-.45 1-1V5H2zm3 9H4V7h1v7zm2 0H6V7h1v7zm2 0H8V7h1v7zm2 0h-1V7h1v7z" fill="#423432"/><path d="M13.25 2H10V.75A.753.753 0 0 0 9.25 0h-3.5A.753.753 0 0 0 5 .75V2H1.75a.752.752 0 0 0-.75.75V4h13V2.75a.752.752 0 0 0-.75-.75zM9 2H6v-.987h3V2z" fill="#423432"/></svg></div>
"""

hazardous_title = '<h2 style="font-family: sans-serif; color:#FE0300; font-size: 14px; text-align: center; text-shadow: 0 0 black;">HAZARDOUS</h2>'
hazardous_bin = """
<div style="text-align: center;"><svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" role="img" width="104" height="104" preserveAspectRatio="xMidYMid meet" viewBox="0 0 16 16"><rect x="0" y="0" width="16" height="16" fill="none" stroke="none" /><path d="M2 5v10c0 .55.45 1 1 1h9c.55 0 1-.45 1-1V5H2zm3 9H4V7h1v7zm2 0H6V7h1v7zm2 0H8V7h1v7zm2 0h-1V7h1v7z" fill="#FE0300"/><path d="M13.25 2H10V.75A.753.753 0 0 0 9.25 0h-3.5A.753.753 0 0 0 5 .75V2H1.75a.752.752 0 0 0-.75.75V4h13V2.75a.752.752 0 0 0-.75-.75zM9 2H6v-.987h3V2z" fill="#FE0300"/></svg></div>
"""

clothes_title = '<h2 style="font-family: sans-serif; color:#B66001; font-size: 14px; text-align: center; text-shadow: 0 0 black;">CLOTHES</h2>'
clothes_bin = """
<div style="text-align: center;"><svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" role="img" width="104" height="104" preserveAspectRatio="xMidYMid meet" viewBox="0 0 16 16"><rect x="0" y="0" width="16" height="16" fill="none" stroke="none" /><path d="M2 5v10c0 .55.45 1 1 1h9c.55 0 1-.45 1-1V5H2zm3 9H4V7h1v7zm2 0H6V7h1v7zm2 0H8V7h1v7zm2 0h-1V7h1v7z" fill="#B66001"/><path d="M13.25 2H10V.75A.753.753 0 0 0 9.25 0h-3.5A.753.753 0 0 0 5 .75V2H1.75a.752.752 0 0 0-.75.75V4h13V2.75a.752.752 0 0 0-.75-.75zM9 2H6v-.987h3V2z" fill="#B66001"/></svg></div>
"""

# Location
find_location = '<h2 style="font-family: sans-serif; color: rgba(17, 63, 8, 0.959); text-align: center; text-shadow: 0 0 black; padding: 16px;">Find the closest location</h2>'


paper_subtitle = '<h2 style="font-family: sans-serif; color:#338ED3; font-size: 8px; text-align: center; text-shadow: 0 0 black; padding-top: 0px;">PAPER</h2>'
paper_small_bin = """
<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" role="img" width="52" height="52" preserveAspectRatio="xMidYMid meet" viewBox="0 0 16 16"><rect x="0" y="0" width="16" height="16" fill="none" stroke="none" /><path d="M2 5v10c0 .55.45 1 1 1h9c.55 0 1-.45 1-1V5H2zm3 9H4V7h1v7zm2 0H6V7h1v7zm2 0H8V7h1v7zm2 0h-1V7h1v7z" fill="#338ED3"/><path d="M13.25 2H10V.75A.753.753 0 0 0 9.25 0h-3.5A.753.753 0 0 0 5 .75V2H1.75a.752.752 0 0 0-.75.75V4h13V2.75a.752.752 0 0 0-.75-.75zM9 2H6v-.987h3V2z" fill="#338ED3"/></svg>
"""

cardboard_subtitle = '<h2 style="font-family: sans-serif; color:#FED400; font-size: 8px; text-align: center; text-shadow: 0 0 black; padding-top: 0px;">CARDBOARD</h2>'
cardboard_small_bin = """
<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" role="img" width="52" height="52" preserveAspectRatio="xMidYMid meet" viewBox="0 0 16 16"><rect x="0" y="0" width="16" height="16" fill="none" stroke="none" /><path d="M2 5v10c0 .55.45 1 1 1h9c.55 0 1-.45 1-1V5H2zm3 9H4V7h1v7zm2 0H6V7h1v7zm2 0H8V7h1v7zm2 0h-1V7h1v7z" fill="#FED400"/><path d="M13.25 2H10V.75A.753.753 0 0 0 9.25 0h-3.5A.753.753 0 0 0 5 .75V2H1.75a.752.752 0 0 0-.75.75V4h13V2.75a.752.752 0 0 0-.75-.75zM9 2H6v-.987h3V2z" fill="#FED400"/></svg>
"""

metal_subtitle = '<h2 style="font-family: sans-serif; color:rgb(38,126,41); font-size: 8px; text-align: center; text-shadow: 0 0 black; padding-top: 0px;">METAL</h2>'
metal_small_bin = """
<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" role="img" width="52" height="52" preserveAspectRatio="xMidYMid meet" viewBox="0 0 16 16"><rect x="0" y="0" width="16" height="16" fill="none" stroke="none" /><path d="M2 5v10c0 .55.45 1 1 1h9c.55 0 1-.45 1-1V5H2zm3 9H4V7h1v7zm2 0H6V7h1v7zm2 0H8V7h1v7zm2 0h-1V7h1v7z" fill="rgb(38,126,41)"/><path d="M13.25 2H10V.75A.753.753 0 0 0 9.25 0h-3.5A.753.753 0 0 0 5 .75V2H1.75a.752.752 0 0 0-.75.75V4h13V2.75a.752.752 0 0 0-.75-.75zM9 2H6v-.987h3V2z" fill="rgb(38,126,41)"/></svg>
"""

plastic_subtitle = '<h2 style="font-family: sans-serif; color:#FE9C00; font-size: 8px; text-align: center; text-shadow: 0 0 black; padding-top: 0px;">PLASTIC</h2>'
plastic_small_bin = """
<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" role="img" width="52" height="52" preserveAspectRatio="xMidYMid meet" viewBox="0 0 16 16"><rect x="0" y="0" width="16" height="16" fill="none" stroke="none" /><path d="M2 5v10c0 .55.45 1 1 1h9c.55 0 1-.45 1-1V5H2zm3 9H4V7h1v7zm2 0H6V7h1v7zm2 0H8V7h1v7zm2 0h-1V7h1v7z" fill="#FE9C00"/><path d="M13.25 2H10V.75A.753.753 0 0 0 9.25 0h-3.5A.753.753 0 0 0 5 .75V2H1.75a.752.752 0 0 0-.75.75V4h13V2.75a.752.752 0 0 0-.75-.75zM9 2H6v-.987h3V2z" fill="#FE9C00"/></svg>
"""

glass_subtitle = '<h2 style="font-family: sans-serif; color:#52B1BE; font-size: 8px; text-align: center; text-shadow: 0 0 black; padding-top: 0px;">GLASS</h2>'
glass_small_bin = """
<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" role="img" width="52" height="52" preserveAspectRatio="xMidYMid meet" viewBox="0 0 16 16"><rect x="0" y="0" width="16" height="16" fill="none" stroke="none" /><path d="M2 5v10c0 .55.45 1 1 1h9c.55 0 1-.45 1-1V5H2zm3 9H4V7h1v7zm2 0H6V7h1v7zm2 0H8V7h1v7zm2 0h-1V7h1v7z" fill="#52B1BE"/><path d="M13.25 2H10V.75A.753.753 0 0 0 9.25 0h-3.5A.753.753 0 0 0 5 .75V2H1.75a.752.752 0 0 0-.75.75V4h13V2.75a.752.752 0 0 0-.75-.75zM9 2H6v-.987h3V2z" fill="#52B1BE"/></svg>
"""

organic_subtitle = '<h2 style="font-family: sans-serif; color:#28DB03; font-size: 8px; text-align: center; text-shadow: 0 0 black; padding-top: 0px;">ORGANIC</h2>'
organic_small_bin = """
<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" role="img" width="52" height="52" preserveAspectRatio="xMidYMid meet" viewBox="0 0 16 16"><rect x="0" y="0" width="16" height="16" fill="none" stroke="none" /><path d="M2 5v10c0 .55.45 1 1 1h9c.55 0 1-.45 1-1V5H2zm3 9H4V7h1v7zm2 0H6V7h1v7zm2 0H8V7h1v7zm2 0h-1V7h1v7z" fill="#28DB03"/><path d="M13.25 2H10V.75A.753.753 0 0 0 9.25 0h-3.5A.753.753 0 0 0 5 .75V2H1.75a.752.752 0 0 0-.75.75V4h13V2.75a.752.752 0 0 0-.75-.75zM9 2H6v-.987h3V2z" fill="#28DB03"/></svg>
"""

electronics_subtitle = '<h2 style="font-family: sans-serif; color:#922DCD; font-size: 8px; text-align: center; text-shadow: 0 0 black; padding-top: 0px;">E-WASTE</h2>'
electronics_small_bin = """
<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" role="img" width="52" height="52" preserveAspectRatio="xMidYMid meet" viewBox="0 0 16 16"><rect x="0" y="0" width="16" height="16" fill="none" stroke="none" /><path d="M2 5v10c0 .55.45 1 1 1h9c.55 0 1-.45 1-1V5H2zm3 9H4V7h1v7zm2 0H6V7h1v7zm2 0H8V7h1v7zm2 0h-1V7h1v7z" fill="#922DCD"/><path d="M13.25 2H10V.75A.753.753 0 0 0 9.25 0h-3.5A.753.753 0 0 0 5 .75V2H1.75a.752.752 0 0 0-.75.75V4h13V2.75a.752.752 0 0 0-.75-.75zM9 2H6v-.987h3V2z" fill="#922DCD"/></svg>
"""

bricks_subtitle = '<h2 style="font-family: sans-serif; color:rgb(206,173,73); font-size: 8px; text-align: center; text-shadow: 0 0 black; padding-top: 0px;">BRICKS</h2>'
bricks_small_bin = """
<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" role="img" width="52" height="52" preserveAspectRatio="xMidYMid meet" viewBox="0 0 16 16"><rect x="0" y="0" width="16" height="16" fill="none" stroke="none" /><path d="M2 5v10c0 .55.45 1 1 1h9c.55 0 1-.45 1-1V5H2zm3 9H4V7h1v7zm2 0H6V7h1v7zm2 0H8V7h1v7zm2 0h-1V7h1v7z" fill="rgb(206,173,73)"/><path d="M13.25 2H10V.75A.753.753 0 0 0 9.25 0h-3.5A.753.753 0 0 0 5 .75V2H1.75a.752.752 0 0 0-.75.75V4h13V2.75a.752.752 0 0 0-.75-.75zM9 2H6v-.987h3V2z" fill="rgb(206,173,73)"/></svg>
"""

telgopor_subtitle = '<h2 style="font-family: sans-serif; color:rgb(126,123,123); font-size: 8px; text-align: center ;text-shadow: 0 0 black; padding-top: 0px;">TELGOPOR</h2>'
telgopor_small_bin = """
<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" role="img" width="52" height="52" preserveAspectRatio="xMidYMid meet" viewBox="0 0 16 16"><rect x="0" y="0" width="16" height="16" fill="none" stroke="none" /><path d="M2 5v10c0 .55.45 1 1 1h9c.55 0 1-.45 1-1V5H2zm3 9H4V7h1v7zm2 0H6V7h1v7zm2 0H8V7h1v7zm2 0h-1V7h1v7z" fill="rgb(126,123,123)"/><path d="M13.25 2H10V.75A.753.753 0 0 0 9.25 0h-3.5A.753.753 0 0 0 5 .75V2H1.75a.752.752 0 0 0-.75.75V4h13V2.75a.752.752 0 0 0-.75-.75zM9 2H6v-.987h3V2z" fill="rgb(126,123,123)"/></svg>
"""

non_recyclable_subtitle = '<h2 style="font-family: sans-serif; color:#423432; font-size: 8px; text-align: center; text-shadow: 0 0 black; padding-top: 0px;">NON-REC</h2>'
non_recyclable_small_bin = """
<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" role="img" width="52" height="52" preserveAspectRatio="xMidYMid meet" viewBox="0 0 16 16"><rect x="0" y="0" width="16" height="16" fill="none" stroke="none" /><path d="M2 5v10c0 .55.45 1 1 1h9c.55 0 1-.45 1-1V5H2zm3 9H4V7h1v7zm2 0H6V7h1v7zm2 0H8V7h1v7zm2 0h-1V7h1v7z" fill="#423432"/><path d="M13.25 2H10V.75A.753.753 0 0 0 9.25 0h-3.5A.753.753 0 0 0 5 .75V2H1.75a.752.752 0 0 0-.75.75V4h13V2.75a.752.752 0 0 0-.75-.75zM9 2H6v-.987h3V2z" fill="#423432"/></svg>
"""

hazardous_subtitle = '<h2 style="font-family: sans-serif; color:#FE0300; font-size: 8px; text-align: center; text-shadow: 0 0 black; padding-top: 0px;">HAZARDOUS</h2>'
hazardous_small_bin = """
<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" role="img" width="52" height="52" preserveAspectRatio="xMidYMid meet" viewBox="0 0 16 16"><rect x="0" y="0" width="16" height="16" fill="none" stroke="none" /><path d="M2 5v10c0 .55.45 1 1 1h9c.55 0 1-.45 1-1V5H2zm3 9H4V7h1v7zm2 0H6V7h1v7zm2 0H8V7h1v7zm2 0h-1V7h1v7z" fill="#FE0300"/><path d="M13.25 2H10V.75A.753.753 0 0 0 9.25 0h-3.5A.753.753 0 0 0 5 .75V2H1.75a.752.752 0 0 0-.75.75V4h13V2.75a.752.752 0 0 0-.75-.75zM9 2H6v-.987h3V2z" fill="#FE0300"/></svg>
"""

clothes_subtitle = '<h2 style="font-family: sans-serif; color:#B66001; font-size: 8px; text-align: center; text-shadow: 0 0 black; padding-top: 0px;">CLOTHES</h2>'
clothes_small_bin = """
<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" role="img" width="52" height="52" preserveAspectRatio="xMidYMid meet" viewBox="0 0 16 16"><rect x="0" y="0" width="16" height="16" fill="none" stroke="none" /><path d="M2 5v10c0 .55.45 1 1 1h9c.55 0 1-.45 1-1V5H2zm3 9H4V7h1v7zm2 0H6V7h1v7zm2 0H8V7h1v7zm2 0h-1V7h1v7z" fill="#B66001"/><path d="M13.25 2H10V.75A.753.753 0 0 0 9.25 0h-3.5A.753.753 0 0 0 5 .75V2H1.75a.752.752 0 0 0-.75.75V4h13V2.75a.752.752 0 0 0-.75-.75zM9 2H6v-.987h3V2z" fill="#B66001"/></svg>
"""

category = '<h2 style="font-family: sans-serif; color: rgba(17, 63, 8, 0.959); text-align: center; text-shadow: 0 0 black; padding: 16px; font-size: 32px;">Category: </h2>'

closest_location = '<h2 style="font-family: sans-serif; color: rgba(17, 63, 8, 0.959); text-align: center; text-shadow: 0 0 black; padding: 16px; font-size: 32px;">Closest location: </h2>'

non_recyclable = '<h2 style="font-family: sans-serif; color:#423432; text-align: center; text-shadow: 0 0 black; padding-left: 16px; padding-right: 16px; padding-top: 48px; padding-bottom: 48px; font-size: 32px;">Unfortunately this material is not recycable!</h2>'
