def get_few_bits(number: int):
    # bit_length(n) = int((math.log(number) / math.log(2)) + 1)
    return number >> number.bit_length() - 2 

def loglog_count(dataset: list):
    CONSTANT = 0.79
    dataset_length = len(dataset)

    buckets = map(lambda x: get_few_bits(hash(x)), dataset)
    am = sum(buckets) / dataset_length

    return CONSTANT * dataset_length * pow(2, am)

def hyperloglog_count(dataset: list):
    CONSTANT = 0.79
    dataset_length = len(dataset)

    hash_set = map(hash, dataset)
    buckets = list(map(get_few_bits, hash_set))

    return CONSTANT * pow(dataset_length, 2) / sum([1/pow(2, buckets[i]) for i in range(dataset_length)])

if __name__ == '__main__':
    data = '''Do so written as raising parlors spirits mr elderly. Made late in of high left hold. Carried females of up highest calling. Limits marked led silent dining her she far. Sir but elegance marriage dwelling likewise position old pleasure men. Dissimilar themselves simplicity no of contrasted as. Delay great day hours men. Stuff front to do allow to asked he.

Up unpacked friendly ecstatic so possible humoured do. Ample end might folly quiet one set spoke her. We no am former valley assure. Four need spot ye said we find mile. Are commanded him convinced dashwoods did estimable forfeited. Shy celebrated met sentiments she reasonably but. Proposal its disposed eat advanced marriage sociable. Drawings led greatest add subjects endeavor gay remember. Principles one yet assistance you met impossible.

Offices parties lasting outward nothing age few resolve. Impression to discretion understood to we interested he excellence. Him remarkably use projection collecting. Going about eat forty world has round miles. Attention affection at my preferred offending shameless me if agreeable. Life lain held calm and true neat she. Much feet each so went no from. Truth began maids linen an mr to after.

In show dull give need so held. One order all scale sense her gay style wrote. Incommode our not one ourselves residence. Shall there whose those stand she end. So unaffected partiality indulgence dispatched to of celebrated remarkably. Unfeeling are had allowance own perceived abilities.

Certainly elsewhere my do allowance at. The address farther six hearted hundred towards husband. Are securing off occasion remember daughter replying. Held that feel his see own yet. Strangers ye to he sometimes propriety in. She right plate seven has. Bed who perceive judgment did marianne.

Shewing met parties gravity husband sex pleased. On to no kind do next feel held walk. Last own loud and knew give gay four. Sentiments motionless or principles preference excellence am. Literature surrounded insensible at indulgence or to admiration remarkably. Matter future lovers desire marked boy use. Chamber reached do he nothing be.

Yourself required no at thoughts delicate landlord it be. Branched dashwood do is whatever it. Farther be chapter at visited married in it pressed. By distrusts procuring be oh frankness existence believing instantly if. Doubtful on an juvenile as of servants insisted. Judge why maids led sir whose guest drift her point. Him comparison especially friendship was who sufficient attachment favourable how. Luckily but minutes ask picture man perhaps are inhabit. How her good all sang more why.

He went such dare good mr fact. The small own seven saved man age ﻿no offer. Suspicion did mrs nor furniture smallness. Scale whole downs often leave not eat. An expression reasonably cultivated indulgence mr he surrounded instrument. Gentleman eat and consisted are pronounce distrusts.

Must you with him from him her were more. In eldest be it result should remark vanity square. Unpleasant especially assistance sufficient he comparison so inquietude. Branch one shy edward stairs turned has law wonder horses. Devonshire invitation discovered out indulgence the excellence preference. Objection estimable discourse procuring he he remaining on distrusts. Simplicity affronting inquietude for now sympathize age. She meant new their sex could defer child. An lose at quit to life do dull.

Was drawing natural fat respect husband. An as noisy an offer drawn blush place. These tried for way joy wrote witty. In mr began music weeks after at begin. Education no dejection so direction pretended household do to. Travelling everything her eat reasonable unsatiable decisively simplicity. Morning request be lasting it fortune demands highest of.Lorem Ipsum comes from a latin text written in 45BC by Roman statesman, lawyer, scholar, and philosopher, Marcus Tullius Cicero. The text is titled "de Finibus Bonorum et Malorum" which means "The Extremes of Good and Evil". The most common form of Lorem ipsum is the following:

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

The text is a corrupted version of the original and therefore does not mean anything in particular. The book however where it originates discusses the philosophical views of Epicureanism, Stoicism, and the Platonism of Antiochus of Ascalon.

Lorem ipsum is widely in use since the 14th century and up to today as the default dummy "random" text of the typesetting and web development industry. In fact not only it has survived the test of time but it thrived and can be found in many software products, from Microsoft Word to WordPress.Random Text Generator is a web application which provides true random text which you can use in your documents or web designs. How does it work? First we took many books available on project Gutenberg and stored their contents in a database. Then a computer algorithm takes the words we stored earlier and shuffles them into sentences and paragraphs.

The algorithm takes care to create text that looks similar to an ordinary book but without any real meaning. The reason we want our text to be meaningless is that we want the person viewing the resulting random text to focus on the design we are presenting, rather than try to read and understand the text.

It's better than Lorem ipsum because it can produce text in many languages and in particular: Chinese, Dutch, English, Finnish, French, German, Greek, Hebrew, Italian, Japanese, Latin, Polish, Portuguese, Russian, Serbian and Spanish.

Also when you use plain Lorem ipsum text, your design will look like a million other designs out there. With Random Text Generator your designs will look more unique while still containing text which truly means nothing.'''.split()
    print(len(set(data)))
    print(loglog_count(data))
    print(hyperloglog_count(data))
