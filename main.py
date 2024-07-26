lst = ['1', '2', '3']
int_lst = []
for number in lst:
    int_lst.append(int(number))
print(int_lst)
# # --------------------------

gen_lst = [int(number) for number in lst]
print(gen_lst)
# # --------------------------

map_lst = map(int, lst)
print(list(map_lst))
# -----------------------------

names = ['dior', 'muhammad', 'sanjar']
map_names = map(str.capitalize, names)
print(names)
print(list(map_names))
# -----------------------------
def double_number(number):
    return number ** 2

lst = [23, 42, 55, 52, 63]

map_lst = map(double_number, lst)

print(lst)

print(list(map_lst))
# -----------------------------

words = ['purple', 'yellow', 'orange', 'apple',
         'nokia', 'windows', 'transformer', 'ton', 'not']

less_5 = []
more_5 = []

for word in words:
    if len(word) <= 5:
        less_5.append(word)
    else:
        more_5.append(word)

print(more_5)
print(less_5)

# ------------------------------
words = ['purple', 'yellow', 'orange', 'apple',
         'nokia', 'windows', 'transformer', 'ton', 'not']

def get_words_less_five(word: str):
    return len(word) <= 5

filter_lst = filter(get_words_less_five, words)
print(list(filter_lst))

# --------------------------------
#
words = ['apple', 'align', 'alive', 'after', 'assembler', 'application',
         'byd', 'banana', 'bmw', 'brain', 'brabus', 'brazilia']

def get_words_with_a(word: str):
    return word.startswith("a")

def get_words_with_b(word: str):
    return word.startswith("b")

filtered_a = filter(get_words_with_a, words)
print(list(filtered_a))

filtered_b = filter(get_words_with_b, words)
print(list(filtered_b))
