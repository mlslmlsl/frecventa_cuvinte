__author__ = 'lauri'
import collections
import  operator

def citeste(nume_fis_in):
    with open(nume_fis_in,'r') as f_in:
        sir = f_in.read()
        sir = sir.replace('\\par','')
        return sir

words = collections.defaultdict(int)
words_sorted = collections.defaultdict(int)

def prelucreaza(sir):
    for word in sir.split():
        word = word.strip('.-,!\\ \n').lower()
        words[word] += 1
    words_sorted = sorted(words.items(), key=operator.itemgetter(1), reverse=True)
    # print(words_sorted)
    return words_sorted

def scriere_in_fis(f_out,words_sorted):
    with  open(f_out,'w') as f_out:
        # f_out.write(str(words_sorted))
        for word,count in words_sorted:
          f_out.write(word+':'+str(count)+'\n')


# with  open('We are.rtf','r') as f_in:
#     sir =f_in.read()
#     sir = sir.replace('\\par','')
#
# with  open('We are1.rtf','w') as f_out:
#    f_out.write(sir)
sir = citeste('We are.rtf')
words_sorted = prelucreaza(sir)
scriere_in_fis('iesire.rtf',words_sorted)

# for word in sir.split():
#   word = word.strip('.-,!\\').lower()
#   words[word] += 1
#
# # print(words)
# words_sorted = sorted(words.items(), key=operator.itemgetter(1), reverse=True)
# print(words_sorted)
# for word,count in words_sorted:
#     print(word,':',count)

