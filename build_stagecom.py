"""Build the static StageCom product page from localisable English content."""
from pathlib import Path
import html,json,re
from urllib.parse import urlencode
ROOT=Path(__file__).parent

def build():
 c=json.loads((ROOT/'locales/en-GB.json').read_text())
 e=lambda s: html.escape(str(s),quote=True)
 raw={
 'screenshots':''.join('<figure class="screenshot-card"><a class="screenshot-image" href="assets/stagecom/'+e(x['file'])+'.jpeg" target="_blank" rel="noopener" aria-label="'+e(c['galleryOpen']+': '+x['title'])+'"><img src="assets/stagecom/'+e(x['file'])+'.jpeg" alt="'+e(x['alt'])+'" width="'+str(x['width'])+'" height="'+str(x['height'])+'" loading="lazy" decoding="async"></a><figcaption><h3>'+e(x['title'])+'</h3><p>'+e(x['text'])+'</p><a class="screenshot-full" href="assets/stagecom/'+e(x['file'])+'.jpeg" target="_blank" rel="noopener">'+e(c['galleryOpen'])+' <span aria-hidden="true">↗</span></a></figcaption></figure>' for x in c['screenshots']),
 'steps':''.join('<article><span class="step-number">'+e(x['number'])+'</span><h3>'+e(x['title'])+'</h3><p>'+e(x['text'])+'</p></article>' for x in c['steps']),
 'requestTypes':''.join('<article class="request-type '+e(x['class'])+'"><span class="type-marker" aria-hidden="true"></span><h3>'+e(x['label'])+'</h3><p>'+e(x['text'])+'</p></article>' for x in c['requestTypes']),
 'faqs':''.join('<details><summary>'+e(x['q'])+'<span aria-hidden="true">+</span></summary><p>'+e(x['a'])+'</p></details>' for x in c['faqs']),
 'betaMail':e('mailto:'+c['betaEmail']+'?'+urlencode({'subject':c['betaSubject'],'body':c['betaBody']})),
 'demoJson':json.dumps({k:c[k] for k in ['menu','close','sent','send','statusReady','waiting','acknowledged','completed','demoSent','demoAck','demoComplete','demoReset']},ensure_ascii=False).replace('<','\\u003c')
 }
 template=(ROOT/'templates/stagecom.html').read_text()
 def replace(m):
  key=m.group(1)
  return raw[key[1:]] if key.startswith('!') else e(c[key]).replace('\n','<br>')
 result=re.sub(r'\{\{(!?\w+)\}\}',replace,template)
 (ROOT/'stagecom.html').write_text(result)
 print('Built StageCom product page from locales/en-GB.json')
if __name__=='__main__':build()
