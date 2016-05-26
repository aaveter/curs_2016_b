
# Сопрограмма



def so():
    for i in range(3):
        x = yield
        print(x)


s = so()

print('from gen:', next(s)) # ОБЯЗАТЕЛЬНОЕ ДЕЙСТВИЕ


s.send('Hello, generator!')
s.send('Hello, generator!')
s.send('Hello, generator!')

# ДЗ
# 1.