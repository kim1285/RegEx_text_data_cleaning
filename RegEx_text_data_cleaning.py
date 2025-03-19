import re
import pyperclip as pypc
import os
print("Current working directory:", os.getcwd())

text = pypc.paste()

pattern_1 = r'(\n)(①|②|③|④|⑤|⑥|⑦|⑧|⑨|⑩)'
pattern_2 = r'(\n)@@(\d+)\.'
pattern_3 = r'(\n)@@(가.|나.|다.|라.|마.|바.|사.|아.|자.|차|.카.|타.|파.|하.)'
pattern_4 = r'(\n)(다만|만일|단|이 경우|특히|이때)'
pattern_5 = r'(\n)@@(다만|만일|단|이 경우|특히|이때)'
pattern_8 = r'(\n)\s+(\d+)\.'
pattern_9 = r'(\n)\s+(①|②|③|④|⑤|⑥|⑦|⑧|⑨|⑩)'
pattern_10 = r'(\s*)(다만|만일|단|이 경우|특히)'
pattern_11 = r'\s+(\d+\.)'
pattern_12 = r'(가.|나.|다.|라.|마.|바.|사.|아.|자.|차|.카.|타.|파.|하.)\r\n@@'
pattern_13 = r'(\r\n)\s+(가.|나.|다.|라.|마.|바.|사.|아.|자.|차|.카.|타.|파.|하.)'
pattern_6 = r'\r\n@@\s*(\(|\<|〈|\[)\s*(본조|본절|본장)?\s*?(전면개정|전문개정|제목개정|개정|신설|삭제|본조\s*신설)\s*(:\s*)?\d+\.\s*\d+\.\s*\d+\.?\s*(\)|\>|〉|\])'
pattern_6_1 = r'\s*(\(|\<|〈|\[)\s*(본조|본절|본장)?\s*?(전면개정|전문개정|제목개정|개정|신설|삭제|본조\s*신설)\s*(:\s*)?\d+\.\s*\d+\.\s*\d+\.?\s*(\)|\>|〉|\])'
pattern_14 = r'\r\n@@\s*(\(|\<|〈|\[)\s*(본조|본절|본장)?\s*?(전면개정|전문개정|제목개정|개정|신설|삭제|본조\s*신설)\s*(:\s*)?\d+\.\s*\d+\.\s*\d+\.\s*,\s*\d+\.\s*\d+\.\s*\d+\.?(\)|\>|〉|\])'
pattern_14_1 = r'\s*(\(|\<|〈|\[)\s*(본조|본절|본장)?\s*?(전면개정|전문개정|제목개정|개정|신설|삭제|본조\s*신설)\s*(:\s*)?\d+\.\s*\d+\.\s*\d+\.\s*,\s*\d+\.\s*\d+\.?\s*\d+\.?(\)|\>|〉|\])'
pattern_15 = r'(①|②|③|④|⑤|⑥|⑦|⑧|⑨|⑩)\s*(\(|\<|〈|\[)\s*(본조|본절|본장)?\s*?(전면개정|제목개정|개정|신설|삭제|본조\s*신설)\s*(:\s*)?\d+\.\s*\d+\.\s*\d+\.?\s*(\)|\>|〉|\])'
pattern_15_1 = r'\r\n@@(①|②|③|④|⑤|⑥|⑦|⑧|⑨|⑩)\s*(\(|\<|〈|\[)\s*(본조|본절|본장)?\s*?(전면개정|제목개정|개정|신설|삭제|본조\s*신설)\s*(:\s*)?\d+\.\s*\d+\.\s*\d+\.?\s*(\)|\>|〉|\])'
pattern_15_2 = r"(〈|<)\s*?(개정|신설|삭제)\s*?:\s*?(’|‘|'|`)\s*?\d+\s*?\.\s*?\d+\s*?\.\s*?\d+\s*?\.?\s*?(>|〉)"
# @@<개정 : `23. 09. 25.>
#제7조〈삭제 : ’22. 7. 19.〉
# <18.12.14. 개정>
pattern_16 = r'<\s*\d+\.\s*\d+\.\s*\d+\.\s*개정s*>'
# <’07.1.1 개정>
pattern_17 = r'<’\s*\d+\.\s*\d+\.\s*\d+\.?\s*(개정|신설)\s*>'
#       1)
pattern_18 = r'(\r\n)(\s+)(1\)|2\)|3\)|4\)|5\)|6\)|7\))'
#     (1)
pattern_19 = r'(\r\n)(\s+)(\(1\)|\(2\)|\(2\)|\(3\)|\(4\)|\(5\)|\(6\)|)'
# before **제~조~**, make one empty line.
pattern_20 = r'(\r\n)(\*\*제)'
# removes empty line in the beginning of document as an exception to pattern_20
pattern_21 = r'(###제 \d+ 절 .*\r\n)\r\n'
# 전문개정'19.12.16.
pattern_22 = r'전문개정\s*\'\d{2}\s*\.\s*\d{2}\s*\.\s*\d{2}\s*\.\s*?'


def replacement_function_1(match):
    return f'{match.group(1)}@@{match.group(2)}'


def replacement_function_2(match):
    return f'{match.group(1)}{match.group(2)}.'


def replacement_function_3(match):
    return f'{match.group(1)}{match.group(2)}'


def replacement_function_4(match):
    return f' {match.group(2)}'


def replacement_function_5(match):
    return f'{match.group(1)}{match.group(2)}.'


def replacement_function_6(match):
    return f'{match.group(1)}{match.group(2)}'


def replacement_function_7(match):
    return f'\r\n{match.group(1)}'


def replacement_function_8(match):
    return f'{match.group(1)}\r\n'


def replacement_function_9(match):
    return f'{match.group(1)}{match.group(2)}'


#       1)
# pattern_18 = r'(\r\n)(\s+)(1\)|2\)|3\)|4\)|5\)|6\)|7\))'
def replacement_function_10(match):
    return f'{match.group(1)}{match.group(3)}'


#     (1)
# pattern_19 = r'(\r\n)(\s+)(\(1\)|\(2\)|\(2\)|\(3\)|\(4\)|\(5\)|\(6\)|)'
def replacement_function_11(match):
    return f'{match.group(1)}{match.group(3)}'


# before **제~조~**, make one empty line.
# pattern_20 = r'(\r\n**제'
def replacement_function_12(match):
    return f'\r\n{match.group(1)}{match.group(2)}'


# removes empty line in the beginning of document as an exception to pattern_20
# pattern_21 = r'(###제 \d+ 절 .*\r\n)\r\n'
def replacement_function_13(match):
    return f'{match.group(1)}'


result = re.sub('###제 1 절 제목없음', '###제 1절 절 없음', text)
result = re.sub('@@##', '', result)
result = re.sub(pattern_6, '', result)
result = re.sub(pattern_6_1, '', result)
result = re.sub(pattern_14, '', result)
result = re.sub(pattern_14_1, '', result)
result = re.sub(pattern_15, '', result)
result = re.sub(pattern_15_1, '', result)
result = re.sub(pattern_1, replacement_function_1, result)
result = re.sub(pattern_2, replacement_function_2, result)
result = re.sub(pattern_3, replacement_function_3, result)
result = re.sub(pattern_4, replacement_function_4, result)
result = re.sub(pattern_5, replacement_function_4, result)
result = re.sub(pattern_4, replacement_function_4, result)
result = re.sub(pattern_8, replacement_function_5, result)
result = re.sub(pattern_9, replacement_function_6, result)
result = re.sub(pattern_1, replacement_function_1, result)
result = re.sub(pattern_10, replacement_function_4, result)
result = re.sub(pattern_11, replacement_function_7, result)
result = re.sub(pattern_12, replacement_function_8, result)
result = re.sub(pattern_1, replacement_function_1, result)
result = re.sub(pattern_13, replacement_function_9, result)
result = re.sub(pattern_15_2, '', result)
result = re.sub('', '', result)
result = re.sub('湯湷', '', result)
# <18.12.14. 개정>
result = re.sub(pattern_16, '', result)
# <’07.1.1 개정>
result = re.sub(pattern_17, '', result)
result = re.sub('󰡒','',result)
result = re.sub('󰡓','',result)
#       1)
result = re.sub(pattern_18, replacement_function_10, result)
#     (1)
result = re.sub(pattern_19, replacement_function_11, result)
# before **제~조~**, make one empty line.
result = re.sub(pattern_20, replacement_function_12, result)
# exception to pattern_20 at the start of the document.
result = re.sub(pattern_21, replacement_function_13, result)
# removes 전문개정'19.12.16.
result = re.sub(pattern_22, '', result)



# print(f"Original text: {text}")
print(f"Modified text: {result}")

pypc.copy(result)

print("/.py is run")









