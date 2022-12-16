import os 
import random
from bs4 import BeautifulSoup
from linebot import LineBotApi, WebhookParser
from linebot.models import MessageEvent, TextMessage, TextSendMessage ,ImageSendMessage

channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)
# coding=utf-8


taichung_names=["1)七面鳥","2)山下公園","3)有囍拉麵","4)創作麵坊・鮭の大助","5)麵屋零",
              "6)MEN monster","7)麵屋六花","8)貍匠拉麵 深夜拉麵","9)麵本初","10)長生塩人台中店"]
taichung_menu=['https://pic.pimg.tw/dream3s/1541153251-1569316239_wn.jpg'
            ,'https://candylife.tw/wp-content/uploads/20200216164706_61.jpg'
            ,'https://live.staticflickr.com/65535/51670566075_603ecd596a_b.jpg'
            ,'https://pic.pimg.tw/lintzuyang79/1611025002-3356502613-g_wn.jpg'
            ,'https://amonblog.com/wp-content/uploads/2017/09/1504266471-3ad04ecac203e13a0efbbc20dd73e808.jpg'
            ,'https://img.blue74.net/uploads/20200707125240_76.jpg'
            ,'https://pic.pimg.tw/etwendy/1645289730-2235485736-g_wn.jpg'
            ,'https://bagaxn.com/wp-content/uploads/034d438fa9f7f103993a684e582283b7.jpg'
            ,'https://safood.tw/wp-content/uploads/20200303213057_44.jpg'
            ,'https://www.tony60533.com/wp-content/uploads/2022/07/5-6.jpg'


]
taichung_address=['台中市西區中美街331巷15號'
                 ,'台中市西區健行路1049號金典綠園道商場三樓'
                 ,'台中市中區中山路82號'
                 ,'台中市西區向上路一段170號'
                 ,'台中市西區向上路一段245巷9號'
                 ,'台中市西屯區慶和街32號'
                 ,'台中市北區學士路236巷2號'
                 ,'台中市南區建成路1053號'
                 ,'台中市北屯區熱河路二段210號'
                 ,'台中市西屯區台灣大道三段486號'

]
taichung_time=['11:30~14:30 17:30~20:30'
                 ,'週一公休 其餘時間11:30~14:00 16:30~20:30'
                 ,'週二公休 其餘時間11:30~14:00 16:30~21:00'
                 ,'11:30~14:30 17:30~20:30'
                 ,'週三公休，其餘時間11:30~14:00 17:30~20:00'
                 ,'週一至週六11:30~14:30 17:00~22:00 週日公休'
                 ,'11:30~20:30'
                 ,'17:00~01:00'
                 ,'週一至週五11:30~14:30  17:30~21:00 週六至週日11:30~21:00'
                 ,'17:00~01:00'

]
taichung_comment=["star: 5\n這碗極濃雞白湯讓我對於濃湯認知更加深厚，比起沾麵的湯更加厚實的口感，用雞泥來描述或許更加貼切，選擇太麵搭配上紮實的湯料較不適合胃口小的客人，但是湯頭厚重卻不會感到油膩，叉燒雞肉清淡但咀嚼得出肉樸實的鮮甜，帶有油脂的鴨肉調味後腥味較少也相當美味，乾炸的蔬菜沾裹著湯吃起來非常契合，湯匙立於湯中是難得品嚐的體驗"
                 ,"star: 5\n開放式的廚房，旁邊是吧檯的座位，平日下午五點就開始有人在排隊。點餐的方式是用機器點餐結帳，我選鹽味雞豚清湯（台灣口味）+一份煎餃。拉麵的頭湯是很香的雞湯味，上面有叉燒+雞肉，吃完服務員還會詢問要不要加麵或飯食量大的人也可以吃很滿足。煎餃是海鮮口味，個人感覺上面的醬跟海鮮口味搭配不太適合。"
                 ,"star: 5\n服務人員態度非常親切拉麵的部分只能說不枉費排一小時，日本鹹度的湯頭很濃郁，吃起來也不會膩，雞湯味非常足，湯裡配料有杏鮑菇也是第一次吃到，搭配起來意外的好吃。麵條為粗麵，硬度非常足，個人平常吃拉麵都是以硬麵為主都覺得很硬，但吃到後來麵還是吸了湯汁變軟一點，建議可以點普通硬度即可。叉燒肉非常的香且入味可說是非常的完美。"
                 ,"star: 4\n那天11:19分拿號碼牌，前面已經有14個人拿走號碼牌，很幸運的一個阿姨把10號的號碼牌放回去我才能第一批進去用餐11:30開門，但爬文看有些人還沒11:00就去拿號碼牌，可以拿完號碼牌，11點再過等叫號進去店員會跟你說你做哪號桌，點餐的時候先按自己的桌號再點餐，只收現金，沒有發票我11:43分才使用到點餐機，12:04拉麵才上桌，12:16我就吃完離開了鮭魚是生魚片炙燒，口感非常的好也非常的鮮，鮭魚卵真的是波ㄗ波ㄗ，旁邊還有腰內肉跟雞胸肉，幾顆蛤蜊這樣看網路上說可以免費要白飯，所應該不是店家主動提供，我麵沒吃完所以也沒有跟店家要白飯，那天旁邊用餐的小哥點了兩碗白飯，可見湯頭有多讚！很少吃到海鮮風味的拉麵，真的有驚艷到，湯頭濃郁但不過鹹，唯一的小缺點就是開水的部分是飲水機，冰水不夠冰，少了拉麵店對我而言最重要的冰水小細節，食物部分給予滿分，好吃無可挑剔"
                 ,"star: 3\n在巷弄裡的小店，蠻有個性的風格。拉麵來說，算是台中裡難得的好味道！過去兩星期，都有光顧。第一次光顧時，叉燒有點冷。第二次光顧時，就一切正常了。炸雞有點乾，仍然是合格以上。食物來說，是優良以上。在店外等候時，廚房跟外邊間隔的玻璃，看到有點髒。建議店家多做一點清潔，讓在門外等候入坐的客人不會被嚇到。入坐後，旁邊的客人用餐完畢離開，服務員也沒有用酒精噴灑桌面清潔。我們也立即拿起酒精自行擦一下自己的桌面好了。不知為甚麼，兩次到訪，在整個用餐過程，總是有一種不受歡迎的感覺。這種感覺得沉重，重得在店裡也不能放鬆用餐，只求盡快用餐完畢離開。"
                 ,"star: 4\n11:30開店，11:15就有人在排隊了，早點到開始排才不用等～泰式香料濃醬拌麵首先必須說醬料是非常香且具有濃郁複雜的味道，配上麵條還蠻不錯（稍微有一點硬，我更喜歡軟一點的），我更喜歡的是配上白飯。兩次免費添飯/麵就怕你們吃不飽！叉燒的部分配上醬汁也是好吃，不過記憶點稍少一點反而是加點的狂獸拉麵（額外肉）之中的雞腿叉燒非常讓我驚艷！煙燻配上鹹香的雞腿，軟嫩不乾柴玉米筍用醬料刷過，再炙燒也非常好吃 印度叉燒香料拌飯也還不錯吃，不過有一點太辣對我而言叉燒配上印度醬汁有咖哩的感覺 還蠻不錯的最後記得要一人一張單子喔！"
                 ,"star: 4\n隱藏在小巷子的店，內用位子不多，人多時可能要在外面等一下~本次點了蒜味豚骨＄220+糖心蛋＄30湯頭的部分蒜味很香，味道濃郁。拉麵的部分為細麵，軟硬度適中，不過較為可惜的是缺乏嚼勁，但可以“不限”次數加麵，這點很有誠意，不過不能加湯。叉燒的部分有點柴不過味道算香。至於糖心蛋的味道則是非常平淡，煮得微微過熟，吃起來有點像是泡過白開水一樣，沒什麼味道，這點是最可惜的部分……整體而言可能有機會會再回訪，但是意願沒有特別高，主要是因為糖心蛋的部分，不過這間不失為是一家水準之上的拉麵店"
                 ,"star: 4\n台中人氣拉麵屋～最近好喜歡吃拉麵，上次吃完旗下吞山郎拉麵後，決定今天要來嚐嚐品牌源頭 - 狸匠拉麵，品牌旗下有各種不同特色的拉麵屋，每個都附有他獨特之處。店內座位區不多，採登記劃位後由店員依序叫號帶入用餐，點餐是以操作點餐機的方式點餐，再將明細交給店員由內場師傅來製作餐點，口味方面，今日點了一份激辛豚骨以及一份豚大盛+90元肉盛，麵條屬於偏硬口感，豚骨的膠質成功融入了湯中，湯頭濃郁口味較重的會很喜歡，叉燒肉、雞叉燒以及牛叉燒經過炙燒後香氣十足，叉燒肥牛肉有嚼勁一肥一瘦讓整碗麵多了點層次，再加上雞叉燒的肉香使其又多了一番風味，但唯一美中不足的是今日的湯有點偏溫，有影響到今日的期待值，還是推"
                 ,"star: 4\n湯頭不算非常濃厚，但香氣很足，鮭白湯的清甜加上松露非常濃厚的香味，形成了強烈的對比，享用的過程可以依照個人喜好慢慢的將松露拌入湯內叉燒我覺得沒有缺點，但也沒有特別突出麵條算有嚼勁的類型，蠻Q的，但不是我喜歡的類型就是了白蘭地溏心蛋在牛庵吃過了，但還是再一次的被驚艷，入口時濃厚的酒香味真的是通體舒暢⋯叉燒飯香氣滿足的，胡麻醬料和炙燒過的豬肉油脂融合在一起包裹著每一粒米飯，讓人意猶未盡關於店內帶位和用餐的機制，我覺得有待加強，不知道是因為店裡的每個人都很忙還是怎樣的，我入店後沒有人理我也沒有跟我說應該怎麼排隊（我前方有兩位小姐也站在店內）後來我想說跟牛庵同體系的話，應該是一樣的點餐方法吧？點餐完後還是沒有人理我，我跟朋友站在原地不知所措，前往詢問以後才知道原來可以直接入座，於此我認為用餐觀感不太好就是了，但也有可能是期望值太高了吧，所以導致我有點失望"
                 ,"star: 2\n排隊的規定很奇怪 :人到齊才能開始排  ??? 到現在還是一頭霧水，先到的人不能先排。建議改成說 : 如果人還沒到齊，就先換下一組入座。建議員工製作餐點的時候戴一下手套或是用夾子 用手直接把肉放在湯裡面 感覺上不是很好。我們是星期四晚上10:00去用餐的，本來還有加點炒泡麵，但賣完了，又想說要再加點翡翠也沒了(?)，蘿蔔也沒了，…，排了1個多小時，結果什麼東西都沒了，真的是會很生氣欸，但還好店員的態度都很好，雖然他們只有兩個服務人員，而且客人又這麼多。辣味肉醬的口味算重，麵體偏硬，旁邊的配料蠻少的，湯是偏鹹的，如果吃比較清淡的朋友，可自行到飲水機加開水-鹽味拉麵還可以，旁邊有放生洋蔥，配料也是少。泡菜沒什麼特別的。這應該不是糖心蛋了吧，應該是水煮蛋了，蛋黃都熟了…，一份要價$30個人是不會再回訪。"
]



tainan_names=["1)八峰亭日式拉麵","2)白露拉麵 bailu ramen","3)一拉麵","4)覺丸拉麵","5)淳鳩一夫拉麵",
              "6)漣戶拉麵","7)麵屋青鳥","8)五黑家日式拉麵","9)寶來軒","10)菜良日式拉麵"]
tainan_menu=['https://2.bp.blogspot.com/-h4TVBPsLfrk/WC9DGuw8x0I/AAAAAAAAUvI/rJqvW9buehg5XUbuCSWOwf45CsS9bKbpwCEw/s1600/IMG_6455.JPG'
            ,'https://pic.pimg.tw/yangyu8100/1592154667-2021133872_wn.jpg'
            ,'https://static.wixstatic.com/media/87b41c_7c056e1a10704559a20922cc9854da3a~mv2.jpg/v1/crop/x_30,y_304,w_1226,h_1354/fill/w_1146,h_1266,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/%E4%B8%80%E6%8B%89%E9%BA%B5_MENU.jpg'
            ,'https://dingeat.com/wp-content/uploads/20211103154409_8.png'
            ,'https://host.easylife.tw/pics/201505/0507/09_0I3A9456.jpg'
            ,'https://pic.pimg.tw/lintzuyang79/1629704392-714999418-g_wn.jpg'
            ,'https://decing.tw/wp-content/uploads/20220911214608_96.jpg'
            ,'https://etaiwan.blog/wp-content/uploads/20180630160922_66.jpg'
            ,'https://img.boylondon.tw/20210211124232_34-scaled.jpg'
            ,'https://pic.pimg.tw/imsean/1509798760-56453110.jpg'


]
tainan_address=['台南市中西區萬昌街15號'
                 ,'台南市中西區城隍街50號'
                 ,'台南市北區長榮路五段35號'
                 ,'台南市東區東興路275號'
                 ,'台南市中西區民權路二段218號'
                 ,'台南市東區莊敬里莊敬路161號'
                 ,'台南市東區崇德路671號'
                 ,'台南市北區公園北路104號'
                 ,'台南市北區公園南路206號'
                 ,'台南市東區崇明路42號'

]
tainan_time=['週四公休 其餘時間10:30~13:30 17:00~20:00'
                 ,'週五17:30~20:00 週六週日11:00~13:30 17:30~20:00 其餘時間公休'
                 ,'週三公休 其餘時間11:30~14:00 17:30~20:15'
                 ,'週二公休 其餘時間11:00~14:00 17:00~20:00'
                 ,'週日週一公休，其餘時間11:30~13:30 17:30~19:30'
                 ,'週三週四公休，其餘時間11:30~13:30 17:30~22:30'
                 ,'週四公休，其餘時間11:30~13:30 17:00~20:00'
                 ,'週一週二公休，週六週日11:00~15:00 17:00~22:00 其餘時間17:00~22:00'
                 ,'11:30~14:00 17:30~20:00'
                 ,'週一公休 其餘時間11:30~14:00 17:30~20:30'

]
tainan_comment=["star: 5\n點了豚骨海苔拉麵（湯頭選正常、背脂選增量），湯頭的部分濃厚同時也順口，熱熱的喝真的好喝好喜歡～麵體選正常不過我個人吃起來覺得偏硬一點點；叉燒的部分是兩塊，不會有太多肥肉的部份而且很軟嫩！整體而言不會特別驚艷但很和諧，不過可能是因為點了背脂增量加上後來湯頭有點冷掉了，吃完時會有點膩（不過喝店裡附贈的冰水就沒事了）叉燒飯只有五六日有賣，可惜沒吃到，下次吃完再來評論！"
               ,"star: 5\n西式的裝潢，賣的是日式的拉麵，台南拉麵名店之一.主打來自法國紅標土雞熬煮而成的湯頭.店面整體看起來很乾淨，採光充足！開放式的廚房，但用餐時卻沒什麼油煙.這次點的是薩索雞白湯拉麵，加點蟹肉棒跟炙燒干貝.湯上浮著一層厚厚的雞油，散發濃濃的脂肪香味，同時也把雞白湯的熱度鎖在裡面，喝了一口湯才發現，湯頭的溫度很夠雖然感覺很濃稠，但是卻不會太油膩不好入口！可以說是濃纖合度，配菜有玉米筍、紫洋蔥碎、水蓮跟白蘿蔔絲，水蓮跟白蘿蔔絲，算是比較少見的組合，水蓮的清脆、白蘿蔔絲的鮮甜在再加上萊姆皮，不斷的刺激味蕾，湯頭算是非常有特色！店員也會貼心提醒，檸檬片不要放在湯裡太久，避免影響整體的風味.麵體則是稍偏軟，溏心蛋入味但是蛋黃偏硬！雞肉的處理很不錯，軟嫩且沒有多餘的調味，肉吸飽了高湯，入口即化多汁又豐含著香氣！蟹肉棒可遇而不可求，肉質新鮮美味又紮實，炙燒干貝則是選用北海道3S生食等級，稍加炙燒之後提供給客人.整碗拉麵可以吃出店主人的用心跟追求完美的態度！離開的時候，也會熱情的客人打招呼，是值得再訪的一間店！"
               ,"star: 5\n店面不大 建議可以先預約 或是提前排隊 但“人數要到齊”才能進去用餐我點的是 柚子鹽雞白湯拉麵湯頭十分濃郁 可以調整鹹度 很讚麵我選硬的 超好吃 硬的超剛好！湯頭雖濃郁 但 柚子的味道淡淡地清香木耳超脆 即使泡在湯裡 吃到最後還是一樣脆小小的缺點是 玉米筍上面有淋 類似醬油膏的東西 稍微過鹹了一點 感覺搭湯會剛好 應該不用另外淋醬 另外有加半球麵 目測大概比原本碗裡多一點點 建議吃不完的 可以先加半球就好  加麵還能調整軟硬度 真的佛心"
               ,"star: 4\n鮮貝豚骨拉麵230 客製化如下： 鹹度：重口味(非重鹹患者慎選)豬背脂：多麵硬度：硬叉燒肉方面，肉屬於瘦肉，不肥嫩，點重口味的，希望你第一口要先吃叉燒肉，避免湯汁搶過叉燒的風采，入口咀嚼，肉不乾不柴，咬起也不爛嫩，個人感覺恰到好處，而且滋味十足，味道穿透整個肉片，再加上用量十足，很對得起加點的30塊錢，我甚至想再加點兩份叉燒，搞成叉燒蓋麵，很少吃到非肥嫩型的叉燒，既不像火腿般千篇一律的口感，也沒有那制式火腿般的肉味，讓我如此滿意。溏心蛋方面，稍感平淡，可能是我有嘗了幾口湯汁，蓋過溏心蛋原味，這真的有點殘念，所以碗裡的配菜食用順序要注意一下，就色感方面我覺得看似可口，我沒有嘗到甜味或是鹹味，口感稍屬一般。湯汁方面，很濃郁，豚骨拉麵的味道就是濃純香，還會黏，入口吞下，還有一股的貝味～沒錯是貝味，這味道沒被豚骨蓋過，反而有被提出來的感覺，尤其是吃完剩下湯汁時，最後的一堆謎樣渣渣，夾入口內！是干貝絲～很棒。但是他的鹹度是會累積的，沒吃重鹹的人真要考慮一下，我中途也是配了好幾杯冰水，要打安全牌的建議就點清淡的。麵條方面，使用細拉麵，我個人喜好偏硬的，整個口感不錯，在齒間咬斷的感覺很棒，但是一樣，他的麵條是單獨煮的，建議麵條要仔細拌開與湯汁混合，不拌開直接入口，一樣會有麵條的味道出現，而且真的很燙嘴。"
               ,"star: 5\n日式濃熟雞白湯$220 雞白湯很鮮甜，清淡口味，油脂部分又能緊緊包覆拉麵，風味十足～ 雞叉燒很嫩(來自友人分享)，好吃，但沒什麼特色 豬叉燒滷的超入味(應該是梅花肉)，滷到輕夾就斷，卻不乾柴，恰到好處！ 溏心蛋給一整顆，味道、熟度也很不錯 小卷新鮮(來自友人的當日限定款)，但就是小卷，也沒特色 入味的豬叉燒我很喜歡，湯頭也不錯，吃到後面可以加看看店家桌上附的辣醬，但我更喜歡原始的味道"
               ,"star: 4\n吃拉麵dinner。店面不大，座位約14個，黑色系裝潢帶有種神祕典雅感，17:30開幕，門口有候位單，提早來登記，很快就客滿，背包外套可以掛後方牆上。點了250元激厚鹽味豚骨拉麵、250元濃厚煮干豚骨拉麵、70元沐花燒餃子，細硬麵口感不錯，叉燒有兩塊，一塊油脂豐富，一塊相對較瘦，配料有水蓮、海苔、紫洋蔥末、蔥花、脆筍、黑木耳、溏心蛋一整顆沒剖半，內餡偏液狀；可免費加麵一次，把替玉牌放到檯面上，會詢問正常還是硬的。用餐能近距離看師傅製作拉麵的過程，製作速度還行，只是好奇第一個結帳但是看身邊的7、8個人都拿到麵了，看起來供應麵的順序很隨性。湯頭鹽味豚骨選正常濃度就夠味了，煮干口味有小魚乾的味道，比較沒那麼耐喝。餃子表現尚可，視覺吸引人，份量只有6顆，已經有淋上調味醬，上方再灑上青蔥。背景配樂是日文歌曲。"
               ,"star: 5\n很容易走過頭沒看見的店外觀入門走到底點餐，取單畫喜歡選項付款醬油雞白湯-味普通脂淡蔥有麵普通口味偏重，麵體選普通口感偏硬焦蔥雞白湯-味普通脂淡蔥有麵軟湯頭比醬油雞白湯多一股香氣口味上也更濃厚一些，個人當沾麵在吃筍乾跟叉燒好吃，溏心蛋給友人吃了！拉麵裡有舒肥雞肉還是不太習慣"
               ,"star: 4\n因為走錯間而結識的拉麵店，一進門就被人潮給嚇到；原來上次是因為記錯時間又走錯棚所以當時是第一組客人，不知道原來是名店。換了麵體之後口感更柔韌Q順，因為很喜歡上次的湯頭所以依然是點邪道（卵入湯）的湯頭；雞肉叉燒柔嫩不會太鹹太甜，咬下去鹹香肉汁四溢。至於鈉含量這種事情就不要再考慮了…反正台灣很多洗腎中心…對了，我必須要講…他們家的桌子拍照實在是太難拍了！黑色花崗岩怎麼拍都不好看！"
               ,"star: 4\n禮拜天晚上大概1750-1800間抵達，現場已經快10個人在排隊。店家很貼心的在外面放置傘架、吊雨衣的衣架以及可以放安全帽的地方。翻桌率其實算快，大概排了20幾分鐘就換我們了。服務人員很親切的招呼及說明餐點。今天點了德島拉麵跟沾麵，通常沾麵都是放兩球麵，女生要吃的話人員會先告知可以先放一球，吃完不夠再加第二球。平均單價200多，但份量超級足夠。湯頭部分是濃郁的，吃到後來會有點膩，但現場有辣椒醬及蒜泥，可以適當加入一些改變一下口味（個人口感較主觀，不見得大家都這麼覺得）。麵條偏粗，但口感非常的Q彈，但不會到硬。叉燒給兩片，肉體很大也很厚，口感不柴很嫩。人員在清理桌子非常的仔細認真，衛生紙也會把邊角拉正，把衛生紙放在桌邊的中間位置，顧客進場跟離開，每個員工都會招呼"
               ,"star: 4\n近期二訪台南二郎系拉麵代表：菜良用餐環境：移到隔壁間重新裝潢，空間變寬…增加吧台以外的座位(位子共25個左右，先給推！)，舒適感提升！服務：店員增加了…服務也較先前到位。餐點：點了烏帽子拉麵(菜多加蒜背脂少醬料少)210元及叉燒飯70元，相較於初訪的不適應(口味未調整所以自己覺得過鹹)，本次體驗變好，豆芽菜脆口解膩，蒜丁提味，叉燒基本是兩片…稍薄，不過肥瘦大概各半，是好吃的！(不過只有兩片…不是很過癮，嗜肉者可能需要加購)。因背脂少醬料少所以醬油湯底顯得清爽不膩口，這樣的口感可能較合我胃口(笑)。不過還是不愛粗麵…且份量算多…吃完很飽。(不知有無麵少的選項XD)另推叉燒飯…與友人共食一碗…叉燒肥瘦比適中，米飯油醬香味十足(八峰亭的份量較多，不過瘦肉居多，應該是有加了鹽巴…所以吃得到鹽粒…較鹹)本次整體感受佳！吃膩了豚骨湯底的八峰亭寶來軒覺丸的…可嘗試醬油底的菜良看看！"
]

taipei_names=['1)鷹流東京豚骨拉麵-極匠','2)隱家拉麵 赤峰店','3)鳥人拉麵-台灣總店TOTTO Ramen','4)五之神製作所','5)柑橘Shinn - Soba','6)豚人拉麵','7)墨洋拉麵','8)豚骨拉麵 Nagi 凪 西門店','9)壹之穴沾麵專門店','10)大和家'
            

]
taipei_menu=["https://cvcc.tw/wp-content/uploads/20200302212254_55.jpg"
            ,"https://pic.pimg.tw/borntoshop/1648556907-1751726733-g_l.jpg"
            ,"https://img.foodieteller.com/20191026161622_32.jpg"
            ,"https://maruko.tw/wp-content/uploads/2018/06/%E4%BA%94%E4%B9%8B%E7%A5%9E%E8%A3%BD%E9%BA%B5%E6%89%80_16.jpg"
            ,"https://n-square0314.com/wp-content/uploads/2021/03/%E6%9F%91%E6%A9%98Shinn-soba%E4%B8%80%E5%BA%97%E8%8F%9C%E5%96%AE.jpg"
            ,"https://img.anikolife.com/uploads/20211109125847_38.jpg"
            ,"https://tenjo.tw/wp-content/uploads/20200811205718_6.jpg"
            ,"https://char.tw/wp-content/uploads/20190111035134_55.jpg"
            ,"https://live.staticflickr.com/65535/50320263052_ec50a9f13d_h.jpg"
            ,"https://pic.pimg.tw/lintzuyang79/1567342358-3709332537_wn.jpg"
]
taipei_address=["台北市中正區汀州路三段104巷4號"
               ,"台北市大同區南京西路25巷28號"
               ,"台北市大安區復興南路一段107巷5弄9號"
               ,"台北市信義區忠孝東路四段553巷6弄6號"
               ,"台北市大安區仁愛路四段228-6號"
               ,"台北市大安區大安路一段16巷6號"
               ,"台北市中正區羅斯福路四段136巷10號"
               ,"台北市萬華區漢中街52號6樓"
               ,"台北市大安區復興南路二段350號"
               ,"台北市大安區市民大道四段12號"

]
taipei_time=["11:30~14:30 17:00~21:00"
            ,"11:30~14:00 16:30~22:00"
            ,"11:30~00:00"
            ,"週六週日11:30~21:00 其餘時間11:30~15:00 17:00~21:00"
            ,"11:30~14:00 17:00~20:30"
            ,"週二公休 其餘時間12:00~15:00 17:00~22:00"
            ,"11:30~14:00 17:00 ~21:00"
            ,"11:30~20:30"
            ,"週日週一公休 其餘時間12:00~14:00 17:00~20:00"
            ,"11:30~22:30"

]
taipei_comment=["star: 3\n鷹流東京豚骨拉麵是一間知名的拉麵店，在台北市擁有好幾間分店。之前去過延吉街的分店，過年時經過公館，看到居然在公館也開分店了，所以進來回味一下。即便在年假期間，外面還是有排隊人潮。按照順序，量體溫、操作自動賣票機買票後，就排隊依序進去。就像日本的店一樣，裡面空間小小的，由於疫情關係，每個位置間都有隔板。跟多年前記憶中延吉店不同的地方，就是以前延吉店可以無限的加麵，現在一人限定最多兩球。由於我的偏好是正港台灣人口味，日本傳統拉麵中的鹹味與豚骨的濃厚油味對我來說是太過的，所以稍微稀釋一下。我點了青蔥口味的拉麵，上面擺著一坨蒜球。有嚼勁麵體是這碗麵另一個亮點，大量的蔥與大蒜的辛辣感會隨著吸附在麵條的湯汁湧入嘴裡。伴隨著大量豆芽菜的清脆口感，把濃厚的湯汁提升到另一個境界。吃完後的心得就是:偶而來吃一下還不錯，但這味道對我來說太重了，無法常吃。"
               ,"star: 5\n麵條十分彈牙好吃 湯頭煮的香甜濃郁 豬肉雞肉堪稱極品 服務態度佳 極度照顧客人"
               ,"star: 5\n紐約來的拉麵，首推雞白湯，湯裡面的洋蔥讓湯頭變得更甜，淋在飯上也是很棒的吃法"
               ,"star: 5\n五之神製作所來自新宿，在台北的分店開在松山文創園區旁巷內，離捷運市政府站不遠。於平日下午到訪，不用排隊不過店內座位不多，呈現客滿的狀態，店址原為酒吧，五之神接手後仍保留部分元素，所以裝潢上不同於傳統拉麵店，但明亮、環境及廁所乾淨是沒問題的。"
               ,"star: 5\n乾麵跟拉麵都很棒，特愛拉麵，湯頭濃，麵條優，雞豬叉燒處理的很棒."
               ,"star: 5\n新開幕的日本拉麵連鎖，在SOGO後面大安路可不可紅茶隔壁的巷子。菜單就分為濃湯的鹽味豚骨和醬油豚骨，以及清爽的鹽味豚骨及醬油豚骨，麵條分成1.中捲麵 （較Q）2.細麵 （較軟）3.天龍麵（較硬、粗）三種，基本上麵條軟硬度、湯的各種口味都能做調整。今天點了徹濃鹽味豚骨配中捲麵，麵很Q，湯蠻厚重的很有豚骨味，但不會濃到像醬，麵條吸附湯汁後的味道很棒。可免費加麵一次，還可選不同的麵種，加麵我選了天龍麵嚐鮮，吃起來像是微寬偏硬的麵，也有淡淡麵香，非常好吃。環境乾淨，小菜有豆芽及雪菜任你夾，店長是位年輕日本女生，非常有元氣的熱情招呼，不收服務費，非常推薦前往嘗試。"
               ,"star: 5\n本次消費：580元，無服務費。極上貝貝拉麵280元+泡系香檸雞豚拉麵250元+單點生食級干貝50元/顆本次體驗：1.今日風雨極強、人潮稍減，下午五點抽號碼牌已排二十幾號，位置不多、翻桌速度還算快。2.貝系海洋風味湯頭十分甘美，干貝炙燒熟度和糖心蛋也控制的很好。3.泡系湯頭頗爲驚人，拌開後儼然就是碗沾麵，口感濃郁擠上新鮮檸檬風味更提升，叉燒很嫩、雞肉飄著微微碳烤香，湯麵和雞軟骨一併咀嚼，口感很有層次，缺點就是肉片太薄、干貝縮水了，價格也漲了ㄧ點，希望店家能在疫情過後長久經營下去，推推～"
               ,"star: 4\n赤王好吃，服務人員親切細心，上麵速度快，桌上配料的雪菜與豆芽品質風味也挺棒的"
               ,"star: 5\n這次點了280$的豚雞沾麵（肉盛）肉給的很多！有附溏心蛋，配料以同價位拉麵來說給的很多，整碗麵吃下來口味豐富不會吃到膩。粗麵是微冷的，口感很好，吃完很後悔沒點大份的（但可能會超飽）吃完真的很飽，沾醬味道也很符我胃口總之蠻推薦的，肉盛的餐點我覺得比一般肉量的更值得點！"
               ,"star: 5\n本次餐點內容：631醬油拉麵(290)、豆芽高麗菜(60)、白飯小碗(10)平日晚間用餐，大約排隊等待15分鐘即可入座，這間店營業時間非常長，彈性非常棒!!店內座位也蠻多的，看起來二樓還有座位，本次用餐尚無開放，拉麵選項不多，不會有選擇障礙!!由於選擇門口四人座位，位於冷氣口正下方，餐點一下就涼掉，尤其加點白飯，上了不到5分鐘口感就變硬，非常影響用餐體驗，建議改善!!!631醬油拉麵：配置海苔六片、豬叉燒三片、溏心蛋乙顆、鵪鶉蛋乙顆、菠菜些許，麵硬、湯頭鹹度普通、湯頭油脂普通，首先湯頭濃郁不死鹹，麵體易吸附湯頭加分，其餘配菜普普!"
               ]

kaoshung_names=["1)麵屋武藏 武骨","2)木易拉麵","3)一本拉麵. 梟","4)沐瀧家拉麵屋","5)瀧澤軒食堂","6)Ramen 初ui拉麵","7)獺鯌拉麵-Takau","8)麵屋祥","9)一支碳拉麵屋","10)品麵屋ラーメン雞白湯專賣"

]
kaoshung_menu=["https://benlife.tw/wp-content/uploads/2022/01/172601493_1717776858423663_6101424824376476927_n-532x1024.jpg"
              ,"https://img.rabbitfunaround.com/2022/02/1644474024-dca8420d173f575e797864f3745716e2.jpg"
              ,"https://pic.pimg.tw/ku5553221/1599984477-2216500373-g_l.jpg"
              ,"https://pic.pimg.tw/lintzuyang79/1589217348-4218325452_wn.jpg"
              ,"https://pic.pimg.tw/lealea0614/1554045231-391196498_wn.jpg"
              ,"https://pic.pimg.tw/lintzuyang79/1548347600-2835361871_n.jpg"
              ,"https://pic.pimg.tw/sunyat/1549467977-2839412621_wn.jpg"
              ,"https://pic.pimg.tw/oxoxooxoxo/1586624705-1092596499_n.jpg"
              ,"https://live.staticflickr.com/65535/50147156597_561e5d907f_c.jpg"
              ,"https://live.staticflickr.com/65535/51737701428_3e131f8488_c.jpg"
]
kaoshung_address=["高雄市左營區站前北路1號3樓"
                 ,"高雄市鳳山區文中街262號"
                 ,"高雄市苓雅區廣州一街123-1號"
                 ,"高雄市三民區義華路294號"
                 ,"高雄市苓雅區林泉街44號"
                 ,"高雄市苓雅區廣州一街123-1號"
                 ,"高雄市鹽埕區大仁路164號"
                 ,"高雄市鼓山區大順一路459號"
                 ,"高雄市左營區新庄仔路259號"
                 ,"高雄市新興區玉竹一街17巷2弄1號"                 
]
kaoshung_time=["11:00~20:30"
            ,"週一公休 其餘時間11:30~14:00 17:30~21:00"
            ,"12:00~22:00"
            ,"週一公休 其餘時間11:30~14:30 17:00~19:30"
            ,"週二公休11:30~14:00 17:00~20:00"
            ,"12:00~22:00"
            ,"17:30~23:30"
            ,"17:30~21:30"
            ,"週一週二週三公休 其餘時間 17:00~00:00"
            ,"12:00~21:00"

]
kaoshung_comment=["star: 5\n因為行程很趕開在這麼方便的地方真是太好了服務人員很親切也都有認真消毒座位位子都有隔板而且在位子上點餐就好了呢點了味玉武骨沾麵270(沒有服務費)上菜還蠻快的蛋非常優秀我喜歡粗麵的口感，很Q不過如果有機會再來會請他麵硬覺得預設有些軟沾湯很燙，內有肉角和蔥白搭配起來鹹香好吃愛重口味的人可以點濃厚版叉燒跟筍干對我來說就比較還好吃到一半時東張西望服務人員會主動問要不要加清湯我是想要蒜末來了一大罐冰冰的調味過的蒜末蠻辛辣的，適合吃到後半段時轉個味整體體驗良好搭車前不排隊立刻享用一碗覺得很幸福下次來再嘗試其他口味"
                 ,"star: 4\n2022/4/29初訪點了醬油特盛(日本鹹、麵硬)、辛辣味噌特盛(日本鹹、麵硬)、叉燒飯、筍乾、小黃瓜環境相當舒適整潔麵條的口感相當不錯辛味噌的鹹度對我而言有點寡淡頗為可惜但醬油的湯頭就相當不錯比起湯底小菜的整體鹹度較高也許是刻意設計成可搭配小菜食用避免過鹹叉燒飯我們都覺得普普通通鹹度一樣不太夠故略顯肥膩不過米飯本身的口感還是很不錯的"
                 ,"star: 5\n內用有兩人座位或是吧台座位，一進門親切的招待我們坐在最裡面，說冷氣會涼一點，的確用餐的過程中完全不會感受到滿頭大汗。桌上有杯子，架上有開水可以自取，第一次來訪不確定口味如何，先倒水備用以免太鹹可以中和一下。拉麵有圖片可以參考，還有詳細內容描述，不然光看品名還真的有點眼花撩亂。看完後再畫記在桌上的小白單中，並櫃檯點餐結帳。等待時間沒有很久拉麵就陸續上桌了，嚐一口湯，表面湯體沒有太燙，溫溫的，後來吃麵才發覺應該是配料的溫度影響到表面湯體溫度，其實底下的麵條跟湯是熱的。湯頭非常濃郁好喝，不算太鹹，不過當麵與配料用完時，剩下的湯單喝就有點膩了。吃拉麵很怕吃到太軟的麵，這間不會，喜歡這個硬度，麵的咬勁和濃湯在嘴中化開，過癮好吃的感覺叉燒肉是很紮實的，肥瘦個人目測大概3:7，SP叉燒武藏豚骨裡面還有一塊雞胸肉，舒肥雞胸肉十分地軟嫩好吃，搭配蔥花洋蔥碎更有味道。整體來說環境乾淨，服務佳，麵硬湯濃味道佳，下次會想再來嘗試其他口味。"
                 ,"star: 5\n假日晚上獨自用餐，可能運氣還不錯，沒有排隊就入座了，過一陣子店家就公告湯頭賣完了，如果假日用餐建議早點過來以免遇上湯頭賣完的情形。沒有部分日式拉麵店麻煩的刻板印象，過久的排隊、囉嗦的規定，價格實惠，來這裡吃上一碗拉麵，氣氛就是住在附近會時不時來上一碗的簡單美味，而不是過於抬舉的外國料理，味道來說，我覺得贏過很多網路包裝的人氣店家。店家說特濃跟豚骨差在，特濃是全豚骨湯頭，豚骨有加入柴魚清湯稀釋，當天點特濃特盛，吃起來很爽，建議直上特盛，有機會會想把其他口味也嚐過。"
                 ,"star: 5\n蒜香豚骨拉麵(全麥粗麵、麵硬、湯適中、豬背脂)上述框內是我客製話點的內容，湯頭方面，感覺是濃韻順口的，有把蒜整個煮到化開，口味沒有重到齒頰留香的回味感。麵條方面，個人喜歡咬起來稍硬的麵勁，所以個人評價為優的，剛上來有點燙嘴，但挾著湯汁囌嚕下去，爽！叉燒方面，咬下剎那間，不禁令我想到跟叉燒飯用的是同一種叉燒嗎？這口感這厚度，就是我想追求的感覺，不油、不膩、不軟，是嫩！厚度夠，我整個最推的就是叉燒！讚！整體來說，這碗拉麵我覺得特色在於他的湯頭跟叉燒，讓我可以打上五顆星。"
                 ,"star: 4\n已到訪多次，環境氣氛溫馨，湯頭濃郁，麵條香Q有勁，推薦味噌和醬油口味。"
                 ,"star: 3\n台灣風拉麵今天吃醬油跟辣味增，辣味增的味道比較有層次，叉燒烤過香氣足，而且油脂不多，不吃太多油脂的我覺得很棒，麵體硬，醬油湯的味道不夠足，吃到後面感覺有點麵粉湯味，木耳是軟的。門口有機車停車位，店內是否提供洗手間需在確認，自助方式，店員送上餐點，自行回收餐具及碗筷到餐車上，露天開放式廚房，室內用餐提供冷氣。"
                 ,"star: 5\n提早一點吃飯就一下排到了，果然名不虛傳，點日本口味湯頭非常濃郁也偏鹹，可以先嚐嚐濃郁口味再跟店家索要清湯，可以吃到不同種風味，點特製份量蠻足的，吃叉燒吃的很過癮，小可惜叉燒飯吃不下且不能外帶。"
                 ,"star: 5\n我們點了熱門的黃金豚骨、會辣的味噌豚骨和小菜黃金泡菜，鹹度正常，加蔥。黃金豚骨湯頭濃郁，會有雞湯的香氣，膠質明顯，麵還沒吃完，就覺得不小心沾到湯的手和筷子黏黏的，我覺得這碗湯都應該喝乾乾淨淨的。到今天我都感覺那碗的雞湯香圍繞在腦海裡…配菜豐富，有叉燒兩片、雲耳、半顆溏心蛋、筍片、海苔片..店家有提供餐前白開水、調味料、辣椒和蒜汁。生意不錯，在我們之後陸續來了三組客人，老闆用心製作，口味獨特，喜歡拉麵的至少要來用餐一次。"
                 ,"star: 5\n是專賣雞白湯和雞叉燒的拉麵店，真的好吃，拉麵愛好者可以來吃吃看。"
]
shinchu_names=["1)麵屋浩Hiroshi","2)橫濱家系拉麵家ラーメン","3)大角拉麵ダージャオラーメン","4)Hiro's らぁ麵Kitchen","5)寫樂拉麵","6)神虎拉麵","7)嵐沺拉麵","8)麵屋吉光","9)らぁ麵東商店","10)大海拉麵竹北文信店"

]
shinchu_menu=["https://3.bp.blogspot.com/-An7FblM6U0c/WEwZ_xCsGII/AAAAAAAAVbA/jWQwnjgnRvo9PXkFEgkLrSBM7bStcBbOQCEw/s1600/IMG_8078.JPG"
             ,"https://sillybaby.tw/wp-content/uploads/20200308164108_32.jpg"
             ,"https://www.foodytw.com/upload/review/image/2020/11/77979458924a885fbbae44589b66353e.jpg"
             ,"https://sillybaby.tw/wp-content/uploads/20181204215139_22.jpg"
             ,"https://pic.pimg.tw/tanpopokayu/1544521301-3893879263.jpg"
             ,"https://pic.pimg.tw/mystussy/1555685280-2208010290_wn.jpg"
             ,"https://pic.pimg.tw/n16802000/1581669015-2505820810_wn.jpg"
             ,"https://i.imgur.com/bJxQGO4.jpg"
             ,"https://i.imgur.com/h1iZBeD.png"
             ,"https://ikuma.cc/wp-content/uploads/flickr/49542775662_1394f0a257_c.jpg"

]
shinchu_address=["新竹市北區北門街87號"
                ,"新竹市東區民生路119號"
                ,"新竹市東區大同路86號東門市場#1022"
                ,"新竹市北區長安街76號"
                ,"新竹市東區勝利路42號"
                ,"新竹市北區世界街114號"
                ,"新竹市東區南門街77號"
                ,"新竹市東區關新東路138號1樓"
                ,"新竹市東區東門市場1160號"
                ,"新竹縣竹北市文信路263號"

]
shinchu_time=["週六週日週一公休 其餘時間 17:30~21:00"
            ,"週三公休 其餘時間11:00~21:30"
            ,"週一週二公休 其餘時間 11:30~13:30 17:30~20:30"
            ,"週四週日公休 其餘時間17:30~21:30"
            ,"11:00~14:20 17:00~20:30"
            ,"週二週三公休 其餘時間 11:30~14:00 17:00~22:00"
            ,"週一公休 其餘時間 11:30~13:45 17:00~20:30"
            ,"週六公休 其餘時間 17:00~21:00"
            ,"週一週二週三公休 其餘時間 17:00~21:00"
            ,"週三公休 其餘時間 11:00~13:45 17:00~20:45"

]
shinchu_comment=["star: 5\n麵屋浩位於新竹市北區北門街，是一間新竹城隍廟附近的在地知名拉麵店，生意從開店以來一直都很好，在正常用餐時間前往大約都要等候一小時左右。但有別於一般拉麵店都需要在現場排隊，麵屋浩可以登記完之後去別的地方繞繞，等時間到再回到現場等候叫號（每八位大約等半小時）。推薦這裡的濃湯SP拉麵，除了有很多一般的叉燒之外還有一片炙燒的叉燒。炙燒過的叉燒香氣更濃郁，也因為是厚切的所以更有大口吃肉的爽感。麵體Q彈有勁，搭配上濃郁的湯底，每一口都帶來滿滿的豚骨味。老闆也會不時地詢問在座客人是否需要加麵/加清湯/加蒜頭，很用心地希望客人都可以用自己最喜歡的方式享受眼前這一碗拉麵。"
                ,"star: 4\n今天吃的是炙燒叉燒拉麵鹽味、麵硬、湯普通鹹度、湯普通油脂湯頭很濃郁，是喜歡的濃湯湯頭叉燒跟預期的口感不太一樣以為是軟嫩的炙燒，實際上是有嚼勁的麵比一般硬的麵還要再硬一些，有些吃不慣下次可以嘗試普通硬度旁邊的海苔跟菠菜有解膩的效果300元的拉麵是期待有溏心蛋的，可惜沒有茶水區有冰開水跟紙巾調味粉可取用會扣一顆星是洗手間沒有清楚標示到後台找了很久，最後是廚房的人出來問我而且洗手間沒有洗手乳，非常不方便尤其現在還是疫情期間，清潔很重要希望店家能加強這個部分"
                ,"star: 4\n一個正妹高中同學在新竹工作知道我喜歡吃拉麵特別推薦了2家曾經的好同事來新竹參選市議員選前的最後一個週末前來幫忙助選結束想把握機會來搜尋後發現另一家週日晚上休息所以來這間在東門市場裡頭，需要找一下通常只要看到有人排隊 那肯定是拉麵店19:00到 外頭有椅子可以坐前方約有8~10人19:15時輪到我用點餐機點餐，一個人來果然比較快！19:19上餐，筷子跟水要自己旁邊拿我點的是清湯，也只有清湯和醬油兩種選擇麵條細，硬麵還是稍微軟了點對我來說鹹度普通的湯清淡不油不濃肉片的水分多，喜歡這種像是吃生肉軟軟薄薄地感覺蛋要+30，有一股特殊的酒味，跟其他甜甜地蛋不同，非常特別！加麵也是+30，是用碟子裝店員都是可愛親切的女生19:31就吃完走人了讓後面可以更快用餐以一間要300元的拉麵來看是真的有點貴而且是在新竹只能說 新竹的經濟真是好~但由於價格&氣氛的部分所以給4顆"
                ,"star: 4\n叉燒肉給超多，麵條好吃湯頭好喝。座位有點少，不適合好友聚餐聊天"
                ,"star: 4\nKB風叉燒拉麵麵很有彈性，湯也濃郁特別。叉燒肉有夠多，整體非常軟嫩。但是因為肥的部分滿多的，所以最後肉吃到有點膩。平日去可以免費加一次面，蠻划算的～"
                ,"star: 4\n叉燒飯（60）：只是嚐鮮點的，但讓我很失望，整個沒什麼特別，以這質量來說我覺得應該只有1、2顆星，我可能會比較想吃滷肉飯。再訪不會考慮再點這個。濃厚豚骨拉麵（280）：這款拉麵沒有辦法調鹹淡，我覺得很鹹（其他款拉麵可以調鹹度），叉燒是三層肉有三塊，吃起來甜甜的有炙燒味，麵是細麵，口感也不錯，唐心蛋也好吃。會考慮再訪吃拉麵。"
                ,"star: 5\n需要造型蛋可以在點餐時先通知味噌是本店招牌系列🇯🇵搭配卷粗麵所以點了起司味噌、叉燒味噌（即叉燒加倍）基本配料有叉燒、海苔、少許豆芽菜與高麗菜葉湯的部分有因應台灣口味調整，因此較淡（本人習慣點濃）若不喜歡拉麵重口味的人，可以調更"
                ,"star: 4\n事先查了一下說至少要提早半小時來排才不會等太久，結果到的時候前面已經16位，注定要等第二輪了(因為店內只有12個吧檯座)，據當地人的建議，平日提早30分鐘可以在第一輪進去，假日則要提早50分鐘。入內後需自行在機器前點餐，如果你沒有事先想清楚一定會被白眼，幫大家分析一下點餐，可以分為1.湯濃還是稀，2.湯的味道要鹹還是淡，3.麵要粗還細(建議點粗麵，因為加麵只能加細麵)，4.麵是硬還軟，5.肉多還是少，點完入座將小白單給店員，出餐速度很快幾乎沒什麼等待(時間都花在排隊跟點餐......)，肉肉系列的沒有付半熟蛋，需加購一顆$30，豚骨白濃在上桌後會建議盡快吃完避免湯體凝固，如果覺得太鹹都可以舉手跟店員要清湯，但我個人覺得清湯也是有味道的，也就是只有解決太濃稠的問題，味覺依然是算重口味，白湯基本可以說成白醬，連同麵一起吸入很好吃味道很夠，但湯如果不稀釋基本上很難入口。神奇的是即便湯頭很濃味道很重，但麵的麵粉香味還是很鮮明，配菜洋蔥清甜，似乎有泡過冰水，筍乾夠味又清脆，吃完還會問你吃飽沒，很有人情味。總結一下，如果不排隊會再訪，現在人的時間很寶貴，加上店內位子少，12個人頭為一單位，一單位大概30分鐘，很容易推算你要排多久..."
                ,"star: 5\n菜山拉麵中碗220 + 溏心蛋30超級過癮的一碗麵！看起來很浮誇但其實上半部幾乎都是豆芽跟高麗菜。因為我之前沒有吃過二郎系，在吃之前還擔心放這麼多菜會不會讓湯頭也有菜味，但我吃了一口（菜）馬上就被驚艷到了。爽脆的口感配上濃郁的gravy（我不知道要怎麼描述上面很像肉汁的東西，吃起來是濃縮的湯頭風味，如果有專業的知道這叫做什麼再告訴我XD）吃起來非常爽，而且因為湯頭本身蒜是蠻重口味，吃到後段的時候一口麵一口菜吃起來就清爽許多。附著著甘醇的豚骨湯頭和濃郁的蒜香的粗麵條，配上表面入口即化的脂肪一起吸入口中，真的是超爽，喜歡濃郁蒜香的一定要來嘗試看看。另外他的肉是厚的，很有口感的同時又很軟嫩，有大口吃肉的快感。中碗我覺得份量就蠻大的了，差不多是其他拉麵店加麵過後的份量，吃得非常飽。"
                ,"star: 4\n好吃！ 湯頭輕重都可調整，也有加蔥加蒜的服務，麵體也可以選擇硬軟 與在日本吃差不多，但是⋯就是覺得湯不夠燙，也許是因為個人喝很燙，但因為不夠燙 油膩感就會出現 導致有點吃不太下！如果擔心這點 可以點餐時稍微備註一下 目前都是使用手機點餐！"
]
taoyuan_names=["1)豚戈屋台拉麵","2)三冬麵舖","3)松津中華拉麵","4)許諺屋","5)11番町豚骨拉麵","6)小郜家雞白湯拉麵","7)無常拉麵","8)麵屋豚彩拉麵店","9)麵屋。濃","10)麵屋一人"
]
taoyuan_menu=["https://2afoodie.com/wp-content/uploads/134420667_1079081449201230_1575591458090853300_n.jpg"
             ,"https://badboniu.com/wp-content/uploads/2021/10/1634929052-bd83398146ca28a66fed6f58b0cad8e4.jpg"
             ,"https://www.darren0322.com/wp-content/uploads/2017/09/1504616886-005b0e2ad000f9bd61eed70c213e3663.jpg"
             ,"https://1.bp.blogspot.com/-Gmn7-jHMeYA/XZoRiTdEDOI/AAAAAAAALfw/HmRAE5d3cpQBEmLzMV_0X4Uvefg2mflDwCEwYBhgL/s1600/IMAG4860.jpg"
             ,"https://www.alberthsieh.com/wp-content/uploads/46756120_366426297437499_7554609850303381504_n.jpg"
             ,"https://pic.pimg.tw/moonblog0505/1599037831-3579241035-g_wn.jpg"
             ,"https://pic.pimg.tw/jenniferhu1104/1584460930-3550372296_wn.jpg"
             ,"https://pic.pimg.tw/jennylee0712/1505660459-1777752194_wn.jpg"
             ,"https://pic.pimg.tw/mai0104/1536588948-3460692771_wn.jpg"
             ,"https://pic.pimg.tw/zhangandy/1594647936-767984524-g_wn.jpg"

]
taoyuan_address=["桃園市桃園區國際路一段98巷52號"
                ,"桃園市桃園區同德十街17號"
                ,"桃園市桃園區正康三街233號"
                ,"桃園市桃園區樹仁三街23號"
                ,"桃園市龜山區文化三路106-1號"
                ,"桃園市八德區介壽路二段208號"
                ,"桃園市八德區建國路1142號"
                ,"桃園市平鎮區中豐路山頂段186號"
                ,"桃園市龜山區文化一路10巷42弄47號"
                ,"桃園市龍潭區中正路108號"
]
taoyuan_time=["週一週二公休 其餘時間 11:30~14:00 17:30~20:30"
            ,"週日週一週二公休 其餘時間16:50~19:50"
            ,"週一公休 其餘時間 11:00~14:00 17:00~21:00"
            ,"週四週日公休 其餘時間17:30~21:30"
            ,"週二公休 其餘時間 11:30~14:00 17:30~20:00"
            ,"11:00~14:00 17:00~20:30"
            ,"週日週一公休 其餘時間 11:30~13:45 16:30~19:15"
            ,"週日週一公休 其餘時間 11:30~13:00 17:00~20:00"
            ,"11:30~14:00 17:30~21:00"
            ,"週一公休 其餘時間 11:30~14:00 17:30~20:30"


]
taoyuan_comment=["star: 5\n肉肉豚骨拉麵260喜歡肉肉的人點這碗~~老闆超佛心~四片跟手掌一樣大的叉燒肉 讓肉食主義的我每一口都很滿足 麵條是常見的細麵 吸飽滿了湯汁 搭配蔥花、豆芽菜、半顆溏心蛋 又別有一番風味！大家最愛的就是他們家的湯頭 熬煮十二小時以上的 超!級!濃!郁!整碗都是熬煮的食物精華"
                ,"star: 5\n週六午餐的時段11:30就開始營業，特地提早11點前就到，想說早到可以先排隊，沒想到門口的簽到本已經排到20組人了，原來可以在開店前先去簽到，就可以先去其他地方晃晃再回來就好，還好開始營業後，翻桌率還滿快的，12點多就輪到了。今天點的是藤椒雞白湯拉麵、叉燒飯、布丁本來想說藤椒是不是會有點辣的口味，沒想到竟然是花椒的麻，對我來說有點蓋過雞白湯的味道，下次來應該直接點原味的就好，另外麵裡附的叉燒中的舒肥雞真的很嫩，叉燒飯炙燒後焦味吃起來滿香的，其實食量大的男生，除了麵以外，也可以點來吃吃看，或兩個人點來一起分也不錯。最後 的布丁 也是很推，肚子有空間，也可以點來吃吃看喔。"
                ,"star: 5\n有特色的店家，拉麵湯偏少，但其實是剛剛好，麵條稍硬，但可以告知店家煮爛一點，叉燒如果切成薄片會比較適合，口味偏清淡符合個人口味，炸豆腐外酥內嫩，推薦大家。"
                ,"star: 4\n符合個人口味的拉麵店，湯頭也很不錯，起初會擔心太濃稠，嘗試後是可接受的範圍，有機會會想再品嚐其他口味！有聽到現場蠻多顧客選了辣味噌拉麵，但個人不吃辣，想嘗試的朋友可以考慮看看。"
                ,"star: 3\n椅子太硬，坐久不太舒適，吃這種熱的湯麵，冷氣溫度再低一點會更合適。從點完餐到拉麵上桌，等待時間大約五分鐘，而炸雞再晚個三分鐘也送上，算是相當快速。味道方面，湯頭喝起來中規中矩，豚骨系的濃郁味道，再加上蒜頭的香氣，喝起來挺順口的，口味較重的朋友應該可以接受。叉燒、筍乾沒什麼亮點，叉燒沒有焦香，走一個比較軟嫩的路線；麵體偏硬，吃起來QQ硬硬的。除此之外還有放高麗菜，讓人挺意外的，吃起來就是一般的脆加硬口感。總體來說，算是中規中矩的拉麵店，味道挺合我的胃口，份量也很多，想吃拉麵解饞的話，順路可以試試。"
                ,"star: 5\n雞湯真的很濃郁，不是清雞湯那種，適合伴著拉麵一起享用～覺得選擇1/2鹹度很剛好，店家在菜單上也很貼心做了鹹度的選項，海老干貝雞湯麵的蝦子很有份量又鮮甜，鹹味雞白湯拉麵的叉燒也是整整兩大片～女生一碗就很飽！老闆希望顧客吃飽，還可以加麵不加價喔！"
                ,"star: 5\n抵達後需先於候位單上登記並等待帶位，由於我是在剛營業沒多久就到了，所以大概只等了5分鐘就入座了～當天點了鹽味雞白湯拉麵、叉燒飯。叉燒飯需拌勻後享用，我中途還淋入些微拉麵的湯汁也好好吃，必點！拉麵裡加了一片檸檬、一片柳橙，我稍微用湯匙擠壓果肉，讓些許的果汁與湯混合，湯頭馬上又提升到另一個層次了，不過要注意的是水果泡在湯裡太久可能會產生苦味唷～舒肥雞和叉燒表面都有炙燒過，肉入口帶點焦香，真的是絕了！溏心蛋也是不容小覷，吃過很多拉麵的溏心蛋蛋黃都會過熟，但這裡的溏心蛋蛋黃是還可以自由流動的程度也很入味，碗緣還有附柚子胡椒可依個人喜好拌入拉麵，所有的用心和堅持造就了這碗拉麵，讓品嚐到的人感到非常幸福！感恩的心  "
                ,"star: 5\n好吃湯頭濃郁不死鹹，份量足夠，加麵也非常多，男生可以吃得很飽，上餐速度快，店內有附茶水可搭配。"
                ,"star: 3\n意外來到此處，發現了這間拉麵店。非常有特色的一間店，裝潢、擺設、風格都滿滿的日本風格。此次點了三種不同風味的拉麵，麵條本身超Q彈，是我非常喜歡的口感。但湯頭本身就非常的日式口味，比較重鹹了一點，可能也是自己點了醬油湯底的關係。其他二種口味比較適中，附的唐揚雞口味也都不錯。可樂餅評價較兩極，我本身感覺還好，但朋友覺得非常美味，可能差別是喜不喜歡起士吧！喜歡拉麵及嚐鮮的朋友，值得一試喔"
                ,"star: 5\n這次點的兩款，其中「白醬油雞清湯」口味偏淡麗系，白醬油的雞清湯較為細膩，除了雞本身淡淡的清甜還有昆布熬煮出來的鮮味，配菜為筍乾與水蓮，肉配置為雞胸叉燒，吃起來十分清爽沒負擔；而另一碗則是「黃金雞白湯」湯頭明顯濃郁許多，雞熬出來的膠原蛋白讓嘴唇變得有點黏黏的，配置一樣有清脆的水蓮，肉除了三片雞叉燒，還有一塊雞腿叉燒肉，一碗裡有兩種不同的肉咀嚼享受。另外加點的「小雞飯」上面鋪滿了炙燒過的塊狀雞叉燒，肉給的挺大方，不過個人覺得整體瘦肉為主吃到後面咀嚼得頗辛苦的，肥瘦比如果稍微調整這碗口味真的很棒。最後用甜點「含笑扮布丁」收尾真的超級完美，焦糖就像小時候阿嬤手工炒糖會有的那種苦甘苦甘感，真的讚！布丁應該減糖版本，不會太甜，個人很喜歡，一定會為了布丁回訪"
]
all_name=taichung_names+tainan_names+taipei_names+kaoshung_names+taoyuan_names+shinchu_names
all_menu=taichung_menu+tainan_menu+taipei_menu+kaoshung_menu+taoyuan_menu+shinchu_menu
all_address=taichung_address+tainan_address+taipei_address+kaoshung_address+taoyuan_address+shinchu_address
all_time=taichung_time+tainan_time+taipei_time+kaoshung_time+taoyuan_time+shinchu_time
all_comment=taichung_comment+tainan_comment+taipei_comment+kaoshung_comment+taoyuan_comment+shinchu_comment
tmp_menu=list()
tmp_address=list()
tmp_time=list()
tmp_comment=list()
tmp_names=list()
global store_name
store_name=""
def search_name(name,id):
    global tmp_menu
    global tmp_names
    global tmp_address
    global tmp_time
    global tmp_comment
    tmp_comment=all_comment.copy()
    tmp_time=all_time.copy()
    tmp_address=all_address.copy()
    tmp_names=all_name.copy()
    tmp_menu=all_menu.copy()
    for i in  range(len(all_name)):
        if(name in all_name[i]):
            return i+1
    return -1

def rand_store(id):
    r=random.randrange(0,len(all_name))
    global tmp_menu
    global tmp_names
    global tmp_address
    global tmp_time
    global tmp_comment
    tmp_comment=all_comment.copy()
    tmp_time=all_time.copy()
    tmp_address=all_address.copy()
    tmp_names=all_name.copy()
    tmp_menu=all_menu.copy()
    return r
def taoyuan_list(id):
    text=""
    for names in taoyuan_names:
        text+=names + "\n"
    global tmp_menu
    global tmp_names
    global tmp_address
    global tmp_time
    global tmp_comment
    tmp_comment=taoyuan_comment.copy()
    tmp_time=taoyuan_time.copy()
    tmp_address=taoyuan_address.copy()
    tmp_names=taoyuan_names.copy()
    tmp_menu=taoyuan_menu.copy()
    print(len(tmp_menu))
    push_message(id,text)
def shinchu_list(id):
    text=""
    for names in shinchu_names:
        text+=names + "\n"
    global tmp_menu
    global tmp_names
    global tmp_address
    global tmp_time
    global tmp_comment
    tmp_comment=shinchu_comment.copy()
    tmp_time=shinchu_time.copy()
    tmp_address=shinchu_address.copy()
    tmp_names=shinchu_names.copy()
    tmp_menu=shinchu_menu.copy()
    print(len(tmp_menu))
    push_message(id,text)
def kaoshung_list(id):
    text=""
    for names in kaoshung_names:
        text+=names + "\n"
    global tmp_menu
    global tmp_names
    global tmp_address
    global tmp_time
    global tmp_comment
    tmp_comment=kaoshung_comment.copy()
    tmp_time=kaoshung_time.copy()
    tmp_address=kaoshung_address.copy()
    tmp_names=kaoshung_names.copy()
    tmp_menu=kaoshung_menu.copy()
    print(len(tmp_menu))
    push_message(id,text)
def tainan_list(id):
    text=""
    for names in tainan_names:
        text+=names + "\n"
    global tmp_menu
    global tmp_names
    global tmp_address
    global tmp_time
    global tmp_comment
    tmp_comment=tainan_comment.copy()
    tmp_time=tainan_time.copy()
    tmp_address=tainan_address.copy()
    tmp_names=tainan_names.copy()
    tmp_menu=tainan_menu.copy()
    print(len(tmp_menu))
    push_message(id,text)
def taipei_list(id):
    text=""
    for names in taipei_names:
        text+=names + "\n"
    global tmp_menu
    global tmp_names
    global tmp_address
    global tmp_time
    global tmp_comment
    tmp_comment=taipei_comment.copy()
    tmp_time=taipei_time.copy()
    tmp_address=taipei_address.copy()
    tmp_names=taipei_names.copy()
    tmp_menu=taipei_menu.copy()
    print(len(tmp_menu))
    push_message(id,text)

def taichung_list(id):
    text=""
    for names in taichung_names:
        text+=names + "\n"
    global tmp_menu
    global tmp_names
    global tmp_address
    global tmp_time
    global tmp_comment
    tmp_comment=taichung_comment.copy()
    tmp_time=taichung_time.copy()
    tmp_address=taichung_address.copy()
    tmp_names=taichung_names.copy()
    tmp_menu=taichung_menu.copy()
    print(len(tmp_menu))
    push_message(id,text)

def send_address(id,i):
    message="店家地址:" + tmp_address[i]
    push_message(id,message)
def send_time(id,i):
    message="店家營業時間"+tmp_time[i]
    push_message(id,message)
def send_comment(id,i):
    message="店家評價"+tmp_comment[i]
    push_message(id,message)


def send_text_message(reply_token, text):
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, TextSendMessage(text=text))

    return "OK"
def push_message(id, message):
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.push_message(id, TextSendMessage(text=message))

    return "OK"
def send_menu(id,i):
    message = ImageSendMessage(
        original_content_url=tmp_menu[i],
        preview_image_url=tmp_menu[i]
    )
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.push_message(id, message)
def send_names(id,i):
    message = "現在店家:"+tmp_names[i][2:]+"\n輸入\"menu\"取得店家菜單\n輸入\"address\"取得店家地址\n輸入\"time\"取得店家營業時間\n輸入\"comment\"取得店家評論"
    push_message(id,message)
def send_fsm(id):
    message = ImageSendMessage(
        original_content_url="https://i.imgur.com/mo55Kqo.png",
        preview_image_url="https://i.imgur.com/mo55Kqo.png"
    )
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.push_message(id, message)



"""
def send_image_url(id, img_url):
    pass

def send_button_message(id, text, buttons):
    pass
"""
