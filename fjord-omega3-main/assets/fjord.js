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
const sel=c=>{cs.forEach(k=>k.classList.toggle('on',k===c));document.querySelectorAll('.det').forEach(d=>d.classList.toggle('on',d.dataset.i===c.dataset.i));
const n=+c.dataset.c,db=+c.dataset.d;document.getElementById('mc').textContent=n;document.getElementById('md').textContent=db;
const st=820/(n-1),pts=Array.from({length:n},(_,i)=>[40+i*st,i%2?40:105]);
ch.innerHTML='';const p=document.createElementNS(N,'path');p.setAttribute('d','M'+pts.map(q=>q.join(',')).join('L'));ch.appendChild(p);
let L=0;for(let i=1;i<n;i++)L+=Math.hypot(pts[i][0]-pts[i-1][0],pts[i][1]-pts[i-1][1]);p.style.setProperty('--L',L);
const gap=(n-3)/db;for(let k=0;k<db;k++){const i=Math.round(2+k*gap),m=[(pts[i][0]+pts[i+1][0])/2,(pts[i][1]+pts[i+1][1])/2],o=document.createElementNS(N,'circle');o.setAttribute('cx',m[0]);o.setAttribute('cy',m[1]);o.setAttribute('r',9);o.style.animationDelay=(.5+k*.18)+'s';ch.appendChild(o)}};
cs.forEach(c=>{c.addEventListener('click',()=>sel(c));c.addEventListener('pointermove',e=>{const r=c.getBoundingClientRect();c.style.setProperty('--mx',e.clientX-r.left+'px');c.style.setProperty('--my',e.clientY-r.top+'px')})});
const first=new IntersectionObserver(e=>{if(e[0].isIntersecting){sel(cs[2]);first.disconnect()}},{threshold:.3});first.observe(document.querySelector('.panel'))})();
