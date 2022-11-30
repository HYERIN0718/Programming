def solution(letter):
    answer = ''
    arr = []
    morse = {
    '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
    '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
    '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
    '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
    '-.--':'y','--..':'z'
    }

    arr_list = letter.split()
    for i in range(len(arr_list)):
        if arr_list[i] in morse:
            arr.append(morse.get(arr_list[i]))
    answer = ''.join(arr)
    return answer
