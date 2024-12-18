import Model
import re


# 读取文件的辅助方法
def readfile(path):
    with open(path, 'r', encoding="utf-8") as file:
        content = file.read()
    return content

def ask():
    model = Model.Model()
    # 读取现代文阅读I文本
    content = readfile("Doc/现代文阅读I.txt")

    content = (
        "对素食者和肠胃疾病患者来说，藜麦的发现是一个奇迹。藜麦不含麸质，富含镁和铁，比其他种子含有更多的蛋白质，包括人体无法独自生成的必需的氨基酸。美国宇航局宣布，藜麦是地球上营养最均衡的食物之一，是宇航员的理想之选。产于安第斯山的藜麦有一个令西方消费者神往的传说：印加人非常重视藜麦，认为它是神圣的，并且称之为＂万谷之母＂。不过，藜麦的爱好者却通过媒体发现了一个令人不安的事实。从 2006年到 2013年，玻利维亚和秘鲁的藜麦价格上涨了两倍。 2011年，《独立报》称，玻利维亚的藜麦消费量＂ 5年间下降了 34％，当地家庭已经吃不起这种主食了，它已经变成了奢侈品＂。《纽约时报》援引研究报告称，蔡麦种植区的儿童营养不良率正在上升。 2013年，《卫报》用煽动性标题提升了人们对这个问题的关注度：＂素食者的肚子能装下藜麦令人反胃的事实吗？＂该报称，贫穷的玻利维亚人和秘鲁人正在食用更加便宜的＂进口垃圾食品＂。《独立报》 2013年一篇报道的标题是＂藜麦：对你有利 --对玻利维亚人有害＂。这些消息传遍了全球，在健康饮食者之中引发了一场良心危机。在社交媒体、素食博客和健康饮食论坛上，人们开始询问食用藜麦是否合适。"
        "这种说法看似可信，被许多人认可，但是经济学家马克·贝勒马尔等人对此则持保留意见。毕竟，藜麦贸易使大量外国资金涌入玻利维亚和秘鲁，其中许多资金进入了南美最贫穷的地区。几位经济学家跟踪了秘鲁家庭支出的调查数据，将种植且食用藜麦的家庭、食用但不种植藜麦的家庭和从不接触藜麦的家庭划分为三个小组。他们发现，从 2004年到 2013年，三个小组的生活水平都上升了，其中藜麦种植户家庭支出的增长速度是最快的。农民们正在变富，他们将这种新收入转化为支出又给周边民众带来了好处。那么藜麦消费量下降 34％又是怎么回事呢？原来，在很长的时间内两个国家的藜麦消费量一直在缓慢而稳定地下降，这意味着消费量的下降和价格的激增不存在明显的联系。更加接近事实的解释是，秘鲁人和玻利维亚人只是想换换口味，吃点别的东西。"
        "为了解藜麦的种植情况，我去了秘鲁科尔卡山谷，这里在印加时代以前就得到了开垦。藜麦是一种美丽的作物，拥有深红色或金黄色的巨大种球。在安第斯山的这片区域，人们在梯田上同时种植藜麦以及当地特有的玉米和马铃薯品种。＂国外需求绝对是一件好事，＂我的秘鲁向导杰西卡说道，＂农民非常高兴，所有想吃藜麦的人仍然买得起这种食物。＂她还解释了另一个好处。之前，秘鲁城里人往往认为他们这片区域吃藜麦的人＂很土＂。现在，由于美国人和欧洲人的重视，食用藜麦被视作一种时尚。＂利马人终于开始尊重我们这些高原人和我们的传统了。＂玻利维亚西南部有一片遥远而不适合居住的区域，那里到处都是盐湖和休眠火山。在那里，我看到了由藜麦资金支持的当地急需的开发和旅游项目。千百年来勉强能够养家糊口的自耕农开始为更加美好的未来而投资。我在 2017年 4月听到的玻利维亚人对于该作物的唯一抱怨是，日益增长的供给正在拉低价格。玻利维亚的藜麦种植面积增长了两倍多，从 2007年的 5万公顷增长到 2016年的 18万公项。马克·贝勒马尔后来对我说：＂这是一个令人悲伤的结局，因为它的价格不太可能再度回升。＂在风景如画的科尔卡山谷，当太阳落山时，我问杰西卡，欧洲和北美的消费者是否应该为吃掉秘鲁人和玻利维亚人的食物而感到内疚。我可以猜到答案，但我想听到当地人的亲口否认。＂相信我，＂杰西卡笑道，＂我们有许多藜麦。＂公众号“小俊语文”"
        "乍一看，这一关于食物热潮、全球贸易和消费者忧虑的事件讲述了谎言被揭穿的过程。不过，这些受到错误解读的真相可能会对当地的人们造成真正的伤害。各行各业有经验的沟通者会通过片面的事实、数字、背景呈现某种世界观，从而影响现实。在这个例子中，新闻工作者和博主出于高尚的理由引导消费者远离藜麦：他们由衷地为一个贫困群体感到担忧，害怕狂暴的全球贸易风潮会危及这一群体的利益。我们很早就知道这一点：每个新手辩论者和犯错误的小学生都知道如何挑选最有利于自己的真相。不过，我们可能不知道这些真相为沟通者提供了多大的灵活性。很多时候，你可以通过许多方式描述一个人、一件事物或者一起事件，这些描述可能具有同等的真实性。我将它们称为＂竞争性真相＂。")

    prompt = "设计ABCD的4个选项，这4个选项都是关于文章论证方法的，再设计之前我建议你提前复习一下论证方法有几种，在这4个选项中故意挑一个改成错误的答案，请最后输出你设计的题目，以及哪一个是错误答案与解析" + content
    # output = model.inout(prompt, 1024)

    # 测试输出
    output = ("题目：以下哪项不是本文采用的论证方法？"
              "A. 对比论证：通过比较藜麦价格上涨前后消费者的变化，展示了藜麦对当地居民的影响。 B. 举例论证：通过引用《独立报》和《纽约时报》的研究报告和报道，证明了藜麦价格上涨对玻利维亚和秘鲁人的影响。 C. 引用论证：通过引用经济学家马克·贝勒马尔的观点，对藜麦价格上涨的影响提出了不同的看法。 D. 数据论证：通过分析秘鲁家庭支出的调查数据，展示了藜麦贸易对当地居民生活水平的影响。"
              "设计ABCD的4个选项，这4个选项都是关于文章论证方法的，再设计之前我建议你提前复习一下论证方法有几种，在这4个选项中故意挑一个改成错误的答案，请最后输出你设计的题目，以及哪一个是错误答案与解析")
    sentence = re.findall(r"A.(.*?)B.(.*?)C.(.*?)D.(.*?)。", output)[0]
    A1 = sentence[0]
    B1 = sentence[1]
    C1 = sentence[2]
    D1 = sentence[3]

    prompt = "请你帮助我给学生命制一道选择题，设计ABCD4个选项，我会给你一篇文章，请你选取文章中的4个原文中的关键词，你只能根据文章内容谈谈你对这四个关键词的理解，并且请你使用逻辑谬误故意使你对其中一个词语的理解与原文意思不相符合，你需要提供你的理解，并指出你对哪一句话故意使用了逻辑谬误，即给出答案与解析。" + content
    # output = model.inout(prompt, 1024)

    output = ("现在，我将提供一道选择题，并指出其中哪一句话使用了逻辑谬误。"
              "选择题：以下哪一项关于藜麦的描述是错误的？"
              "A.藜麦是一种营养丰富的食物，受到全球消费者的喜爱。"
              "B.藜麦价格上涨使其成为一种奢侈品，让一些贫困人群难以承受。"
              "C.由于藜麦价格上涨，玻利维亚和秘鲁的藜麦消费量下降，当地居民生活水平下降。"
              "D.藜麦在全球市场上的需求不断增长，导致其价格不断攀升。"
              "答案与解析：选项C"
              "是错误的。虽然一些媒体报道了藜麦在产地玻利维亚和秘鲁的消费量下降，以及当地居民生活水平下降的消息，但实际上，根据经济学家的研究，藜麦种植户的家庭支出增长速度是最快的，"
              "这意味着藜麦价格上涨并没有导致当地居民生活水平下降。在这里，我使用了逻辑谬误，将藜麦价格上涨与当地居民生活水平下降之间建立了错误的联系。")
    sentence = re.findall(r"A.(.*?)B.(.*?)C.(.*?)D.(.*?)。", output)[0]
    A2 = sentence[0]
    B2 = sentence[1]
    C2 = sentence[2]
    D2 = sentence[3]

    prompt = ("我将给你一篇文章，然后给你一道选择题“3. 下列选项，最适合作为论据来支撑第二段观点的一项是（   ）"
              "A. “粮食优先”智库的工作人员塔尼娅·科森在谈到安第斯山藜麦种植者时表示：“坦率地说，他们厌倦了藜麦，因此开始购买其他食物。”"
              "B. 加拿大《环球邮报》一则新闻的标题为“你对藜麦的爱越深，你对玻利维亚人和秘鲁人的伤害就越深”。"
              "C. 制片人迈克尔·威尔科克斯专门为这个问题制作了一部纪录片，他说：“我见过一些反对食用藜麦的文字评论，实际上，停止消费才会真正伤害这些农民。”"
              "D. 英国广播公司播音员埃文·戴维斯指出：“事实上，说谎常常是没有必要的。你可以在不使用任何谎言的情况下完成许多有效的欺骗。”在这道题目中我们可以看到它找与文章相关的四句必须是引用他人的话中，有3"
              "句话只是单纯与文章的信息相关但并非论据，其中一句话则是可以证明论点的论据，所以请你模仿该种题型，引用4句他人的话，设计为ABCD4个选项，并将其中一个选项设计为论据作为正确选项。并在最后给出你的答案与解析。") + content

    # output = model.inout(prompt, 1024)
    output = ("A. 营养学家张教授说：“藜麦确实营养均衡，含有大量人体必需的氨基酸和矿物质，对素食者和肠胃疾病患者来说是个好选择。”"
              "B. 美国宇航局发言人表示：“藜麦是地球上营养最均衡的食物之一，适合宇航员食用，说明它的营养价值非常高。”"
              "C. 玻利维亚农民何塞说：“藜麦的价格上涨让我们富裕起来，我们用这些钱改善了生活，孩子们也能吃到更好的食物。”"
              "D. 秘鲁农民妇女玛利亚说：“藜麦是我们的传统作物，现在它为我们带来了更多的收入，让我们能够投资教育和健康。”"
              "答案：C"
              "解析："
              "A项和B项都是关于藜麦对玻利维亚人和秘鲁人的负面影响的说法，与第二段观点相反，因此不是合适的论据。"
              "D项是关于欺骗的观点，与藜麦的论点无关，也不是合适的论据。"
              "C项中，制片人迈克尔·威尔科克斯的话指出停止消费藜麦实际上会伤害农民，这一观点支持了第二段的观点，即藜麦的消费对农民是有好处的，因此是合适的论据。")
    sentence = re.findall(r"A.(.*?)B.(.*?)C.(.*?)D.(.*?)。", output)[0]
    A3 = sentence[0]
    B3 = sentence[1]
    C3 = sentence[2]
    D3 = sentence[3]

    with open("Doc/现代文阅读I题目.txt", "w", encoding="utf-8") as file:
        file.write(A1 + '\n')
        file.write(B1 + '\n')
        file.write(C1 + '\n')
        file.write(D1 + '\n')
        file.write(A2 + '\n')
        file.write(B2 + '\n')
        file.write(C2 + '\n')
        file.write(D2 + '\n')
        file.write(A3 + '\n')
        file.write(B3 + '\n')
        file.write(C3 + '\n')
        file.write(D3 + '\n')

    prompt = ("我将给你一篇文章，然后给你一道问答题，这道问答题涉及关于文本内容的概括，问答题如下“"
              "4. 请简要说明文本中的西方媒体在报道时使用了哪些“竞争性真相”。”这道问答题的答案如下“"
              "4. ①《独立报》通过片面的事实和数据，称藜麦价格的上涨使玻利维亚人吃不起藜麦了；②《纽约时报》直接援引他人研究，得出藜麦种植区的儿童营养不良率正在上升的结论；"
              "③《卫报》和《独立报》使用具有明显倾向性的标题强调藜麦价格上涨对藜麦种植者造成的伤害。”请你模仿这道题的格式，选取文章的一个相关性内容较多的专有名词，"
              "设计一道有关文章内容的概括题。并给出答案与解析。") + content

    # output = model.inout(prompt, 1024)
    output = "请简要说明文本中关于“藜麦价格上涨和藜麦消费量下降”的问题，文中哪些信息表明这一现象并非如西方媒体所报道的那样简单。"
    with open("Doc/现代文阅读I题目.txt", "a", encoding="utf-8") as file:
        file.write(output + '\n')

    prompt = ("我将给你一篇文章，下面我将给你一道题目“5. 作者采用哪些方法证明关于藜麦的新闻报道结论有误？请根据文本概括。”这是这道题目的答案“"
              "5. ①借助名家观点与事实论据加以批判，比如第二段引出马克·贝勒马尔等人的质疑，引用相关经济学家的调查论证，用事实反驳报道中的错误信息；"
              "②借助实地考察的真相加以批驳，比如第三段用亲自调查时掌握的第一手材料，反驳报道中的错误信息；③借助常规逻辑认知加以批判，"
              "比如最后一段以新手论辩与犯错误小学生的自我辩护的技巧进行类比，批判报道中的“竞争性真相”。“很明显这是一道关于论证方法的题，请你选取文章的一个论点，"
              "并且进行模仿那个题目，设计一道考察关于论证那个论点的论证方法的问答题。")

    # output = model.inout(prompt, 1024)
    output = "题目：5. 作者如何运用不同的论证方法来反驳关于藜麦价格上涨对当地居民造成负面影响的观点？"
    question = re.findall("5. (.*)", output)[0]
    with open("Doc/现代文阅读I题目.txt", "a", encoding='utf-8') as file:
        file.write(question + '\n')

    # 读取现代文阅读II文本

    content = readfile("Doc/现代文阅读II.txt")

    prompt = ("我将给你一篇文章，下面我将给你一道题目“6. 下列对文本相关内容的理解，不正确的一项是（   ）A. 文章开头部分，父亲想象儿子上大学后会像时髦青年一样爱旅游，由此切入长大成人和出门旅行这两个关联话题。"
              "B. 儿子在渡船上会邂逅许多陌生人，父亲教给儿子，如何通过看他们的神情、听他们的言语来判断他们是否心存善意。"
              "C. 父亲设想儿子一路上常会遇到狗，并建议儿子离开时带走一条狗，可见狗应是父亲当年乡村生活中难忘一部分。"
              "D. 儿子的板桥之旅除了坐车乘船，还需步行走过许多路，如江堤、大路、大埂、渠边小路、石桥等，带有较浓的寻访意味。”可以看到这是一道有关文章内容理解的题，下面请你仿照这道题，设计ABCD4"
              "个选项，分别包含与文章相关的4"
              "个内容的理解，其中有一个选项故意改为与原文内容并不相符存在偏差，设计为错误选项。并给出答案与解析。") + content

    # output = model.inout(prompt, 1024)
    output = ("题目：下列对文本相关内容的理解，不正确的一项是（   ）"
    "A. 父亲在信中告诉儿子，他的成长过程中会经历许多不同的阶段，其中之一就是进入大学，并鼓励儿子在第一个暑假去旅行，体验生活。"
    "B. 父亲详细描述了儿子在旅行途中可能会经过的地方，如芜湖、江堤、村子、河边等，这些地方都富有生活气息，让人感受到乡村的宁静和友好。"
    "C. 父亲提醒儿子在村子中要找到与他父亲当年相似的人，他们可能会记得父亲当年的点点滴滴，并告诉儿子一些有关父亲的故事。"
    "D. 父亲建议儿子在旅行时带走一条狗，这表明狗在父亲的心中有着特殊的地位，也许是他当年乡村生活中的一部分。"
    "错误选项：B"
    "解析：选项B中提到“这些地方都富有生活气息”，但在原文中，并没有明确提到这些地方富有生活气息，而是详细描述了儿子在旅行途中可能会经过的地方。其他选项A、C、D都与原文内容相符。因此，选项B为错误选项。")

    sentence = re.findall(r"A.(.*?)B.(.*?)C.(.*?)D.(.*?)。", output)[0]
    A6 = sentence[0]
    B6 = sentence[1]
    C6 = sentence[2]
    D6 = sentence[3]

    prompt = ("我将要求你设计一道选择题，我将给你一篇文请根据提供的文章内容，设计一道选择题，要求如下："
              "1. 选项需要从文章中选取，保证选择正确选项需分析与鉴赏文章中的句子。"
              "2. 设计中必须包含一个错误选项，该选项需要错误地反映文章内容，但必须确保与文章主题相关且无误导性。"
              "3. 请明确指出哪个选项是错误的，并解析为何该选项错误。"
              "4. 提供的文章内容中，每个句子都是需要分析的部分，请确保题目中所有选项都与文章内容相关且准确地反映出文章中的信息。"
              "5. 保持题目格式清晰，并直接对应文章内容，避免添加任何不必要的信息或详细解析。请注意，所有选项均需直接对应文章内容，不得更改或添加任何不准确或无关的信息。"
              "很明显，这是一道关于文章句子理解的题目，请你根据文章内容设计ABCD4个选项，选项中是从文章中选取的4个原句，其中3"
              "个选项是对这个句子的正确解读，其中一个选项解读错误，设计为错误选项。并给出答案与解析，请记住在题干里把相应句子显示出来。") + content

    # output = model.inout(prompt, 1024)
    output = ("题目：根据文中划线句子，下列关于社戏的描述，不正确的一项是（ ）"
              "A. 社戏是在秋季举行的，与文章中提到的“九月二十二”和“适逢秋天橘子收获时节”相呼应。 "
              "B. 社戏是萝卜溪村一年一度的重大活动，受到村民的重视和期待。 "
              "C. 社戏的演出地点在伏波宫前空坪中，演出时间为六天，符合往年成例。 D. "
              "社戏期间，村里人会穿上新衣服，携带零用钱，类似于过盛大节日。"
              "正确答案是D。")

    sentence = re.findall(r"A.(.*?)B.(.*?)C.(.*?)D.(.*?)。", output)[0]
    A7 = sentence[0]
    B7 = sentence[1]
    C7 = sentence[2]
    D7 = sentence[3]

    prompt = ("我将给你一篇文章，根据这篇文章设计一个新的题目，在文章中选取一句富含情感深意的话，"
              "要求题目要能准确反映出刚刚从文章中选取的这句话所传递出的情感。请从文中挖掘出至少四个不同的感受点，并加以概括，"
              "作为设计新题目的基础。每个感受点的描述需要简洁明了，直接相关于刚刚选取的这句话。请确保你的答案能够反映出文章主人公内心深处的感悟。"
              "以下是给你的模板题目：\"8．下田去吧，儿子这个段落，写出了多重的身心感受。请加以梳理概括。（4分）“模板题目的答案是："
              "①对自己过去插队生活的怀念。②对儿子(年轻人)经受劳动洗礼身心得到磨砺的期望。③对村庄的风情风物不能因现代化而丢弃的④对大地无止无息地输出以溢养人类的感激。\"请根据模板来生成一道类似的题目。") + content
    # output = model.inout(prompt, 1024)
    output = ("题目：8．“我看到了你的黑黑的人影，我的心里充满了慌乱。”这句话描绘了多重的情感体验。请加以梳理概括。（4分）"
              "文章选取句子：“我看到了你的黑黑的人影，我的心里充满了慌乱。”"
              "感受点描述： ① 对弟弟离开的失落与想念。 ② 面对弟弟成长的欣喜与不安。 ③ 对流浪生活的担忧与同情。 ④ 对抗日救国的支持与自豪。")

    question1 = re.findall('8.(.*)（4分）', output)[0]

    prompt = ("：我会先给一个文章，阅读这篇文章，请根据下面的模板设计一个新的题目。"
              "题目需要围绕一个给定的关键词，写一篇文学短评。短评需要有三个部分：①该关键词在文章中的具体作用和意义；②这个关键词如何体现了文章的主题；"
              "③这个关键词对于理解和解读文章有何重要性，不需要和我给你的模板题目一模一样，要有自己的思考。每个部分请至少包含一点以上，评分每部分2分。"
              "面是一个模板题目：9．读书小组要为此文写一则文学短评。经讨论，甲组提出一组关键词：未来·回忆·成长；乙组提出一个关键词：河流。请任选一个小组加入，"
              "围绕关键词写出你的短评思路。（6分）") + content

    # output = model.inout(prompt, 1024)

    output = ("题目： 9．读书小组要为此文写一则文学短评。经讨论，甲组提出一组关键词：未来·回忆·成长；乙组提出一个关键词：河流。请任选一个小组加入，围绕关键词写出你的短评思路。（6分）"
              "短评："
              "我选择加入甲组，围绕关键词“未来·回忆·成长”来写我的短评。"
              "① 在文章中，“未来”一词承载了作者对弟弟成长道路的期望和祝福。文章通过对弟弟未来成长的描述，展现了作者对弟弟长大成人、独立思考的期待。同时，“未来”也体现了文章的主题，即弟弟的成长过程和人生道路的选择。"
              "② “回忆”在文章中起到了串联过去和现在的纽带作用。作者通过回忆自己和弟弟的成长经历，以及对弟弟童年时光的回忆，"
              "表达了对过去的怀念和对弟弟的关爱。这种对比使得主人公对过去的怀念更加深刻，也让他对未来的期待变得更加迫切。"
              "③成长”一词体现了主人公在文章中的心灵变化。在面对困境和挑战时，主人公逐渐学会了独立思考和承担责任。"
              "他不再沉溺于回忆，而是勇敢地面对现实，努力为自己的未来拼搏。这个关键词凸显了文章的主题，即在人生的道路上，每个人都要经历成长，面对未来的挑战。"
              "综上所述，“未来·回忆·成长”这三个关键词在文章中起到了穿针引线的作用，不仅体现了文章的主题，也揭示了主人公的心灵历程。对于理解和解读文章，这三个关键词具有重要的意义。")
    question2 = re.findall("9.(.*)（6分）", output)[0]

    with open("Doc/现代文阅读II题目.txt", "w", encoding="utf-8") as file:
        file.write(A6 + '\n')
        file.write(B6 + '\n')
        file.write(C6 + '\n')
        file.write(D6 + '\n')
        file.write(A7 + '\n')
        file.write(B7 + '\n')
        file.write(C7 + '\n')
        file.write(D7 + '\n')
        file.write(question1 + '\n')
        file.write(question2 + '\n')

    # 读取文言文阅读
    content = readfile("Doc/文言文阅读.txt")
    prompt = (
        "我将给你一篇文言文，请模仿高考语文考试中的“断句”题型，设计一道类似的题目。"
        "题目要求：根据文言文中的节选，标出需要断句的地方，并在答题卡上涂黑相应位置的答案。请提供以下信息：文言文材料中的句子是“夫子B善之C引D"
        "以张本E然F后难之G岂有H不似哉？”。在设计题目时，确保包含以下要素："
        "1. 确定需要断句的句子；"
        "2. 明确考察断句技巧的要求；"
        "3. 确定每正确断句给分标准；"
        "4. 清楚错误断句不得分。"
        "注意，题目应具有思考性和操作性，要求考生根据文意进行断句，考验理解力和语言表达能力。")
    # output = model.inout(prompt, 256)
    output = ("【问题】请根据文意对以下句子进行断句，并在答题卡上涂黑相应位置的答案。每正确断句一次给一分，错误断句不得分。"
              "“韩非书云夫子善之引以张本然后难之岂有不似哉？”")
    sentence_duanju = re.findall("“(.*)”", output)[0]

    prompt = (
                 "我将会给你一篇文言文请按照以下格式设计一道题：认真阅读我给你的文章，然后根据这段文字设计一个选择题，要求选择中只包含不正确的一项。文中提到的词语及解释不得更改，保持原样。设计题目时，请确保题目格式与提供的例子保持一致，包括正确的选项和错误的选项。错误选项应明确指出，并确保题目内容不添加任何新的信息或背景。以下是例子："
                 "“11．下列对材料中加点的词语及相关内容的解说，不正确的一项是（3分）"
                 "A．围，指被围困，“傅说举于版筑之间”的“举”表示被选拔，两者用法相同。'"
                 "B．劝，指鼓励、劝勉，与《兼爱》“不可以不劝爱人”中的“劝”词义不相同。"
                 "C．具臣，文中与“有功”相对，是指没有功劳的一般人臣，具体就是指高赫。"
                 "D．诬说，指没有事实依据的胡说妄言，与现在所说的“诬蔑之辞”并不一样。”"
                 "请设计的题目格式与例子保持一致，并确保题目内容符合上述要求。") + content

    # output = model.inout(prompt, 1024)
    output = ("根据您提供的文言文，我们可以设计如下选择题："
              "“24．下列对材料中加点的词语及相关内容的解说，不正确的一项是（3分） A．武臣，指文章中的陈人武臣，他提出了对韩非子观点的看法。 "
              "B．子鲋，指武臣的儿子，他回应武臣的观点并提出了自己的见解。 "
              "C．具臣，指赵襄子行赏时先加封的臣子，子鲋用此例来说明韩非子书中的观点。 D．夫子，在文中指孔子，子鲋用孔子的卒年来反驳韩非子对历史的记载。”"
              "错误选项解释： C．具臣，指赵襄子行赏时先加封的臣子，子鲋用此例来说明韩非子书中的观点。这个选项的解说是正确的，因此不是错误选项。正确的错误选项应该是在解释上与原文不符的选项。")
    # 处理文本
    choice = re.findall(r"A.(.*?)B.(.*?)C.(.*?)D.(.*?)。", output)[0]
    A11 = choice[0]
    B11 = choice[1]
    C11 = choice[2]
    D11 = choice[3]

    prompt = ("我将给你一篇文言文，请根据以下要求设计一道文言文选择题，设计ABCD4个选项："
              "1. 仔细阅读以下文段，对文章内容有深入理解者，可模仿此格式设计一道选择题。"
              "2. 请根据文章的题材、风格和内容，设计一个恰当的题目，并确保题目格式与所模仿的例子一致。"
              "3. 题目设计应能准确地反映出文章的主要信息，不得修改或遗漏任何原文中的关键信息。"
              "4. 请模仿文段中的格式，设计答案选项，并确保这些选项与原文内容相符合，并具有正确性、有益性，不得包含任何有害信息。"
              "5. 设计的题目格式必须遵循以下例子：“12．下列对材料有关内容的概述，不正确的一项是（3分）"
              "A．主上设置有关法令，令行禁止，群臣不敢越职侵权，也没有了奸诈之心，他们履职行事，有了功劳就能得到赏赐，韩非认为这样才叫＂善赏罚＂。"
              "B．在武臣看来，韩非与孔子观点不同的地方很多，在遏奸劝善等方面，韩非不一定就不对，孔子也不一定就合理，韩非也可以称得上是当世圣人。"
              "C．世人说到高必定会以上天作比，说到低必定会以深渊作比，他们常通过引经据典、援用圣贤来成就自己，使自己更加贤能，以争取民众的信任。"
              "D．子鲋对韩非之类的诸子学说闭口不言，充耳不闻，而武臣却深信不疑，进而怀疑圣人，子鲋对此深感失望，认为武臣是见识短浅，不明大道。”"
              "请保持一致，并确保题目内容符合上述要求。") + content
    # output = model.inout(prompt, 1024)
    output = ("根据您提供的文言文段落，我为您设计以下选择题："
              "下列对材料有关内容的概述，不正确的一项是（3分）"
              "A．武臣认为韩非的立法与孔子的论点有许多不同之处，他认为在遏制邪恶和鼓励善行方面，韩非的观点可能与孔子相当。"
              "B．子鲋指出，当今世人喜欢用极端的比喻来描述高低，并且喜欢引用经典和圣人的话来提升自己的形象，以赢得他人的信任。"
              "C．子鲋举例说明，赵襄子在行赏时，先赏赐那些有具体贡献的臣子，后赏赐那些有功之人，这与韩非书中的描述相矛盾，显示出韩非的记载可能有诈。"
              "D．子鲋批评武臣相信诸子百家的学说，认为这是错误的，因为诸子书中的内容都是如此，他举例说明韩非的记载与历史事实不符，以此质疑韩非的可靠性。"
              "正确答案：D"
              "解释：根据文段内容，子鲋并没有直接批评武臣相信诸子百家的学说，而是批评了世人对诸子书中的内容盲目相信。他"
              "通过举例说明韩非的记载与历史事实不符，以此质疑韩非的可靠性。因此，选项D的概述不正确。其他选项A、B、C都能准确反映文段中的内容。")

    # 处理文本
    choice = re.findall(r"A.(.*?)B.(.*?)C.(.*?)D.(.*?)。", output)[0]
    A12 = choice[0]
    B12 = choice[1]
    C12 = choice[2]
    D12 = choice[3]

    prompt = ("我将给你请提供一篇文言文段落，认真阅读并设计两道翻译题。题目需要采用格式化的表达方式，例如：“请翻译以下句子为现代汉语：（8"
              "分）”，应从文段中选出两个句子并翻译。请保证题目格式与给出的例子一致，且题目内容必须符合以下要求：要求翻译的句子为文段中的直接引述，"
              "请确保引述的内容准确无误，并保持原意的忠实性和语言的准确性。题目的模板是”（1"
              "）吾群臣无有不骄侮之意者，唯赫子不失君臣之礼，是以先之。"
              "（2）请略说一隅，而君子审其信否焉。“") + content
    # output = model.inout(prompt, 1024)
    output = ("请翻译以下句子为现代汉语：（8分）"
              "（1）今世人有言高者必以极天为称，言下者必以深渊为名。"
              "（2）昔我先君以春秋哀公十六年四月己丑卒，至二十七年荀瑶与韩、赵、魏伐郑，遇陈恒而还，是时夫子卒已十一年矣，而晋四卿皆在也。")
    sentence = re.findall("（1）(.*)（2）(.*)。", output)[0]
    sentence1 = sentence[0]
    sentence2 = sentence[1]

    prompt = ("我将给你一篇文言文，请详细分析并设计一道与文言文段落内容相关的具体问题。"
              "问题的设计必须准确地从文段中找出支持某个观点或结论的具体依据。请确保问题的格式与所给文段不同，"
              "且题目要反映出对文段中逻辑结构的深刻理解。请根据文段内容提出一个格式符合要求的问题，并确保问题的内容与文段中的信息相关，"
              "能够准确地反映出文段中的逻辑依据。") + content
    # output = model.inout(prompt, 1024)
    output = ("【问题】子鲋如何反驳武臣将韩非视为“世之圣人”的观点？"
              "【分析】 "
              "在文段中，武臣认为韩非的立法与孔子的理论有所不同，但仍然将其视为当世的圣人。子鲋则通过举例和时间线的对比，"
              "指出韩非的书中存在事实错误，以此来反驳将韩非视为圣人的观点。子鲋认为，韩非在书中对历史事件的描述与实际历史不符，"
              "这说明韩非的著作并非完全可靠，因此不能将其视为圣人。子鲋的逻辑依据在于通过具体的历史事实来质疑韩非的可靠性，从而否定武臣将韩非视为圣人的看法。")
    question1 = re.findall("【问题】(.*)【分析】", output)[0]

    # 写入文件
    with open("Doc/文言文题目.txt", 'w', encoding="utf-8") as file:
        file.write(sentence_duanju + '\n')
        file.write(A11 + '\n')
        file.write(B11 + '\n')
        file.write(C11 + '\n')
        file.write(D11 + '\n')
        file.write(A12 + '\n')
        file.write(B12 + '\n')
        file.write(C12 + '\n')
        file.write(D12 + '\n')
        file.write(sentence1 + '\n')
        file.write(sentence2 + '\n')
        file.write(question1 + '\n')

    # 读取古诗
    content = readfile("Doc/古诗文.txt")
    prompt = ("请根据给定的古诗，命制一道高中语文古诗词鉴赏题，包含两个小题。第一小题是一道选择题，有四个选项，选项内容是对诗句内容的理解或赏析，"
              "其中有三个选项是正确的理解，一个选项是不正确的，要求学生从这四个选项中选择出唯一不正确的的选项。第二小题是一道问答题，要求学生赏析古诗中某一个句子的情感。"
              "下面是给出的古诗")
    # output = model.inout(prompt, 1024)
    output = ("题目：阅读王维的《送梓州李使君》，回答以下问题。"
              "【小题1】下列对诗句内容的理解与赏析，不正确的一项是： A. “万壑树参天，千山响杜鹃”：形象地描绘了梓州山林的壮丽景象，万壑千山，树木参天，杜鹃声声，生动再现了自然的宏伟与生机。 B. "
              "“山中一夜雨，树杪百重泉”：通过“一夜雨”和“百重泉”的描写，表现了山中气候的多变与山泉的壮丽，雨后山泉从树梢倾泻而下，形成百泉争流的景象。 C. "
              "“汉女输棂布，巴人讼芋田”：反映了当时蜀地百姓的生活情景，汉女织布纳税，巴人争论田地，体现了诗人对百姓生活的高度关注。 D. "
              "“文翁翻教授，不敢倚先贤”：诗人以文翁喻李使君，期望李使君能够发扬前人的教育事业，翻新教化，而不依赖于前人的成就，显示了诗人对李使君的期望与鼓励。"
              "【小题2】请赏析诗句“山中一夜雨，树杪百重泉”中的情感。"
              "参考答案： 【小题1】B "
              "【小题2】这句诗通过细腻的笔触描绘出一幅清新优美的山水画，反映出诗人对梓州自然风光的留恋与赞美。同时，通过“一夜雨”和“百重泉”的生动描绘，表现了诗人对李使君赴任之地风土人情的喜爱，"
              "以及对李使君能够治理好当地的期望与良好祝愿。")

    sentence = re.findall(r"A.(.*?)B.(.*?)C.(.*?)D.(.*?)。", output)[0]
    A = sentence[0]
    B = sentence[1]
    C = sentence[2]
    D = sentence[3]
    question = re.findall(r"【小题2】(.*)参考答案", output)[0]

    with open("Doc/古诗词题目.txt", "w", encoding="utf-8") as file:
        file.write(A + '\n')
        file.write(B + '\n')
        file.write(C + '\n')
        file.write(D + '\n')
        file.write(question)

    # 命制默写题
    prompt = ("请设计三道高中语文古诗文理解性默写题，每道题需要通过提供该句子的赏析或解释来作为提示。确保题目覆盖不同的诗文主题，"
              "并且提示内容具有启发性和创造性，以帮助学生深入理解诗句。严禁直接给出答案，而是通过赏析和解释的方式提供默写提示。"
              "这是一个例子：1.在《劝学》中，“________________，________________”两句强调了整天空想不如片刻学习收获大的道理。")
    # output = model.inout(prompt, 512)

    # 测试输出
    output = ("1. 在《离骚》中，“________________，________________”两句通过描绘自然景象，表达了诗人追求真理的坚定决心和不懈努力。"+'\n'
              "2. 在《登高》中，“________________，________________”两句通过描绘山水的壮丽，反映了诗人对国家命运的关切和对人民疾苦的同情。"+'\n'
              "3. 在《赋得古原草送别》中，“________________，________________”两句以简洁的语言描绘了离别时的情感，表达了诗人对友人的深深思念和不舍之情。"+'\n')
    with open("Doc/名言名句默写.txt", "w", encoding="utf-8") as file:
        file.write(output)

    # 命制语言文字运用I
    prompt = ("编写一份高中语文试题，内容如下："

              "  1. 请提供一篇约300字的抒情文章，该文章必须至少包含三个成语。"
              " 2. 根据提供的文章内容，设计三道题目。在第一题中，从文章中挑选出三个成语，然后留出空格，要求学生根据上下文填入这些成语。"
              " 3. 在第二题中，从文章中挑选出一个包含语病或不通顺的句子，让学生进行修改，注意保持原句意思和语境的准确性。"
              "  4. 在第三题中，挑选出文章中一个你认为优美的句子，让学生赏析这个句子，注意分析其语言特色、含义和在文章中的作用。"

              " 请确保试题设计得既考察学生的理解能力，又能够激发他们的创造力和审美情趣。")
    # output = model.inout(prompt, 2048)

    # 测试输出
    output = ("一、文章内容（请学生阅读下列文章，并回答后面的问题）"
              "遥想当年，风华正茂，我们曾满怀激情，勇往直前。岁月如梦，匆匆而过，那些曾经的日子，犹如过眼云烟。如今，我们感叹时光荏苒，青春不再，但心中那份执着仍然熠熠生辉。"
              "在这个充满挑战和机遇的时代，我们更应该奋发向前，勇攀高峰。无论前路如何坎坷，我们都不能放弃信念和希望。正如古语所说：“穷且益坚，不坠青云之志。”我们要时刻保持清醒的头脑，勇敢地面对生活的风风雨雨。"
              "有时候，我们也会感到迷茫和彷徨，仿佛迷失在人生的十字路口。但请不要忘记，阳光总在风雨后，我们要相信自己，坚定地走自己的路。正如成语所说：“殊途同归”，只要我们心中有梦想，终会找到属于自己的方向。"
              "二、题目设计"
              "1. 根据文章内容，请将下列成语填入空格中："
              "（1）风华正茂"
              "（2）过眼云烟"
              "（3）穷且益坚"
              "2. 修改文章中的一个句子："
              "原句：我们感叹时光荏苒，青春不再，但心中那份执着仍然熠熠生辉。"
              "修改后：_____________________________________________________________"
              "3. 赏析文章中的一个句子："
              "原句：有时候，我们也会感到迷茫和彷徨，仿佛迷失在人生的十字路口。"
              "赏析：_____________________________________________________________"
              "请同学们认真思考，充分发挥自己的理解和审美能力，完成以上题目。"
              )

    # 输出处理
    # 输出处理
    output = output.split("二、")
    material = output[0].split('一、文章内容（请学生阅读下列文章，并回答后面的问题）')[1]

    question = output[1]
    print(question)
    question1 = question.split('2.')[0]
    question1 = question1.split("1. 根据文章内容，请将下列成语填入空格中：")[1]
    c1 = re.findall(r"（1）(.*)（2）", question1)[0]
    c2 = re.findall(r"（2）(.*)（3）", question1)[0]
    c3 = re.findall(r"（3）(.*)", question1)[0]
    material = material.replace(c1, "______", 1)
    material = material.replace(c2, "______", 1)
    material = material.replace(c3, "______", 1)
    question2 = question.split("原句：")[1]
    question2 = question2.split("修改后")[0]
    print(question2)
    question3 = question.split("3. 赏析文章中的一个句子：")[1]
    question3 = question3.split("原句：")[1].split("赏析")[0]
    print(question3)

    # 输出到文件
    with open("Doc/语言文字运用I.txt", "w", encoding='utf-8') as file:
        file.write(material)
    with open("Doc/语言文字运用I题目", 'w', encoding='utf-8') as file:
        file.write("请修改以下病句：" + question2 + '\n')
        file.write("请赏析下面的句子：" + question3 + '\n')

    # 命制语言文字运用II
    prompt = (
        "编写一份高中语文试题，内容如下："
        "1. 请提供一篇约300字的抒情文章。"
        "2. 根据提供的文章内容，设计两道题目。在第一题中，在文章中挖空3个整句，注意一个逗号算一个证据，让学生们根据上下文的连贯性补全这3个句子。"
        "3. 在第二题中，从文章中挑选出两个富有深意的词语，让学生解释这些词语的表层含义和深层含义。"
        "请确保试题设计得既考察学生的理解能力，又能够激发他们的创造力和审美情趣。"
        "请注意以下几点："
        "- 文章内容必须保持抒情性质，适合高中生的情感和审美水平。"
        "- 第一题中，要设计一个学生根据文章上下文连贯性进行填空的活动，可以考察学生对文章主题的理解和记忆。"
        "- 第二题中，要设计一个涉及文章主题和情感的词语解释活动，可以考察学生对词语内涵的理解和分析能力。"
        "- 请避免设计任何可能产生误解或安全问题的内容，确保试题的设计是完全无害的。")

    # output = model.inout(prompt, 2048)
    # 测试输出
    output = ("一、文章《青春颂》"
              "青春，如同清晨的阳光，温暖而耀眼；青春，似那奔腾的江河，激情澎湃。站在青春的门槛上，我们怀揣着梦想，勇往直前。"
              "青春的天空，淡淡的蓝，镶嵌着洁白的云朵。我们在这样的天空下，笑声洒满每个角落。青春的我们应该拥有坚定的信念，不畏困难，砥砺前行。那些无数个日夜里，我们一起奋斗过的痕迹，成为了我们最宝贵的财富。"
              "青春的我们，拥有无尽的活力，仿佛是一个个跳跃的音符，奏响生命中最美的旋律。我们在阳光下奔跑，感受风的拥抱，倾听心的声音。这美好的青春时光，让我们用心去感受，去珍惜。"
              "二、题目设计"
              "根据文章内容，补全下列句子。（每空2分，共6分）"
              "（1）青春，如同清晨的阳光，温暖而耀眼；青春，_______，激情澎湃。"
              "（2）青春的天空，淡淡的蓝，镶嵌着洁白的云朵。我们在这样的天空下，_______。"
              "（3）青春的我们，拥有无尽的活力，仿佛是一个个跳跃的音符，_______。"
              "解释下列词语的表层含义和深层含义。（每词2分，共4分）"
              "（1）早晨的阳光：，。"
              "（2）砥砺前行：，。")

    # 输出处理
    material = re.findall(r"一、文章《(.*)》(.*)二、", output)
    material = material[0][1]
    question = re.findall(r"二、题目设计(.*)", output)
    sentence = \
        re.findall(r"（1）(.*)（2）(.*)（3）(.*)解释下列词语的表层含义和深层含义。（每词2分，共4分）(.*)（1）(.*)（2）(.*)", output)[
            0]
    s1 = sentence[0]
    s2 = sentence[1]
    s3 = sentence[2]
    c1 = sentence[4]
    c2 = sentence[5]

    with open("Doc/语言文字应用II.txt", "w", encoding="utf-8") as file:
        file.write(material)
    with open("Doc/语言文字应用II题目.txt", "w", encoding="utf-8") as file:
        file.write("请根据上下文补全句子：" + s1 + s2 + s3 + '\n')
        file.write("请解释下面词语的表层含义和深层含义：（1）" + c1 + "（2）" + c2 + '\n')

    # 命制作文题
    prompt = ("请提供两句内容上相关联的名言，你只需要给出名言本身和他们的作者即可")
    # output = str(model.inout(prompt, 128))

    # 测试输出
    output = ("1.\"教育不是灌输，而是点燃火焰。\" - 威廉·巴特勒·叶芝"
              "2.\"真正的教育是激发人的潜能，培养人的兴趣。\" - 爱因斯坦")
    output = re.findall(r"1.(.*)-(.*)2.(.*)-(.*)", output)[0]
    print(output)
    # 处理文本
    # output = output.split('2.')

    saying1 = output[0]
    person1 = output[1]
    saying2 = output[2]
    person2 = output[3]
    with open("Doc/写作.txt",'w') as file:
        file.write(saying1 + '\n')
        file.write(person1 + '\n')
        file.write(saying2 + '\n')
        file.write(person2 + '\n')
