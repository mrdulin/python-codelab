try:
    x = int(input('请输入x:'))
    y = int(input('请输入y:'))
    assert x > 2 and y > 2, 'x和y必须为大于2的整数'
    if x > y:
        x, y = y, x
    num = []
    i = x
    # i开始的值为大于等于x的值
    for i in range(x, y + 1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            num.append(i)
    print('{}和{}之间的质数为: {}'.format(x, y, num))
except Exception as exc:
    print('异常信息：', exc)
