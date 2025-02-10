def removeComments(source):
    result = []
    state = 'no comment'
    for line in source:
        new_line = []
        i = 0
        while i < len(line):
            if state == 'no comment':
                if i + 1 < len(line) and line[i] == '/' and line[i + 1] == '/':
                    break
                elif i + 1 < len(line) and line[i] == '/' and line[i + 1] == '*':
                    state = 'block comment'
                    i += 1
                else:
                    new_line.append(line[i])
            elif state == 'block comment':
                if i + 1 < len(line) and line[i] == '*' and line[i + 1] == '/':
                    state = 'no comment'
                    i += 1
            i += 1
        if new_line:
            result.append(''.join(new_line))
    return result

