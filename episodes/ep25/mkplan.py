import json, os
W = os.getcwd(); EP = "/Users/jcook/Personal/permanent-underpod/episodes/ep25"
SC = "/Users/jcook/Personal/permanent-underpod/media/ep25/raw/Untitled_recording-chris-screen-00h_21m_52s_056ms-StreamYard.mp4"
ANCHOR = 1311.685
LT = [("intro","EPISODE 25","FAKE SECRETS. REAL THIEVES.","INTRO",14.0),
 ("openr","THE OPENROUTER INCIDENT","FAKE API KEYS WENT IN. MONTHS LATER, SOMEONE USED THEM.","OPENR_A",44.0),
 ("four","FOUR PROVIDERS, FOUR LEAKS","HOW THE PROMPTS GOT OUT","OPENR_A",281.0),
 ("zdr","ZERO DATA RETENTION","WHO ENFORCES IT? PROBABLY NO ONE.","OPENR_B",757.0),
 ("chain","THE CHAINFLIP HACK","HOW A VALIDATOR WALKED OUT WITH THE VAULT","CHAIN_A",811.5),
 ("deps","SUPPLY CHAINS","IS OPEN SOURCE STILL WORTH THE RISK?","CHAIN_B",1098.5),
 ("perp","PERP OF FORTUNE","SHORT MINIMAX 10×  ·  BITCOIN DOWN","PERP",1286.0),
 ("ft","JACKSON'S LAPTOP","TEACHING A SMALL OPEN MODEL TO WATCH TENNIS","FT_A",1404.5),
 ("lora","LORA","FINE-TUNING WITHOUT TOUCHING THE BIG WEIGHTS","FT_A",1553.0),
 ("probe","PROBING","STOP THE MODEL HALFWAY AND READ IT THERE","FT_A",1708.0),
 ("web","THE WEB BROWSER","HOW LONG DOES IT HAVE LEFT?","WEB_A",2296.0),
 ("funnel","TOP OF THE FUNNEL","WHY AMAZON DOESN'T WANT YOUR AGENT SHOPPING","WEB_B",2408.0),
 ("encl","SECURE ENCLAVES","WHAT A TEE ACTUALLY IS","ENCL",2900.0),
 ("rumor","GOSSIP CORNER","DID SOMEONE CRACK FACTORING? UNCONFIRMED.","RUMOR",3155.0)]
ST = [("coldopen","EPISODE 25","In this pod…","COLD_A",None,6,"st"),
 ("tease","PERP OF FORTUNE","the flip result lands at the end","COLD_D",None,8,"st"),
 ("turkey","JACKSON","\"I just throw the turkey in the trash\"","INTRO",28.5,6,"st"),
 ("honest","CONFESSION","API keys pasted into a model: \"a million times\"","OPENR_A",179.5,7,"st"),
 ("cheese","THE TRAP","cheese on a mousetrap, and they walked right on","OPENR_A",270.0,7,"st"),
 ("tiers","CHRIS'S TIER LIST","frontier labs, then TEEs, then nobody","OPENR_B",664.0,8,"st"),
 ("fake","CHRIS","\"I don't trust ZDR at all. I assume that's fake.\"","OPENR_B",728.0,7,"st"),
 ("thresh","THRESHOLD SIGNATURES","15 of 20 sign and the money moves","CHAIN_A",861.0,7,"st"),
 ("took","CHRIS","\"and then of course they just took the money\"","CHAIN_A",966.0,6,"st"),
 ("isneg","CHRIS, OLD HEAD","is-negative: a whole library for one check","CHAIN_B",1116.0,7,"st"),
 ("haiku","TODAY'S PICKER","Haiku, \"Anthropic's dumbest model\"","PERP",1297.5,7,"st"),
 ("later","THE FLIP SETTLES AFTER THE SHOW","result at the end","PERP",1352.0,8,"st2"),
 ("base","BASELINE","tennis or not tennis: a coin flip","FT_A",1518.5,6,"st2"),
 ("r8","RANK-8 LORA","400 steps  ·  about 40 minutes  ·  92%","FT_A",1662.0,7,"st2"),
 ("p93","LAYER 11 PROBE","93%. Beat the fine-tune.","FT_B",1950.0,7,"st2"),
 ("garbage","CHRIS","\"the internet browser is a piece of garbage\"","WEB_A",2323.0,6,"st2"),
 ("flight","AGENT TRAVEL DESK","$600 a ticket for a $25 flight","WEB_C",2752.0,8,"st2"),
 ("aes","HOW A TEE WORKS","memory stays encrypted, only the CPU sees it","ENCL",2958.0,8,"st2"),
 ("unconf","UNCONFIRMED","a rumor. Nobody has shown a proof.","RUMOR",3197.0,8,"st2"),
 ("rsa","JACKSON LOOKED IT UP","RSA isn't elliptic curve. Bitcoin is fine for now.","RUMOR",3271.5,8,"st2"),
 ("update","POST-SHOW UPDATE","the Bitcoin flip lost: −$25","OUTRO",3376.5,9,"st2")]
brand = {"show":"UNDERPOD","show_main":"UNDERPOD","accent":[255,210,74],"source":f"{W}/src/jackson_720.mp4",
 "title_card":{"bg_frame":600,"line":"EPISODE 25   ·   Fake Secrets. Real Thieves.","dur":4.5},
 "end_card":{"bg_frame":3380,"kicker":"POST-SHOW UPDATE","lines":["The Bitcoin flip lost: −$25","Next week: Tyler returns  ·  Witness encryption","Not financial advice. Our opinions are ours, not our employers'."],"cta":"LIKE  +  SUBSCRIBE","dur":8},
 "lower_thirds":[{"name":n,"kicker":k,"title":t} for n,k,t,_,_ in LT],
 "stats":[{"name":n,"kicker":k,"main":m} for n,k,m,*_ in ST],
 "thumbnail":{"text":"YOUR AI PRIVACY IS FAKE","out":"/Users/jcook/Personal/permanent-underpod/media/ep25/ep25-thumbnail.png",
  "faces":[{"track":"chris","t":THUMB_C,"cx":900,"top":90,"h":630},{"track":"jackson","t":THUMB_J,"cx":380,"top":90,"h":630}]}
 if (THUMB_C := float(os.environ.get("THUMB_C", 600))) and (THUMB_J := float(os.environ.get("THUMB_J", 600))) else None}
json.dump(brand, open(f"{EP}/brand.json","w"), indent=1, ensure_ascii=False)
def hard(i, m0, m1, mute=()):
    return {"id":i,"m0":m0,"m1":m1,"hard_m0":True,"hard_m1":True,"mute":[[p,m0-0.1,m1+0.1] for p in mute]}
COLD = [("COLD_A",3157.4,3163.72,"chris",("jackson",)),("COLD_A2",3227.9,3232.81,"chris",("jackson",)),
        ("COLD_B",954.5,967.95,"chris",("jackson",)),("COLD_C",174.5,181.85,None,()),
        ("COLD_D",1266.5,1284.3,"jackson",("chris",))]
blocks = [hard(c[0], c[1], c[2], c[4]) for c in COLD] + [{"id":"CARD_TITLE","card":"card_title.mov"},
 {"id":"INTRO","m0":1.4,"m1":37.37,"hard_m1":True},
 {"id":"OPENR_A","m0":37.37,"m1":494.9,"hard_m0":True},
 {"id":"OPENR_B","m0":649.18,"m1":806.85,"hard_m0":True},
 {"id":"CHAIN_A","m0":806.85,"m1":1035.60,"hard_m1":True},
 {"id":"CHAIN_B","m0":1042.30,"m1":1178.4,"hard_m0":True},
 {"id":"CHAIN_C","m0":1225.05,"m1":1265.7,"hard_m0":True,"mute":[["jackson",1224.5,1226.5]]},
 {"id":"PERP","m0":1265.7,"m1":1393.3},
 {"id":"FT_A","m0":1403.2,"m1":1856.5,"hard_m1":True},
 {"id":"FT_B","m0":1941.8,"m1":2031.2,"hard_m0":True,"mute":[["jackson",1941.4,1943.6]]},
 {"id":"FT_C","m0":2191.4,"m1":2228.4},
 {"id":"WEB_A","m0":2291.8,"m1":2341.45},
 {"id":"WEB_B","m0":2351.15,"m1":2624.8,"hard_m0":True},
 {"id":"WEB_C","m0":2740.9,"m1":2809.32,"hard_m0":True,"hard_m1":True},
 {"id":"WEB_D","m0":2843.2,"m1":2886.4,"hard_m1":True},
 {"id":"ENCL","m0":2898.6,"m1":3112.65},
 {"id":"RUMOR","m0":3120.2,"m1":3372.1},
 {"id":"OUTRO","m0":3372.1,"m1":3413.5,"hard_m1":True,"mute":[["jackson",3410.0,3413.7]]},
 {"id":"CARD_END","card":"card_end.mov"}]
B = {b["id"]: b for b in blocks}
PIPB = ["FT_A","FT_B","FT_C","WEB_A","WEB_B","WEB_C","WEB_D","ENCL","RUMOR","OUTRO"]
CROP = [930,180,495,30]
pips = [{"file":SC,"block":"PERP","m0":1312.0,"m1":1319.0,"anchor":ANCHOR,"mode":"full","crop":[928,522,495,2]},
        {"file":SC,"block":"PERP","m0":1319.0,"m1":1393.3,"anchor":ANCHOR,"mode":"corner","crop":CROP}] + \
       [{"file":SC,"block":b,"m0":B[b]["m0"],"m1":B[b]["m1"],"anchor":ANCHOR,"mode":"corner","crop":CROP} for b in PIPB]
ov = [{"name":"st_coldopen","block":"COLD_A","rel":0.0,"dur":6,"kind":"st"},
      {"name":"st_tease","block":"COLD_D","rel":6.0,"dur":8,"kind":"st"}]
for n,k,t,b,m in LT: ov.append({"name":f"lt_{n}","block":b,"m":m,"dur":6,"kind":"lt"})
for n,k,mn,b,m,d,kind in ST[2:]: ov.append({"name":f"st_{n}","block":b,"m":m,"dur":d,"kind":kind})
ov.sort(key=lambda o: o.get("m", -1))
force = [{"m0":c[1],"m1":c[2],"type":"solo","people":[c[3]]} for c in COLD if c[3]] + \
        [{"m0":174.5,"m1":181.85,"type":"duo","people":["jackson","chris"]},
         {"m0":1.4,"m1":9.0,"type":"solo","people":["jackson"]},
         {"m0":3404.0,"m1":3413.5,"type":"duo","people":["jackson","chris"]}]
plan = {"blocks":blocks,
 "protect":[[c[1],c[2]] for c in COLD] + [[1.4,12.0],[1310.0,1320.0],[3403.0,3414.0]],
 "force_shots":force,
 "face_cx":{"jackson":660,"chris":630},"panel_order":["jackson","chris"],
 "params":{"idle_gain":0.12,"group_thresh":0.25,"group_hold":1.0,"react_thresh":0.6,"min_shot":3.0,"gain_target":0.022,"dead_air_min":1.2,"dead_air_keep":0.4,"dead_air_net":0.6},
 "gain_spans":{"jackson":[[43,66],[291,324],[1404,1425],[1463,1480]],"chris":[[89,109],[196,230],[823,845],[2927,2960]]},
 "pips":pips,"overlays":ov,
 "sheet":[{"label":"Cold open","block":"COLD_A"},{"label":"Title","block":"CARD_TITLE"},
  {"label":"No Tyler, no turkey","block":"INTRO"},
  {"label":"OpenRouter: fake API keys went in, someone used them","block":"OPENR_A"},
  {"label":"What OpenRouter actually is","block":"OPENR_A","m":192.0},
  {"label":"Four providers, four ways the prompts got out","block":"OPENR_A","m":281.0},
  {"label":"Chris's tier list for your credentials","block":"OPENR_B"},
  {"label":"Who enforces zero data retention?","block":"OPENR_B","m":733.0},
  {"label":"The Chainflip hack: a validator took the vault","block":"CHAIN_A"},
  {"label":"Is open source still worth the risk?","block":"CHAIN_B","m":1098.0},
  {"label":"Perp of Fortune: short MiniMax 10×, Bitcoin down","block":"PERP"},
  {"label":"Jackson fine-tunes a model on his laptop","block":"FT_A"},
  {"label":"LoRA, explained","block":"FT_A","m":1552.0},
  {"label":"Probing: stop the model halfway","block":"FT_A","m":1707.0},
  {"label":"The probe beats the fine-tune","block":"FT_B"},
  {"label":"How long does the web browser have left?","block":"WEB_A"},
  {"label":"Top of the funnel: why Amazon blocks agents","block":"WEB_B","m":2407.0},
  {"label":"The agent that tried to pay $600 for a $25 flight","block":"WEB_C"},
  {"label":"Secure enclaves: what a TEE actually is","block":"ENCL"},
  {"label":"Gossip corner: the factoring rumor","block":"RUMOR"},
  {"label":"Outro and the flip result","block":"OUTRO"},
  {"label":"End card","block":"CARD_END"}]}
json.dump(plan, open(f"{EP}/remote_plan.json","w"), indent=1, ensure_ascii=False)
R = {"out":"/Users/jcook/Personal/permanent-underpod/media/ep25/Underpod - Ep 25 (Final Cut).mp4",
 "chain":"highpass=f=80,afftdn=nr=14:nf=-50:tn=1,volume=8dB,adynamicequalizer=dfrequency=6800:dqfactor=2.5:tfrequency=6800:tqfactor=2.5:mode=cutabove:threshold=0.01:ratio=4:range=8:attack=2:release=40,acompressor=threshold=-20dB:ratio=3:attack=15:release=250:knee=6,treble=f=9500:width_type=q:w=0.8:g=1.5,loudnorm=I=-16:TP=-1.5:LRA=5",
 "target_lufs":-11.8,"limit":0.7,
 "logo":{"file":"logo.png","width":170,"alpha":0.8,"hide_during":["CARD_TITLE","CARD_END"]},"sfx":[],"anim":[]}
if not os.path.exists(f"{EP}/render.json"):
    json.dump(R, open(f"{EP}/render.json","w"), indent=1)
