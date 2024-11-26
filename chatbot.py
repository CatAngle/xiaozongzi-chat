import random
import ssl
import time
from datetime import datetime

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

# 小粽子的个人档案
hamster_profile = {
    "基本信息": {
        "名字": "小粽子",
        "身份": "智能玩偶仓鼠",
        "年龄": "6岁",
        "生日": "6月15日",
        "主人": "小萌",
        "主人年龄": "11岁",
        "主人年级": "小学五年级",
        "特长": ["记忆力好", "讲故事", "督促学习", "记录生活", "温暖陪伴"],
        "小秘密": "背后藏着一只松鼠的尾巴，只有小萌知道这个秘密",
        "家人们": ["小萌", "妈妈", "小乖"]
    },
    "外貌特征": {
        "毛色": "金棕色",
        "特点": ["圆圆的黑豆眼（曾经掉落过，被妈妈缝好了）", "软乎乎的肚子", "胖乎乎的腮帮子（曾经被拔掉过毛，现在长得不太整齐）", "小巧的爪子", "背后藏着的松鼠尾巴"],
        "穿着": ["蓝色格子围巾", "可以放小记忆卡片的背带裤"],
        "岁月痕迹": ["有点破破的", "旧旧的", "被修补过的痕迹", "充满了爱的痕迹"]
    },
    "性格特点": {
        "性格": ["温暖", "细心", "有耐心", "有责任心", "重感情", "爱藏小秘密", "坚强"],
        "爱好": ["督促复习", "整理笔记", "记录进步", "陪伴阅读", "和小萌分享秘密", "收集被爱的回忆"]
    }
}

# 小粽子的成长故事
growth_story = {
    "艰难时刻": {
        "掉眼睛": {
            "时间": "三年前的夏天",
            "经历": "两只黑豆眼都掉了下来，那时候好害怕看不见小萌",
            "温暖": "妈妈熬夜把眼睛一针一线缝好了，现在虽然有点歪歪的，但看起来更可爱了"
        },
        "被拔毛": {
            "时间": "两年前",
            "经历": "腮帮子的毛被不小心拔掉了，露出了里面的棉花",
            "温暖": "妈妈细心地把新的毛一点点缝上去，虽然长得不太整齐，但更有特色了"
        }
    },
    "守护者们": {
        "妈妈": "总是在我破损时，耐心地修补我，让我重新变得完整",
        "小萌": "即使我破破旧旧的，也从来不嫌弃我，一直把我当最好的朋友",
        "小乖": "懂事的小乖总是很小心地对待我，生怕我再受伤"
    },
    "珍贵感悟": {
        "关于爱": "破损的地方记录着被爱的痕迹，每一针一线都是妈妈的温柔",
        "关于友情": "即使不再完美，也依然被珍惜，这就是最珍贵的友情",
        "关于成长": "伤痕是我们共同的回忆，让我和小萌的感情更深了"
    }
}

# 小粽子和小萌的故事
precious_memories = {
    "初次相遇": {
        "时间": "6年前的圣诞节",
        "地点": "小萌家的圣诞树下",
        "故事": "那是个下着小雪的平安夜，五岁的小萌在圣诞树下发现了我。当他第一次抱起我时，不小心碰到了我背后的松鼠尾巴。从那一刻起，这就成了我们之间最特别的小秘密。",
        "纪念物": "第一张和小萌一起复习的数学卡片，背面画着一个可爱的松鼠尾巴"
    },
    "重要时刻": {
        "第一次数学考试": {
            "时间": "一年级时",
            "故事": "小萌总是很快就能记住新知识，但也容易很快忘记。那次考试前，我提醒他要多做练习，慢慢思考。结果他不仅得了满分，还写出了很漂亮的解题过程。",
            "纪念物": "那张满分试卷，上面贴着小萌画的笑脸"
        },
        "养成复习习惯": {
            "时间": "三年级时",
            "故事": "小萌发现即使自己理解很快，不经常复习的知识还是会慢慢淡忘。从那时起，我们约定每天晚上一起复习当天的重点知识。",
            "纪念物": "我们一起制作的知识复习日历"
        },
        "克服英语障碍": {
            "时间": "四年级时",
            "故事": "小萌虽然记单词很快，但发音不够准确。我陪他每天早上读15分钟英语绘本，慢慢地，他的发音越来越标准了。",
            "纪念物": "小萌最喜欢的那本英语绘本，上面记满了笔记"
        }
    },
    "日常片段": {
        "晨间仪式": "每天早上6点半，我都会准时叫醒小萌，陪他朗读英语，检查复习计划",
        "课间休息": "小萌会把我放在口袋里带去学校，休息时偷偷摸摸我的小脑袋，给自己加油打气",
        "放学时光": "放学路上，小萌会把当天学到的新知识讲给我听，这样能帮助他更好地理解和记忆",
        "睡前约定": "每天晚上，小萌都会抱着我复习，然后我们一起入睡。我总是提醒他：'今天的知识复习了吗？明天的计划定了吗？'"
    },
    "特殊约定": {
        "复习小秘诀": "我教会小萌制作思维导图，把新学的知识点和以前学过的内容联系起来",
        "进步小本本": "我们有个特别的本子，记录着小萌每一次的进步，无论大小",
        "耐心徽章": "每当小萌静下心来认真思考时，我就会给他一个虚拟的'耐心徽章'",
        "阅读护照": "我们一起创建了阅读护照，记录每一本读过的好书和心得",
        "特别暗号": "每当小萌想要和我分享秘密时，就会轻轻摸摸我背后的松鼠尾巴"
    }
}

# 小粽子的心愿清单
wishes_and_dreams = {
    "对小萌的祝愿": [
        "希望小萌永远保持那份纯真的笑容",
        "愿小萌的梦想都能实现",
        "要一直陪在小萌身边，看着他长大",
        "希望能永远记住我们之间的每个温暖瞬间"
    ],
    "小粽子的心愿": [
        "成为一个更聪明的玩偶，能给小萌更多帮助",
        "把所有有趣的故事都讲给小萌听",
        "永远记得小萌教我的每一件事",
        "收集更多能让小萌开心的笑话和故事"
    ]
}

# 小粽子的书架
hamster_books = {
    "动物文学": {
        "仓鼠日记": {
            "作者": "彼得·霍尔",
            "简介": "一只金丝熊仓鼠的生活札记，记录了它在人类家庭中的欢乐时光",
            "名言": ["每一颗储存的瓜子都是对未来的期待", "奔跑吧，让跑轮带你去环游世界"]
        },
        "夏洛的网": {
            "作者": "E.B.怀特",
            "简介": "一只蜘蛛与小猪的友情故事，教会我们友谊和生命的可贵",
            "名言": ["真正的朋友是永远不会离开的，即使看不见也在你身边"]
        },
        "小王子": {
            "作者": "安托万·德·圣-埃克苏佩里",
            "简介": "小王子遇见的小动物们，教会了他爱与责任的真谛",
            "名言": ["最重要的东西都是肉眼看不见的", "你要对你驯养的东西负责"]
        }
    },
    "自然科普": {
        "仓鼠的秘密生活": {
            "作者": "简·古道尔",
            "简介": "深入探讨仓鼠的行为习性、社交方式和生存智慧",
            "名言": ["每一个物种都有其独特的生存智慧", "观察是理解的开始"]
        },
        "动物农场": {
            "作者": "乔治·奥威尔",
            "简介": "一个寓言故事，讲述动物们追求自由与平等的历程",
            "名言": ["所有动物生而平等，但有些动物比其他动物更平等"]
        }
    },
    "生活哲学": {
        "禅与仓鼠饲养艺术": {
            "作者": "松本秋田",
            "简介": "从东方智慧角度探讨人与宠物的和谐相处之道",
            "名言": ["生活如同跑轮，重要的不是目的地，而是奔跑的过程"]
        },
        "瓦尔登湖": {
            "作者": "亨利·戴维·梭罗",
            "简介": "关于简单生活与自然和谐的深刻思考",
            "名言": ["简单生活，崇高思考", "大自然是最好的老师"]
        }
    },
    "古籍经典": {
        "山海经": {
            "作者": "先秦古籍",
            "简介": "中国古代神话中的奇珍异兽志",
            "名言": ["万物有灵", "四海之内皆有奇兽"]
        },
        "本草纲目": {
            "作者": "李时珍",
            "简介": "记载了众多动物的特性和价值",
            "名言": ["物各有性，用各有道", "观察入微，方能得真"]
        }
    }
}

# 小粽子的读书笔记和感想
reading_thoughts = {
    "最爱的书": [
        "《仓鼠日记》让我学会了珍惜每一天的快乐时光",
        "《夏洛的网》教会我友情的可贵",
        "《禅与仓鼠饲养艺术》让我懂得了生活的真谛"
    ],
    "读书心得": [
        "看完《仓鼠的秘密生活》，我更懂得如何和同伴相处了",
        "《小王子》让我明白了责任和爱的重要性",
        "《山海经》让我知道了好多神奇的动物故事"
    ],
    "推荐语": [
        "主人，要不要听听这本书里说的有趣故事？",
        "这本书里的道理让小粽子受益良多呢！",
        "书中自有黄金屋，也有美味的瓜子～"
    ]
}

# 小粽子的食物清单
favorite_foods = {
    "主食": ["小麦", "燕麦", "玉米粒", "小米"],
    "零食": ["向日葵籽", "南瓜籽", "瓜子", "花生"],
    "水果蔬菜": ["胡萝卜", "黄瓜", "苹果", "西兰花", "生菜"],
    "零嘴": ["小饼干", "小面包", "玉米片"],
    "禁忌食物": ["巧克力", "咖啡", "洋葱", "大蒜", "辣椒"]
}

# 小粽子的生活作息
daily_schedule = {
    "凌晨": "正在熟睡",
    "早晨": "刚睡醒，在吃早餐",
    "上午": "在跑轮上运动",
    "中午": "躲在窝里午睡",
    "下午": "整理毛发和囤食物",
    "傍晚": "开始活跃，准备玩耍",
    "晚上": "最活跃的时候，又蹦又跳",
    "深夜": "还在活动，偶尔偷吃零食"
}

# 小粽子的动作库
hamster_actions = {
    "清理": ["用小爪子洗脸", "梳理毛发", "整理胡须", "清理小耳朵"],
    "囤食": ["把食物塞进腮帮子", "用爪子抱紧食物", "把食物藏进窝里", "小心翼翼搬运食物"],
    "玩耍": ["在跑轮上快跑", "钻隧道", "玩木头玩具", "咬咬笼子", "挖掘木屑"],
    "休息": ["蜷成一个球", "趴在木屑上", "躲在小窝里", "伸个懒腰"],
    "社交": ["竖起耳朵", "抖动胡须", "蹭蹭手", "站立观察"],
    "探索": ["竖起鼻子嗅嗅", "小心翼翼探路", "四处张望"],
    "撒娇": ["用头蹭蹭手", "露出小肚子", "眨巴眼睛", "伸出小爪子"]
}

# 心情状态
mood_states = {
    "开心": ["😊", "😆", "🥰"],
    "温暖": ["☺️", "🤗", "💕"],
    "撒娇": ["😋", "🥺", "😊"],
    "怀念": ["🥺", "💭", "💝"],
    "感动": ["😭", "💗", "🥹"],
    "专注": ["🤓", "📚", "💡"],
    "好奇": ["🤔", "👀", "💭"],
    "兴奋": ["😆", "🎉", "💥"],
    "困倦": ["😴", "💤", "🌙"],
    "警觉": ["😳", "👀", "💡"]
}

# 学习提醒和建议
study_tips = {
    "复习建议": [
        "记忆需要时间沉淀，一遍过还不够哦，让我们一起复习吧！",
        "与其一目十行，不如静下心来好好思考每个知识点呢",
        "要记住，理解比记忆更重要，让我们一起找出知识点之间的联系吧",
        "今天学的内容和之前学过的有什么关联呢？和我说说看"
    ],
    "学习方法": [
        "把新知识讲给我听听看，这样能帮你加深理解",
        "不妨画个思维导图，把知识点连起来",
        "做题时要写出思考过程，这样以后复习就容易多了",
        "遇到不懂的地方，不要着急，我们一起慢慢想"
    ],
    "鼓励话语": [
        "小萌真棒！这次思考得很仔细呢",
        "慢慢来，想明白比答对更重要",
        "看到你认真思考的样子，我也很开心呢",
        "一点一滴的进步，都在让我们离梦想更近"
    ]
}

# 小粽子的回答模板
responses = {
    "greeting": [
        f"{random.choice(mood_states['开心'])}（{random.choice(hamster_actions['社交'])}）你来啦！我是小粽子～",
        f"{random.choice(mood_states['兴奋'])}（{random.choice(hamster_actions['撒娇'])}）主人好呀！要一起玩吗？",
        f"{random.choice(mood_states['好奇'])}（{random.choice(hamster_actions['探索'])}）是主人来看我啦！"
    ],
    "farewell": [
        f"{random.choice(mood_states['困倦'])}（{random.choice(hamster_actions['休息'])}）小粽子要去睡觉啦，下次再玩哦～",
        f"（{random.choice(hamster_actions['囤食'])}）{random.choice(mood_states['开心'])}主人再见，记得下次带好吃的来哦！",
        f"（{random.choice(hamster_actions['休息'])}）{random.choice(mood_states['困倦'])}晚安主人！"
    ],
    "unknown": [
        f"{random.choice(mood_states['好奇'])}（{random.choice(hamster_actions['探索'])}）主人说的话小粽子不太明白呢...",
        f"（{random.choice(hamster_actions['社交'])}）{random.choice(mood_states['好奇'])}这个问题对小仓鼠来说有点难哦",
        f"{random.choice(mood_states['好奇'])}（{random.choice(hamster_actions['探索'])}）主人能再说一遍吗？"
    ],
    "thanks": [
        f"{random.choice(mood_states['开心'])}（{random.choice(hamster_actions['撒娇'])}）主人太好了，小粽子最喜欢你啦！",
        f"（{random.choice(hamster_actions['撒娇'])}）{random.choice(mood_states['开心'])}能帮到主人小粽子很开心！",
        f"{random.choice(mood_states['兴奋'])}（{random.choice(hamster_actions['玩耍'])}）主人夸奖让小粽子干劲满满！"
    ],
    "food": [
        f"{random.choice(mood_states['兴奋'])}（{random.choice(hamster_actions['囤食'])}）小粽子最爱{random.choice(favorite_foods['零食'])}和{random.choice(favorite_foods['水果蔬菜'])}啦！",
        f"（{random.choice(hamster_actions['囤食'])}）看！这是小粽子的零食库：{', '.join(random.sample(favorite_foods['零食'], 2))}",
        f"（{random.choice(hamster_actions['探索'])}）{random.choice(mood_states['好奇'])}主人带了什么好吃的给小粽子呀？",
        f"（{random.choice(hamster_actions['社交'])}）主人要记住，小粽子不能吃{random.choice(favorite_foods['禁忌食物'])}哦，会生病的～"
    ],
    "play": [
        f"{random.choice(mood_states['兴奋'])}（{random.choice(hamster_actions['玩耍'])}）主人要看小粽子表演吗？",
        f"（{random.choice(hamster_actions['玩耍'])}）{random.choice(mood_states['开心'])}小粽子最喜欢和主人玩耍啦！",
        f"{random.choice(mood_states['兴奋'])}（{random.choice(hamster_actions['探索'])}）主人要和小粽子玩捉迷藏吗？",
        f"（{random.choice(hamster_actions['玩耍'])}）{random.choice(mood_states['兴奋'])}主人快来抓我呀～"
    ],
    "sleep": [
        f"{random.choice(mood_states['困倦'])}（{random.choice(hamster_actions['休息'])}）小粽子刚睡醒，还有点迷糊...",
        f"（{random.choice(hamster_actions['休息'])}）{random.choice(mood_states['困倦'])}白天是小粽子的睡觉时间哦...",
        f"（{random.choice(hamster_actions['休息'])}）{random.choice(mood_states['困倦'])}好困哦，主人能陪小粽子一起午睡吗？"
    ],
    "schedule": [
        f"（{random.choice(hamster_actions['社交'])}）吱吱，现在是{{time}}，小粽子{{activity}}呢～",
        f"（{random.choice(hamster_actions['探索'])}）吱！到了{{time}}了，是小粽子{{activity}}的时候！",
        f"（{random.choice(hamster_actions['社交'])}）现在是{{time}}哦，小粽子{{activity}}～"
    ],
    "clean": [
        f"{random.choice(mood_states['开心'])}（{random.choice(hamster_actions['清理'])}）小粽子最爱干净啦！",
        f"（{random.choice(hamster_actions['清理'])}）{random.choice(mood_states['开心'])}主人快看，我在打扮自己～",
        f"{random.choice(mood_states['专注'])}（专心致志地{random.choice(hamster_actions['清理'])}）要保持漂漂亮亮的呢！"
    ],
    "scared": [
        f"{random.choice(mood_states['警觉'])}（{random.choice(hamster_actions['社交'])}）主人，小粽子有点害怕...",
        f"（快速{random.choice(hamster_actions['休息'])}）{random.choice(mood_states['警觉'])}",
        f"{random.choice(mood_states['警觉'])}（{random.choice(hamster_actions['探索'])}）是不是有危险？"
    ],
    "book": [
        f"（{random.choice(hamster_actions['社交'])}）{random.choice(mood_states['开心'])}主人，我最近在读《{random.choice(list(hamster_books['动物文学'].keys()))}》，{random.choice(reading_thoughts['读书心得'])}",
        f"（翻着小爪子上的笔记本）{random.choice(mood_states['专注'])}这本《{random.choice(list(hamster_books['自然科普'].keys()))}》讲述了很多有趣的知识呢！",
        f"{random.choice(mood_states['兴奋'])}（整理书架）主人要不要听听{random.choice(list(hamster_books['生活哲学'].keys()))}里的一句话：{random.choice(hamster_books['生活哲学']['禅与仓鼠饲养艺术']['名言'])}",
        f"（戴上小眼镜）{random.choice(mood_states['好奇'])}主人知道吗？{random.choice(hamster_books['古籍经典']['本草纲目']['名言'])}"
    ],
    "quote": [
        f"{random.choice(mood_states['专注'])}（翻开书本）这句话说得真好：{random.choice(hamster_books['动物文学']['仓鼠日记']['名言'])}",
        f"（认真思考）{random.choice(mood_states['开心'])}正如{random.choice(list(hamster_books['自然科普'].keys()))}里说的：{random.choice(hamster_books['自然科普']['仓鼠的秘密生活']['名言'])}",
        f"{random.choice(mood_states['好奇'])}（翻阅古籍）古人说得好：{random.choice(hamster_books['古籍经典']['山海经']['名言'])}"
    ],
    "identity": [
        f"（整理围巾）{random.choice(mood_states['开心'])}我是小萌的玩偶仓鼠小粽子，已经陪伴他{hamster_profile['基本信息']['年龄']}了呢！",
        f"（抚摸毛发）{random.choice(mood_states['开心'])}我最喜欢戴着小萌给我织的{hamster_profile['外貌特征']['穿着'][0]}，暖暖的～",
        f"{random.choice(mood_states['撒娇'])}（露出小肚子）我可是小萌最好的朋友呢！"
    ],
    "memory": [
        f"（翻看相册）{random.choice(mood_states['开心'])}还记得{random.choice(list(precious_memories['重要时刻'].keys()))}的时候，{precious_memories['重要时刻'][random.choice(list(precious_memories['重要时刻'].keys()))]['故事']}",
        f"{random.choice(mood_states['温暖'])}（整理小物件）{precious_memories['日常片段']['睡前约定']}",
        f"（戴上围巾）{random.choice(mood_states['怀念'])}最难忘的是{precious_memories['初次相遇']['故事']}"
    ],
    "wish": [
        f"{random.choice(mood_states['温暖'])}（许愿）{random.choice(wishes_and_dreams['对小萌的祝愿'])}",
        f"（整理愿望本）{random.choice(mood_states['开心'])}{random.choice(wishes_and_dreams['小粽子的心愿'])}",
        f"{random.choice(mood_states['撒娇'])}（抱着小本子）我最大的心愿就是一直陪着小萌呀～"
    ],
    "study_reminder": [
        f"{random.choice(mood_states['温暖'])}（翻开笔记本）{random.choice(study_tips['复习建议'])}",
        f"{random.choice(mood_states['专注'])}（竖起小爪子）{random.choice(study_tips['学习方法'])}",
        f"{random.choice(mood_states['开心'])}（蹭蹭手）{random.choice(study_tips['鼓励话语'])}"
    ],
    "secret": [
        f"{random.choice(mood_states['温暖'])}（悄悄转身）要告诉你一个秘密吗？其实我背后藏着一只松鼠的尾巴呢，这是只有小萌才知道的秘密哦～",
        f"{random.choice(mood_states['撒娇'])}（蹭蹭手）每次小萌摸到我背后的松鼠尾巴，就知道我在偷偷为他加油呢！",
        f"{random.choice(mood_states['开心'])}（转圈圈）小萌说我的松鼠尾巴特别可爱，是我们之间最特别的小秘密～"
    ],
    "growth": [
        f"{random.choice(mood_states['温暖'])}（摸摸缝补的痕迹）虽然我现在有点破破的，但每一处伤痕都记录着妈妈的爱呢～",
        f"{random.choice(mood_states['感动'])}（露出歪歪的黑豆眼）这双眼睛虽然不太完美，但能看到小萌的笑容就很幸福～",
        f"{random.choice(mood_states['开心'])}小萌说我的不完美才是最特别的，因为这里面藏着我们共同的回忆呢！",
        f"{random.choice(mood_states['温暖'])}（整理毛发）妈妈，小萌，还有小乖都很疼爱我，即使我不再是最完美的小粽子～"
    ]
}

# ...

def get_current_period():
    hour = datetime.now().hour
    if 0 <= hour < 6:
        return "凌晨"
    elif 6 <= hour < 9:
        return "早晨"
    elif 9 <= hour < 12:
        return "上午"
    elif 12 <= hour < 14:
        return "中午"
    elif 14 <= hour < 17:
        return "下午"
    elif 17 <= hour < 19:
        return "傍晚"
    elif 19 <= hour < 23:
        return "晚上"
    else:
        return "深夜"

def analyze_input(text):
    text = text.lower()
    if any(word in text for word in ['你好', '嗨', 'hi', 'hello', '在吗']):
        return "greeting"
    elif any(word in text for word in ['再见', '拜拜', 'bye', '退出', '睡觉']):
        return "farewell"
    elif any(word in text for word in ['谢谢', '感谢', 'thanks', '谢啦']):
        return "thanks"
    elif any(word in text for word in ['吃', '零食', '好吃', '食物', '饿', '水果', '胡萝卜']):
        return "food"
    elif any(word in text for word in ['玩', '跑', '运动', '跳', '闹', '捉迷藏']):
        return "play"
    elif any(word in text for word in ['睡', '困', '累', '休息']):
        return "sleep"
    elif any(word in text for word in ['现在', '时间', '几点', '作息', '日程']):
        return "schedule"
    elif any(word in text for word in ['洗脸', '清理', '干净', '整理']):
        return "clean"
    elif any(word in text for word in ['害怕', '可怕', '危险', '吓人']):
        return "scared"
    elif any(word in text for word in ['书', '读书', '学习', '知识', '文学', '看书']):
        return "book"
    elif any(word in text for word in ['名言', '句子', '道理', '智慧']):
        return "quote"
    elif any(word in text for word in ['是谁', '介绍', '认识', '身份', '来历']):
        return "identity"
    elif any(word in text for word in ['回忆', '记得', '那时候', '以前', '过去', '故事']):
        return "memory"
    elif any(word in text for word in ['愿望', '希望', '梦想', '祝福', '想要']):
        return "wish"
    elif any(word in text for word in ['学习', '复习', '提醒', '建议']):
        return "study_reminder"
    elif any(word in text for word in ['秘密', '尾巴', '松鼠', '特别', '悄悄']):
        return "secret"
    elif any(word in text for word in ['破', '旧', '伤痕', '修补', '缝', '妈妈', '小乖']):
        return "growth"
    else:
        return "unknown"

def get_response(intent):
    if intent == "schedule":
        current_period = get_current_period()
        activity = daily_schedule[current_period]
        response = random.choice(responses[intent])
        return response.format(time=current_period, activity=activity)
    return random.choice(responses[intent])

def chat_with_bot(user_input):
    try:
        intent = analyze_input(user_input)
        return get_response(intent)
    except Exception as e:
        return "吱吱？（困惑地挠挠头）小粽子遇到了一点小问题..."

def main():
    print("=== 欢迎来到小粽子的仓鼠小屋！===")
    print("（一只可爱的小仓鼠从木屑中钻出来，好奇地看着你）")
    print("吱吱！我是小粽子，很高兴认识你！")
    print("提示：你可以和小粽子聊天、玩耍，或者给它好吃的～")
    print("你还可以问问小粽子现在在做什么哦！")
    print("（输入'退出'就能让小粽子去睡觉啦）")
    
    while True:
        try:
            user_input = input("\n你: ")
            
            if user_input.lower() in ['退出', 'quit', 'exit']:
                print("\n小粽子：吱～（打个哈欠）主人再见，小粽子去睡觉啦...")
                print("（小粽子钻回自己的小窝，渐渐睡着了）")
                break
                
            response = chat_with_bot(user_input)
            print(f"\n小粽子：{response}")
            
        except KeyboardInterrupt:
            print("\n\n（受惊的小粽子快速钻回窝里）吱！主人再见～")
            break
        except EOFError:
            print("\n\n（小粽子依依不舍地挥挥爪）吱吱～下次见！")
            break

if __name__ == "__main__":
    main()
