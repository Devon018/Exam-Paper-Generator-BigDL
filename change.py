from jinja2 import Template
import subprocess
import os


def template(self):
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
           foot-content    = {语文试题第;页（共~;页）}
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
       本试卷共 10 页，23 题。全卷满分 150 分。考试用时 150 分钟。


       \begin{notice}
         \item 答题前，先将自己的姓名、准考证号、考场号、座位号填写在试卷和答题卡上，
           并将准考证号条形码粘贴在答题卡上的指定位置。
         \item 选择题的作答：每小题选出答案后，用 2B 铅笔把答题卡上对应题目的答案标号涂黑。
           写在试卷、草稿纸和答题卡上的非答题区域均无效。
         \item 填空题和解答题的作答：用黑色签字笔直接答在答题卡上对应的答题区域内。
           写在试卷、草稿纸和答题卡上的非答题区域均无效。
         \item 考试结束后，请将本试卷和答题卡一并上交。
       \end{notice}



       \section{现代文阅读（35 分）}[source={{{sourceScienceReading1}}}]

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

       materials21
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

       \begin{material}[source = {{{sourceAncientReading1}}}]

         {{materials31}}

       \end{material}


       \begin{question}
         {{question101}}
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


       \begin{poem}[author = {{authorPoem1}}, title = {{{titlePoem1}}}]
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
         {{sentence11}}\\\\
         {{sentence21}}
       \end{material}

       以上论述具有启示意义。请结合材料写一篇文章，体现你的感悟与思考。

       要求：选准角度，确定立意，明确文体，自拟标题；不要套作，不得抄袭；不得泄露个人信息：不少于 800 字。

       \end{document}
       ''')

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
                                              sourceScienceReading1=sourceScienceReading,
                                              titleNovelReading1=titleNovelReading,
                                              authorNovelReading1=authorNovelReading
                                              )

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
    command = [os.path.join('C:\\texlive\\2023\\bin\\windows', 'xelatex.exe'), tex_file]

    # 执行命令，并将标准输出和标准错误输出捕获到管道中
    try:
        # 使用subprocess.run运行命令
        compilation_result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)

        # 输出命令执行的结果
        print("Success!")

    except subprocess.CalledProcessError as e:
        # 如果命令执行失败，则打印错误信息
        print(f"Error compiling {filename}:")
        print(e.stderr.decode())
