def close_them_all(string):
    stack = []
    dict_hooks = {
        '}': '{',
        '>': '<',
        ')': '(',
        ']': '['
    }
    for symbol in string:
        if symbol in '(){}<>[]':
            try: #Если стек пуст или мы обрабатываем открывающуюся скобку, то просто заносим текущую скобку в стек
                if stack[-1] == dict_hooks[symbol]:
                    stack.pop() #Если скобка закрывает ту, которая была в стеке последней, то удаляем ее из него
                else: #Во всех остальных случаях добавляем скобку в наш стек
                        stack.append(symbol)
            except (IndexError, KeyError):
                stack.append(symbol)

    if not stack: #Если стек пуст т.е. все скобки успешно закрыты, то строка подходит
        return True
    return False


print(close_them_all('(ab[cd]({fg1})toy)')) # True
print(close_them_all('(ab[cd]({fg1})toy)))')) # False
print(close_them_all('({)}')) # False
print(close_them_all('({[<>]})')) # True