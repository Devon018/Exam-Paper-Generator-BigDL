from jinja2 import Template
import subprocess
import os


def template():
    # 定义 LaTeX 模板
    latex_template = Template(r'''
       \let\stop\empty
       \documentclass[zihao = -4]{exam-zh}
       % !TeX root = ./exam-zh-chinese.tex

       \usepackage{graphicx}


       \examsetup{
         page = {
           size            = a3paper,
           show-columnline = false,
           foot-content    = {语文试题第;页（共8页）}
         },
         font = times,
         fillin/no-answer-type = none,
         sealline = {
           show        = true,
           scope       = mod-2,
           circle-show = false,
           line-type   = solid,
           odd-info-content = {
             {\heiti \zihao{4}姓名} {\underline{\hspace*{8em}}},
             {\heiti \zihao{4}准考证号} {\examsquare{9}},
             {\heiti \zihao{4}考场号} {\examsquare{2}},
             {\heiti \zihao{4}座位号} {\examsquare{2}},
           },
           odd-info-xshift = 12mm,
           text = {此卷只装订不密封},
           text-width  = 0.98\textheight,
           text-format = \zihao{-3}\sffamily,
           text-xshift = 20mm
         },
         square = {
           x-length = 1.8em,
           y-length = 1.6em
         },
         select = {
           pre-content  = {},
           post-content = {},
           separator    = \qquad
         }
       }


       \ctexset{
         subsection = {
           number     = \chinese{subsection},
           name       = {（,）},
           aftername  = {},
           format     = \bfseries,
           indent     = 2\ccwd,
           beforeskip = .25\baselineskip,
           afterskip  = .25\baselineskip
         },
         subsubsection = {
           numbering  = false,
           indent     = 2\ccwd,
           format     = \sffamily\bfseries,
           beforeskip = .25\baselineskip,
           afterskip  = .25\baselineskip
         }
       }


       \xeCJKsetup{
         underdot = {
           depth  = 0.4em,
           format = \large,
           boxdepth = 0pt
         },
         underline = {
           thickness = 0.8pt
         }
       }

       \setlist[enumerate, 2]{
         left       = 0pt,
         labelsep   = 0pt,
         label      = {（\arabic *）}
       }


       \title{2024年普通高等学校招生考试统一模拟演练}

       \subject[3.5em]{语文}

       \AtEndPreamble{
         \geometry{
           % showframe
           margin  = 0.9in,
           inner   = 1.25in,
           outer   = 1.2in,
         }
       }


       \begin{document}

       \secret

       \maketitle
       本试卷共 8 页，23 题。全卷满分 150 分。考试用时 150 分钟。


       \begin{notice}
         \item 答题前，先将自己的姓名、准考证号、考场号、座位号填写在试卷和答题卡上，
           并将准考证号条形码粘贴在答题卡上的指定位置。
         \item 选择题的作答：每小题选出答案后，用 2B 铅笔把答题卡上对应题目的答案标号涂黑。
           写在试卷、草稿纸和答题卡上的非答题区域均无效。
         \item 填空题和解答题的作答：用黑色签字笔直接答在答题卡上对应的答题区域内。
           写在试卷、草稿纸和答题卡上的非答题区域均无效。
         \item 考试结束后，请将本试卷和答题卡一并上交。
       \end{notice}



       \section{现代文阅读（35 分）}

       \subsection{现代文阅读 I（本题共 5 小题，19分）}

       阅读下面的文字，完成1～5题。

       \begin{material}
       {{materials11}}
       \end{material}


       \begin{question}
         {{question11}}
         \begin{choices}
           \item {{Q1A1}}
           \item {{Q1B1}}
           \item {{Q1C1}}
           \item {{Q1D1}}
         \end{choices}
       \end{question}

       \begin{question}
         {{question21}}
         \begin{choices}
           \item {{Q2A1}}
           \item {{Q2B1}}
           \item {{Q2C1}}
           \item {{Q2D1}}
         \end{choices}
       \end{question}

       \begin{question}
         {{question31}}
         \begin{choices}
           \item {{Q3A1}}
           \item {{Q3B1}}
           \item  {{Q3C1}}
           \item {{Q3D1}}
         \end{choices}
       \end{question}

       \begin{question}
         {{question41}}
       \end{question}

       \begin{question}
         {{question51}}
       \end{question}


       \subsection{现代文阅读 II（本题共4小题，16分）}

       阅读下面的文字，完成6～9题。


       \begin{material}[
         title = {{titleNovelReading1}}, author = {{authorNovelReading1}},
       ]

       {{materials21}}
       \end{material}


       \begin{question}
         {{question61}}
         \begin{choices}
           \item {{Q6A1}}
           \item {{Q6B1}}
           \item {{Q6C1}}
           \item {{Q6D1}}
         \end{choices}
       \end{question}

       \begin{question}
         {{question71}}
         \begin{choices}
           \item {{Q7A1}}
           \item {{Q7B1}}
           \item {{Q7C1}}
           \item {{Q7D1}}  
         \end{choices}
       \end{question}

       \begin{question}
         {{question81}}
       \end{question}

       \begin{question}
         {{question91}}
       \end{question}



       \section{古代诗文阅读（35 分）}

       \subsection{文言文阅读（本题共 5 小题，20 分）}

       阅读下面的文言文，完成10～14题。

       \begin{material}[source = {{sourceAncientReading1}}]

         {{materials31}}

       \end{material}


       \begin{question}
         {{question101}}
        {{duanju}}
       \end{question}

       \begin{question}
         {{question111}}
         \begin{choices}
           \item {{Q11A1}}
           \item {{Q11B1}}
           \item {{Q11C1}}
           \item {{Q11D1}}  
         \end{choices}
       \end{question}

       \begin{question}
         {{question121}}
         \begin{choices}
           \item {{Q12A1}}
           \item {{Q12B1}}
           \item {{Q12C1}}
           \item  {{Q12D1}}
         \end{choices}
       \end{question}

       \begin{question}
         {{question131}}
         \begin{enumerate}
           \item {{translation11}}
           \item {{translation21}}
         \end{enumerate}
       \end{question}

       \begin{question}
         {{question141}}
       \end{question}


       \subsection{古代诗歌阅读（本题共 2 小题，9 分）}

       阅读下面这首唐诗，完成 15～16 题。


       \begin{poem}[author = {{authorPoem1}}, title = {{titlePoem1}}]
         {{materials41}}
       \end{poem}

       \begin{question}
         {{question151}}
         \begin{choices}
           \item {{Q15A1}}
           \item {{Q15B1}}
           \item  {{Q15C1}}
           \item {{Q15D1}}
         \end{choices}
       \end{question}

       \begin{question}
         {{question161}}
       \end{question}


       \subsection{名篇名句默写（本题共 1 小题，6 分）}

       \begin{question}
         补写出下列句子中的空缺部分。（6分）
         \begin{enumerate}
           \item {{writing11}}
           \item {{writing21}}
           \item {{writing31}}
         \end{enumerate}
       \end{question}



       \section{语言文字运用（20 分）}

       \subsection{语言文字运用 I（本题共 3 小题，11 分）}

       阅读下面的文字，完成18～20题。

       \begin{material}
        {{materials51}}
       \end{material}

       \begin{question}
       {{question181}}
       \end{question}

       \begin{question}
         {{question191}}
       \end{question}

       \begin{question}
         {{question201}}
       \end{question}


       \subsection{语言文字运用 II（本题共 2 小题，9 分）}

       \examsetup{
         fillin = {
           no-answer-type = counter,
           no-answer-counter-label = \circlednumber*
         }
       }

       阅读下面的文字，完成21～22题。

       \begin{material}
         {{materials61}}
       \end{material}

       \begin{question}
         {{question211}}
       \end{question}


       \begin{question}
         {{question221}}
       \end{question}



       \section{写作（60 分）}

       \begin{question}
         阅读下面的材料，根据要求写作。（60分）
       \end{question}

       \begin{material}
         {{sentence11}}
         {{sentence21}}
       \end{material}

       以上论述具有启示意义。请结合材料写一篇文章，体现你的感悟与思考。

       要求：选准角度，确定立意，明确文体，自拟标题；不要套作，不得抄袭；不得泄露个人信息：不少于 800 字。

       \end{document}
       ''')
    print("1")
    # 读取文本与题目
    with open('Doc/现代文阅读I.txt', 'r', encoding="utf-8") as f1:
        source1 = f1.readline()
        # author1 = f1.readline()
        materials1 = f1.readline() + '\\\\'
        temp = f1.readline()
        while temp:
            if materials1 == '\\\\':
                break
            materials1 = materials1 + str(temp) + '\\\\'
            temp = f1.readline()
    sourceScienceReading = "（摘编自" + "《" + source1 + "》）"
    print("2")
    with open('Doc/现代文阅读II.txt', 'r', encoding="utf-8") as f2:
        titleNovelReading = f2.readline()
        authorNovelReading = f2.readline()
        materials2 = f2.readline() + '\\\\'
        temp = f2.readline()
        while temp:
            if materials2 == '\\\\':
                break
            materials2 = materials2 + str(temp) + '\\\\'
            temp = f2.readline()
    print("3")
    with open('Doc/现代文阅读I题目.txt', 'r', encoding="utf-8") as f3:
        question1 = "下列对材料相关内容的理解和分析，不正确的一项是（3分）"
        question2 = "下列对材料相关内容的理解和分析，不正确的一项是（3分）"
        question3 = "根据材料内容，下列说法正确的一项是（3分）"
        Q1A = f3.readline()
        Q1B = f3.readline()
        Q1C = f3.readline()
        Q1D = f3.readline()
        Q2A = f3.readline()
        Q2B = f3.readline()
        Q2C = f3.readline()
        Q2D = f3.readline()
        Q3A = f3.readline()
        Q3B = f3.readline()
        Q3C = f3.readline()
        Q3D = f3.readline()
        question4 = f3.readline() + "(4分)"
        question5 = f3.readline() + "(6分)"
        answer1 = f3.readline()
        answer2 = f3.readline()
        answer3 = f3.readline()
        answer4 = f3.readline()
        answer5 = f3.readline()
    print("5")
    with open("Doc/现代文阅读II题目.txt", 'r', encoding="utf-8") as f4:
        question6 = "下列对小说相关内容的理解，正确的一项是（3 分）"
        question7 = "下列对小说艺术特色的分析鉴赏，不正确的一项是（3 分）"
        Q6A = f4.readline()
        Q6B = f4.readline()
        Q6C = f4.readline()
        Q6D = f4.readline()
        Q7A = f4.readline()
        Q7B = f4.readline()
        Q7C = f4.readline()
        Q7D = f4.readline()
        question8 = f4.readline() + "(4分)"
        question9 = f4.readline() + "(6分)"
        answer6 = f4.readline()
        answer7 = f4.readline()
        answer8 = f4.readline()
        answer9 = f4.readline()
    print("5")
    with open("Doc/文言文阅读.txt", 'r', encoding="utf-8") as f5:
        sourceAncientReading = "(节选自《" + f5.readline() + "》)"
        materials3 = f5.readline() + '\\\\'
        temp = f5.readline()
        while temp:
            if materials3 == '\\\\':
                break
            materials3 = materials3 + str(temp) + '\\\\'
            temp = f5.readline()
    print("6")
    with open("Doc/文言文题目.txt", 'r', encoding="utf-8") as f6:
        question10 = "以下句子有三处需要断句，请用铅笔将答题卡上相应位置的答案标号涂黑"+'\\\\'
        question11 = "下列对文中加点词语的相关内容的解说，不正确的一项是（3 分）"
        question12 = "下列对原文有关内容的概述，不正确的一项是（3 分）"
        duanju = f6.readline()
        Q11A = f6.readline()
        Q11B = f6.readline()
        Q11C = f6.readline()
        Q11D = f6.readline()
        Q12A = f6.readline()
        Q12B = f6.readline()
        Q12C = f6.readline()
        Q12D = f6.readline()
        question13 = "把文中画横线的句子翻译成现代汉语。（8 分）"
        translation1 = f6.readline()
        translation2 = f6.readline()
        question14 = f6.readline() + "(3分)"
        answer11 = f6.readline()
        answer12 = f6.readline()
        answer13_1 = f6.readline()
        answer13_2 = f6.readline()
        answer14 = f6.readline()
    print("7")
    with open("Doc/古诗文.txt", 'r', encoding="utf-8") as f7:
        titlePoem = f7.readline()
        authorPoem = f7.readline()
        materials4_1 = f7.readline()
        temp = f7.readline()
        while temp:
            if not materials4_1:
                break
            materials4_1 = materials4_1 + str(temp)
            temp = f7.readline()
        a_0 = materials4_1.split('。')
        materials4 = a_0[0] + "。\\\\"
        for i in range(1, len(a_0)-1):
            materials4 = materials4 + '\n' + a_0[i] + "。\\\\"
    print("8")
    with open("Doc/古诗词题目.txt", 'r', encoding="utf-8") as f8:
        question15 = "下列对这首诗的理解和赏析，不正确的一项是（3 分）"
        Q15A = f8.readline()
        Q15B = f8.readline()
        Q15C = f8.readline()
        Q15D = f8.readline()
        question16 = f8.readline() + "(6分)"
    print(9)
    with open("Doc/名言名句默写.txt", 'r', encoding="utf-8") as f9:
        question17 = "补写出下列句子中的空缺部分。（6 分）"
        writing1 = f9.readline()
        writing1 = writing1.replace('“________________，________________”','“\\fillin[width = 5em][]”')
        writing2 = f9.readline()
        writing2 = writing2.replace('“________________，________________”','“\\fillin[width = 5em][]”')
        writing3 = f9.readline()
        writing3 = writing3.replace('“________________，________________”','“\\fillin[width = 5em][]”')
    print("10")
    with open("Doc/语言文字运用I.txt", 'r', encoding="utf-8") as f10:
        materials5 = f10.readline() + '\\\\'
        temp = f10.readline()
        while temp:
            if materials5 == '\\\\':
                break
            materials5 = materials5 + str(temp) + '\\\\'
            temp = f10.readline()
        materials5 = materials5.replace('______', '\\underline{\\hspace*{3.5em}}')
    print("11")
    with open("Doc/语言文字运用I题目", 'r', encoding="utf-8") as f11:
        question18 = "请在文中横线处填入适当的成语"
        question19 = f11.readline()
        question20 = f11.readline()
    print("11")
    with open("Doc/语言文字应用II.txt", 'r', encoding="utf-8") as f12:
        materials6 = f12.readline() + '\\\\'
        temp = f12.readline()
        while temp:
            if materials6 == '\\\\':
                break
            materials6 = materials6 + str(temp) + '\\\\'
            temp = f12.readline()
        materials6 = materials6.replace('_______', "\\fillin")
    print("11")
    with open("Doc/语言文字应用II题目.txt", 'r', encoding="utf-8") as f13:
        question21 = f13.readline().replace('_______', "\\fillin")
        question22 = f13.readline().replace('_______', "\\fillin")
    print("11")
    with open("Doc/写作.txt", 'r') as f14:
        saying1 = f14.readline()
        person1 = f14.readline()
        saying2 = f14.readline()
        person2 = f14.readline()
        sentence1 = str(saying1) + '----' + str(person1) + '\\\\'
        sentence2 = str(saying2) + '----' + str(person2) + '\\\\'
    # print(sentence1)
    # print(sentence2)

    print("开始渲染")
    # 渲染模板
    rendered_template = latex_template.render(materials11=materials1,
                                              materials21=materials2,
                                              materials31=materials3,
                                              materials41=materials4,
                                              materials51=materials5,
                                              materials61=materials6,
                                              question11=question1,
                                              question21=question2,
                                              question31=question3,
                                              question41=question4,
                                              question51=question5,
                                              question61=question6,
                                              question71=question7,
                                              question81=question8,
                                              question91=question9,
                                              question101=question10,
                                              question111=question11,
                                              question121=question12,
                                              question131=question13,
                                              question141=question14,
                                              question151=question15,
                                              question161=question16,
                                              question171=question17,
                                              question181=question18,
                                              question191=question19,
                                              question201=question20,
                                              question211=question21,
                                              question221=question22,
                                              Q1A1=Q1A,
                                              Q1B1=Q1B,
                                              Q1C1=Q1C,
                                              Q1D1=Q1D,
                                              Q2A1=Q2A,
                                              Q2B1=Q2B,
                                              Q2C1=Q2C,
                                              Q2D1=Q2D,
                                              Q3A1=Q3A,
                                              Q3B1=Q3B,
                                              Q3C1=Q3C,
                                              Q3D1=Q3D,
                                              Q6A1=Q6A,
                                              Q6B1=Q6B,
                                              Q6C1=Q6C,
                                              Q6D1=Q6D,
                                              Q7A1=Q7A,
                                              Q7B1=Q7B,
                                              Q7C1=Q7C,
                                              Q7D1=Q7D,
                                              Q11A1=Q11A,
                                              Q11B1=Q11B,
                                              Q11C1=Q11C,
                                              Q11D1=Q11D,
                                              Q12A1=Q12A,
                                              Q12B1=Q12B,
                                              Q12C1=Q12C,
                                              Q12D1=Q12D,
                                              Q15A1=Q15A,
                                              Q15B1=Q15B,
                                              Q15C1=Q15C,
                                              Q15D1=Q15D,
                                              duanju=duanju,
                                              sentence11=sentence1,
                                              sentence21=sentence2,
                                              authorPoem1=authorPoem,
                                              titlePoem1=titlePoem,
                                              translation11=translation1,
                                              translation21=translation2,
                                              writing11=writing1,
                                              writing21=writing2,
                                              writing31=writing3,
                                              sourceAncientReading1=sourceAncientReading,
                                              titleNovelReading1=titleNovelReading,
                                              authorNovelReading1=authorNovelReading
                                              )
    # readtxt()
    print("读取完成")
    # 保存生成的 LaTeX 代码到文件
    with open('exam-zh-chinese.tex', 'w', encoding='utf-8') as f:
        f.write(rendered_template)


def compile_tex_to_pdf(tex_file):
    #
    # path = os.path.abspath(tex_file)
    # pdf_file = tex_file.replace('.tex', '.pdf')
    # cmd = ['pip','-v']
    # p = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    # print(p.communicate()[0])
    # print(f"Successfully converted {tex_file} to {pdf_file} using xelatex")
    # current_directory = os.getcwd()
    # 遍历当前目录下的所有文件
    print("开始转换")

    # 执行命令，并将标准输出和标准错误输出捕获到管道中
    try:
        # 使用subprocess.run运行命令
        print(tex_file)
        current_path = os.getcwd()
        os.chdir(tex_file)
        command = ['xelatex', current_path+"\\exam-zh-chinese.tex"]
        subprocess.call(command)

        # 输出命令执行的结果
        print("Success!")

    except subprocess.CalledProcessError as e:
        # 如果命令执行失败，则打印错误信息
        # print(f"Error compiling {filename}:")
        print(e.stderr.decode())

    print("转换完成")


def readtxt():
    with open('Doc/现代文阅读I.txt', 'r', encoding="utf-8") as f1:
        source1 = f1.readline()
        author1 = f1.readline()
        materials1 = f1.readline() + '\\\\'
        while materials1:
            materials1 = materials1 + str(f1.readline()) + '\\\\'
    sourceScienceReading = "（摘编自" + author1 + "《" + source1 + "》）"

    with open('Doc/现代文阅读II.txt', 'r', encoding="utf-8") as f2:
        titleNovelReading = f2.readline()
        authorNovelReading = f2.readline()
        materials2 = f2.readline() + '\\\\'
        while materials2:
            materials2 = materials2 + str(f2.readline()) + '\\\\'

    with open('Doc/现代文阅读I题目.txt', 'r', encoding="utf-8") as f3:
        question1 = "下列对材料相关内容的理解和分析，不正确的一项是（3分）"
        question2 = "下列对材料相关内容的理解和分析，不正确的一项是（3分）"
        question3 = "根据材料内容，下列说法正确的一项是（3分）"
        Q1A = f3.readline()
        Q1B = f3.readline()
        Q1C = f3.readline()
        Q1D = f3.readline()
        Q2A = f3.readline()
        Q2B = f3.readline()
        Q2C = f3.readline()
        Q2D = f3.readline()
        Q3A = f3.readline()
        Q3B = f3.readline()
        Q3C = f3.readline()
        Q3D = f3.readline()
        question4 = f3.readline() + "(4分)"
        question5 = f3.readline() + "(6分)"
        answer1 = f3.readline()
        answer2 = f3.readline()
        answer3 = f3.readline()
        answer4 = f3.readline()
        answer5 = f3.readline()

    with open("Doc/现代文阅读II题目.txt", 'r', encoding="utf-8") as f4:
        Q6A = f4.readline()
        Q6B = f4.readline()
        Q6C = f4.readline()
        Q6D = f4.readline()
        Q7A = f4.readline()
        Q7B = f4.readline()
        Q7C = f4.readline()
        Q7D = f4.readline()
        question8 = f4.readline() + "(4分)"
        question9 = f4.readline() + "(6分)"
        answer6 = f4.readline()
        answer7 = f4.readline()
        answer8 = f4.readline()
        answer9 = f4.readline()

    with open("Doc/文言文.txt", 'r', encoding="utf-8") as f5:
        sourceAncientReading = "(节选自《" + f5.readline() + "》)"
        materials3 = f5.readline() + '\\\\'
        while materials3:
            materials3 = materials3 + str(f5.readline()) + '\\\\'

    with open("Doc/文言文题目.txt", 'r', encoding="utf-8") as f6:
        question10 = f6.readline()
        question11 = "下列对文中加点词语的相关内容的解说，不正确的一项是（3 分）"
        question12 = "下列对原文有关内容的概述，不正确的一项是（3 分）"
        Q11A = f6.readline()
        Q11B = f6.readline()
        Q11C = f6.readline()
        Q11D = f6.readline()
        Q12A = f6.readline()
        Q12B = f6.readline()
        Q12C = f6.readline()
        Q12D = f6.readline()
        question13 = "把文中画横线的句子翻译成现代汉语。（8 分）"
        translation1 = f6.readline()
        translation2 = f6.readline()
        question14 = f6.readline() + "(3分)"
        answer11 = f6.readline()
        answer12 = f6.readline()
        answer13_1 = f6.readline()
        answer13_2 = f6.readline()
        answer14 = f6.readline()

    with open("Doc/古诗词.txt", 'r', encoding="utf-8") as f7:
        titlePoem = f7.readline()
        authorPoem = f7.readline()
        materials4_1 = f7.readline()
        while materials4_1:
            materials4_1 = materials4_1 + str(f7.readline())
        a_0 = materials4_1.split('。')
        materials4 = a_0[0] + "。\\\\"
        for i in range(1, len(a_0)):
            materials4 = materials4 + '\n' + a_0[i] + "。\\\\"

    with open("Doc/古诗词题目.txt", 'r', encoding="utf-8") as f8:
        question15 = "下列对这首诗的理解和赏析，不正确的一项是（3 分）"
        Q15A = f8.readline()
        Q15B = f8.readline()
        Q15C = f8.readline()
        Q15D = f8.readline()
        question16 = f8.readline() + "(6分)"

    with open("Doc/名言名句默写.txt", 'r', encoding="utf-8") as f9:
        writing1 = f9.readline()
        writing2 = f9.readline()
        writing3 = f9.readline()

    with open("Doc/语言文字运用I.txt", 'r', encoding="utf-8") as f10:
        materials5 = f10.readline() + '\\\\'
        while materials5:
            materials5 = materials5 + str(f10.readline()) + '\\\\'

    with open("Doc/语言文字运用I题目", 'r', encoding="utf-8") as f11:
        question18 = "请在文中横线处填入适当的成语"
        question19 = f11.readline()
        question20 = f11.readline()

    with open("Doc/语言文字运用II.txt", 'r', encoding="utf-8") as f12:
        materials6 = f12.readline() + '\\\\'
        while materials6:
            materials6 = materials6 + str(f12.readline()) + '\\\\'

    with open("Doc/语言文字运用II题目.txt", 'r', encoding="utf-8") as f13:
        question21 = f13.readline()
        question22 = f13.readline()

    with open("Doc/写作.txt", 'r', encoding="utf-8") as f14:
        saying1 = f14.readline()
        person1 = f14.readline()
        saying2 = f14.readline()
        person2 = f14.readline()
        sentence1 = '“' + str(saying1) + '”' + '----' + str(person1)
        sentence2 = '“' + str(saying2) + '”' + '----' + str(person2)
