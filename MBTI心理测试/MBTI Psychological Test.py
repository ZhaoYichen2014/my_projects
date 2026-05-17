import pygame
import openpyxl
import sys
import time
import datetime
from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.commons.utils import JsCode
file_path=input("请输入“MBTI心理测试问卷试题.xlsx”文件地址:")
wb=openpyxl.load_workbook(file_path)
ws=wb["Sheet1"]
factor_E=0
factor_S=0
factor_T=0
factor_J=0
factor_I=0
factor_N=0
factor_F=0
factor_P=0
question_number=0
skip_count=0

print("题目正在加载中，请稍等一下。")
print("在答题时，按下“A”键选A，按下“B”键选B，如果按下没有反应，请按一下“shift”")
MBTI_questionnaire=[]
for questionnaire in ws.iter_rows(min_row=2,values_only=True):
    questionnaires=[]
    questionnaire=list(questionnaire)
    question=str(questionnaire[0])+"."+questionnaire[1]
    answer1="A:"+questionnaire[2]
    answer2 = "B:" + questionnaire[3]
    factor=questionnaire[4].split("/")
    factor1=factor[0]
    factor2=factor[1]
    factor1=factor1.strip()
    factor2=factor2.strip()
    questionnaires.append(question)
    questionnaires.append(answer1)
    questionnaires.append(answer2)
    questionnaires.append(factor1)
    questionnaires.append(factor2)
    MBTI_questionnaire.append(questionnaires)

pygame.init()
pygame.display.set_caption("MBTI心理测试")
font_path = "C:\Windows\Fonts\msyh.ttc"
myfont1 = pygame.font.Font(font_path, 30)
myfont2 = pygame.font.Font(font_path, 20)
win=pygame.display.set_mode((1300,700))
print("请打开pygame弹窗开始答题")
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                if MBTI_questionnaire[question_number][3] == 'E':
                    factor_E+=1
                elif MBTI_questionnaire[question_number][3] =='I':
                    factor_I+=1
                elif MBTI_questionnaire[question_number][3] =='S':
                    factor_S+= 1
                elif MBTI_questionnaire[question_number][3] =='N':
                    factor_N+=1
                elif MBTI_questionnaire[question_number][3] =='T':
                    factor_T+=1
                elif MBTI_questionnaire[question_number][3] =='F':
                    factor_F+=1
                elif MBTI_questionnaire[question_number][3] =='J':
                    factor_J+=1
                elif MBTI_questionnaire[question_number][3] =='P':
                    factor_P+=1
                question_number += 1
            elif event.key == pygame.K_b:
                if MBTI_questionnaire[question_number][4] == 'E':
                    factor_E+=1
                elif MBTI_questionnaire[question_number][4] =='I':
                    factor_I+=1
                elif MBTI_questionnaire[question_number][4] =='S':
                    factor_S+= 1
                elif MBTI_questionnaire[question_number][4] =='N':
                    factor_N+=1
                elif MBTI_questionnaire[question_number][4] =='T':
                    factor_T+=1
                elif MBTI_questionnaire[question_number][4] =='F':
                    factor_F+=1
                elif MBTI_questionnaire[question_number][4] =='J':
                    factor_J+=1
                elif MBTI_questionnaire[question_number][4] =='P':
                    factor_P+=1
                question_number += 1
            elif event.key == pygame.K_SPACE:
                skip_count+=1
                if skip_count >13:
                    time.sleep(1)
                else:
                    question_number += 1

    win.fill((253, 246, 227))
    if question_number <= 92 :
        ordinal_number = myfont2.render("第{}题/共93题".format(question_number+1), True, (0, 0, 0))
        guide_text=myfont2.render("本心理问卷由权威网站和大模型提供，分析结果仅供参考。",True,(0,0,0))
        hint_text_one=myfont2.render("在答题时，请给出你认为正确的答案，在键盘上打出正确答案的选项",True,(0,0,0))
        hint_text_two=myfont2.render("如果无法解答题目，可按下空格键跳过，最多可跳过13次",True,(0, 0, 0))
        quansw_text= myfont1.render(MBTI_questionnaire[question_number][0], True, (0, 0, 0))
        answer_text_one=myfont1.render(MBTI_questionnaire[question_number][1], True, (0, 0, 0))
        answer_text_two=myfont1.render(MBTI_questionnaire[question_number][2], True, (0, 0, 0))
        win.blit(quansw_text,(70,50))
        win.blit(answer_text_one, (90, 120))
        win.blit(answer_text_two, (90, 170))
        win.blit(hint_text_one,(293,640))
        win.blit(guide_text, (340, 600))
        win.blit(hint_text_two, (340, 560))
        win.blit(ordinal_number, (560, 20))
    else:
        break
    pygame.display.update()

current_time = datetime.datetime.now()
safe_time = current_time.strftime("%Y-%m-%d_%H-%M-%S")
print("正在计算...")
test_report_str=""
test_report_list=[]
if factor_E > factor_I:
    test_report_list.append("外向")
    test_report_str = test_report_str + "E"
elif factor_E < factor_I:
    test_report_list.append("内向")
    test_report_str = test_report_str + "I"
else:
    test_report_list.append("内向")
    test_report_str = test_report_str + "I"
if factor_S > factor_N:
    test_report_list.append("实感")
    test_report_str = test_report_str + "S"
elif factor_S < factor_N:
    test_report_list.append("直觉")
    test_report_str = test_report_str + "N"
else:
    test_report_list.append("直觉")
    test_report_str = test_report_str + "N"
if factor_T > factor_F:
    test_report_list.append("思维")
    test_report_str = test_report_str + "T"
elif factor_T < factor_F:
    test_report_list.append("情感")
    test_report_str = test_report_str + "F"
else:
    test_report_list.append("情感")
    test_report_str = test_report_str + "F"
if factor_J> factor_P:
    test_report_list.append("判断")
    test_report_str = test_report_str + "J"
elif factor_J < factor_P:
    test_report_list.append("知觉")
    test_report_str = test_report_str + "P"
else:
    test_report_list.append("知觉")
    test_report_str = test_report_str + "P"
if "ST" in test_report_str:
    MBTI_type="务实"
    if test_report_str == "ISTJ":
        MBTI_personality = "检查员"
    elif test_report_str == "ESTJ":
        MBTI_personality = "管理者"
    elif test_report_str == "ISTP":
        MBTI_personality = "工匠"
    elif test_report_str == "ESTP":
        MBTI_personality = "企业家"
if "SF" in test_report_str:
    MBTI_type="友善"
    if test_report_str == "ISFJ":
        MBTI_personality = "保护者"
    elif test_report_str == "ESFJ":
        MBTI_personality = "供给者"
    elif test_report_str == "ISFP":
        MBTI_personality = "艺术家"
    elif test_report_str == "ESFP":
        MBTI_personality = "表演者"
if "NF" in test_report_str:
    MBTI_type="理想主义"
    if test_report_str == "INFJ":
        MBTI_personality = "提倡者"
    elif test_report_str == "ENFJ":
        MBTI_personality = "教育家"
    elif test_report_str == "INFP":
        MBTI_personality = "调解员"
    elif test_report_str == "ENFP":
        MBTI_personality = "倡导者"
if "NT" in test_report_str:
    MBTI_type="理性"
    if test_report_str == "INTJ":
        MBTI_personality = "战略家"
    elif test_report_str == "ENTJ":
        MBTI_personality = "指挥官"
    elif test_report_str == "INTP":
        MBTI_personality = "思想家"
    elif test_report_str == "ENTP":
        MBTI_personality = "辩论家"

c = (
    Bar()
    .add_xaxis(["外向","内向","实感","直觉","思维","情感","判断","知觉"])
    .add_yaxis("各个维度值", [factor_E,factor_I,factor_S,factor_N,factor_T,factor_N,factor_J,factor_P], category_gap="60%")
    .set_series_opts(
        itemstyle_opts={
            "normal": {
                "color": JsCode(
                    """new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                offset: 0,
                color: 'rgba(0, 244, 255, 1)'
            }, {
                offset: 1,
                color: 'rgba(0, 77, 167, 1)'
            }], false)"""
                ),
                "barBorderRadius": [30, 30, 30, 30],
                "shadowColor": "rgb(0, 160, 221)",
            }
        }
    )
    .set_global_opts(title_opts=opts.TitleOpts(title="您的MBTI心理测试结果", subtitle="您是一名{}的{}".format(MBTI_type,MBTI_personality)))
    .render("{}进行的MBTI心理测试结果.html".format(safe_time))
)

print("计算完成")
print("您是一个{}、{}、{}、{}的人".format(test_report_list[0],test_report_list[1],test_report_list[2],test_report_list[3]))
print("您是一名{}的{}".format(MBTI_type,MBTI_personality))
print("请在存放该文件的文件夹中找到“{}进行的MBTI心理测试结果.html”并用浏览器运行".format(safe_time))
