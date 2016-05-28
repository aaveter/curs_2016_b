


# yield ? инструкция

print('Hello!')



def func():
    yield

# print( func() )
#
# generator = func()
# print( type(generator) )


for a in func():
    print(a)



def mic_record(samplerate=22050):
    r = Recorder(samplerate)
    while True:
        chunk = r.record_chunk()
        yield chunck


for a in mic_record(samplerate=44100):
    print(a)



def calc_gen():

    while True:
        getted_from_user = input(u'Напиши что-нибудь')
        if 'exit' in getted_from_user:
            break
        yield getted_from_user


for a in calc_gen():
    pass




def ls():
    import os
    for filename in os.listdir('.'):
        yield filename


def grep(gen, filter_word):
    for line in gen:
        if filter_word in line:
            yield line


for a in grep(ls(), filter_word='0'):
    print( a )