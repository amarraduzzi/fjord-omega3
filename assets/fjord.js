(()=>{const n=document.querySelector('.nav');addEventListener('scroll',()=>n.classList.toggle('solid',scrollY>40),{passive:true});
const io=new IntersectionObserver(e=>e.forEach(x=>x.isIntersecting&&(x.target.classList.add('on'),io.unobserve(x.target))),{threshold:.15});
document.querySelectorAll('.rv').forEach(el=>io.observe(el));
document.querySelectorAll('[data-count]').forEach(el=>{const t=+el.dataset.count;let s=null;const f=ts=>{s=s||ts;const p=Math.min((ts-s)/1800,1);el.textContent=Math.round(t*(1-Math.pow(1-p,3)));p<1&&requestAnimationFrame(f)};setTimeout(()=>requestAnimationFrame(f),700)});
const c=document.getElementById('sea');if(!c)return;const x=c.getContext('2d');let W,H,mx=.5,my=.5,P=[];
const rs=()=>{const d=Math.min(devicePixelRatio||1,2);W=c.width=c.clientWidth*d;H=c.height=c.clientHeight*d;x.setTransform(1,0,0,1,0,0);P=Array.from({length:Math.min(110,innerWidth/9)|0},()=>({x:Math.random()*W,y:Math.random()*H,r:(Math.random()*2.2+.6)*d,v:Math.random()*.35+.08,a:Math.random()*6.28,g:Math.random()<.35}))};
rs();addEventListener('resize',rs);addEventListener('pointermove',e=>{mx=e.clientX/innerWidth;my=e.clientY/innerHeight});
let t=0;(function L(){t+=.008;x.clearRect(0,0,W,H);
for(let k=0;k<3;k++){x.beginPath();x.moveTo(0,H);for(let i=0;i<=W;i+=24){x.lineTo(i,H*(.80+k*.06)+Math.sin(i*.0035+t*(1+k*.4)+k)*(26+k*10)*(1+(mx-.5)*.6))}x.lineTo(W,H);x.fillStyle=`rgba(${20+k*10},${90+k*25},${130+k*20},${.14-k*.03})`;x.fill()}
P.forEach(p=>{p.y-=p.v*(1+(.5-my)*.8);p.x+=Math.sin(t*2+p.a)*.35+(mx-.5)*.5;if(p.y<-10){p.y=H+10;p.x=Math.random()*W}
const g=x.createRadialGradient(p.x,p.y,0,p.x,p.y,p.r*5);const col=p.g?'240,192,96':'63,208,201';g.addColorStop(0,`rgba(${col},.9)`);g.addColorStop(1,`rgba(${col},0)`);x.fillStyle=g;x.beginPath();x.arc(p.x,p.y,p.r*5,0,6.28);x.fill()});
requestAnimationFrame(L)})()})();
(()=>{const cs=[...document.querySelectorAll('.card')];if(!cs.length)return;const ch=document.getElementById('chain'),N='http://www.w3.org/2000/svg';
const sel=c=>{cs.forEach(k=>k.classList.toggle('sel',k===c));document.querySelectorAll('.det').forEach(d=>d.classList.toggle('on',d.dataset.i===c.dataset.i));
const pn=document.querySelector('.panel'),r1=c.getBoundingClientRect(),r2=pn.getBoundingClientRect();pn.style.setProperty('--ax',(r1.left+r1.width/2-r2.left)+'px');const n=+c.dataset.c,db=+c.dataset.d;document.getElementById('mc').textContent=n;document.getElementById('md').textContent=db;
const st=820/(n-1),pts=Array.from({length:n},(_,i)=>[40+i*st,i%2?40:105]);
ch.innerHTML='';const p=document.createElementNS(N,'path');p.setAttribute('d','M'+pts.map(q=>q.join(',')).join('L'));ch.appendChild(p);
let L=0;for(let i=1;i<n;i++)L+=Math.hypot(pts[i][0]-pts[i-1][0],pts[i][1]-pts[i-1][1]);p.style.setProperty('--L',L);
const gap=(n-3)/db;for(let k=0;k<db;k++){const i=Math.round(2+k*gap),m=[(pts[i][0]+pts[i+1][0])/2,(pts[i][1]+pts[i+1][1])/2],o=document.createElementNS(N,'circle');o.setAttribute('cx',m[0]);o.setAttribute('cy',m[1]);o.setAttribute('r',9);o.style.animationDelay=(.5+k*.18)+'s';ch.appendChild(o)}};
cs.forEach(c=>{c.addEventListener('click',()=>sel(c));c.addEventListener('pointermove',e=>{const r=c.getBoundingClientRect();c.style.setProperty('--mx',e.clientX-r.left+'px');c.style.setProperty('--my',e.clientY-r.top+'px')})});
const first=new IntersectionObserver(e=>{if(e[0].isIntersecting){sel(cs[2]);first.disconnect()}},{threshold:.3});first.observe(document.querySelector('.panel'))})();
(()=>{const tb=[...document.querySelectorAll('.tab')];if(!tb.length)return;
tb.forEach(b=>b.addEventListener('click',()=>{tb.forEach(k=>k.classList.toggle('on',k===b));document.querySelectorAll('.grp').forEach(g=>{const on=g.dataset.g===b.dataset.g;g.hidden=!on;if(on)g.querySelectorAll('.fx').forEach(f=>{f.classList.remove('on');void f.offsetWidth;f.classList.add('on')})})}));
const cf=document.getElementById('cf'),cp=document.getElementById('cp'),box=document.querySelector('.cbox'),nf=new Intl.NumberFormat(box.dataset.lg,{maximumFractionDigits:2}),REF=1.75;
const up=()=>{const t=+cf.value*+cp.value;document.getElementById('cn').textContent=cp.value;document.getElementById('cv').textContent=nf.format(t);const p=Math.round(t/REF*100);document.getElementById('cpct').textContent=p;document.getElementById('cgb').style.width=Math.min(100,p)+'%'};
cf.addEventListener('change',up);cp.addEventListener('input',up);new IntersectionObserver((e,o)=>{if(e[0].isIntersecting){up();o.disconnect()}},{threshold:.4}).observe(box)})();
(()=>{const T=document.querySelector('.tl');if(T){const tiles=[...T.querySelectorAll('.tile')],wd=[...T.querySelectorAll('.wd')],msg=T.querySelector('.tmsg'),M=msg.dataset.m.split('|');
const up=()=>{let w=0;wd.forEach((d,i)=>{const all=tiles.filter(t=>+t.dataset.w===i),on=all.filter(t=>t.classList.contains('on')).length;d.querySelector('b').style.width=(on/all.length*100)+'%';d.querySelector('em').textContent=on+'/'+all.length;d.classList.toggle('full',on>0);if(on)w++});msg.textContent=M[w];T.classList.toggle('w3',w===3)};
tiles.forEach(t=>t.addEventListener('click',()=>{const o=t.classList.toggle('on');t.setAttribute('aria-pressed',o);up()}))}
document.querySelectorAll('.mc').forEach(c=>c.addEventListener('click',()=>{const o=c.classList.toggle('flip');c.setAttribute('aria-pressed',o)}));
document.querySelectorAll('.chk.tick').forEach(ul=>{const box=ul.nextElementSibling,N=+box.dataset.n,bar=box.querySelector('.bar i'),sp=box.querySelector('span'),dn=box.querySelector('p'),li=[...ul.children];
const up=()=>{const n=li.filter(x=>x.classList.contains('ok')).length;bar.style.width=(n/N*100)+'%';sp.textContent=n+' / '+N;dn.hidden=n<N};
li.forEach(x=>{const f=()=>{const o=x.classList.toggle('ok');x.setAttribute('aria-checked',o);up()};x.addEventListener('click',f);x.addEventListener('keydown',e=>{if(e.key==='Enter'||e.key===' '){e.preventDefault();f()}})})})})();

(()=>{const B=document.querySelector('.ckb');if(!B)return;const qs=[...B.querySelectorAll('.cq')],dots=[...B.querySelectorAll('.cdots i')],ft=B.querySelector('.cf2'),lk=ft.querySelector('.cl'),v=[];
const go=n=>{qs.forEach((q,i)=>q.hidden=i!==n);dots.forEach((d,i)=>d.classList.toggle('d',i<n))};
const fin=()=>{dots.forEach(d=>d.classList.add('d'));qs.forEach(q=>q.hidden=true);const f=v[0]>0,p=v[1]>0,k=f&&p?'mix':f?'sea':p?'plant':'none';B.querySelectorAll('.cr').forEach(r=>r.hidden=r.dataset.k!==k);const w=v[2]<2?'1':'2';lk.href=lk.dataset['a'+w];lk.innerHTML=lk.dataset['t'+w];ft.hidden=false};
qs.forEach((q,i)=>q.querySelectorAll('.co button').forEach(b=>b.addEventListener('click',()=>{v[i]=+b.dataset.v;i<2?go(i+1):fin()})));
B.querySelector('.cagain').addEventListener('click',()=>{v.length=0;B.querySelectorAll('.cr').forEach(r=>r.hidden=true);ft.hidden=true;dots.forEach(d=>d.classList.remove('d'));go(0)})})();
