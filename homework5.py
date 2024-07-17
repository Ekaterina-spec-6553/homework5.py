immutable_var = ("Idea", 456, 789, [321, 654], True)
print(immutable_var)

# immutable_var[3][0] = 147
# print(immutable_var)
# ('Idea', 456, 789, [147, 654], True). Мы можем изменить в самом элементе некоторые данные. Например, я в списке [321, 654], который считается отдельным элементом, изменила одно число из двух, находящееся внутри списка.
# immutable_var[3] = [963, 741]
# print(immutable_var)
# TypeError: 'tuple' object does not support item assignment. В данном случае я попыталась изменить весь список, точнее заменить его абсолютно другими данными. Программа не дала мне этого сделать, так как кортеж - неизменяемый объект, и менять полностью один элемент на другой нельзя.

mutable_list = ["Idea", 456, 789, [321, 654], True]
mutable_list[0] = "Surprise"
mutable_list.remove(789)
mutable_list.extend("Moscow")
mutable_list[2][1] = 123
mutable_list.append("Travelling")
print(mutable_list)