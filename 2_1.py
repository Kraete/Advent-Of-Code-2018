import re

input = ["crruafyzloguvxwctqmphenbkd","srcjafyzlcguvrwctqmphenbkd","srijafyzlogbpxwctgmphenbkd","zrijafyzloguvxrctqmphendkd","srijabyzloguvowcqqmphenbkd","srijafyzsoguvxwctbmpienbkd","srirtfyzlognvxwctqmphenbkd","srijafyzloguvxwctgmphenbmq","senjafyzloguvxectqmphenbkd","srijafyeloguvxwwtqmphembkd","srijafyzlogurxtctqmpkenbkd","srijafyzlkguvxictqhphenbkd","srijafgzlogunxwctqophenbkd","shijabyzloguvxwctqmqhenbkd","srjoafyzloguvxwctqmphenbwd","srijafyhloguvxwmtqmphenkkd","srijadyzlogwvxwctqmphenbed","brijafyzloguvmwctqmphenhkd","smijafyzlhguvxwctqmphjnbkd","sriqafvzloguvxwctqmpheebkd","srijafyzloguvxwisqmpuenbkd","mrijakyuloguvxwctqmphenbkd","srnfafyzloguvxwctqmphgnbkd","srijadyzloguvxwhfqmphenbkd","srijafhzloguvxwctdmlhenbkd","srijafyzloguvxwcsqmphykbkd","srijafyzlogwvxwatqmphhnbkd","srijafyzlozqvxwctqmphenbku","srijafyzloguvxwcbamphenbgd","srijafyzlfguvxwctqmphzybkd","srijafyzloguqxwetqmphenkkd","srijafyylogubxwttqmphenbkd","srijafyzloguvxzctadphenbkd","srijafyzloguoxwhtqmchenbkd","srijafyzloguvxwcvqmzhenbko","srijnfyzloguvxwctqmchenjkd","srijaryzloggvxwctqzphenbkd","srijafhzleguvxwcxqmphenbkd","ssijafyzllguvxfctqmphenbkd","srijafyzloguvxdctqmfhenbcd","srijafyzloguvxfctqmplynbkd","srijaftzlogavxwcrqmphenbkd","sriwaoyzloguvxwctqmphenbtd","srijahyzlogunxwctqmphenbvd","srjjafyzloguzxwctumphenbkd","nrijafyzlxguvxwctqmphanbkd","srijafezlqguyxwctqmphenbkd","srijafygloguvxwjtqcphenbkd","erijafyzloguvxoctqmnhenbkd","ssijafyzllguvxwbtqmphenbkd","sriaafyzloguvxwctqqphenbkv","frijafyzloguvswctwmphenbkd","srijafyzyogkvxwctqmprenbkd","syijafyzuoguvxwctqmkhenbkd","srijafyzloganxwctqmphenbkf","srijafyzloguvxwftqmxhenbkq","srijafyflogxvxwctqmghenbkd","srijafyzsoguvxwctqmpjenwkd","srujafylloguvxwctqmphenckd","srijafyzlpzuvxwctqmphenbud","srijafyzlogfvxwctqmhhenbwd","srijafjzlogusxwctqmphepbkd","srijlfyzloguvxwctqfphenzkd","srijafyzlogwvxwctqyphenbqd","srijafyzloluvxwctqtphenukd","srizafyzlowuvxwctqmphqnbkd","sritafkzlkguvxwctqmphenbkd","sbijafdzloguvxgctqmphenbkd","crijafyeloguvxwctqmpsenbkd","srijafyvlogulxwctqmphenbkk","srijafyologuvxwctqmehegbkd","siijafyzloguvxwctjmphenbmd","srijafyzlupuvxwctqmpheabkd","srijafyzlogumxwctqqphanbkd","srijxfyzlogujxwcqqmphenbkd","irijafizeoguvxwctqmphenbkd","sgijafyzloguvtwctqmpfenbkd","srijzfyzloguvmwctnmphenbkd","srijafyzwohuvxwctqmthenbkd","srijafyzlhguvxoctqwphenbkd","srgjafyplogxvxwctqmphenbkd","srijafyqlogovxwctqzphenbkd","srijafjzloguvlnvtqmphenbkd","srijafyzooguvxwctqmphenvud","srijafyzgoguvxwctumphgnbkd","srijaffzloguvxwdqqmphenbkd","srijafyzlogugxwctqxphenbkr","srijafyzlogutxwctqmmcenbkd","srifafyzlhguwxwctqmphenbkd","mrimajyzloguvxwctqmphenbkd","sriyafyzloguvxwcthmphejbkd","srieakyzlokuvxwctqmphenbkd","srisafyzloguhxwctqmphecbkd","srijanyzloguvxcctqmxhenbkd","srijafyzypguvxwctqmqhenbkd","sryjtfyzlvguvxwctqmphenbkd","srijafyzlsguvxwctqmqfenbkd","srijafyzlogudxwbtqwphenbkd","srijysyzloguvxwctqmpvenbkd","srijafyzloggvxwjtqmphegbkd","srijgfyzloguvxwctqmbhdnbkd","ssijufyzloguvawctqmphenbkd","skojafyzloguvxwctqmphenbnd","srijafylloguvxwcqqmpienbkd","trioafyzloguvqwctqmphenbkd","srijafydloguvxwctqmpzjnbkd","saijafvzloguvxwcqqmphenbkd","srhjapyzloguvxwctqmbhenbkd","srijafyzlfguvxwcsqmpwenbkd","shijafyzboguvxwctqmphenbmd","srizafysloguvxwrtqmphenbkd","srijafyzloguvxwciqmwhenbkj","qrijafyzloduvxwctqmphenbko","srijefyuloguvxwctqmphenbed","srijafyzlobuvxwctqmphenhbd","srijafyzloxuvxwctqmpheabkq","srijafyzloguvrwctqmghenkkd","sfisafywloguvxwctqmphenbkd","srgjafyzlogurxwctqmphenbkp","srijafhzloguvxwcjqmphenhkd","srijafyylogufxwrtqmphenbkd","srijafyzvoguvxwzkqmphenbkd","sqijafyzloguvxwctqmpheqbxd","srijafyvloguvxwctqzpherbkd","srijufyzloguvxlcsqmphenbkd","srijafykloguvxlccqmphenbkd","srijafyzloguexwcrqmphenzkd","sridifyzloguyxwctqmphenbkd","srijafyzlogfvxwctqlphenbkl","srijafyzlodqdxwctqmphenbkd","srijafyzloruvxactqmphenekd","grijafyzloguvxpctmmphenbkd","srsjakyzloguvxwctqmphvnbkd","srikafyvloguvxwrtqmphenbkd","srijafyzloguvxwctqjpserbkd","jrijafyzloguvxwctqmpgesbkd","swijafyzluguvxwctqmfhenbkd","srijanynlogovxwctqmphenbkd","jrijafyzloguvxwctymphrnbkd","srinafyzloguvewctqmphenbzd","srijakyzloguvxwctqmphcnbka","srijafyhlobuvxwctqmphenbka","srijafyzcogusxwctqmphwnbkd","srijavyzlosuvxwctqmphjnbkd","orijafyzxoguvxwcnqmphenbkd","srijafyzlogcvxwvtqmthenbkd","srijapyzloauvxwctqmphenvkd","srijaflzloguhxwctqmphenbwd","smijafyzlonuvxwctqmphenbkw","jrijafyzloguvxwclqmnhenbkd","srijaqyzloguvqwctqmphenskd","srijasyzloguvxwctqmvhenbku","crijtfyzloguvxwctqmthenbkd","srrkafyzvoguvxwctqmphenbkd","srijatyzloguvewctqmphenbld","srfjafyyloguvnwctqmphenbkd","srijafyzloguvxwctqjpbenbkt","hrijafyzooguvxwctqmphenbld","srijafbzlogscxwctqmphenbkd","srinafyzlogxvxwctqqphenbkd","slijafyzloglvxwctqmphenbdd","srijafyzlogjvxwcsqmphenbld","sryjcfyzloguvewctqmphenbkd","srijafyzloguexwctqmohknbkd","jaijafyzlogevxwctqmphenbkd","srijafbzlogavxwctqmphenbki","srijafozlogpvxwctqmphgnbkd","srijdfyzloguvxwczqmphenbkm","srijafyzlobuvxwctqmphxndkd","mrijifyzlhguvxwctqmphenbkd","srijafyzloguvxbctumphjnbkd","srijafyzloyuvxwptqmphlnbkd","arijafyzloguvxwcsqmohenbkd","srijaftzioguvxwttqmphenbkd","srijafyzlqsuvxwctqmphxnbkd","srijafyzioguvxwctqnphetbkd","prijafbzloguvxdctqmphenbkd","srijaeyzlnguvxwmtqmphenbkd","srijofyzloguvqwctqmphonbkd","srixaryzpoguvxwctqmphenbkd","srijafyzlowuvxwcwhmphenbkd","srijafydloguvxwctqmptenikd","srijqfyzlogtvfwctqmphenbkd","srijafyzloguvxlctqmpvenbgd","srijafyzlbguvxwjtqgphenbkd","srijafyzlohuqxwctqmphenbka","srijafyzroguvxictqmphynbkd","srijafyzloguvxdctjmphenjkd","srijaoczloguvxwctqmphenbjd","srajafhzloguvxwctqmphenbke","srijofyzloduvxwctqmphanbkd","srijafytloguvxwmtnmphenbkd","srijafyzuoguvxwceqmpgenbkd","rrijafyzloyuvxwctqmphlnbkd","srljafyzloguvxictqmohenbkd","srijafyzlogulxwcrqrphenbkd","srajafyzloguvxwctqmphanbke","srijafyzlhguvxwxtqmpheabkd","sxijafyzloggwxwctqmphenbkd","srijafyultguvxwctqmphinbkd","srijafyzloguvtwctqmfhvnbkd","srijafwzloruvxwctquphenbkd","srbjafyzxoguuxwctqmphenbkd","erijafyzlxguvxbctqmphenbkd","srijagyzlojubxwctqmphenbkd","srijafyzloguvxwdtqmchenakd","srijafkzlogukxwctqiphenbkd","mridafyzloguvxwctqmphenrkd","szqjafyzloguvxwctqmpheibkd","srijahyzloguvxwctcmphenekd","srijafyzloguvxwczpuphenbkd","srijafyzcoguvfwctqmphenbkq","qriiafyzloguvxwctqmpheebkd","srijpfyzloguvxlctqmphenokd","srijzfyzlotuvxwcjqmphenbkd","srinafyqloguvxwctfmphenbkd","srijafyzlogjvxpltqmphenbkd","srijafyzlotuvxwutqmphenbtd","sridafyzloguvxwctqmpyenokd","srxjafyzqogyvxwctqmphenbkd","ssijafyzzoguvxwctqmphenbad","srijafrzloguvxwctqmphekpkd","srijafyzlfgrvxactqmphenbkd","srijafyzroguvxwttqmphekbkd","srijefyzloguvxwctqmpqenbrd","srijefycloguvxwctqmchenbkd","srzjafyzloguvxwcqqmphanbkd","srijauyzlhguvxwctqmphenbgd","srijafyzloguvmwvnqmphenbkd","srihafyzloguvlwotqmphenbkd","srigafyzloguvxwctqmphennsd","sriuafzzloguvxwcuqmphenbkd","srijavuzllguvxwctqmphenbkd","srijafjzloguvlnctqmphenbkd","lrirafyzloguvxwctqmphenbld","soijarxzloguvxwctqmphenbkd","srijapyzlnguvxwctqmdhenbkd","srijafyzkogujxmctqmphenbkd","srijafuzloguvxwcsqvphenbkd","srijagyzzoguvxwctqmpvenbkd","srijafyzlovuvxwctqmrhenbxd","srijafyzqoguvxwctwmpienbkd","sxijafyzloguvxwutqmphenlkd","srijafyzlhgzvxwctqmphqnbkd","srijajyzloguvxwcbwmphenbkd","srijazyzloguvxwhtqmphenbkx","srgjafyzloguvvwctqmphdnbkd","rrivafyzloguvxjctqmphenbkd","srijifyzdoguvxwctqmphenbka","hrijafyzloguvxectqmpheybkd"]
twos = int(0)
threes = int(0)
inctwos = int(0)
incthrees = int(0)

for item in input:
  print(item)
  for character in set(item):
    if item.count(character) == 2:
      inctwos = 1
    if item.count(character) == 3:
      incthrees = 1
  twos += inctwos
  threes += incthrees
  inctwos = 0
  incthrees = 0
  print('twos: '+str(twos))
  print('threes: '+str(threes))
  

print(twos)
print(threes)
print(twos*threes)
