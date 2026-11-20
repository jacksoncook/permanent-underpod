import json, os
W = os.getcwd(); EP = "/Users/jcook/Personal/permanent-underpod/episodes/ep24"
SC = "/Users/jcook/Personal/permanent-underpod/media/ep24/raw/Untitled_recording-chris-screen-00h_29m_02s_332ms-StreamYard.mp4"
ANCHOR = 1741.852
LT = [("intro","EPISODE 24","NINE OUTAGES. ZERO HACKERS.","INTRO",20.0),
 ("faa","THE FAA GROUND STOP","FRIDAY THE 13TH: EVERY DEPARTURE STOPPED","OUT_B",134.0),
 ("msft","MICROSOFT 365","HOW DOES IT STAY DOWN FOR A WHOLE DAY?","OUT_B",422.0),
 ("vendor","THE BREAK-INS","WHEN THE WAY IN IS YOUR VENDOR","OUT_B",608.5),
 ("chain","THE CHAINALYSIS BREACH","THE COMPANY THAT TRACES CRYPTO GOT HACKED","CHAIN",842.0),
 ("who","WHO DID IT?","TYLER BORROWS THE HAT","CHAIN_B",1119.5),
 ("ablit","ABLITERATED","NOT \"OBLITERATED.\" JACKSON FINDS OUT.","CHAIN_D",1584.0),
 ("perp","PERP OF FORTUNE","SHORT SK HYNIX 10×  ·  BITCOIN DOWN","PERP",1686.0),
 ("vibes","THE BITCOIN VIBES","IS IRREVERSIBLE MONEY A HARDER SELL NOW?","PERP",1800.0),
 ("ipo","ANTHROPIC GOES PUBLIC","THE STATEMENT AND THE IPO, SAME WEEK","ANTH",2100.0),
 ("float","LOW FLOAT, HIGH FDV","THE IPO THAT LOOKS LIKE A TOKEN LAUNCH","ANTH",2222.0),
 ("disc","PRICE DISCOVERY","DID THE PERP CALL THE IPO?","ANTH",2721.0),
 ("rain","PERP STARTUP PITCH","RAIN PERPS FOR YOUR WEEKEND","ANTH",2791.0),
 ("gta","GTA 6","CHRIS, ON THE GROUND","GTA",3004.5),
 ("ondev","ON-DEVICE AGENTS","WHAT IF YOUR PHONE WATCHED EVERYTHING?","ONDEV",3258.0),
 ("final","PERP FINAL","BOTH BETS GREEN","FINAL",3458.5)]
ST = [("coldopen","EPISODE 24","In this pod…","COLD_A",None,6,"st"),
 ("count","JACKSON DID THE LEGWORK","6 of 9 outages: their own change","INTRO",43.0,8,"st"),
 ("house","TYLER","\"it's coming from within the house\"","INTRO",69.0,6,"st"),
 ("nine","THE BREAK-INS","9 of 13 came in through a vendor","INTRO",92.0,7,"st"),
 ("fifty","TYLER","50 years of uptime. Then a new router.","OUT_B",163.0,7,"st"),
 ("jim","CHRIS","Jim has the key. Jim is in the Bahamas.","OUT_B",592.0,7,"st"),
 ("corn","TYLER","corn123  →  corn1234","OUT_B",750.0,6,"st"),
 ("phrase","PHRASE OF THE MONTH","\"not a cyber attack\"","OUT_B",766.0,7,"st"),
 ("open","CHAINALYSIS","disclosed Oct 30  ·  still unresolved","CHAIN",866.0,8,"st"),
 ("word","JACKSON","\"one of the most… I don't even know the word\"","PERP",1643.5,7,"st"),
 ("green","FIRST TIME IN POD HISTORY","both bets green at once","PERP",1752.0,7,"st2"),
 ("wall","ERIC WALL'S THREAD","irreversible cuts both ways","PERP",1853.0,7,"st2"),
 ("pct","FACT CHECK","the IPO floated about 7%","ANTH",2393.0,7,"st2"),
 ("vote","TYLER","\"no voting rights, and you will be happy\"","ANTH",2689.0,7,"st2"),
 ("dryer","PREDICTION MARKETS","a hair dryer vs. the airport thermometer","ANTH",2841.0,8,"st2"),
 ("human","CHRIS","\"maybe the last human-made game ever\"","GTA",3069.0,7,"st2"),
 ("food","JACKSON'S FOOD MATH","quality = deliciousness ÷ price","ONDEV",3359.0,8,"st2"),
 ("tally","PERP FINAL","the flip: about $25  ·  SK Hynix short: about $2","FINAL",3466.0,8,"st2")]
brand = {"show":"UNDERPOD","show_main":"UNDERPOD","accent":[255,210,74],"source":f"{W}/src/jackson_720.mp4",
 "title_card":{"bg_frame":600,"line":"EPISODE 24   ·   Nine Outages. Zero Hackers.","dur":4.5},
 "end_card":{"bg_frame":3400,"kicker":"NEXT WEEK ON","lines":["Perp of Fortune  ·  The layer-2 series returns","Not financial advice. Our opinions are ours, not our employers'."],"cta":"LIKE  +  SUBSCRIBE","dur":7},
 "lower_thirds":[{"name":n,"kicker":k,"title":t} for n,k,t,_,_ in LT],
 "stats":[{"name":n,"kicker":k,"main":m} for n,k,m,*_ in ST],
 "thumbnail":{"text":"WHO BROKE THE INTERNET?","out":"/Users/jcook/Personal/permanent-underpod/media/ep24/ep24-thumbnail.png","faces":[{"track":"chris","t":348.0,"cx":640,"top":60,"h":660},{"track":"jackson","t":256.0,"cx":240,"top":130,"h":590},{"track":"tyler","t":258.0,"cx":1040,"top":140,"h":580}]}}
json.dump(brand, open(f"{EP}/brand.json","w"), indent=1, ensure_ascii=False)
def hard(i, m0, m1, mute=()):
    return {"id":i,"m0":m0,"m1":m1,"hard_m0":True,"hard_m1":True,"mute":[[p,m0-0.1,m1+0.1] for p in mute]}
COLD = [("COLD_A",160.95,175.01,"tyler",("chris",)),("COLD_B",401.3,408.3,"jackson",("chris","tyler")),
        ("COLD_C",3104.2,3111.75,"chris",("tyler","jackson")),("COLD_D",1737.3,1743.5,None,("tyler",))]
LSJ, LSC, LSC_SHORT, LST = (3517.0,3519.3), (3521.2,3527.9), (3523.75,3527.9), (3531.6,3533.2)
LS = [("LS1_J",LSJ,"jackson"),("LS1_C",LSC_SHORT,"chris"),("LS2_J",LSJ,"jackson"),("LS2_C",LSC,"chris"),("LS2_T",LST,"tyler")]
def ls(i):
    n, (a, b), who = next(x for x in LS if x[0] == i)
    return hard(n, a, b, tuple(p for p in ("jackson","chris","tyler") if p != who))
blocks = [hard(c[0], c[1], c[2], c[4]) for c in COLD] + [{"id":"CARD_TITLE","card":"card_title.mov"},
 {"id":"INTRO","m0":1.4,"m1":110.0},
 ls("LS1_J"), ls("LS1_C"),
 {"id":"OUT_B","m0":110.0,"m1":835.35},
 {"id":"CHAIN","m0":835.35,"m1":1071.5},
 {"id":"CHAIN_B","m0":1118.45,"m1":1226.35,"mute":[["jackson",1119.4,1120.9]]},
 {"id":"CHAIN_C","m0":1242.14,"m1":1343.16,"hard_m1":True},
 {"id":"CHAIN_D","m0":1346.55,"m1":1621.1,"hard_m0":True,"mute":[["chris",1346.3,1347.7]]},
 ls("LS2_J"), ls("LS2_C"), ls("LS2_T"),
 {"id":"PERP","m0":1621.1,"m1":1960.37},
 {"id":"BTC_B","m0":2080.5,"m1":2093.8},
 {"id":"ANTH","m0":2093.8,"m1":3000.67,"hard_m1":True},
 {"id":"GTA","m0":3000.67,"m1":3175.3,"hard_m0":True,"hard_m1":True,"mute":[["tyler",3173.4,3177.5]]},
 {"id":"ONDEV","m0":3257.3,"m1":3457.2,"hard_m0":True,"mute":[["chris",3255.9,3257.5]]},
 {"id":"FINAL","m0":3457.2,"m1":3535.6,"hard_m1":True},
 {"id":"OUTRO_END","m0":3567.75,"m1":3571.9,"hard_m0":True,"hard_m1":True},
 {"id":"CARD_END","card":"card_end.mov"}]
PIPB = [("PERP",1749.0,1960.37),("BTC_B",2080.5,2093.8),("ANTH",2093.8,3000.67),("GTA",3000.67,3175.3),("ONDEV",3257.3,3457.2),
        ("FINAL",3457.2,3535.6),("OUTRO_END",3567.75,3571.9)]
CROP = [1010,205,455,222]
pips = [{"file":SC,"block":"PERP","m0":1742.3,"m1":1749.0,"anchor":ANCHOR,"mode":"full"}] + \
       [{"file":SC,"block":b,"m0":a,"m1":z,"anchor":ANCHOR,"mode":"corner","crop":CROP} for b,a,z in PIPB]
ov = [{"name":"st_coldopen","block":"COLD_A","rel":0.0,"dur":6,"kind":"st"}]
for n,k,t,b,m in LT: ov.append({"name":f"lt_{n}","block":b,"m":m,"dur":6,"kind":"lt"})
for n,k,mn,b,m,d,kind in ST[1:]: ov.append({"name":f"st_{n}","block":b,"m":m,"dur":d,"kind":kind})
ov.sort(key=lambda o: o.get("m", -1))
force = [{"m0":c[1],"m1":c[2],"type":"solo","people":[c[3]]} for c in COLD if c[3]] + \
        [{"m0":1737.3,"m1":1743.5,"type":"duo","people":["jackson","chris"]},
         {"m0":1.4,"m1":8.0,"type":"solo","people":["jackson"]},
         {"m0":LSJ[0],"m1":LSJ[1],"type":"solo","people":["jackson"]},
         {"m0":LSC[0],"m1":LSC[1],"type":"solo","people":["chris"]},
         {"m0":LST[0],"m1":LST[1],"type":"solo","people":["tyler"]},
         {"m0":3533.2,"m1":3535.6,"type":"trio"},
         {"m0":3567.75,"m1":3571.9,"type":"trio"}]
plan = {"blocks":blocks,
 "protect":[[c[1],c[2]] for c in COLD] + [[1.4,12.0],[1741.0,1750.0],[3516.5,3535.6],[3567.0,3572.0]],
 "force_shots":force,
 "face_cx":{"jackson":580,"chris":610,"tyler":800},"panel_order":["jackson","chris","tyler"],
 "params":{"idle_gain":0.12,"group_thresh":0.25,"group_hold":1.0,"react_thresh":0.6,"min_shot":3.0,"gain_target":0.028,"dead_air_min":1.2,"dead_air_keep":0.4,"dead_air_net":0.6},
 "gain_spans":{"jackson":[[20,48],[302,314],[514,558],[1363,1383]],"chris":[[258,281],[477,510],[949,997],[2234,2262]],"tyler":[[151,173],[422,452],[1159,1190],[1804,1850]]},
 "pips":pips,"overlays":ov,
 "sheet":[{"label":"Cold open","block":"COLD_A"},{"label":"Title","block":"CARD_TITLE"},
  {"label":"Nine outages, zero hackers","block":"INTRO"},
  {"label":"The FAA ground stop and the one router","block":"OUT_B","m":116.0},
  {"label":"How does Microsoft stay down for a day?","block":"OUT_B","m":422.0},
  {"label":"The break-ins: when the way in is your vendor","block":"OUT_B","m":608.0},
  {"label":"The Chainalysis breach","block":"CHAIN"},
  {"label":"Who did it? Tyler's theories","block":"CHAIN_B"},
  {"label":"Is Chainalysis why your bitcoin is traceable?","block":"CHAIN_D","m":1360.0},
  {"label":"Abliterated, not obliterated","block":"CHAIN_D","m":1509.0},
  {"label":"Perp of Fortune: short SK Hynix 10×, Bitcoin down","block":"PERP"},
  {"label":"The Bitcoin vibes: Eric Wall on irreversible money","block":"PERP","m":1797.0},
  {"label":"Anthropic goes public: the statement and the IPO","block":"ANTH"},
  {"label":"Low float, high FDV: the IPO that looks like a token launch","block":"ANTH","m":2221.0},
  {"label":"Governance as an afterthought","block":"ANTH","m":2667.0},
  {"label":"Did the perp call the IPO? Plus rain perps","block":"ANTH","m":2721.0},
  {"label":"The hair dryer, the intern, and the SBF documentary","block":"ANTH","m":2815.0},
  {"label":"GTA 6: Chris, on the ground","block":"GTA"},
  {"label":"On-device agents and Jackson's $7 curry","block":"ONDEV"},
  {"label":"Perp final, and the like-and-subscribe audition","block":"FINAL"},
  {"label":"End card","block":"CARD_END"}]}
json.dump(plan, open(f"{EP}/remote_plan.json","w"), indent=1, ensure_ascii=False)
