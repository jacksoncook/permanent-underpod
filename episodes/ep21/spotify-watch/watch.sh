#!/bin/zsh
cd "$(dirname "$0")"
LOG=watch.log
START=$(date +%s)
log(){ echo "$(date '+%H:%M:%S') $*" >> $LOG; }
log "watcher start pid=$$"
while true; do
  if (( $(date +%s) - START > 21600 )); then log "TIMEOUT 6h, exiting"; exit 1; fi
  S=$(osascript state.scpt 2>&1)
  case "$S" in
    GONE_URL*|TAB_NOT_FOUND*) log "STOP: $S"; exit 0;;
  esac
  PROG=$(echo "$S" | grep -m1 -E "^TEXT (Uploading|About)" | cut -c6-)
  PUB=$(echo "$S" | grep -m1 "^PUBLISH")
  log "${PROG:-no-upload-text} | ${PUB:-no-publish-button}"
  if echo "$S" | grep -q "PUBLISH enabled=true" && ! echo "$S" | grep -q "TEXT Uploading"; then
    log "publish enabled, upload text gone -> pressing"
    R=$(osascript state.scpt press 2>&1); log "press1: $(echo "$R" | grep -E 'PRESSED|NOT_ENABLED|PUBLISH')"
    sleep 10
    R2=$(osascript state.scpt 2>&1); log "after press1: $(echo "$R2" | tr '\n' ' ' | cut -c1-400)"
    if echo "$R2" | grep -q "PUBLISH enabled=true"; then
      log "publish still enabled (confirm dialog?) -> pressing again"
      R3=$(osascript state.scpt press 2>&1); log "press2: $(echo "$R3" | grep -E 'PRESSED|NOT_ENABLED')"
      sleep 10
      R4=$(osascript state.scpt 2>&1); log "after press2: $(echo "$R4" | tr '\n' ' ' | cut -c1-400)"
    fi
    URL=$(osascript -e 'tell application "Google Chrome" to get URL of active tab of front window' 2>&1)
    log "DONE url=$URL"
    exit 0
  fi
  sleep 180
done
