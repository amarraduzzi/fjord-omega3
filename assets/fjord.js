(()=>{const $=(s,r=document)=>r.querySelector(s),$$=(s,r=document)=>[...r.querySelectorAll(s)];
const rm=matchMedia('(prefers-reduced-motion:reduce)').matches;
const cv=$('#sea');let vis=true;
if(cv&&!rm){const x=cv.getContext('2d');let w,h,P=[],t=0;
const rs=()=>{w=cv.width=cv.offsetWidth;h=cv.height=cv.offsetHeight;P=Array.from({length:Math.min(70,w/18|0)},()=>({x:Math.random()*w,y:Math.random()*h,r:1+Math.random()*3,v:.2+Math.random()*.7,s:Math.random()*6}))};
rs();addEventListener('resize',rs);new IntersectionObserver(e=>vis=e[0].isIntersecting).observe(cv);
(function f(){requestAnimationFrame(f);if(!vis)return;t+=.01;x.clearRect(0,0,w,h);
for(let i=0;i<4;i++){const g=x.createLinearGradient(0,0,0,h);g.addColorStop(0,'rgba(190,235,235,.14)');g.addColorStop(1,'rgba(190,235,235,0)');x.fillStyle=g;const b=w*(.12+i*.26)+Math.sin(t+i)*40,s=Math.sin(t*.7+i)*60;x.beginPath();x.moveTo(b-25,0);x.lineTo(b+25,0);x.lineTo(b+130+s,h);x.lineTo(b-130+s,h);x.fill()}
x.fillStyle='rgba(242,246,245,.4)';P.forEach(p=>{p.y-=p.v;p.x+=Math.sin(t*2+p.s)*.3;if(p.y<-5){p.y=h+5;p.x=Math.random()*w}x.beginPath();x.arc(p.x,p.y,p.r,0,7);x.fill()})})()}
const dm=$('#dm'),df=$('#df'),sc=()=>{const p=Math.min(1,scrollY/Math.max(1,document.documentElement.scrollHeight-innerHeight));dm.textContent=Math.round(p*200);df.style.height=p*100+'%'};
addEventListener('scroll',sc,{passive:true});sc();
const io=new IntersectionObserver(e=>e.forEach(i=>{if(i.isIntersecting){i.target.classList.add('in');io.unobserve(i.target)}}),{threshold:.6});$$('h2').forEach(h=>io.observe(h));
const D={ALA:[18,3],EPA:[20,5],DHA:[22,6]},mol=$('#mol'),stat=$('#stat');
function show(k){$$('[data-ac]').forEach(b=>b.setAttribute('aria-selected',b.dataset.ac==k));$$('[data-ap]').forEach(p=>p.hidden=p.dataset.ap!=k);$('#hint').hidden=true;
const[n,m]=D[k],dx=44,P=[];for(let i=0;i<n;i++)P.push([40+i*dx,70+(i%2?-22:22)]);
let s=`<svg viewBox="0 0 ${80+n*dx} 140" role="img" aria-label="${k}"><g fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round"><path class="dr" pathLength="1" d="M${P.map(p=>p.join(' ')).join(' L')}"/>`;
for(let j=0;j<m;j++){const a=P[2+3*j],b=P[3+3*j];s+=`<path class="db${j?'':' om2'}" d="M${a[0]} ${a[1]+8} L${b[0]} ${b[1]+8}"/>`}
s+=`</g><text x="${P[0][0]-12}" y="${P[0][1]+36}">CH₃</text><text x="${P[n-1][0]-14}" y="${P[n-1][1]+(n%2?-30:38)}">COOH</text><text class="ot" x="${P[2][0]-6}" y="${P[2][1]+36}">ω-3</text></svg>`;
mol.innerHTML=s;stat.textContent=`${n} ${stat.dataset.c} · ${m} ${stat.dataset.d}`}
$$('[data-ac]').forEach(b=>b.onclick=()=>show(b.dataset.ac));show('DHA');$('#hint').hidden=false;
const st=$$('[data-st]'),sp=$$('[data-sp]');let si=0,auto=!rm;
function ss(i,u){si=i;if(u)auto=false;st.forEach((b,j)=>b.setAttribute('aria-selected',j==i));sp.forEach((p,j)=>p.hidden=j!=i);$('#lf').style.width=i*100/3+'%'}
st.forEach((b,j)=>b.onclick=()=>ss(j,1));ss(0);setInterval(()=>{if(auto&&!document.hidden)ss((si+1)%st.length)},4500);
const fs=$('#food'),po=$('#por'),ti=$('#tim'),rv=$('#rv'),rmk=$('#rm');let cur=0;
function calc(){const mg=fs.selectedOptions[0].dataset.mg*po.value/100*ti.value/7;$('#pv').textContent=po.value+' g';$('#tv').textContent=ti.value;
$('#gb').style.width=Math.min(100,mg/5)+'%';rmk.textContent=mg>=250?rmk.dataset.hi:rmk.dataset.lo;
const from=cur;cur=mg;if(rm){rv.textContent=Math.round(mg);return}const t0=performance.now();(function f(n){const k=Math.min(1,(n-t0)/500);rv.textContent=Math.round(from+(mg-from)*k);if(k<1)requestAnimationFrame(f)})(t0)}
[fs,po,ti].forEach(e=>e.addEventListener('input',calc));calc();
})();
