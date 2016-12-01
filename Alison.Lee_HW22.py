# Team Number Juan - Tahseen Chowdhury, Erick Cho, Oskar Mai, Alison Lee
# IntroCS2 pd8
# HW22 -- Further Explorations in Toy_Encryption (Labwork)
# 2016-03-26

# 1
# Summary: 
#   For rot13Chr, I used a helper function called rot13, which will "rotate" the letter 13
#       places. rot13Chr will return that result based on the position of the letter in the
#       alphabet.
#   rot13Wrd will return the rot13 encoded version of a word by converting the letters one
#       by one and appending them together in a string. 

# 2
def rot13Chr( ch ) :
    if ch.upper() == ch :
        offset = ord( 'A' )  #65
    else :
        offset = ord( 'a' )  #97
    if (( ch == " " ) or ( ord( ch ) < 65 ) \
        or (( 90 < ord( ch ) < 97 )) \
        or ( ord( ch ) > 122 )) :
        result = ch
        # I modified rot13Chr so that it will not return a different character
        # for anything other than the alphabet
    else :
        result = chr( (ord(ch)+13-offset) % 26  + offset )
    # ( ord( chr ) + 13 - offset ) will return a number btwn 13 and 26. The remainder
    # of this and 26 will be from 0 (the number should be closer to this if it is closer
    # to z) to 13 (if it is closer to a), and added to offset, should return the
    # rot13 equivalent. 
    return result

print rot13Chr("i")
# should print v
print rot13Chr("l")
# should print y
    
# 4
def rot13( phrase ) :
    # is basically the same as rot13Wrd, but it implements the changed
    # rot13Chr function
    index = 0
    newPhrase = ""
    while index < len( phrase ) :
        newPhrase += rot13Chr( phrase[ index ] )
        index += 1
        # will convert the letter one by one
    return newPhrase

print rot13 ( "Team Number Juan!!" )
# should print "Grnz Ahzore Whna!!"

#Challenge
def rotN( c , n ) :
    # like rot13Chr, but will rotate it any number of places
    if c.upper() == c :
        offset = ord( "A" )
    else :
        offset = ord( "a" )
    return chr(( ord( c ) + n - offset ) % 26 + offset )

def rotNPhrase(phrase,n):
    returnstring=""
    pos=0
    while pos<len(phrase): 
        if (ord(phrase[pos])>=65 and ord(phrase[pos])<=90) \
           or (ord(phrase[pos])>=97 and ord(phrase[pos])<= 122):
               returnstring+=rotN(phrase[pos],n)
        else:
               returnstring+=phrase[pos]
        pos+=1
    return returnstring
print rotNPhrase

def decryptor(phrase):
    n = 0
    while n < 26: #prints out different rot
        n += 1
        print "shift of " + str(n) + ": " + rotNPhrase(phrase, n) 
      
print decryptor("Roi roi! Ry ry! Cyzr-Pbycr CSXQ! tecd cdyvo dro cryg!")
# should print:
# shift of 1: Spj spj! Sz sz! Dzas-Qczds DTYR! ufde dezwp esp dszh!
# shift of 2: Tqk tqk! Ta ta! Eabt-Rdaet EUZS! vgef efaxq ftq etai!
# shift of 3: Url url! Ub ub! Fbcu-Sebfu FVAT! whfg fgbyr gur fubj!
# shift of 4: Vsm vsm! Vc vc! Gcdv-Tfcgv GWBU! xigh ghczs hvs gvck!
# shift of 5: Wtn wtn! Wd wd! Hdew-Ugdhw HXCV! yjhi hidat iwt hwdl!
# shift of 6: Xuo xuo! Xe xe! Iefx-Vheix IYDW! zkij ijebu jxu ixem!
# shift of 7: Yvp yvp! Yf yf! Jfgy-Wifjy JZEX! aljk jkfcv kyv jyfn!
# shift of 8: Zwq zwq! Zg zg! Kghz-Xjgkz KAFY! bmkl klgdw lzw kzgo!
# shift of 9: Axr axr! Ah ah! Lhia-Ykhla LBGZ! cnlm lmhex max lahp!
# shift of 10: Bys bys! Bi bi! Mijb-Zlimb MCHA! domn mnify nby mbiq!
# shift of 11: Czt czt! Cj cj! Njkc-Amjnc NDIB! epno nojgz ocz ncjr!
# shift of 12: Dau dau! Dk dk! Okld-Bnkod OEJC! fqop opkha pda odks!
# shift of 13: Ebv ebv! El el! Plme-Colpe PFKD! grpq pqlib qeb pelt!
# shift of 14: Fcw fcw! Fm fm! Qmnf-Dpmqf QGLE! hsqr qrmjc rfc qfmu!
# shift of 15: Gdx gdx! Gn gn! Rnog-Eqnrg RHMF! itrs rsnkd sgd rgnv!
# shift of 16: Hey hey! Ho ho! Soph-Frosh SING! just stole the show!
# shift of 17: Ifz ifz! Ip ip! Tpqi-Gspti TJOH! kvtu tupmf uif tipx!
# shift of 18: Jga jga! Jq jq! Uqrj-Htquj UKPI! lwuv uvqng vjg ujqy!
# shift of 19: Khb khb! Kr kr! Vrsk-Iurvk VLQJ! mxvw vwroh wkh vkrz!
# shift of 20: Lic lic! Ls ls! Wstl-Jvswl WMRK! nywx wxspi xli wlsa!
# shift of 21: Mjd mjd! Mt mt! Xtum-Kwtxm XNSL! ozxy xytqj ymj xmtb!
# shift of 22: Nke nke! Nu nu! Yuvn-Lxuyn YOTM! payz yzurk znk ynuc!
# shift of 23: Olf olf! Ov ov! Zvwo-Myvzo ZPUN! qbza zavsl aol zovd!
# shift of 24: Pmg pmg! Pw pw! Awxp-Nzwap AQVO! rcab abwtm bpm apwe!
# shift of 25: Qnh qnh! Qx qx! Bxyq-Oaxbq BRWP! sdbc bcxun cqn bqxf!
# shift of 26: Roi roi! Ry ry! Cyzr-Pbycr CSXQ! tecd cdyvo dro cryg!



