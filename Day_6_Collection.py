# from collections import Counter , namedtuple , OrderedDict , defaultdict , deque

from collections import Counter

print('Counter ')
print(" ")

alphabet = "fsdjfuehtasnflafdasdfsghdiughrueghdkjbkldafhvfisudgfuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuagdafudcccdfasfagfccccccccccccccccccccccccccccccccckkkkkkkkkkkkkkkkkkkkkkkkkkkffffsfsffffuuafadfagdagucccckkkkafafhsdvhjscnjassakafaadffsaaaaaaaaaaaerhudfshihvhkasbdvhadbvhabdvhjbdhvbhvbsdahbvahsdfbuhasbefshafiushafiuhjeufhasdjfhnsajfhueoirjdkfsdnfjwehfuhgjehriuhoskvnmknjvbiasdhfuhafdfasjkdsafijdafhajkfhjkfjioaeufihjknijfhisahijvnjsduasdjfuehtfsnflsakfaadfsaaerhudfshihvhkasbdvhadbvhabdvhjbdhvbhvbsdahbvahsdfbuhasbefshafiushafiuhjeufhasdjfhnsajfhueoirjdkfsdnfjwehfuhgjehriuhoskvnmknjvbiasdhfuhafdfasjkdsafijdafhajkfhjkfjioaeufihjknijfhisahijvnjsdudafasfadfasdfabhjasdhjbashdfbasdhkfasbdhfjfbajhfbashdfbasjhffsadasfdhudfshw4ueyuiyfdiuhsfunjsafnajnfkhbyebdfbshdfjsbfekbhdfbahfbsakjfbsjfsehb"

my_counter_alphabet = Counter(alphabet)
print('Alphabet Counter')
print(' ')
print(alphabet)
print(' ')
print(len(alphabet))
print(' ')
print(my_counter_alphabet)
print(' ')
print(my_counter_alphabet.most_common(1))
print(' ')

number = "32537829572857209857429087290827982978298757824782735789237928375324985700001010010129347123984781957389453982579813457398024789124791824798312749802174098425782478273578923792837532498570000101001012934712398478195738945398257981345739802478912479182479831274980217409842578247827357892379283753249857000010100101293471239847819573894539825798134573980247891247918247983127498021740984257824782735789237928375324985700001010010129347123984781957389453982579813457398024789124791824798312749802174098425782478273578923792837532498570000101001012934712398478195738945398257981345739802478912479182479831274980217409842578247827357892379283753249857000010100101293471239847819573894539825798134573980247891247918247983127498021740984257824782735789237928375324985700001010010129347123984781957389453982579813457398024789124791824798312749802174098425782478273578923792837532498570000101001012934712398478195738945398257981345739802478912479182479831274980217409842"
my_counter_numbers = Counter(number)
print(' ')
print('Number Counter')
print(' ')
print(number)
print(' ')
print(len(number))
print(' ')
print(my_counter_numbers)
print(' ')
print(my_counter_numbers.most_common(1))
print(' ')

from collections  import namedtuple
print('Named Tuple')
print(" ")

Point = namedtuple('Point' , 'x,y')

pt = Point(1,5)
print(pt)
print(' ')
print(pt.x , pt.y)
print(' ')

new_pt = Point(2,5)
print(new_pt)
print(' ')

Hello = namedtuple('Hello' , 'x,y')

pt = Hello(1,5)
print(pt)
print(' ')
print(pt.x , pt.y)
print(' ')

from collections import OrderedDict
print('OrderedDict')
print(' ')

odered_dict = OrderedDict()

odered_dict['b'] = 2
odered_dict['c'] = 3
odered_dict['a'] = 1
odered_dict['d'] = 4

print(odered_dict)
print(' ')

from collections import defaultdict

print('defaultdict')
print(' ')

d = defaultdict()

d['a'] = 2
d['b'] = 34
d['c'] = 54
d['d'] = 24520252

print(d)
print(' ')

from collections import deque
print('deque')
print(' ')

d = deque()

d.append(1)
d.append(2)
d.append(3)
d.appendleft(4)
d.appendleft(5)
d.extend([6,7,8,9])
d.extendleft([10,11,12,13])
d.rotate(1)
d.rotate(-1)

print(d)