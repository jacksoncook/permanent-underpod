import json, os
W = os.getcwd(); EP = "/Users/jcook/Personal/permanent-underpod/episodes/ep23"
SC = "/Users/jcook/Personal/permanent-underpod/media/ep23/raw/Untitled_recording-chris-screen-00h_23m_11s_158ms-StreamYard.mp4"
ANCHOR = 1390.816
LT = [("intro","EPISODE 23","OPEN MODELS JUST LOST THEIR CHAMPION","INTRO",19.5),
 ("fingerprint","THE FINGERPRINT","A BLOG POST SAYS THE WEIGHTS GIVE AWAY THE GPU","INTRO",222.5),
 ("after","AFTER JENSEN","DOES NVIDIA'S OPEN-MODEL PUSH SURVIVE HIM?","NV_B",481.0),
 ("timing","WHY NOW?","CHRIS PUTS ON THE HAT","NV_B",699.0),
 ("nyse","NYSE × AVALANCHE","24/7 TOKENIZED STOCKS ON A PRIVATE CHAIN","NYSE",1077.0),
 ("perp","PERP OF FORTUNE","LONG GOOGLE 20×  ·  BITCOIN DOWN","PERP",1357.0),
 ("tpu","GOOGLE'S NEW TPU","PRIVATE INFERENCE COMES TO THE BIG CLOUD","TPU",1484.0),
 ("agent","CHRIS'S PRIVATE AGENT","AN ASSISTANT SERVED OUT OF AN ENCLAVE","AGENT",1949.0),
 ("gpu","COLLECTOR'S ITEM","THE JENSEN-ERA GPU","AGENT",2089.0),
 ("econ","THE ECONOMICS","WHAT DOES PRIVATE INFERENCE COST?","ECON",2395.0),
 ("flip","THE BITCOIN FLIP","21 SECONDS FROM OUR FIRST WIN","ECON",2777.0),
 ("million","THE OFFER","$1M AND WE'LL LIST ANY PERP YOU WANT","ECON_B",3081.5),
 ("liquid","LAYER-2 SERIES","LIQUID: THE SIDECHAIN THAT ISN'T AN L2","LIQUID",3168.5)]
ST = [("coldopen","EPISODE 23","In this pod…","COLD_A",None,6,"st"),
 ("megaspeed","THE ALLEGATION","export-controlled GPUs, routed via Singapore","INTRO",68.0,8,"st"),
 ("claim","THE BLOG POST'S CLAIM","99.99999%: trained on Blackwells","INTRO",291.0,8,"st"),
 ("suck","THE EXPORT RULE","\"you can sell chips, but they have to suck\"","NV_B",385.0,7,"st"),
 ("reports","CHRIS","\"a thousand and two reports\"","NV_B",668.5,6,"st"),
 ("singapore","NVIDIA REVENUE, PER CHRIS","Singapore: 22%  ·  $10.2B a quarter","NV_C",900.0,8,"st"),
 ("friends","THE VALIDATORS","\"me and five of my friends at the NYSE\"","NYSE",1191.0,7,"st"),
 ("database","CHRIS'S TEST","why couldn't that be a database?","NYSE",1313.0,7,"st"),
 ("random","THE THESIS","\"random draw\"","PERP",1442.0,6,"st2"),
 ("monkey","JACKSON","true entropy from a Vietnamese tree monkey","PERP",1462.0,7,"st2"),
 ("trust","PRIVATE INFERENCE","trust the chip, not the provider","TPU",1601.0,7,"st2"),
 ("embody","EMBODY.IS","Intel TDX enclave + privately served models","AGENT",2016.0,8,"st2"),
 ("gas","GEAR ACQUISITION SYNDROME","buy the thing, never do the hobby","AGENT",2247.0,7,"st2"),
 ("bike","JACKSON","a full Ironman on a commuter bike","AGENT",2294.0,7,"st2"),
 ("price","GLM 5.3 FLASH  ·  PER 1M TOKENS","from 4¢ in the clear  ·  15¢ private","ECON",2511.0,8,"st2"),
 ("cvm","THE WORKSPACE","a confidential VM: about $25 a month","ECON",2605.0,7,"st2"),
 ("settled","THE FLIP SETTLES","Bitcoin down: +$22.68","ECON",2812.0,8,"st2"),
 ("poly","THE TRICK","50 accounts. Post the one that won.","ECON",2852.0,7,"st2"),
 ("vix","UNDERPOD VOLATILITY INDEX","Jackson's tennis ranking ÷ the Bitcoin price","ECON_B",3118.0,8,"st2"),
 ("multisig","LIQUID","an 11-of-15 federation multisig","LIQ_B",3237.0,7,"st2"),
 ("recap","RECAPITALIZED","back to 100% backing","LIQ_B",3363.0,7,"st2"),
 ("testnet","TYLER","\"a quasi testnet for Bitcoin\"","LIQ_B",3496.0,7,"st2"),
 ("devcon","CHRIS'S SELL SIGNAL","saw Vitalik dancing. Did not sell.","LIQ_C",3762.0,7,"st2"),
 ("final","PERP FINAL","Flip +$22.68  ·  Long Google 20×: +$4.28","OUTRO_B",3871.5,8,"st2")]
brand = {"show":"UNDERPOD","show_main":"UNDERPOD","accent":[255,210,74],"source":f"{W}/src/jackson_720.mov",
 "title_card":{"bg_frame":600,"line":"EPISODE 23   ·   Open Models Just Lost Their Champion","dur":4.5},
 "end_card":{"bg_frame":3400,"kicker":"NEXT WEEK ON","lines":["Life after Jensen  ·  Perp of Fortune","The layer-2 series continues","Not financial advice. Our opinions are ours, not our employers'."],"cta":"LIKE  +  SUBSCRIBE","dur":7},
 "lower_thirds":[{"name":n,"kicker":k,"title":t} for n,k,t,_,_ in LT],
 "stats":[{"name":n,"kicker":k,"main":m} for n,k,m,*_ in ST],
 "thumbnail":{"text":"THE CHIP KING IS OUT","out":"/Users/jcook/Personal/permanent-underpod/media/ep23/ep23-thumbnail.png","faces":[{"track":"jackson","file":"src/jackson_720.mov","t":1399.0,"cx":640,"top":90,"h":630},{"track":"tyler","t":1216.0,"cx":250,"top":120,"h":590},{"track":"chris","t":2747.0,"cx":1040,"top":140,"h":570}]}}
json.dump(brand, open(f"{EP}/brand.json","w"), indent=1, ensure_ascii=False)
def cold(i, m0, m1, who, mute=()):
    return {"id":i,"m0":m0,"m1":m1,"hard_m0":True,"hard_m1":True,"mute":[[p,m0-0.1,m1+0.1] for p in mute]}
COLD = [("COLD_A",599.7,610.1,"chris",("tyler","jackson")),("COLD_B",377.23,389.87,"tyler",("chris","jackson")),
        ("COLD_C",2088.2,2097.6,"tyler",("chris","jackson")),("COLD_D",2776.1,2788.2,"jackson",("chris","tyler"))]
blocks = [cold(*c) for c in COLD] + [{"id":"CARD_TITLE","card":"card_title.mov"},
 {"id":"INTRO","m0":0.6,"m1":306.03,"hard_m1":True},
 {"id":"NV_B","m0":355.24,"m1":724.71},
 {"id":"NV_C","m0":761.1,"m1":959.4,"hard_m0":True},
 {"id":"NV_D","m0":1063.8,"m1":1073.22},
 {"id":"NYSE","m0":1073.22,"m1":1352.5},
 {"id":"PERP","m0":1352.5,"m1":1476.2,"hard_m1":True},
 {"id":"TPU","m0":1476.2,"m1":1932.0,"hard_m0":True,"mute":[["chris",1475.9,1476.7]]},
 {"id":"AGENT","m0":1932.0,"m1":2329.98,"hard_m1":True},
 {"id":"ECON","m0":2392.19,"m1":2973.5,"mute":[["jackson",2390.9,2393.3]]},
 {"id":"ECON_B","m0":3078.4,"m1":3162.0},
 {"id":"LIQUID","m0":3162.0,"m1":3181.7},
 {"id":"LIQ_B","m0":3205.48,"m1":3614.65},
 {"id":"LIQ_C","m0":3654.74,"m1":3835.85,"hard_m1":True,"mute":[["tyler",3654.7,3656.9],["tyler",3834.3,3836.0]]},
 {"id":"OUTRO_B","m0":3870.4,"m1":3884.0,"hard_m0":True,"hard_m1":True},
 {"id":"CARD_END","card":"card_end.mov"}]
PIPB = [("PERP",1399.0,1476.2),("TPU",1476.2,1932.0),("AGENT",1932.0,2329.98),("ECON",2392.19,2973.5),("ECON_B",3078.4,3162.0),("LIQUID",3162.0,3181.7),
        ("LIQ_B",3205.48,3614.65),("LIQ_C",3654.74,3835.85),("OUTRO_B",3870.4,3884.0)]
CROP = [1010,205,455,222]
pips = [{"file":SC,"block":"PERP","m0":1391.6,"m1":1399.0,"anchor":ANCHOR,"mode":"full"}] + \
       [{"file":SC,"block":b,"m0":a,"m1":z,"anchor":ANCHOR,"mode":"corner","crop":CROP} for b,a,z in PIPB]
ov = [{"name":"st_coldopen","block":"COLD_A","rel":0.0,"dur":6,"kind":"st"}]
for n,k,t,b,m in LT: ov.append({"name":f"lt_{n}","block":b,"m":m,"dur":6,"kind":"lt"})
for n,k,mn,b,m,d,kind in ST[1:]: ov.append({"name":f"st_{n}","block":b,"m":m,"dur":d,"kind":kind})
ov.sort(key=lambda o: o.get("m", -1))
plan = {"blocks":blocks,
 "protect":[[c[1],c[2]] for c in COLD] + [[0.9,12.0],[1391.0,1400.0],[2776.0,2815.0],[3863.0,3884.0]],
 "force_shots":[{"m0":c[1],"m1":c[2],"type":"solo","people":[c[3]]} for c in COLD] + [{"m0":0.6,"m1":10.5,"type":"solo","people":["jackson"]},{"m0":3870.4,"m1":3884.0,"type":"trio"}],
 "face_cx":{"jackson":660,"chris":634,"tyler":790},"panel_order":["jackson","chris","tyler"],
 "params":{"idle_gain":0.12,"group_thresh":0.25,"group_hold":1.0,"react_thresh":0.6,"min_shot":3.0,"gain_target":0.028,"dead_air_min":1.2,"dead_air_keep":0.4,"dead_air_net":0.6},
 "gain_spans":{"jackson":[[1683,1728],[2249,2262],[3187,3201],[3870.5,3883]],"chris":[[1098,1183],[1295,1346],[1730,1790],[1956,2080]],"tyler":[[125,195],[398,445],[1504,1648],[3227,3283]]},
 "pips":pips,"overlays":ov,
 "sheet":[{"label":"Cold open","block":"COLD_A"},{"label":"Title","block":"CARD_TITLE"},
  {"label":"Jensen is out: open models lose their champion","block":"INTRO"},
  {"label":"The fingerprint: a blog post says China's models trained on Blackwells","block":"INTRO","m":220.0},
  {"label":"Does Nvidia's open-model push survive him?","block":"NV_B","m":462.0},
  {"label":"Why now? The timing, and who knew","block":"NV_B","m":695.0},
  {"label":"What Jensen does next","block":"NV_C","m":928.0},
  {"label":"NYSE picks Avalanche for 24/7 tokenized stocks","block":"NYSE"},
  {"label":"Perp of Fortune: long Google 20×, Bitcoin down by random draw","block":"PERP"},
  {"label":"Google's new TPU brings private inference to the cloud","block":"TPU"},
  {"label":"Chris's private agent, served out of an enclave","block":"AGENT"},
  {"label":"The Jensen-era GPU as a collector's item (and gear acquisition syndrome)","block":"AGENT","m":2083.0},
  {"label":"What private inference costs","block":"ECON"},
  {"label":"The Bitcoin flip settles: the first win","block":"ECON","m":2766.0},
  {"label":"After-hours perps, Korea, and the $1M perp offer","block":"ECON","m":2900.0},
  {"label":"Layer-2 series: Liquid, the sidechain that isn't an L2","block":"LIQUID"},
  {"label":"Formal verification and Ethereum's social consensus","block":"LIQ_C"},
  {"label":"Outro","block":"OUTRO_B"},{"label":"End card","block":"CARD_END"}]}
json.dump(plan, open(f"{EP}/remote_plan.json","w"), indent=1, ensure_ascii=False)
