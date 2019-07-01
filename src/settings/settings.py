class Settings:
    def __init__(self):
        self.filter_order = 100
        self.coef = {
            'bandpass_1': self.BANDPASS_1,
            'bandpass_2': self.BANDPASS_2,
            'bandpass_3': self.BANDPASS_3,
            'bandpass_4': self.BANDPASS_4,
            'bandpass_5': self.BANDPASS_5,
            'bandpass_6': self.BANDPASS_6
        }
        
    BANDPASS_1 = [
        0.0005639060613766,0.0006040811817713,0.0006594282091518,0.0007321077497322,
        0.000824205122477,0.0009377075753765, 0.001074481997452, 0.001236253346934,
        0.001424584011586, 0.001640854310537, 0.001886244338259, 0.002161717340569,
        0.002468004799849, 0.002805593392128, 0.003174713962476, 0.003575332647349,
        0.004007144253383, 0.004469567981749, 0.004961745565819, 0.005482541867649,
        0.006030547956054, 0.006604086665812, 0.007201220614251, 0.007819762628193,
        0.008457288511276, 0.009111152059257, 0.009778502209185,  0.01045630218766,
        0.01114135050375,  0.01183030361412,  0.01251970007099,  0.01320598594893,
        0.01388554133324,  0.01455470764158,  0.01520981554175,   0.0158472132214,
        0.01646329476163,  0.01705452836341,  0.01761748417698,  0.01814886148603,
        0.01864551500423,  0.01910448004822,  0.01952299636119,  0.01989853037251,
        0.02022879569254,  0.02051177165769,  0.02074571975755,  0.02092919779564,
        0.02106107165501,  0.02114052456208,  0.02116706376446,  0.02114052456208,
        0.02106107165501,  0.02092919779564,  0.02074571975755,  0.02051177165769,
        0.02022879569254,  0.01989853037251,  0.01952299636119,  0.01910448004822,
        0.01864551500423,  0.01814886148603,  0.01761748417698,  0.01705452836341,
        0.01646329476163,   0.0158472132214,  0.01520981554175,  0.01455470764158,
        0.01388554133324,  0.01320598594893,  0.01251970007099,  0.01183030361412,
        0.01114135050375,  0.01045630218766, 0.009778502209185, 0.009111152059257,
        0.008457288511276, 0.007819762628193, 0.007201220614251, 0.006604086665812,
        0.006030547956054, 0.005482541867649, 0.004961745565819, 0.004469567981749,
        0.004007144253383, 0.003575332647349, 0.003174713962476, 0.002805593392128,
        0.002468004799849, 0.002161717340569, 0.001886244338259, 0.001640854310537,
        0.001424584011586, 0.001236253346934, 0.001074481997452,0.0009377075753765,
        0.000824205122477,0.0007321077497322,0.0006594282091518,0.0006040811817713,
        0.0005639060613766
    ]
    
    BANDPASS_2 = [
        -0.0001726904172201,-0.0002933469155436,-0.0004358440110315,-0.0006082237934274,
        -0.0008190323010985, -0.00107686946266,-0.001389893132383,-0.001765295505541,
        -0.002208772105075,-0.002724004734854,-0.003312180233975,-0.003971566504304,
        -0.004697166111213,-0.005480465796034,-0.006309297537642,-0.007167823437112,
        -0.00803665277632,-0.008893095243509,-0.009711549669248, -0.01046402283137,
        -0.01112076813181, -0.01165102938871, -0.01202387078728, -0.01220907034693,
        -0.01217805122959, -0.01190482295499, -0.01136690319752, -0.01054619038445,
        -0.009429757832601,-0.008010541654124,-0.006287897103564,-0.004268001365066,
        -0.001964084899278, 0.000603521737421, 0.003407533367614, 0.006414050043576,
         0.00958308748798,  0.01286928847399,  0.01622279982314,  0.01959029440752,
         0.02291611280585,  0.02614349523918,  0.02921587123963,  0.03207817229378,
         0.03467813153268,  0.03696753445893,  0.03890338571907,   0.0404489590241,
         0.04157470043161,  0.04225895923832,  0.04248852556909,  0.04225895923832,
         0.04157470043161,   0.0404489590241,  0.03890338571907,  0.03696753445893,
         0.03467813153268,  0.03207817229378,  0.02921587123963,  0.02614349523918,
         0.02291611280585,  0.01959029440752,  0.01622279982314,  0.01286928847399,
         0.00958308748798, 0.006414050043576, 0.003407533367614, 0.000603521737421,
        -0.001964084899278,-0.004268001365066,-0.006287897103564,-0.008010541654124,
        -0.009429757832601, -0.01054619038445, -0.01136690319752, -0.01190482295499,
        -0.01217805122959, -0.01220907034693, -0.01202387078728, -0.01165102938871,
        -0.01112076813181, -0.01046402283137,-0.009711549669248,-0.008893095243509,
        -0.00803665277632,-0.007167823437112,-0.006309297537642,-0.005480465796034,
        -0.004697166111213,-0.003971566504304,-0.003312180233975,-0.002724004734854,
        -0.002208772105075,-0.001765295505541,-0.001389893132383, -0.00107686946266,
        -0.0008190323010985,-0.0006082237934274,-0.0004358440110315,-0.0002933469155436,
        -0.0001726904172201
    ]
    
    BANDPASS_3 = [
        -0.0004039583508639,-0.000181438338525,5.729460785044e-05,0.0003091973125062,
        0.0005673312378581,0.0008192196224903, 0.001046531709455, 0.001226481834851,
        0.001335016266699, 0.001351493523904, 0.001264204495226, 0.001075790681893,
        0.0008074597219516,0.0005009086772282,0.0002170655669723, 3.11383883322e-05,
        2.397958211603e-05,0.0002703684279051,0.0008254021458566, 0.001710679231681,
        0.00290227158251, 0.004322548797283, 0.005837700777718, 0.007262301815823,
        0.008371508568819, 0.008920560909718, 0.008670263905455, 0.007416194661858,
        0.005018626222963, 0.001429705614411,-0.003285650981351, -0.00893833332382,
        -0.01521550391163, -0.02169425518757, -0.02786838408336, -0.03318673512915,
        -0.03710015051052, -0.03911288467732,  -0.0388335435622, -0.03602030818625,
        -0.03061546095864,  -0.0227650498107, -0.01282083546544,-0.001323346441913,
        0.01103325606399,  0.02345192466998,  0.03509483441337,  0.04515132749014,
        0.05290543338925,  0.05779660187447,  0.05946783979604,  0.05779660187447,
        0.05290543338925,  0.04515132749014,  0.03509483441337,  0.02345192466998,
        0.01103325606399,-0.001323346441913, -0.01282083546544,  -0.0227650498107,
        -0.03061546095864, -0.03602030818625,  -0.0388335435622, -0.03911288467732,
        -0.03710015051052, -0.03318673512915, -0.02786838408336, -0.02169425518757,
        -0.01521550391163, -0.00893833332382,-0.003285650981351, 0.001429705614411,
        0.005018626222963, 0.007416194661858, 0.008670263905455, 0.008920560909718,
        0.008371508568819, 0.007262301815823, 0.005837700777718, 0.004322548797283,
        0.00290227158251, 0.001710679231681,0.0008254021458566,0.0002703684279051,
        2.397958211603e-05, 3.11383883322e-05,0.0002170655669723,0.0005009086772282,
        0.0008074597219516, 0.001075790681893, 0.001264204495226, 0.001351493523904,
        0.001335016266699, 0.001226481834851, 0.001046531709455,0.0008192196224903,
        0.0005673312378581,0.0003091973125062,5.729460785044e-05,-0.000181438338525,
        -0.0004039583508639
    ]
    
    BANDPASS_4 = [
        0.0003060861469567,0.0004177211592812,0.0003365207076688,8.316327078423e-06,
        -0.0005304642495015,  -0.0011385259016,-0.001593808663034,-0.001665524346198,
        -0.001218907248224,-0.0003086855086205,0.0007957030130298, 0.001691396737518,
        0.002018164383378, 0.001657684859794, 0.000849137079777,0.0001320011363265,
        0.0001020125514679, 0.001069331338602,  0.00278647598232, 0.004416682342253,
        0.004821912831776, 0.003093601167083,-0.0008996579131276,-0.006232399325386,
        -0.01111501321445, -0.01355895833732, -0.01227062339752,-0.007366888338088,
        -0.0005220445008256, 0.005625351889915, 0.008633432179062, 0.007498565018756,
        0.003367166319015,-0.0007318342655544,-0.001173958813551, 0.004410001397736,
        0.01552884579835,  0.02830207288532,  0.03646794198106,  0.03374753934436,
        0.01673149098861, -0.01290989371817, -0.04797117995742, -0.07747887486447,
        -0.09026476465375, -0.07912762083705, -0.04399660504667, 0.007235211301633,
        0.06072173110775,   0.1009572803221,   0.1158815103081,   0.1009572803221,
        0.06072173110775, 0.007235211301633, -0.04399660504667, -0.07912762083705,
        -0.09026476465375, -0.07747887486447, -0.04797117995742, -0.01290989371817,
        0.01673149098861,  0.03374753934436,  0.03646794198106,  0.02830207288532,
        0.01552884579835, 0.004410001397736,-0.001173958813551,-0.0007318342655544,
        0.003367166319015, 0.007498565018756, 0.008633432179062, 0.005625351889915,
        -0.0005220445008256,-0.007366888338088, -0.01227062339752, -0.01355895833732,
        -0.01111501321445,-0.006232399325386,-0.0008996579131276, 0.003093601167083,
        0.004821912831776, 0.004416682342253,  0.00278647598232, 0.001069331338602,
        0.0001020125514679,0.0001320011363265, 0.000849137079777, 0.001657684859794,
        0.002018164383378, 0.001691396737518,0.0007957030130298,-0.0003086855086205,
        -0.001218907248224,-0.001665524346198,-0.001593808663034,  -0.0011385259016,
        -0.0005304642495015,8.316327078423e-06,0.0003365207076688,0.0004177211592812,
        0.0003060861469567
    ]
    
    BANDPASS_5 = [
        0.0003288424362641,-0.0003827422716574,-0.001079769913162,-0.0006599317853435,
        0.0005080113186277,0.0009399439532154,0.0003008066366843,1.983338879416e-05,
        0.0007869853904436,0.0008872399503366,-0.001082934385987,-0.003018458623164,
        -0.001804598615934, 0.001410116455254, 0.002334999515798,0.0005282031113904,
        0.0004144244428199, 0.003107589177009, 0.002883739709048,-0.003348726636294,
        -0.008438785412895,-0.004579359426591, 0.003407878071807, 0.004675514093952,
        0.0003892355812154, 0.001947796491711, 0.009395451313453, 0.007529630249497,
        -0.008455990747043, -0.01949211487359,-0.009671495235102, 0.006836340942674,
        0.00725614929092,-0.001228419846613, 0.006511920863426,  0.02500216733709,
        0.01812811341955,   -0.020286721962, -0.04392398843324, -0.02036460718645,
        0.01374444229103, 0.009248781664749,-0.008503747073743,  0.02376131447549,
        0.08386108150186,  0.06110595341206, -0.07731202712478,  -0.1873738322976,
        -0.1064097564821,    0.113372423332,   0.2326364154549,    0.113372423332,
        -0.1064097564821,  -0.1873738322976, -0.07731202712478,  0.06110595341206,
        0.08386108150186,  0.02376131447549,-0.008503747073743, 0.009248781664749,
        0.01374444229103, -0.02036460718645, -0.04392398843324,   -0.020286721962,
        0.01812811341955,  0.02500216733709, 0.006511920863426,-0.001228419846613,
        0.00725614929092, 0.006836340942674,-0.009671495235102, -0.01949211487359,
        -0.008455990747043, 0.007529630249497, 0.009395451313453, 0.001947796491711,
        0.0003892355812154, 0.004675514093952, 0.003407878071807,-0.004579359426591,
        -0.008438785412895,-0.003348726636294, 0.002883739709048, 0.003107589177009,
        0.0004144244428199,0.0005282031113904, 0.002334999515798, 0.001410116455254,
        -0.001804598615934,-0.003018458623164,-0.001082934385987,0.0008872399503366,
        0.0007869853904436,1.983338879416e-05,0.0003008066366843,0.0009399439532154,
        0.0005080113186277,-0.0006599317853435,-0.001079769913162,-0.0003827422716574,
        0.0003288424362641     
    ]
    
    BANDPASS_6 = [
        -0.000509473986852,-7.318465256838e-05,0.0005305501163213,0.0002622168309665,
        -0.0005352568941969,-0.0005047225358005, 0.000488026708817,0.0008103610049497,
        -0.0003355104047203,-0.001160326816433,1.903989270256e-05, 0.001499796633188,
        0.0005079410021795,  -0.0017378434367,-0.001260480995252,  0.00175624565239,
        0.00220453326249,-0.001427062701601,-0.003245074552508,0.0006371821266481,
        0.004223248189631,0.0006834328050767,-0.004924607327811,-0.002534062858363,
        0.005098809597555,  0.00482067373852,   -0.004489171146,-0.007342467319042,
        0.002868646467459, 0.009790076698568,-7.737969574412e-05, -0.01175561501314,
        -0.003943762109079,  0.01275156646555, 0.009129149672687, -0.01223100188457,
        -0.01527833014315, 0.009594221360316,  0.02206266989136,-0.004151159943228,
        -0.02904914657274,-0.005035111793811,  0.03573926663703,  0.01965377129804,
        -0.04161880493218, -0.04394622927151,  0.04621233138323,  0.09376498788242,
        -0.04913558755933,  -0.3142475623172,   0.5503931109016,  -0.3142475623172,
        -0.04913558755933,  0.09376498788242,  0.04621233138323, -0.04394622927151,
        -0.04161880493218,  0.01965377129804,  0.03573926663703,-0.005035111793811,
        -0.02904914657274,-0.004151159943228,  0.02206266989136, 0.009594221360316,
        -0.01527833014315, -0.01223100188457, 0.009129149672687,  0.01275156646555,
        -0.003943762109079, -0.01175561501314,-7.737969574412e-05, 0.009790076698568,
        0.002868646467459,-0.007342467319042,   -0.004489171146,  0.00482067373852,
        0.005098809597555,-0.002534062858363,-0.004924607327811,0.0006834328050767,
        0.004223248189631,0.0006371821266481,-0.003245074552508,-0.001427062701601,
        0.00220453326249,  0.00175624565239,-0.001260480995252,  -0.0017378434367,
        0.0005079410021795, 0.001499796633188,1.903989270256e-05,-0.001160326816433,
        -0.0003355104047203,0.0008103610049497, 0.000488026708817,-0.0005047225358005,
        -0.0005352568941969,0.0002622168309665,0.0005305501163213,-7.318465256838e-05,
        -0.000509473986852  
    ]
    
settings = Settings()