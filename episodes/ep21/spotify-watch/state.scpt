-- usage: osascript state.scpt [press]
on run argv
  set doPress to (count of argv) > 0
  global outS, pubBtn, foundPub
  set outS to ""
  set foundPub to false
  tell application "Google Chrome"
    set found to false
    repeat with w in windows
      set i to 0
      repeat with t in tabs of w
        set i to i + 1
        if URL of t contains "6gZiCGPcQarUouHjoaM7lZ" then
          set found to true
          if URL of t does not contain "/wizard" then return "GONE_URL " & (URL of t)
          if active tab index of w is not i then set active tab index of w to i
          set index of w to 1
        end if
      end repeat
    end repeat
    if not found then return "TAB_NOT_FOUND"
  end tell
  tell application "System Events" to tell process "Google Chrome"
    set value of attribute "AXEnhancedUserInterface" to true
    delay 1
    set w to front window
  end tell
  walk(w, 0)
  if doPress and foundPub then
    tell application "System Events"
      if enabled of pubBtn then
        perform action "AXPress" of pubBtn
        set outS to outS & "PRESSED" & linefeed
      else
        set outS to outS & "NOT_ENABLED" & linefeed
      end if
    end tell
  end if
  return outS
end run

on walk(el, depth)
  global outS, pubBtn, foundPub
  if depth > 40 then return
  tell application "System Events"
    set r to ""
    try
      set r to role of el
    end try
    if r is "AXButton" or r is "AXProgressIndicator" or r is "AXStaticText" then
      set n to ""
      try
        set n to name of el
      end try
      if n is missing value then set n to ""
      if r is "AXButton" and n is "Publish" then
        set pubBtn to el
        set foundPub to true
        set outS to outS & "PUBLISH enabled=" & (enabled of el as text) & linefeed
      else if r is "AXProgressIndicator" then
        set outS to outS & "PROGRESS " & n & " value=" & (value of el as text) & linefeed
      else if r is "AXStaticText" and (n contains "remaining" or n contains "Uploading" or n contains "ublished" or n contains "rocessing" or n contains "failed" or n contains "error" or n contains "Error") then
        set outS to outS & "TEXT " & n & linefeed
      end if
    end if
    set kids to {}
    try
      set kids to UI elements of el
    end try
    repeat with k in kids
      my walk(k, depth + 1)
    end repeat
  end tell
end walk
