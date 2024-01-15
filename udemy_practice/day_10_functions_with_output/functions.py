#title case, formatirane na 1va bukva da e glavna
# def format_name(f_name, l_name):
#     print(f_name.title())
#     print(l_name.title())
#
# format_name("angela", "ANGELA")
#

def format_name(f_name, l_name):
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()

    # print(f"{formated_f_name} {formated_l_name}")
    return  f"{formated_f_name} {formated_l_name}"


print(format_name("AnGELA", "YU"))