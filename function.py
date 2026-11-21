def love_score(name1,name2):
    comebind_name=name1+name2
    lower_name=comebind_name.lower()
    t=lower_name.count("t")
    r=lower_name.count("r")
    u=lower_name.count("u")
    e=lower_name.count("e")
    total=t+r+u+e
    print(total)
    l=lower_name.count("l")
    o=lower_name.count("o")
    v=lower_name.count("v")
    e=lower_name.count("e")
    total1=l+o+v+e
    print(total1)
    score=str(int(total))+str(total1)
    print(score)
love_score("lenvo","amrullahHazrati")

