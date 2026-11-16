# 사용법: python3 data/build.py 2026-11-23   (자료 기준일)
import json,sys,datetime,os
d=os.path.dirname(os.path.abspath(__file__))
day=datetime.date.fromisoformat(sys.argv[1]) if len(sys.argv)>1 else datetime.date.today()
t=open(f'{d}/template.html',encoding='utf-8').read()
ev=json.load(open(f'{d}/events.json',encoding='utf-8')); soc=json.load(open(f'{d}/soc.json',encoding='utf-8'))
assert all(e.get('url') for e in ev), '링크 없는 일정이 있습니다'
out=t.replace('__EVENTS__',json.dumps(ev,ensure_ascii=False)).replace('__SOCIETIES__',json.dumps(soc,ensure_ascii=False)).replace('__CHECKED__',f'{day.year}년 {day.month}월 {day.day}일')
open(os.path.join(d,'..','index.html'),'w',encoding='utf-8').write(out)
print('built',len(ev),'events',len(soc),'societies')
