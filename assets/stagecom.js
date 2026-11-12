const copy=JSON.parse(document.getElementById('demo-copy').textContent);
const menu=document.querySelector('.menu');const nav=document.querySelector('#navigation');
function closeMenu(){menu.setAttribute('aria-expanded','false');menu.textContent=copy.menu;nav.classList.remove('open')}
menu.addEventListener('click',()=>{const open=menu.getAttribute('aria-expanded')!=='true';menu.setAttribute('aria-expanded',String(open));menu.textContent=open?copy.close:copy.menu;nav.classList.toggle('open',open)});
nav.querySelectorAll('a').forEach(link=>link.addEventListener('click',closeMenu));
document.addEventListener('keydown',event=>{if(event.key==='Escape'&&menu.getAttribute('aria-expanded')==='true'){closeMenu();menu.focus()}});
const get=id=>document.getElementById(id);const send=get('send-request');const ack=get('acknowledge');const complete=get('complete');const reset=get('reset-demo');
function announce(key){get('demo-status').textContent=copy[key]}
send.addEventListener('click',()=>{get('empty-request').hidden=true;get('engineer-request').hidden=false;get('request-count').textContent='1';get('performer-status').textContent=copy.waiting;send.disabled=true;send.firstChild.textContent=copy.sent+' ';announce('demoSent');ack.focus()});
ack.addEventListener('click',()=>{ack.hidden=true;complete.hidden=false;get('performer-status').textContent=copy.acknowledged;get('step-ack').classList.add('current');announce('demoAck');complete.focus()});
complete.addEventListener('click',()=>{complete.hidden=true;reset.hidden=false;get('performer-status').textContent=copy.completed;get('performer-status').classList.add('is-complete');get('step-complete').classList.add('current');get('request-count').textContent='0';announce('demoComplete');reset.focus()});
reset.addEventListener('click',()=>{reset.hidden=true;ack.hidden=false;get('engineer-request').hidden=true;get('empty-request').hidden=false;send.disabled=false;send.firstChild.textContent=copy.send+' ';get('performer-status').textContent=copy.statusReady;get('performer-status').classList.remove('is-complete');get('step-ack').classList.remove('current');get('step-complete').classList.remove('current');announce('demoReset');send.focus()});
